#!/usr/bin/env python3
"""Inventory local Valheim prefab assets through a running AssetRipper 2.0 API."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import hashlib
import html
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import Request, urlopen

from asset_index import bundle_facts, english_translations, localize_name
from inspection_common import game_data


def request(base, endpoint, data=None):
    """Use only the selected loopback service, with bounded request timeouts."""
    body = urlencode(data).encode() if data is not None else None
    with urlopen(Request(base + endpoint, data=body), timeout=180) as response:
        return response.read()


def asset_json(base, locator):
    """Preserve signed 64-bit asset IDs through Python's integer-safe JSON parser."""
    query = urlencode({"Path": json.dumps(locator, separators=(",", ":"))})
    result = json.loads(request(base, "/Assets/Json?" + query))
    if not isinstance(result, dict):
        raise ValueError("Expected an asset property object")
    return result


def bundle_locator(base, name):
    """Read the bundle's locator from an actual API-generated asset link."""
    page = request(base, "/Search/View?q=AssetBundle").decode()
    for row in re.findall(r'<tr data-class="AssetBundle">(.*?)</tr>', page):
        match = re.search(r'<a href="(/Assets/View\?[^\"]+)"[^>]*>(.*?)</a>', row)
        if match and html.unescape(match[2]) == name:
            query = parse_qs(urlsplit(html.unescape(match[1])).query)
            return json.loads(query["Path"][0])
    return None


def parse_manifest(path):
    """Read explicit prefab records, not arbitrary GameObject names."""
    data = path.read_text(encoding="utf-8-sig")
    pattern = r"(?m)^- asset ID: ([^\n]+)\n  bundle: ([^\n]+)\n  path in bundle: ([^\n]+)"
    entries = {}
    for asset_id, bundle, asset_path in re.findall(pattern, data):
        if asset_path.lower().endswith(".prefab"):
            key = (bundle, asset_path.casefold())
            if key in entries:
                raise ValueError("Duplicate prefab identity in manifest")
            entries[key] = {"bundle": bundle, "path": asset_path, "asset_id": asset_id}
    if not entries:
        raise ValueError("No prefab entries found; inspect the manifest format")
    return entries


def root_details(base, locator, entry):
    """Inspect the actual root without loading or guessing missing dependencies."""
    row = dict(entry)
    try:
        obj = asset_json(base, locator)
        if "m_Components" not in obj:
            reference = obj.get("m_RootGameObject", {})
            if reference.get("m_FileID") == 0 and reference.get("m_PathID"):
                locator = {"C": locator["C"], "D": reference["m_PathID"]}
                obj = asset_json(base, locator)
        row["root_name"] = obj.get("m_Name", PurePosixPath(row["path"]).stem)
        row["components"] = len(obj["m_Components"]) if "m_Components" in obj else None
        row["active"] = obj.get("m_IsActive")
    except (OSError, ValueError) as error:
        row["inspection_error"] = type(error).__name__
    return row


def inspect_bundles(base, manifest, bundles_dir, cache_path, fingerprint):
    """Load each relevant bundle separately to keep memory use bounded."""
    rows = {}
    if cache_path.exists():
        saved = json.loads(cache_path.read_text())
        if saved.get("manifest_sha256") != fingerprint:
            raise ValueError("The cache belongs to another manifest; use a new cache file")
        rows = {(r["bundle"], r["path"].casefold()): r for r in saved["rows"]}
        completed = set(saved["completed"])
    else:
        completed = set()
    names = sorted({key[0] for key in manifest}, key=lambda b: (-sum(k[0] == b for k in manifest), b))
    for position, name in enumerate(names, 1):
        if name in completed:
            continue
        path = bundles_dir / name
        if not path.is_file():
            raise ValueError(f"Missing bundle: {name}")
        locator = bundle_locator(base, name)
        if locator is None:
            request(base, "/LoadFile", {"Path": str(path)})
            locator = bundle_locator(base, name)
        if locator is None:
            raise ValueError(f"AssetRipper did not load bundle: {name}")
        container = asset_json(base, locator).get("m_Container", {})
        work = []
        for asset_path, value in container.items():
            if not asset_path.lower().endswith(".prefab"):
                continue
            key = (name, asset_path.casefold())
            entry = dict(manifest.get(key, {"bundle": name, "path": asset_path, "asset_id": None}))
            pointer = value["m_Asset"]
            if pointer["m_FileID"] != 0:
                rows[key] = {**entry, "inspection_error": "ExternalRootReference"}
                continue
            work.append(({"C": locator["C"], "D": pointer["m_PathID"]}, entry))
        with ThreadPoolExecutor(max_workers=4) as executor:
            for row in executor.map(lambda task: root_details(base, *task), work):
                rows[(name, row["path"].casefold())] = row
        for key, entry in manifest.items():
            if key[0] == name and key not in rows:
                rows[key] = {**entry, "inspection_error": "CatalogOnly"}
        completed.add(name)
        cache_path.write_text(json.dumps({"manifest_sha256": fingerprint,
                                         "completed": sorted(completed), "rows": list(rows.values())}), encoding="utf-8")
        if position == 1 or position % 20 == 0 or position == len(names):
            print(f"Inspected {position}/{len(names)} prefab bundles; {len(rows)} prefab entries", flush=True)
    return list(rows.values()), len(names)


def family(path):
    """Derive a transparent folder-based family, not a gameplay classification."""
    parts = PurePosixPath(path).parts
    if len(parts) > 3 and parts[1].lower() == "gameelements":
        return "/".join(parts[1:3])
    return "/".join(parts[1:3]) if len(parts) > 3 else "/".join(parts[1:-1])


