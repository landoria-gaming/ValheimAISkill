#!/usr/bin/env python3
"""Exercise inspection helpers with synthetic data; no game installation required."""

import io
import json
from pathlib import Path
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/valheim-modding/scripts"
sys.path.insert(0, str(SCRIPTS))

import asset_index
import asset_ripper
import inspect_assets
import inspect_code
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

    def test_game_root_data_and_mac_layouts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for layout in ("valheim_Data", "Valheim.app/Contents/Resources/Data"):
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
