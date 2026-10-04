#!/usr/bin/env python3
"""Find Valheim assets and export exact inventory icons through AssetRipper."""

import argparse
import io
from importlib.metadata import version
from pathlib import Path

import asset_ripper as ar
from asset_index import (bundle_facts, english_translations, find_collection_bundle,
                         find_prefab, localize_name, manifest_entries)
from inspection_common import cache_dir, cached_result, digest, game_data, print_json, save_bytes, save_json, stamp


def input_identity(inputs):
    """Include nearby resource streams and script metadata that a loader may read."""
    paths = [Path(p).resolve(strict=True) for p in inputs]
    dependencies = set()
    for path in paths:
        dependencies.update(p for p in path.parent.iterdir()
                            if p.is_file() and p.suffix.lower() in {".ress", ".resource"})
        dependencies.update((path.parent / "Managed").glob("*.dll"))
    return {"ordered_inputs": [stamp(p) for p in paths],
            "dependencies": [stamp(p) for p in sorted(dependencies)]}


def prefab_info(data, name):
    manifest = data / "StreamingAssets/SoftRef/manifest_extended"
    entry = find_prefab(manifest_entries(manifest), name)
    bundle = manifest.parent / "Bundles" / entry["bundle"]
    rows = bundle_facts(bundle)
    matches = [r for r in rows if r["path"].casefold() == entry["path"].casefold()]
    if len(matches) != 1:
        raise ValueError("Prefab is catalogued but its root data could not be read")
    row = dict(matches[0])
    translations = english_translations(data / "resources.assets")["translations"]
    row["english_names"] = [text for token in row["name_tokens"]
                            if (text := localize_name(token, translations))]
    return row, bundle


def crop_sprite(payload, sprite):
    """AssetRipper 2.0 returns the atlas. Extract the rectangle with original alpha."""
    from PIL import Image
    image = Image.open(io.BytesIO(payload)).convert("RGBA")
    rd = sprite["m_RD"]
    rect = rd["m_TextureRect"]
    x, y, width, height = [int(rect["m_" + k]) for k in ("X", "Y", "Width", "Height")]
    if width <= 0 or height <= 0 or x < 0 or y < 0 or x + width > image.width or y + height > image.height:
        raise ValueError("Sprite rectangle does not fit the exported texture")
    flags = rd["m_SettingsRaw"]
    if not (flags >> 1) & 1:
        raise ValueError("Tight-packed sprite needs mesh-aware extraction; rectangular cropping is not safe")
    if sprite.get("m_SpriteAtlas", {}).get("m_PathID") or rd.get("m_AlphaTexture", {}).get("m_PathID"):
        raise ValueError("External atlas or separate alpha needs explicit dependency-aware extraction")
    # Unity's rectangle starts at the lower left; PNG rows start at the top.
    image = image.crop((x, image.height - y - height, x + width, image.height - y))
    rotation = (flags >> 2) & 15 if flags & 1 else 0
    transform = {0: None, 1: Image.Transpose.FLIP_LEFT_RIGHT,
                 2: Image.Transpose.FLIP_TOP_BOTTOM, 3: Image.Transpose.ROTATE_180,
                 4: Image.Transpose.ROTATE_90}
    if rotation not in transform:
        raise ValueError("Unknown sprite packing rotation")
    if transform[rotation] is not None:
        image = image.transpose(transform[rotation])
    return image


def inventory_icon(data, name, variant=0, base=None, tool=None):
    row, source = prefab_info(data, name)
    if variant < 0 or variant >= len(row["icons"]) or not row["icons"][variant]:
        raise ValueError(f"No inventory icon variant {variant} on this prefab; no replacement image will be invented")
    target = row["icons"][variant]
    bundle = find_collection_bundle(source.parent, target["collection"])
    identity = {"scripts": [digest(p) for p in sorted(Path(__file__).parent.glob("*.py"))],
                "prefab": row["path"], "variant": variant,
                "source": stamp(source), "icon_bundle": stamp(bundle), "target": target,
                "tool": ar.cache_identity(tool), "english_names": row["english_names"],
                "inputs": input_identity([source, bundle]),
                "libraries": {name: version(name) for name in ("UnityPy", "Pillow")}}
    folder = cache_dir(identity, persistent=True, category="images")
    path = folder / "inventory-icon.png"
    metadata = folder / "provenance.json"
    result = cached_result(path, identity) if tool else None
    if result is not None:
        return {**result, "path": str(path), "cache_hit": True}
    # The small sprite bundle is sufficient for most inventory icons; never load
    # the entire game or guess by a sprite's name alone.
    with ar.session(base, tool) as address:
        ar.load(address, [bundle])
        matches = [r for r in ar.search(address, "Sprite")
                   if r["class"] == "Sprite" and r["locator"]["D"] == target["path_id"]]
        if len(matches) != 1:
            raise ValueError("The referenced inventory Sprite was not uniquely decoded")
        selected = matches[0]
        sprite = ar.asset_json(address, selected["locator"])
        image = crop_sprite(ar.export(address, selected["locator"], "png"), sprite)
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        save_bytes(path, buffer.getvalue())
    result = {"prefab": row["root_name"], "english_names": row["english_names"],
              "path": str(path), "width": image.width, "height": image.height,
              "variant": variant, "sprite": selected["name"], "png_sha256": digest(path), "output_sha256": digest(path),
              "source": identity, "exporter": "AssetRipper 2.0 + metadata-guided sprite crop"}
    save_json(metadata, result)
    return {**result, "cache_hit": False}


