#!/usr/bin/env python3
"""Test distribution and real template behavior without changing a live profile."""

import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path
from zipfile import ZipFile

from package_skill import FILES, SKILL_ROOT, TEMPLATE, build_archive, load_sources, validate_sources


WITH_GAME = "--with-game" in sys.argv
if WITH_GAME:
    sys.argv.remove("--with-game")


def run(*args, success=True):
    """Run a bounded command and expose its output only on unexpected failure."""
    result = subprocess.run(args, capture_output=True, text=True, timeout=180)
    if (result.returncode == 0) != success:
        raise AssertionError(f"Unexpected exit {result.returncode}:\n{result.stdout}\n{result.stderr}")
    return result.stdout + result.stderr


class DistributionTests(unittest.TestCase):
    """Keep cache files and accidental private content out of distribution."""

    def test_sources(self):
        """Validate real source files, including all local heading links."""
        validate_sources(load_sources(SKILL_ROOT))

    def test_archive_is_reproducible_and_excludes_unlisted_files(self):
        """Package from an extracted copy with an injected cache and extra file."""
        with tempfile.TemporaryDirectory(prefix="valheim-skill-test-") as temp:
            root = Path(temp)
            build_archive(SKILL_ROOT, root / "original.zip")
            with ZipFile(root / "original.zip") as archive:
                archive.extractall(root / "extracted")
            source = root / "extracted/valheim-modding"
            cache = source / TEMPLATE / "obj/private.cache"
            cache.parent.mkdir()
            cache.write_text("not for distribution", encoding="utf-8")
            (source / "unreviewed.txt").write_text("exclude me", encoding="utf-8")
            build_archive(source, root / "repeat.zip")
            self.assertEqual((root / "original.zip").read_bytes(), (root / "repeat.zip").read_bytes())
            with ZipFile(root / "repeat.zip") as archive:
                self.assertEqual(len(FILES), len(archive.namelist()))
                self.assertIn("valheim-modding/" + TEMPLATE + ".template.config/template.json", archive.namelist())

    def test_broken_reference_is_rejected(self):
        """A missing shipped resource must fail even if a source cache exists."""
        files = load_sources(SKILL_ROOT)
        files["SKILL.md"] += b"\n[Broken](references/missing.md)\n"
        with self.assertRaisesRegex(ValueError, "Broken local link"):
            validate_sources(files)

    def test_broken_anchor_is_rejected(self):
        """Keep the task router's section links usable."""
        files = load_sources(SKILL_ROOT)
        files["SKILL.md"] += b"\n[Broken](references/environment.md#missing-heading)\n"
        with self.assertRaisesRegex(ValueError, "Broken heading link"):
            validate_sources(files)

    def test_personal_path_is_rejected(self):
        """Reject accidental absolute home paths without echoing their contents."""
        with tempfile.TemporaryDirectory(prefix="valheim-skill-test-") as temp:
            root = Path(temp)
            build_archive(SKILL_ROOT, root / "skill.zip")
            with ZipFile(root / "skill.zip") as archive:
                archive.extractall(root)
            source = root / "valheim-modding"
            path = source / "references/sources.md"
            path.write_text("Local file: C:/Users/ExamplePerson/private/file.txt", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Absolute personal path"):
                load_sources(source)


class TemplateTests(unittest.TestCase):
    """Generate and optionally compile mods using a private template registry."""

    @classmethod
    def setUpClass(cls):
        """Register only a clean extracted template, never the global registry."""
        if not shutil.which("dotnet"):
            raise RuntimeError("Install the .NET 10 SDK to run template tests")
        cls.temp = tempfile.TemporaryDirectory(prefix="valheim-template-test-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.root = Path(cls.temp.name)
        cls.hive = cls.root / "hive"
        build_archive(SKILL_ROOT, cls.root / "skill.zip")
        with ZipFile(cls.root / "skill.zip") as archive:
            archive.extractall(cls.root / "source")
        run("dotnet", "new", "install", str(cls.root / "source/valheim-modding" / TEMPLATE),
            "--debug:custom-hive", str(cls.hive), "--force")

    def generate(self, name, version=None):
        """Create a neutral test mod with optional version substitution."""
        project = self.root / name
        args = ["dotnet", "new", "valheim-mod", "-n", name, "-o", str(project),
                "--pluginId", "org.example.testmod", "--modAuthor", "Example Team",
                "--debug:custom-hive", str(self.hive), "--no-update-check"]
        if version:
            args += ["--modVersion", version]
        run(*args)
        return project

    def test_generated_versions_and_metadata(self):
        """Keep release versions aligned without changing dependency versions."""
        for custom, expected in ((None, "1.0.0"), ("1.0.1", "1.0.1")):
            with self.subTest(version=expected):
                name = "DefaultMod" if custom is None else "PatchMod"
                project = self.generate(name, custom)
                manifest = json.loads((project / "manifest.json").read_text())
                self.assertEqual(manifest["version_number"], expected)
                self.assertEqual(manifest["name"], name)
                plugin = (project / "Plugin.cs").read_text()
                self.assertIn(f'PluginVersion = "{expected}"', plugin)
                self.assertIn('PluginGuid = "org.example.testmod"', plugin)
                assembly = (project / "Properties/AssemblyInfo.cs").read_text()
                for attribute, value in (("AssemblyVersion", expected + ".*"),
                                         ("AssemblyFileVersion", expected),
                                         ("AssemblyInformationalVersion", expected)):
                    self.assertIn(f'{attribute}("{value}")', assembly)
                self.assertIn("## " + expected, (project / "CHANGELOG.md").read_text())
                csproj = ET.parse(project / (name + ".csproj"))
                self.assertEqual("1.0.0", csproj.find(".//PackageReference[@Include='HarmonyValidator']").get("Version"))
                self.assertEqual("false", csproj.findtext(".//DeployOnBuild"))
                self.assertFalse((project / ".template.config").exists())
                self.assertFalse((project / "obj").exists())
                self.assertTrue((project / ".gitignore").exists())

    @unittest.skipUnless(WITH_GAME, "Use --with-game and local game paths for build checks")
    def test_build_deploy_and_package(self):
        """Test opt-in deployment and a ZIP built from actual game references."""
        for variable in ("VALHEIM_PATH", "BEPINEX_PATH"):
            self.assertTrue(os.environ.get(variable), f"Set {variable} for --with-game")
        project = self.generate("BuildCheck")
        csproj = str(project / "BuildCheck.csproj")
        deploy = self.root / "isolated-profile/plugins/BuildCheck"
        props = ["-p:Configuration=Release", f"-p:ModDeployPath={deploy}"]
        managed = os.environ.get("VALHEIM_MANAGED_PATH")
        if managed:
            props.append(f"-p:ValheimManagedPath={managed}")
        run("dotnet", "build", csproj, *props)
        self.assertFalse(deploy.exists(), "A normal build must not deploy")
        dll = project / "bin/Release/net48/BuildCheck.dll"
        self.assertTrue(dll.is_file())
        run("dotnet", "build", csproj, *props, "-p:DeployOnBuild=true")
        self.assertEqual(dll.read_bytes(), (deploy / "BuildCheck.dll").read_bytes())
        self.assertEqual(["BuildCheck.dll"], [p.name for p in deploy.iterdir()])
        package = ["dotnet", "msbuild", csproj, "-restore", "-t:PackageMod", *props,
                   "-p:DeployOnBuild=false"]
        failure = run(*package, success=False)
        self.assertIn("icon.png", failure)
        self.assertFalse((project / "artifacts/BuildCheck.zip").exists())
        # A generated test-only PNG fixture, never shipped as a mod icon.
        def chunk(kind, data):
            """Encode one PNG chunk with its checksum."""
            return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
        pixels = (b"\x00" + b"\xff\xff\xff" * 256) * 256
        png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">2I5B", 256, 256, 8, 2, 0, 0, 0))
        (project / "icon.png").write_bytes(png + chunk(b"IDAT", zlib.compress(pixels)) + chunk(b"IEND", b""))
        run(*package)
        with ZipFile(project / "artifacts/BuildCheck.zip") as archive:
            entries = {p.filename for p in archive.infolist() if not p.is_dir()}
            self.assertEqual(entries, {"manifest.json", "icon.png", "README.md", "CHANGELOG.md",
                                       "LICENSE", "BepInEx/plugins/BuildCheck/BuildCheck.dll"})
            self.assertEqual(archive.read("BepInEx/plugins/BuildCheck/BuildCheck.dll"), dll.read_bytes())
            self.assertEqual(json.loads(archive.read("manifest.json"))["version_number"], "1.0.0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