def cell(value):
    """Keep asset names from breaking Markdown rows."""
    return html.escape(str(value)).replace("|", "&#124;").replace("\n", " ")


def render(rows, manifest_path, game_version, bundle_count, catalog_count):
    """Write one sorted table with explicit coverage and property limitations."""
    rows.sort(key=lambda row: ((row.get("root_name") or PurePosixPath(row["path"]).stem).casefold(), row["path"], row["bundle"]))
    inspected = sum(row.get("components") is not None for row in rows)
    extra = sum(row.get("asset_id") is None for row in rows)
    named = sum(bool(row.get("english_names")) for row in rows)
    lines = ["# Valheim Prefab Inventory", "", f"Extracted on {date.today().isoformat()} from the local Steam build **Valheim {game_version}**.", "",
             f"- **{len(rows):,} prefab assets**, sorted by root name (or file stem when unavailable).",
             f"- All **{catalog_count:,}** prefab records from `valheim_Data/StreamingAssets/SoftRef/manifest_extended` are included.",
             f"- AssetRipper **2.0.0 Free** inspected **{bundle_count}** referenced bundles and found **{extra}** additional prefab container entries.",
             f"- Root properties were read for **{inspected:,}** entries; unavailable values are marked explicitly.",
             f"- Verified English display names were found for **{named:,}** entries using local prefab fields and localization data.",
             f"- Source manifest SHA-256: `{hashlib.sha256(manifest_path.read_bytes()).hexdigest()}`.", "",
             "## Reading the table", "",
             "The folder family is derived from the original asset path, not a verified gameplay role.",
             "Root components counts components attached directly to the root, not all descendants.",
             "Active is the serialized root state, not proof that the object currently exists in a world.",
             "Source identifies the bundle and original asset path; identical names are not merged.", "",
             "English name uses display-name fields on root components (including ItemDrop, Piece,",
             "Character, and pickable item references). Localization files follow LocalizationSettings",
             "load order. Names are not guessed from prefab identifiers. An em dash means no verified",
             "name was found, not proof that no name exists. Runtime renaming, child-only labels, and",
             "mod overrides are not evaluated. Technical prefabs often have no player-facing name.", "",
             "This is an inventory of prefab files in the inspected shipping bundles, not console commands",
             "or an enumeration of a running game's objects. It does not include mod-added or dynamically",
             "created prefabs, and does not establish that every listed asset can be spawned. References to",
             "unloaded dependency bundles may remain unresolved. Game version was checked in the local",
             "assembly's Version.CurrentVersion; no save or game file was changed.", "",
             "## Prefabs", "", "| Prefab / root name | English name | Folder family | Root properties | Source: bundle / asset path |", "| --- | --- | --- | --- | --- |"]
    for row in rows:
        name = row.get("root_name") or PurePosixPath(row["path"]).stem
        if row.get("components") is not None:
            active = "yes" if row.get("active") is True else "no" if row.get("active") is False else "unavailable"
            properties = f"{row['components']} components; active: {active}"
        else:
            properties = "Not decoded (" + row.get("inspection_error", "root properties unavailable") + ")"
        values = (name, "; ".join(row.get("english_names", [])) or "—", family(row["path"]), properties, row["bundle"] + " / " + row["path"])
        lines.append("| " + " | ".join(cell(v) for v in values) + " |")
    return "\n".join(lines) + "\n"


def main():
    """Export an explicitly requested inventory without launching or editing the game."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--game-version", required=True)
    parser.add_argument("--cache", type=Path, required=True, help="Fresh task-local metadata cache outside the repo")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--english-names", action="store_true", help="Resolve display names from local components and localization (requires UnityPy)")
    args = parser.parse_args()
    game_data(str(args.manifest.parent.parent.parent))
    address = urlsplit(args.base_url)
    if address.scheme != "http" or address.hostname not in {"127.0.0.1", "localhost", "::1"}:
        parser.error("Use a loopback AssetRipper service")
    manifest = parse_manifest(args.manifest)
    fingerprint = hashlib.sha256(args.manifest.read_bytes()).hexdigest()
    rows, count = inspect_bundles(args.base_url.rstrip("/"), manifest, args.manifest.parent / "Bundles", args.cache, fingerprint)
    if not set(manifest).issubset({(r["bundle"], r["path"].casefold()) for r in rows}):
        raise ValueError("Incomplete manifest coverage")
    if args.english_names:
        translations = english_translations(args.manifest.parent.parent.parent / "resources.assets")["translations"]
        by_bundle = {}
        for row in rows:
            by_bundle.setdefault(row["bundle"], []).append(row)
        for i, (bundle, group) in enumerate(sorted(by_bundle.items()), 1):
            facts = {r["path"].casefold(): r for r in bundle_facts(args.manifest.parent / "Bundles" / bundle)}
            for row in group:
                details = facts.get(row["path"].casefold(), {})
                row["english_names"] = list(dict.fromkeys(text for token in details.get("name_tokens", [])
                                                         if (text := localize_name(token, translations))))
            if i == 1 or i % 20 == 0 or i == len(by_bundle):
                print(f"Resolved names in {i}/{len(by_bundle)} bundles", flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(rows, args.manifest, args.game_version, count, len(manifest)), encoding="utf-8")
    print(f"Wrote {len(rows)} prefab rows to {args.output}", flush=True)


if __name__ == "__main__":
    main()
