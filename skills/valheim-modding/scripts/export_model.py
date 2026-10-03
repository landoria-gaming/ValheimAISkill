#!/usr/bin/env python3
"""Export one static Valheim prefab as an isolated Unity model package."""

import argparse
from collections import Counter
import gc
import gzip
import hashlib
import io
from pathlib import Path
import re
import shutil
import sys
import tarfile
import tempfile
import time

import asset_ripper as ar
from asset_index import collection_objects, find_prefab, manifest_entries, unitypy
from inspection_common import digest, game_data, persistent_cache_root, print_json, save_json, stamp


COMPONENTS = {"Transform", "MeshFilter", "MeshRenderer", "LODGroup"}
DEPENDENCIES = {"Mesh", "Material", "Texture2D"}
ASSETS = Path(__file__).resolve().parents[1] / "assets/model-export"
NULL = {"m_FileID": 0, "m_PathID": 0}


def pointers(value):
    if isinstance(value, dict):
        if set(value) == {"m_FileID", "m_PathID"}:
            yield value
        else:
            for child in value.values():
                yield from pointers(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            yield from pointers(child)


def safe_name(name):
    value = re.sub(r"[^A-Za-z0-9_-]", "_", name).strip("_")
    if not value or value.upper() in {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(10)), *(f"LPT{i}" for i in range(10))}:
        raise ValueError("Prefab name is not safe as an export directory")
    return value


