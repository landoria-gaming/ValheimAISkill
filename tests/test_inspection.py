#!/usr/bin/env python3
"""Exercise inspection helpers with synthetic data; no game installation required."""

import io
import copy
from contextlib import nullcontext
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "src/scripts"
sys.path.insert(0, str(SCRIPTS))

import asset_index
import asset_ripper
import inspect_assets
import inspect_code
import export_model
import inspection_common
from inspection_common import game_data
from PIL import Image


class MetadataTests(unittest.TestCase):
    def test_localization_csv_and_missing_tokens(self):
        text = '\"\",\"English\",\"French\"\nitem_wood,Wood,Bois\nitem_test,\"A, B\",Test\n//comment,skip,skip\n'
        translations = asset_index.parse_localization(text)
        self.assertEqual(translations, {"item_wood": "Wood", "item_test": "A, B"})
        self.assertEqual(asset_index.localize_name("$item_wood (2)", translations), "Wood (2)")
        self.assertEqual(asset_index.localize_name("Plain name", translations), "Plain name")
        self.assertIsNone(asset_index.localize_name("$item_unknown", translations))

    def test_exact_prefab_and_ambiguity(self):
        rows = [{"path": "Assets/Items/Wood.prefab"}, {"path": "Assets/Props/Wood.prefab"}]
        self.assertEqual(asset_index.find_prefab(rows, rows[0]["path"]), rows[0])
        with self.assertRaisesRegex(ValueError, "found 2"):
            asset_index.find_prefab(rows, "Wood")
        with self.assertRaisesRegex(ValueError, "found 0"):
            asset_index.find_prefab(rows, "NotWood")

    def test_name_fields_do_not_use_descriptions_or_internal_object_name(self):
        values = [(1, {"m_Name": "Internal", "m_description": "$item_wood"}),
                  (2, {"m_itemData": {"m_shared": {"m_name": "$item_wood"}}}),
                  (3, {"m_name": "$item_wood"})]
        self.assertEqual(asset_index.name_tokens(None, values), ["$item_wood"])

    def test_null_icon_pointer_stays_absent(self):
        self.assertIsNone(asset_index.pointer_target(None, {"m_FileID": 0, "m_PathID": 0}))

    def test_game_client_server_data_and_mac_layouts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for layout in ("valheim_Data", "valheim_server_Data", "Valheim.app/Contents/Resources/Data"):
                game = root / layout.split("/")[0].replace(".", "-")
                data = game / layout
                (data / "Managed").mkdir(parents=True)
                (data / "Managed/assembly_valheim.dll").touch()
                (data / "resources.assets").touch()
                # Windows short paths and macOS /var aliases resolve to the same
                # directory but do not have identical textual representations.
                self.assertEqual(game_data(str(game)), data.resolve())
                self.assertEqual(game_data(str(data)), data.resolve())

    def test_game_gate_rejects_detached_dlls_and_missing_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaisesRegex(ValueError, "missing or inaccessible"):
                game_data(str(root))
            (root / "Managed").mkdir()
            (root / "Managed/assembly_valheim.dll").touch()
            with self.assertRaisesRegex(ValueError, "assets are missing"):
                game_data(str(root))

    def test_bundle_directory_without_decompressing_payload(self):
        directory = b"\0" * 16 + struct.pack(">II", 0, 1) + struct.pack(">qqI", 0, 1000000, 4) + b"CAB-test\0"
        header = b"UnityFS\0" + struct.pack(">I", 7) + b"2022.x\0" + b"6000.0.75f1\0"
        header += struct.pack(">QIII", 0, len(directory), len(directory), 0x40)
        header += b"\0" * (-len(header) % 16)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bundle"
            path.write_bytes(header + directory)
            self.assertEqual(asset_index.bundle_members(path), ["CAB-test"])


