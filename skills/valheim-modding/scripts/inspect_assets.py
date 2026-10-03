#!/usr/bin/env python3
"""Find Valheim assets and export exact inventory icons through AssetRipper."""

import argparse
import io
import json
from pathlib import Path

import asset_ripper as ar
from asset_index import (bundle_facts, english_translations, find_collection_bundle,
                         find_prefab, localize_name, manifest_entries)
from inspection_common import cache_dir, digest, game_data, print_json, save_json, stamp


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
                "source": stamp(source), "icon_bundle": stamp(bundle), "target": target}
    folder = cache_dir(identity)
    path = folder / "inventory-icon.png"
    metadata = folder / "provenance.json"
    if path.is_file() and metadata.is_file():
        result = json.loads(metadata.read_text(encoding="utf-8"))
        if digest(path) == result.get("png_sha256"):
            return {**result, "cache_hit": True}
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
        image.save(path, format="PNG")
    result = {"prefab": row["root_name"], "english_names": row["english_names"],
              "path": str(path), "width": image.width, "height": image.height,
              "variant": variant, "sprite": selected["name"], "png_sha256": digest(path),
              "source": identity, "exporter": "AssetRipper 2.0 + metadata-guided sprite crop"}
    save_json(metadata, result)
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
        else:
            with ar.session(args.base_url, args.tool) as base:
                ar.load(base, args.input)
                rows = [r for r in ar.search(base, args.query)
                        if (not args.kind or r["class"] == args.kind)
                        and (args.id is None or r["locator"]["D"] == args.id)]
                if args.command == "search":
                    print_json(rows)
                else:
                    if len(rows) != 1:
                        raise ValueError(f"Expected one asset, found {len(rows)}; refine --query, --class, or --id")
                    folder = cache_dir([digest(__file__), [stamp(p) for p in args.input], rows[0], args.format])
                    payload = ar.export(base, rows[0]["locator"], args.format)
                    path = folder / ("asset." + {"text": "txt", "binary": "bin"}.get(args.format, args.format))
                    if args.format == "png" and rows[0]["class"] == "Sprite":
                        crop_sprite(payload, ar.asset_json(base, rows[0]["locator"])).save(path, format="PNG")
                    else:
                        path.write_bytes(payload)
                    save_json(folder / "provenance.json", {"inputs": [stamp(p) for p in args.input], "asset": rows[0]})
                    print_json({"path": str(path), "bytes": path.stat().st_size, "asset": rows[0]})
    except (OSError, ValueError, KeyError, ImportError) as error:
        parser.exit(1, f"Asset inspection failed: {error}\n")


if __name__ == "__main__":
    main()