class StaticSelection:
    """Filter a copy in memory. Never write the game's original bundle."""

    def __init__(self, collection):
        self.collection = collection
        self.selected = {}
        self.trees = {}
        self.excluded = Counter()
        self.materials = []
        self.omitted_maps = set()

    def resolve(self, pointer):
        if not pointer["m_PathID"]:
            return None
        if pointer["m_FileID"]:
            raise ValueError("External model dependency: this exporter currently requires one serialized collection")
        try:
            return self.collection.objects[pointer["m_PathID"]]
        except KeyError as error:
            raise ValueError("Missing model dependency; refusing an incomplete export") from error

    def add(self, obj, tree=None):
        self.selected[obj.path_id] = obj
        self.trees[obj.path_id] = obj.read_typetree() if tree is None else tree

    def hierarchy(self, root):
        queue = [root]
        seen = set()
        while queue:
            obj = queue.pop()
            if obj.path_id in seen:
                raise ValueError("Cyclic or shared GameObject hierarchy")
            seen.add(obj.path_id)
            if obj.type.name != "GameObject":
                raise ValueError("Expected a prefab GameObject")
            tree = obj.read_typetree()
            kept = []
            transform_count = 0
            for entry in tree["m_Component"]:
                component = self.resolve(entry.get("component", entry.get("m_Component")))
                kind = component.type.name
                if kind in {"SkinnedMeshRenderer", "Animator", "Animation", "Cloth"}:
                    raise ValueError("Animated/skinned models are not supported yet; select a static prefab")
                if kind not in COMPONENTS:
                    self.excluded[kind] += 1
                    continue
                values = component.read_typetree()
                if kind == "Transform":
                    transform_count += 1
                    for child in values["m_Children"]:
                        child_transform = self.resolve(child)
                        queue.append(self.resolve(child_transform.read_typetree()["m_GameObject"]))
                    if obj is root:
                        values["m_Father"] = dict(NULL)
                        values["m_LocalPosition"] = {"x": 0.0, "y": 0.0, "z": 0.0}
                if kind == "MeshRenderer":
                    if values.get("m_StaticBatchInfo", {}).get("subMeshCount", 0):
                        raise ValueError("Static-batched renderers need a dedicated mesh reconstruction")
                    for field in ("m_StaticBatchRoot", "m_ProbeAnchor", "m_LightProbeVolumeOverride"):
                        if field in values:
                            values[field] = dict(NULL)
                    for field in ("m_LightmapIndex", "m_LightmapIndexDynamic"):
                        if field in values:
                            values[field] = 65535
                self.add(component, values)
                kept.append(entry)
            if transform_count != 1:
                raise ValueError("Expected exactly one Transform per GameObject")
            tree["m_Component"] = kept
            tree["m_Layer"] = 0
            tree["m_Tag"] = 0
            self.add(obj, tree)

    def dependencies(self):
        queue = list(self.selected)
        while queue:
            obj_id = queue.pop()
            for pointer in pointers(self.trees[obj_id]):
                target = self.resolve(pointer)
                if target is None or target.path_id in self.selected:
                    continue
                kind = target.type.name
                if kind not in DEPENDENCIES:
                    raise ValueError(f"Unsupported visual dependency: {kind}")
                tree = target.read_typetree()
                if kind == "Material":
                    self.materials.append(tree["m_Name"])
                    # Compiled game shaders are not portable editor shader source.
                    tree["m_Shader"] = dict(NULL)
                    if tree.get("m_Parent", {}).get("m_PathID"):
                        raise ValueError("Material variants require explicit flattening")
                    for key in ("m_ValidKeywords", "m_InvalidKeywords", "disabledShaderPasses"):
                        if key in tree:
                            tree[key] = []
                    maps = tree["m_SavedProperties"]["m_TexEnvs"]
                    self.omitted_maps.update(key for key, value in maps if key != "_MainTex" and value["m_Texture"]["m_PathID"])
                    tree["m_SavedProperties"]["m_TexEnvs"] = [(key, value) for key, value in maps if key == "_MainTex"]
                self.add(target, tree)
                queue.append(target.path_id)
        if not any(o.type.name == "Mesh" for o in self.selected.values()):
            raise ValueError("The prefab has no supported static mesh")

    def write(self, destination):
        from UnityPy.helpers.ResourceReader import get_resource_data
        for obj_id, obj in self.selected.items():
            tree = self.trees[obj_id]
            stream = tree.get("m_StreamData")
            if stream and stream.get("size"):
                payload = get_resource_data(stream["path"], self.collection, stream["offset"], stream["size"])
                if len(payload) != stream["size"]:
                    raise ValueError("Incomplete streamed mesh or texture data")
                if obj.type.name == "Texture2D":
                    tree["image data"] = payload
                elif obj.type.name == "Mesh":
                    tree["m_VertexData"]["m_DataSize"] = list(payload)
                else:
                    raise ValueError("Unsupported streamed asset")
                stream.update(path="", offset=0, size=0)
            obj.save_typetree(tree)
        # Only the selected objects are written. Do not retain the full catalog,
        # MonoScripts, type metadata for unrelated scripts, or external imports.
        used_types = sorted({o.type_id for o in self.selected.values()})
        type_map = {old: new for new, old in enumerate(used_types)}
        self.collection.types = [self.collection.types[i] for i in used_types]
        for obj in self.selected.values():
            obj.type_id = type_map[obj.type_id]
        self.collection.objects = dict(self.selected)
        self.collection.externals = []
        self.collection.script_types = []
        self.collection.ref_types = []
        destination.write_bytes(self.collection.save())


def select_model(data, name, destination):
    api = unitypy()
    manifest = data / "StreamingAssets/SoftRef/manifest_extended"
    entry = find_prefab(manifest_entries(manifest), name)
    source = manifest.parent / "Bundles" / entry["bundle"]
    env = api.load(str(source))
    roots = [(collection, info.asset.deref())
             for collection, container in collection_objects(env)
             for path, info in container if path.casefold() == entry["path"].casefold()]
    if len(roots) != 1:
        raise ValueError("The exact prefab root could not be resolved")
    collection, root = roots[0]
    selection = StaticSelection(collection)
    selection.hierarchy(root)
    selection.dependencies()
    result = {"prefab": root.read_typetree()["m_Name"], "asset_path": entry["path"],
              "unity_version": str(collection.unity_version), "source": stamp(source),
              "objects": dict(Counter(o.type.name for o in selection.selected.values())),
              "excluded_components": dict(selection.excluded), "materials": selection.materials,
              "omitted_texture_properties": sorted(selection.omitted_maps),
              "unitypy_version": api.__version__}
    selection.write(destination)
    del selection, env, collection, root, roots
    gc.collect()
    return result