class AssetRipperTests(unittest.TestCase):
    def test_only_loopback(self):
        self.assertEqual(asset_ripper.validate_base("http://127.0.0.1:1234/"), "http://127.0.0.1:1234")
        for url in ("https://localhost:1", "http://example.com", "http://user@localhost", "http://localhost/a"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                asset_ripper.validate_base(url)

    def test_asset_id_precision(self):
        path_id = -3530902432537365392
        from urllib.parse import urlencode
        locator = {"C": {"B": {"P": [0]}, "I": 0}, "D": path_id}
        query = urlencode({"Path": json.dumps(locator)})
        page = f'<tr data-class="Sprite"><td><a href="/Assets/View?{query}">A &amp; B</a></td></tr>'
        with patch.object(asset_ripper, "request", return_value=page.encode()):
            row = asset_ripper.search("http://localhost:123", "test")[0]
        self.assertEqual(row["locator"]["D"], path_id)
        self.assertEqual(row["name"], "A & B")

    def test_non_png_response_rejected(self):
        with patch.object(asset_ripper, "request", return_value=b"missing dependency"):
            with self.assertRaisesRegex(ValueError, "PNG"):
                asset_ripper.export("http://localhost:123", {}, "png")

    def test_existing_service_is_not_started_or_stopped(self):
        with patch.object(asset_ripper.subprocess, "Popen") as process:
            with asset_ripper.session("http://localhost:123") as base:
                self.assertEqual(base, "http://localhost:123")
            process.assert_not_called()


class SpriteTests(unittest.TestCase):
    def fixture(self, flags=3):
        image = Image.new("RGBA", (8, 8), (0, 0, 0, 0))
        image.putpixel((2, 4), (255, 0, 0, 128))
        image.putpixel((3, 5), (0, 255, 0, 255))
        stream = io.BytesIO()
        image.save(stream, format="PNG")
        sprite = {"m_RD": {"m_TextureRect": {"m_X": 2, "m_Y": 2, "m_Width": 2, "m_Height": 2},
                           "m_SettingsRaw": flags}}
        return stream.getvalue(), sprite

    def test_atlas_crop_coordinates_and_alpha(self):
        result = inspect_assets.crop_sprite(*self.fixture())
        self.assertEqual(result.size, (2, 2))
        self.assertEqual(result.getpixel((0, 0)), (255, 0, 0, 128))
        self.assertEqual(result.getpixel((1, 1)), (0, 255, 0, 255))

    def test_packing_rotation(self):
        plain = inspect_assets.crop_sprite(*self.fixture())
        rotated = inspect_assets.crop_sprite(*self.fixture(3 | (4 << 2)))
        self.assertEqual(rotated.tobytes(), plain.transpose(Image.Transpose.ROTATE_90).tobytes())

    def test_tight_packing_rejected(self):
        with self.assertRaisesRegex(ValueError, "Tight-packed"):
            inspect_assets.crop_sprite(*self.fixture(1))

    def test_out_of_bounds_rejected(self):
        payload, sprite = self.fixture()
        sprite["m_RD"]["m_TextureRect"]["m_X"] = 7
        with self.assertRaisesRegex(ValueError, "does not fit"):
            inspect_assets.crop_sprite(payload, sprite)


class CodeCacheTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        env = patch.dict(inspection_common.os.environ, {"VALHEIM_SKILL_CACHE": tmp.name})
        env.start()
        self.addCleanup(env.stop)

    def test_cached_type_and_changed_dll(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dll = root / "sample.dll"
            dll.write_bytes(b"synthetic-v1")
            with patch.object(inspect_code.shutil, "which", return_value="ilspycmd"), \
                 patch.object(inspect_code, "run_ilspy", side_effect=lambda tool, args: "v1" if args == ["--version"] else "class Sample {}") as call:
                first, hit = inspect_code.inspect(dll, "type", "Sample")
                self.assertFalse(hit)
                repeat, hit = inspect_code.inspect(dll, "type", "Sample")
                self.assertTrue(hit)
                self.assertEqual(first, repeat)
                self.assertEqual(sum(args[0][1] != ["--version"] for args in call.call_args_list), 1)
                self.assertEqual(first.parent.parent.name, "code")
                first.write_text("damaged", encoding="utf-8")
                repaired, hit = inspect_code.inspect(dll, "type", "Sample")
                self.assertFalse(hit)
                self.assertEqual(repaired.read_text(), "class Sample {}")
                dll.write_bytes(b"synthetic-v2")
                changed, hit = inspect_code.inspect(dll, "type", "Sample")
                self.assertFalse(hit)
                self.assertNotEqual(first, changed)

    def test_types_are_requested_as_separate_supported_kinds(self):
        with tempfile.TemporaryDirectory() as tmp:
            dll = Path(tmp) / "kinds.dll"
            dll.write_bytes(b"fixture")
            with patch.object(inspect_code.shutil, "which", return_value="ilspycmd"), \
                 patch.object(inspect_code, "run_ilspy", return_value="fixture") as call:
                inspect_code.inspect(dll, "types")
            kinds = [c.args[1][1] for c in call.call_args_list if c.args[1][0] == "-l"]
            self.assertEqual(set(kinds), set("cised"))


class AssetExportCacheTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        env = patch.dict(inspection_common.os.environ, {"VALHEIM_SKILL_CACHE": str(self.root / "cache")})
        env.start()
        self.addCleanup(env.stop)
        self.source = self.root / "bundle"
        self.source.write_bytes(b"source")
        self.tool = self.root / "AssetRipper"
        self.tool.write_bytes(b"tool v1")
        for name, value in (("session", nullcontext("http://localhost:1")), ("load", None),
                            ("search", [{"class": "GameObject", "name": "Wood", "locator": {"D": -9007199254740993}}]),
                            ("export", b'{"m_Name":"Wood"}')):
            mock = patch.object(asset_ripper, name, return_value=value)
            setattr(self, name, mock.start())
            self.addCleanup(mock.stop)

    def run_export(self, **kwargs):
        return inspect_assets.export_asset([self.source], "Wood", tool=str(self.tool), **kwargs)

    def test_json_hit_does_not_start_load_or_search(self):
        first = self.run_export()
        repeat = self.run_export()
        self.assertFalse(first["cache_hit"])
        self.assertTrue(repeat["cache_hit"])
        self.assertEqual(first["path"], repeat["path"])
        self.assertEqual(repeat["asset"]["path_id"], -9007199254740993)
        for call in (self.session, self.load, self.search, self.export):
            self.assertEqual(call.call_count, 1)

    def test_changed_inputs_options_tool_and_corruption_miss(self):
        first = self.run_export()
        Path(first["path"]).write_bytes(b"broken")
        self.assertFalse(self.run_export()["cache_hit"])
        self.source.write_bytes(b"new source")
        changed = self.run_export()
        self.assertNotEqual(first["path"], changed["path"])
        self.tool.write_bytes(b"new tool build")
        changed_tool = self.run_export()
        self.assertNotEqual(changed["path"], changed_tool["path"])
        self.assertNotEqual(changed_tool["path"], self.run_export(path_id=-9007199254740993)["path"])

    def test_external_service_does_not_reuse_unverified_cache(self):
        for _ in range(2):
            result = inspect_assets.export_asset([self.source], "Wood", base="http://localhost:1")
            self.assertFalse(result["cache_hit"])
        self.assertEqual(self.load.call_count, 2)

    def test_resource_stream_change_invalidates(self):
        resource = self.root / "bundle.resS"
        resource.write_bytes(b"texture v1")
        first = self.run_export()
        resource.write_bytes(b"texture changed")
        second = self.run_export()
        self.assertFalse(second["cache_hit"])
        self.assertNotEqual(first["path"], second["path"])

    def test_ambiguous_query_is_not_cached(self):
        self.search.return_value *= 2
        with self.assertRaisesRegex(ValueError, "found 2"):
            self.run_export()
        self.assertFalse(list((self.root / "cache").rglob("provenance.json")))

    def test_inventory_icon_persistent_hit_and_damage(self):
        payload, sprite = SpriteTests().fixture()
        self.export.return_value = payload
        self.search.return_value = [{"class": "Sprite", "name": "Wood", "locator": {"D": 123}}]
        row = {"path": "Wood.prefab", "root_name": "Wood", "english_names": ["Wood"],
               "icons": [{"collection": "CAB-test", "path_id": 123}]}
        with patch.object(inspect_assets, "prefab_info", return_value=(row, self.source)), \
             patch.object(inspect_assets, "find_collection_bundle", return_value=self.source), \
             patch.object(asset_ripper, "asset_json", return_value=sprite):
            first = inspect_assets.inventory_icon(self.root, "Wood", tool=str(self.tool))
            self.assertFalse(first["cache_hit"])
            self.assertTrue(inspect_assets.inventory_icon(self.root, "Wood", tool=str(self.tool))["cache_hit"])
            self.assertEqual(self.load.call_count, 1)
            self.assertEqual(Path(first["path"]).parent.parent.name, "images")
            Path(first["path"]).write_bytes(b"broken PNG")
            self.assertFalse(inspect_assets.inventory_icon(self.root, "Wood", tool=str(self.tool))["cache_hit"])
            self.assertEqual(self.load.call_count, 2)


class PersistentCacheTests(unittest.TestCase):
    def test_windows_default_ignores_app_sandbox(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.dict(inspection_common.os.environ, {"LOCALAPPDATA": "redirected-app-cache"}, clear=True), \
                 patch.object(inspection_common.sys, "platform", "win32"), \
                 patch.object(inspection_common.Path, "home", return_value=Path(tmp)):
                self.assertEqual(inspection_common.persistent_cache_root(), (Path(tmp) / ".cache/valheim-ai-skill").resolve())

    def test_asset_index_reused_and_invalidated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundles = root / "bundles"
            bundles.mkdir()
            source = bundles / "fixture"
            source.write_bytes(b"v1")
            with patch.dict(inspection_common.os.environ, {"VALHEIM_SKILL_CACHE": str(root / "cache")}), \
                 patch.object(asset_index, "bundle_members", return_value=["CAB-test"]) as scan:
                asset_index.find_collection_bundle(bundles, "CAB-test")
                asset_index.find_collection_bundle(bundles, "CAB-test")
                self.assertEqual(scan.call_count, 1)
                self.assertEqual(len(list((root / "cache/indexes").glob("*/collections.json"))), 1)
                source.write_bytes(b"v2 changed")
                asset_index.find_collection_bundle(bundles, "CAB-test")
                self.assertEqual(scan.call_count, 2)

    def test_cache_override_outside_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".git").mkdir()
            with patch.dict(inspection_common.os.environ, {"VALHEIM_SKILL_CACHE": str(root / "cache")}):
                with self.assertRaisesRegex(ValueError, "outside Git"):
                    inspection_common.persistent_cache_root()
            with patch.dict(inspection_common.os.environ, {"VALHEIM_SKILL_CACHE": "relative/cache"}):
                with self.assertRaisesRegex(ValueError, "absolute"):
                    inspection_common.persistent_cache_root()

    def test_unspecified_work_cache_remains_temporary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.dict(inspection_common.os.environ, {"VALHEIM_SKILL_CACHE": str(root / "persistent")}), \
                 patch.object(inspection_common.tempfile, "gettempdir", return_value=str(root / "temp")):
                path = inspection_common.cache_dir(["fixture"])
                self.assertTrue(path.is_relative_to(root / "temp"))
                self.assertFalse((root / "persistent").exists())


class StaticModelTests(unittest.TestCase):
    @staticmethod
    def pointer(number, file_id=0):
        return {"m_FileID": file_id, "m_PathID": number}

    def fixture(self):
        ptr = self.pointer
        def obj(number, kind, tree):
            return SimpleNamespace(path_id=number, type=SimpleNamespace(name=kind),
                                   read_typetree=lambda: copy.deepcopy(tree))
        objects = {
            1: obj(1, "GameObject", {"m_Name": "Fixture", "m_IsActive": True, "m_Layer": 9, "m_Tag": 2,
                "m_Component": [{"component": ptr(i)} for i in (2, 3, 4, 5)]}),
            2: obj(2, "Transform", {"m_GameObject": ptr(1), "m_Children": [], "m_Father": ptr(0),
                "m_LocalPosition": {"x": 0, "y": 50, "z": 0}}),
            3: obj(3, "MeshFilter", {"m_GameObject": ptr(1), "m_Mesh": ptr(10)}),
            4: obj(4, "MeshRenderer", {"m_GameObject": ptr(1), "m_Materials": [ptr(20)]}),
            5: obj(5, "MonoBehaviour", {"m_Script": ptr(900)}),
            10: obj(10, "Mesh", {"m_Name": "Mesh"}),
            20: obj(20, "Material", {"m_Name": "Mat", "m_Shader": ptr(800), "m_SavedProperties": {
                "m_TexEnvs": [("_MainTex", {"m_Texture": ptr(30)}), ("_NoiseTex", {"m_Texture": ptr(700)})]}}),
            30: obj(30, "Texture2D", {"m_Name": "Base"}),
        }
        return export_model.StaticSelection(SimpleNamespace(objects=objects)), objects[1]

    def test_visual_dependency_closure_excludes_gameplay(self):
        selection, root = self.fixture()
        selection.hierarchy(root)
        selection.dependencies()
        self.assertEqual(set(selection.selected), {1, 2, 3, 4, 10, 20, 30})
        self.assertEqual(selection.excluded, {"MonoBehaviour": 1})
        self.assertEqual(selection.trees[2]["m_LocalPosition"]["y"], 0)
        self.assertTrue(selection.trees[1]["m_IsActive"])
        self.assertEqual(selection.trees[20]["m_Shader"], self.pointer(0))
        self.assertEqual(selection.omitted_maps, {"_NoiseTex"})

    def test_skinned_export_rejected_instead_of_silent_loss(self):
        selection, root = self.fixture()
        selection.collection.objects[5].type.name = "SkinnedMeshRenderer"
        with self.assertRaisesRegex(ValueError, "not supported yet"):
            selection.hierarchy(root)

    def test_missing_and_external_dependencies_fail(self):
        selection, root = self.fixture()
        selection.hierarchy(root)
        del selection.collection.objects[10]
        with self.assertRaisesRegex(ValueError, "Missing model dependency"):
            selection.dependencies()
        with self.assertRaisesRegex(ValueError, "External model dependency"):
            selection.resolve(self.pointer(10, 1))

    def test_refuses_existing_output_and_game_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "game/valheim_Data"
            data.mkdir(parents=True)
            with self.assertRaisesRegex(ValueError, "outside the game"):
                export_model.prepare_output(data / "export", data)
            existing = root / "existing"
            existing.mkdir()
            with self.assertRaises(FileExistsError):
                export_model.prepare_output(existing, data)

    def test_equivalent_game_path_is_rejected_before_creating_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            data = root / "game/valheim_Data"
            data.mkdir(parents=True)
            # Reproduce an unresolved alias on every OS, without symlink privileges.
            alias = root / "game/../game/valheim_Data"
            output = data / "export"
            with self.assertRaisesRegex(ValueError, "outside the game"):
                export_model.prepare_output(output, alias)
            self.assertFalse(output.exists())

    def test_unitypackage_members_and_broken_guid(self):
        import tarfile
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            assets = root / "Assets/Test"
            assets.mkdir(parents=True)
            asset = assets / "Test.asset"
            asset.write_bytes(b"%YAML 1.1\nfixture: true\n")
            guid = "123456789abcdef0123456789abcdef0"
            Path(str(asset) + ".meta").write_text(f"fileFormatVersion: 2\nguid: {guid}\n")
            package = root / "model.unitypackage"
            self.assertEqual(export_model.package_assets(root, package), 1)
            # A .unitypackage filename in the gzip header produces an empty
            # import in Unity 6.5; match Unity's embedded tar filename.
            self.assertEqual(package.read_bytes()[10:].split(b"\0", 1)[0], b"archtemp.tar")
            with tarfile.open(package) as archive:
                self.assertTrue({guid, *(f"{guid}/{n}" for n in ("asset", "asset.meta", "pathname"))}.issubset(archive.getnames()))
                self.assertEqual(archive.extractfile(f"{guid}/pathname").read(), b"Assets/Test/Test.asset")
                folder = next(m for m in archive if m.name.endswith("/asset.meta") and b"folderAsset: yes" in archive.extractfile(m).read())
                self.assertEqual(archive.extractfile(folder.name.replace("asset.meta", "pathname")).read(), b"Assets/Test")
            asset.write_bytes(b"%YAML 1.1\nreference: {guid: ffffffffffffffffffffffffffffffff}\n")
            with self.assertRaisesRegex(ValueError, "Unresolved"):
                export_model.package_assets(root, root / "bad.unitypackage")


if __name__ == "__main__":
    unittest.main(verbosity=2)