def export_asset(inputs, query, kind=None, path_id=None, format_name="json", base=None, tool=None):
    """Cache a targeted export before starting AssetRipper; never reuse live locators."""
    identity = {"scripts": [digest(Path(__file__)), digest(Path(ar.__file__))],
                "inputs": input_identity(inputs), "query": query, "class": kind,
                "id": path_id, "format": format_name, "tool": ar.cache_identity(tool)}
    if format_name == "png":
        identity["pillow"] = version("Pillow")
    folder = cache_dir(identity, persistent=True, category="images" if format_name == "png" else "assets")
    path = folder / ("asset." + {"text": "txt", "binary": "bin"}.get(format_name, format_name))
    result = cached_result(path, identity) if tool else None
    if result is not None:
        return {**result, "path": str(path), "cache_hit": True}
    with ar.session(base, tool) as address:
        ar.load(address, inputs)
        rows = [r for r in ar.search(address, query)
                if (not kind or r["class"] == kind) and (path_id is None or r["locator"]["D"] == path_id)]
        if len(rows) != 1:
            raise ValueError(f"Expected one asset, found {len(rows)}; refine --query, --class, or --id")
        payload = ar.export(address, rows[0]["locator"], format_name)
        if format_name == "png" and rows[0]["class"] == "Sprite":
            image = crop_sprite(payload, ar.asset_json(address, rows[0]["locator"]))
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            payload = buffer.getvalue()
        save_bytes(path, payload)
    result = {"path": str(path), "bytes": path.stat().st_size, "source": identity,
              "asset": {"name": rows[0]["name"], "class": rows[0]["class"], "path_id": rows[0]["locator"]["D"]},
              "output_sha256": digest(path)}
    save_json(folder / "provenance.json", result)
    return {**result, "cache_hit": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game")
    service = parser.add_mutually_exclusive_group()
    service.add_argument("--base-url", help="Dedicated loopback service; loading replaces its current session")
    service.add_argument("--tool", help="AssetRipper executable; start hidden and stop when finished")
    sub = parser.add_subparsers(dest="command", required=True)
    catalog = sub.add_parser("catalog", help="Search the manifest without loading assets")
    catalog.add_argument("query")
    prefab = sub.add_parser("prefab", help="Inspect the name and icon references of an exact prefab")
    prefab.add_argument("name")
    icon = sub.add_parser("icon", help="Extract the actual inventory icon, not the model or the whole atlas")
    icon.add_argument("name")
    icon.add_argument("--variant", type=int, default=0)
    for command in ("search", "export"):
        target = sub.add_parser(command, help="Search loaded files or export one exact asset")
        target.add_argument("--input", type=Path, action="append", required=True)
        target.add_argument("--query", required=True)
        target.add_argument("--class", dest="kind")
        target.add_argument("--id", type=int, help="Exact signed 64-bit path ID from search")
        if command == "export":
            target.add_argument("--format", choices=["json", "yaml", "text", "png", "binary"], default="json")
    args = parser.parse_args()
    try:
        data = game_data(args.game)
        if args.command == "catalog":
            rows = manifest_entries(data / "StreamingAssets/SoftRef/manifest_extended")
            print_json([r for r in rows if args.query.casefold() in r["path"].casefold()])
        elif args.command == "prefab":
            print_json(prefab_info(data, args.name)[0])
        elif args.command == "icon":
            print_json(inventory_icon(data, args.name, args.variant, args.base_url, args.tool))
        elif args.command == "export":
            print_json(export_asset(args.input, args.query, args.kind, args.id, args.format, args.base_url, args.tool))
        else:
            with ar.session(args.base_url, args.tool) as base:
                ar.load(base, args.input)
                rows = [r for r in ar.search(base, args.query)
                        if (not args.kind or r["class"] == args.kind)
                        and (args.id is None or r["locator"]["D"] == args.id)]
                print_json(rows)
    except (OSError, ValueError, KeyError, ImportError) as error:
        parser.exit(1, f"Asset inspection failed: {error}\n")


if __name__ == "__main__":
    main()