def prepare_output(path, data):
    if path is None:
        parent = persistent_cache_root() / "exports"
        parent.mkdir(exist_ok=True)
        return Path(tempfile.mkdtemp(prefix="model-", dir=parent))
    path = Path(path).expanduser().resolve()
    if path.is_relative_to(data.parent) or any((p / ".git").exists() for p in (path, *path.parents)):
        raise ValueError("Export outside the game installation and Git repositories")
    path.mkdir(parents=True, exist_ok=False)
    return path


def collect_export(project, output, name):
    source = project / "ExportedProject/Assets"
    if not source.is_dir():
        raise ValueError("AssetRipper did not produce ExportedProject/Assets")
    # Copy only supported editor assets; never ship reconstructed game scripts.
    files = [p for p in source.rglob("*") if p.is_file() and p.suffix != ".meta"]
    if not files or any(p.suffix.lower() not in {".prefab", ".asset", ".mat", ".png", ".tga", ".jpg", ".jpeg", ".exr"} for p in files):
        raise ValueError("Unexpected AssetRipper output; inspect it before sharing")
    prefabs = [p for p in files if p.suffix == ".prefab"]
    if len(prefabs) != 1:
        raise ValueError("Expected exactly one exported model prefab")
    target = output / "Assets/ValheimModels" / name
    shader_guid = hashlib.sha256(f"ValheimModelExport/{name}/Preview".encode()).hexdigest()[:32]
    target.mkdir(parents=True)
    for path in files:
        relative = path.relative_to(source)
        dest = target / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)
        shutil.copyfile(Path(str(path) + ".meta"), Path(str(dest) + ".meta"))
        if dest.suffix == ".mat":
            text = dest.read_text(encoding="utf-8-sig")
            text, count = re.subn(r"(?m)^  m_Shader:.*$", f"  m_Shader: {{fileID: 4800000, guid: {shader_guid}, type: 3}}", text)
            if count != 1:
                raise ValueError("Unexpected material YAML")
            dest.write_text(text, encoding="utf-8")
    shader = target / "ModelPreview.shader"
    shutil.copyfile(ASSETS / "ModelPreview.shader", shader)
    Path(str(shader) + ".meta").write_text(f"fileFormatVersion: 2\nguid: {shader_guid}\nShaderImporter:\n  externalObjects: {{}}\n  defaultTextures: []\n  nonModifiableTextures: []\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n", encoding="utf-8")
    return target / prefabs[0].relative_to(source)


def package_assets(output, destination):
    """Create a Unity custom package; only selected asset bytes and their metadata."""
    files = sorted(p for p in (output / "Assets").rglob("*") if p.is_file() and p.suffix != ".meta")
    # Native Unity packages include folder assets, not just files with nested paths.
    folders = sorted(p for p in (output / "Assets").rglob("*") if p.is_dir())
    for folder in folders:
        meta = Path(str(folder) + ".meta")
        if not meta.exists():
            guid = hashlib.sha256(f"ValheimModelExport/{folder.relative_to(output).as_posix()}".encode()).hexdigest()[:32]
            meta.write_text(f"fileFormatVersion: 2\nguid: {guid}\nfolderAsset: yes\nDefaultImporter:\n  externalObjects: {{}}\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n", encoding="utf-8")
    entries = []
    guids = set()
    for path in [*folders, *files]:
        meta = Path(str(path) + ".meta").read_bytes()
        match = re.search(rb"(?m)^guid: ([0-9a-f]{32})\s*$", meta)
        if not match or match[1] in guids:
            raise ValueError("Missing or duplicate Unity asset GUID")
        guids.add(match[1])
        entries.append((match[1].decode(), path, meta))
    for _, path, _ in entries:
        if path.suffix in {".prefab", ".asset", ".mat"}:
            payload = path.read_bytes()
            if not payload.startswith(b"%YAML"):
                raise ValueError("Unexpected non-YAML native asset")
            for guid in re.findall(rb"guid: ([0-9a-f]{32})", payload):
                if guid not in guids and guid != b"0" * 32:
                    raise ValueError("Unresolved exported asset GUID")
    # Unity expects the gzip payload's original filename to identify a tar archive.
    with destination.open("wb") as output_stream, \
         gzip.GzipFile(filename="archtemp.tar", mode="wb", fileobj=output_stream) as compressed, \
         tarfile.open(fileobj=compressed, mode="w", format=tarfile.GNU_FORMAT) as archive:
        modified = int(time.time())
        for guid, path, meta in entries:
            directory = tarfile.TarInfo(guid + "/")
            directory.type = tarfile.DIRTYPE
            directory.mode = 0o755
            directory.mtime = modified
            archive.addfile(directory)
            members = [("asset.meta", meta), ("pathname", path.relative_to(output).as_posix().encode())]
            if path.is_file():
                members.insert(0, ("asset", path.read_bytes()))
            for leaf, payload in members:
                member = tarfile.TarInfo(f"{guid}/{leaf}")
                member.size = len(payload)
                member.mode = 0o644
                member.mtime = modified
                archive.addfile(member, io.BytesIO(payload))
    return len(files)


