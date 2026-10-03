"""Fast local metadata index for AssetRipper workflows (UnityPy 1.25.2, read-only)."""

import csv
import gc
import io
import json
from pathlib import Path, PurePosixPath
import re
import struct

from inspection_common import cache_dir, digest, save_json, stamp


def unitypy():
    try:
        import UnityPy
    except ImportError as error:
        raise ValueError("Install the scripts' requirements-assets.txt in an isolated Python environment") from error
    return UnityPy


def manifest_entries(path):
    text = Path(path).read_text(encoding="utf-8-sig")
    pattern = r"(?m)^- asset ID: ([^\n]+)\n  bundle: ([^\n]+)\n  path in bundle: ([^\n]+)"
    rows = [{"asset_id": asset_id, "bundle": bundle, "path": asset_path}
            for asset_id, bundle, asset_path in re.findall(pattern, text)]
    if not rows:
        raise ValueError("Unrecognized or empty SoftRef manifest")
    if any(Path(r["bundle"]).name != r["bundle"] or r["bundle"] in {".", ".."} for r in rows):
        raise ValueError("Unsafe bundle name in manifest")
    return rows


def find_prefab(manifest, name):
    entries = [r for r in manifest if r["path"].lower().endswith(".prefab") and
               (r["path"].casefold() == name.casefold() or PurePosixPath(r["path"]).stem.casefold() == name.casefold())]
    if len(entries) != 1:
        raise ValueError(f"Expected one prefab, found {len(entries)}. Use catalog search and pass the exact asset path")
    return entries[0]


def collection_objects(env):
    """Read each AssetBundle container once; avoid Environment.container's costly merging."""
    for collection in env.assets:
        for obj in collection.objects.values():
            if obj.type.name == "AssetBundle":
                yield collection, obj.read().m_Container


def components(collection, root):
    result = []
    for entry in root.get("m_Component", []):
        ref = entry.get("component", entry.get("m_Component", {}))
        if ref.get("m_FileID") or ref.get("m_PathID") not in collection.objects:
            raise ValueError("Unresolved root component")
        obj = collection.objects[ref["m_PathID"]]
        if obj.type.name == "MonoBehaviour":
            result.append((obj.path_id, obj.read_typetree()))
    return result


def pointer_target(collection, pointer):
    index = pointer["m_FileID"]
    if not pointer["m_PathID"]:
        return None
    name = collection.name if index == 0 else PurePosixPath(collection.externals[index - 1].path).name
    return {"collection": name, "path_id": pointer["m_PathID"]}


def name_tokens(collection, values):
    """Only display-name fields, never inferred title casing or description text."""
    names = []
    for _, data in values:
        item = data.get("m_itemData", {}).get("m_shared", {})
        candidate = item.get("m_name") or data.get("m_name")
        if data.get("m_overrideName"):
            candidate = data["m_overrideName"]
        elif not candidate and "m_itemPrefab" in data and ("m_respawnTimeMinutes" in data or "m_overrideName" in data or "m_stackSize" in data):
            ref = data["m_itemPrefab"]
            if ref.get("m_FileID") == 0 and ref.get("m_PathID") in collection.objects:
                target = collection.objects[ref["m_PathID"]]
                if target.type.name == "GameObject":
                    children = components(collection, target.read_typetree())
                elif target.type.name == "MonoBehaviour":
                    children = [(target.path_id, target.read_typetree())]
                else:
                    children = []
                for _, child in children:
                    candidate = child.get("m_itemData", {}).get("m_shared", {}).get("m_name")
                    if candidate:
                        break
        if isinstance(candidate, str) and candidate.strip() and candidate not in names:
            names.append(candidate)
    return names


def bundle_facts(bundle_path):
    """Cache factual prefab metadata; no game assets or translations enter the skill."""
    api = unitypy()
    folder = cache_dir([digest(__file__), api.__version__, stamp(bundle_path)], persistent=True)
    cached = folder / "prefabs.json"
    if cached.exists():
        return json.loads(cached.read_text(encoding="utf-8"))
    env = api.load(str(bundle_path))
    rows = []
    for collection, container in collection_objects(env):
        for path, info in container:
            if not path.lower().endswith(".prefab"):
                continue
            row = {"path": path, "bundle": Path(bundle_path).name, "name_tokens": [], "icons": []}
            try:
                root_obj = info.asset.deref()
                root = root_obj.read_typetree()
                if "m_RootGameObject" in root:
                    ref = root["m_RootGameObject"]
                    if ref["m_FileID"]:
                        raise ValueError("External prefab root")
                    root = collection.objects[ref["m_PathID"]].read_typetree()
                if "m_Component" not in root:
                    raise ValueError("Root GameObject was not decoded")
                row["root_name"] = root["m_Name"]
                values = components(collection, root)
                row["name_tokens"] = name_tokens(collection, values)
                for _, data in values:
                    shared = data.get("m_itemData", {}).get("m_shared", {})
                    if "m_icons" in shared:
                        row["icons"] = [pointer_target(collection, p) for p in shared["m_icons"]]
                row["name_status"] = "inspected"
            except (ValueError, KeyError, AttributeError, FileNotFoundError, IndexError) as error:
                row["name_status"] = type(error).__name__
            rows.append(row)
    save_json(cached, rows)
    del env
    gc.collect()
    return rows


def parse_localization(text):
    rows = csv.reader(io.StringIO(text))
    header = next(rows)
    index = header.index("English")
    return {row[0]: (row[index].strip() or row[1]) for row in rows
            if len(row) > index and row[0] and not row[0].startswith("//")}