def export_model(data, name, tool=None, base=None, output=None):
    folder = prepare_output(output, data)
    print("Selecting static prefab and visual dependencies...", file=sys.stderr)
    with tempfile.TemporaryDirectory(prefix="valheim-model-work-") as work:
        work = Path(work)
        selected = work / "selected.assets"
        provenance = select_model(data, name, selected)
        name = safe_name(provenance["prefab"])
        with ar.session(base, tool) as address:
            ar.load(address, [selected])
            ar.request(address, "/Export/UnityProject", {"Path": str(work / "export")}, timeout=300)
        prefab = collect_export(work / "export", folder, name)
    package = folder / f"{name}.unitypackage"
    count = package_assets(folder, package)
    provenance.update({"package": str(package), "prefab_file": str(prefab), "asset_count": count,
                       "package_sha256": digest(package), "exporter": "AssetRipper Unity project export (static selection)",
                       "limits": ["Static visual model, not a working gameplay prefab", "No scripts, colliders, physics, audio, particles, or animation",
                                  "Preview shader replaces Valheim shaders; rain/snow and other game effects are not reproduced",
                                  "Only base textures (_MainTex) are included; normal, emission, and shader-specific maps are omitted",
                                  "Root position reset to zero; child transforms and active states retained"],
                       "scripts_sha256": {p.name: digest(p) for p in (Path(__file__), Path(ar.__file__), ASSETS / "ModelPreview.shader")}})
    save_json(folder / "provenance.json", provenance)
    (folder / "IMPORT.md").write_text(
        f"# {name}: Unity visual model\n\n"
        f"Import `{package.name}` with **Assets > Import Package > Custom Package**.\n"
        f"Use a separate Unity {provenance['unity_version']} or compatible newer 6.x Built-in Render Pipeline project.\n"
        f"Open `{prefab.relative_to(folder).as_posix()}` or drag it into a scene.\n\n"
        "This is a static inspection export, not the original authoring project or a playable mod.\n"
        "The supplied preview shader approximates diffuse lighting; original game shader effects are not reconstructed.\n"
        "Base textures and tint are retained; normal, emission, and shader-specific maps are not included.\n"
        "URP/HDRP need material conversion. Inactive visual variants remain inactive.\n"
        "The game installation is unchanged. Keep game-owned assets local; do not include them in the skill repository or publish them.\n",
        encoding="utf-8")
    return provenance


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Exact static prefab name or catalog asset path")
    parser.add_argument("--game")
    parser.add_argument("--output", type=Path, help="New directory outside the game and repositories; default: persistent local cache")
    service = parser.add_mutually_exclusive_group(required=True)
    service.add_argument("--tool", help="AssetRipper executable; run a hidden task-owned service")
    service.add_argument("--base-url", help="Dedicated loopback service; loading replaces its current session")
    args = parser.parse_args()
    try:
        print_json(export_model(game_data(args.game), args.name, args.tool, args.base_url, args.output))
    except (OSError, ValueError, KeyError, ImportError, NotImplementedError) as error:
        parser.exit(1, f"Model export failed: {error}\n")


if __name__ == "__main__":
    main()