def localization_order(obj):
    """Decode the verified Unity 6 settings layout when stripped type trees omit it."""
    data = obj.read_typetree(check_read=False)
    if "m_localizations" in data:
        return data["m_localizations"]
    if str(obj.assets_file.unity_version).split(".")[0] != "6000":
        raise ValueError("Unknown stripped LocalizationSettings layout; inspect it with ILSpy first")
    raw = obj.get_raw_data()
    # GameObject PPtr (12), enabled + alignment (4), MonoScript PPtr (12), name.
    size = struct.unpack_from("<i", raw, 28)[0]
    if raw[32:32 + size] != b"LocalizationSettings":
        raise ValueError("Unexpected LocalizationSettings header")
    offset = (32 + size + 3) & ~3
    count = struct.unpack_from("<i", raw, offset)[0]
    if not 0 < count < 100:
        raise ValueError("Invalid localization file count")
    offset += 4
    refs = []
    for _ in range(count):
        file_id, path_id = struct.unpack_from("<iq", raw, offset)
        refs.append({"m_FileID": file_id, "m_PathID": path_id})
        offset += 12
    # The next field is the professionally translated language list. Validate to EOF.
    count = struct.unpack_from("<i", raw, offset)[0]
    offset += 4
    if not 0 < count < 100:
        raise ValueError("Unexpected LocalizationSettings language list")
    for _ in range(count):
        size = struct.unpack_from("<i", raw, offset)[0]
        if not 0 < size < 100:
            raise ValueError("Invalid language name length")
        offset = (offset + 4 + size + 3) & ~3
    if offset != len(raw):
        raise ValueError("LocalizationSettings schema changed; inspect the new layout")
    return refs


def english_translations(resources):
    api = unitypy()
    folder = cache_dir([digest(__file__), api.__version__, stamp(resources)], persistent=True)
    cached = folder / "english.json"
    if cached.exists():
        return json.loads(cached.read_text(encoding="utf-8"))
    env = api.load(str(resources))
    settings = [o for o in env.objects if o.type.name == "MonoBehaviour" and o.peek_name() == "LocalizationSettings"]
    if len(settings) != 1:
        raise ValueError("Expected one LocalizationSettings object")
    obj = settings[0]
    result = {"translations": {}, "files": []}
    for ref in localization_order(obj):
        if ref["m_FileID"]:
            raise ValueError("External localization file; load its dependency explicitly")
        text = obj.assets_file.objects[ref["m_PathID"]].read()
        result["files"].append(text.m_Name)
        script = text.m_Script.decode("utf-8-sig") if isinstance(text.m_Script, bytes) else text.m_Script
        result["translations"].update(parse_localization(script))
    save_json(cached, result)
    return result


def localize_name(token, translations):
    missing = []
    def replace(match):
        key = match[0][1:]
        if key not in translations:
            missing.append(key)
        return translations.get(key, match[0])
    text = re.sub(r"\$[^ (){}\[\]+!?/\\&%,.:=<>\n\-]+", replace, token)
    return None if missing else text


def bundle_members(path):
    """Read only the UnityFS directory, not multi-gigabyte texture payloads."""
    from UnityPy.helpers.CompressionHelper import decompress_lzma
    from lz4.block import decompress
    def cstring(stream):
        value = bytearray()
        for _ in range(4096):
            char = stream.read(1)
            if char == b"\0":
                return value.decode("utf-8")
            if not char:
                break
            value.extend(char)
        raise ValueError("Invalid UnityFS string")
    with Path(path).open("rb") as stream:
        if cstring(stream) != "UnityFS":
            raise ValueError("Expected a UnityFS bundle")
        version = struct.unpack(">I", stream.read(4))[0]
        cstring(stream)
        cstring(stream)
        total, compressed, uncompressed, flags = struct.unpack(">QIII", stream.read(20))
        if version < 7 or compressed > 64 * 1024 * 1024 or uncompressed > 64 * 1024 * 1024:
            raise ValueError("Unsupported UnityFS directory layout or size")
        stream.seek((stream.tell() + 15) & ~15)
        if flags & 0x80:
            stream.seek(total - compressed)
        payload = stream.read(compressed)
        mode = flags & 0x3f
        if mode in (2, 3):
            payload = decompress(payload, uncompressed_size=uncompressed)
        elif mode == 1:
            payload = decompress_lzma(payload)
        elif mode != 0:
            raise ValueError("Unsupported bundle compression")
        if len(payload) != uncompressed:
            raise ValueError("Invalid UnityFS directory length")
        directory = io.BytesIO(payload)
        directory.seek(16)
        blocks = struct.unpack(">I", directory.read(4))[0]
        directory.seek(10 * blocks, 1)
        count = struct.unpack(">I", directory.read(4))[0]
        names = []
        for _ in range(count):
            directory.seek(20, 1)
            names.append(cstring(directory))
        return names


def find_collection_bundle(directory, collection):
    files = sorted(p for p in Path(directory).iterdir() if p.is_file())
    folder = cache_dir([digest(__file__), [stamp(p) for p in files]], persistent=True)
    cached = folder / "collections.json"
    if cached.exists():
        index = json.loads(cached.read_text(encoding="utf-8"))
    else:
        index = {}
        for path in files:
            for name in bundle_members(path):
                index.setdefault(name.casefold(), []).append(path.name)
        save_json(cached, index)
    matches = index.get(collection.casefold(), [])
    if len(matches) != 1:
        raise ValueError(f"Expected one bundle for collection {collection}; found {len(matches)}")
    return Path(directory) / matches[0]
