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

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "scripts/SkillPackage.proj"
SKILL_ROOT = ROOT / "src"
TEMPLATE = "assets/mod-template/"


WITH_GAME = "--with-game" in sys.argv
if WITH_GAME:
    sys.argv.remove("--with-game")


def run(*args, success=True, env=None):
    """Run a bounded command and expose its output only on unexpected failure."""
    result = subprocess.run(args, capture_output=True, text=True, timeout=180, env=env)
    if (result.returncode == 0) != success:
        raise AssertionError(f"Unexpected exit {result.returncode}:\n{result.stdout}\n{result.stderr}")
    return result.stdout + result.stderr


def package(source, destination, success=True):
    """Run the cross-platform MSBuild skill packager against a source folder."""
    return run("dotnet", "msbuild", str(PROJECT), "-t:package",
               f"-p:SkillSource={source}", f"-p:PackageFile={destination}", success=success)


class DistributionTests(unittest.TestCase):
    """Keep cache files and accidental private content out of distribution."""

    def test_daily_cache_cleanup_clears_results_once_and_preserves_metadata(self):
        """Clear all generated cache data once per date without losing install state."""
        with tempfile.TemporaryDirectory(prefix="valheim-cache-cleanup-test-") as temp:
            root = Path(temp) / "cache"
            (root / "code/1.0.0").mkdir(parents=True)
            (root / "exports/model").mkdir(parents=True)
            (root / "code/1.0.0/Game.cs").write_text("cached", encoding="utf-8")
            (root / "exports/model/model.unitypackage").write_text("cached", encoding="utf-8")
            installation = root / "installation.json"
            installation.write_text("{}", encoding="utf-8")
            (root / "last-cleanup.txt").write_text("2000-01-01\n", encoding="ascii")
            env = os.environ.copy()
            env["VALHEIM_SKILL_CACHE"] = str(root)
            script = SKILL_ROOT / "scripts/cleanup_cache.py"

            first = run(sys.executable, str(script), env=env)
            self.assertIn("removed 2 cache item", first)
            self.assertTrue(installation.is_file())
            self.assertRegex((root / "last-cleanup.txt").read_text(encoding="ascii").strip(), r"^\d{4}-\d{2}-\d{2}$")
            self.assertEqual(["installation.json", "last-cleanup.txt"], sorted(path.name for path in root.iterdir()))

            (root / "code").mkdir()
            (root / "code/new.cs").write_text("new cache", encoding="utf-8")
            second = run(sys.executable, str(script), env=env)
            self.assertIn("already completed", second)
            self.assertTrue((root / "code/new.cs").is_file())

    def test_sources(self):
        """Validate real source files, including all local heading links."""
        run("dotnet", "msbuild", str(PROJECT), "-t:ValidateSkill")

    def test_local_deploy_target_is_safe_without_mutating_installation(self):
        """Compile and validate local deploy paths without replacing the installed skill."""
        output = run("dotnet", "msbuild", str(PROJECT), "-t:ValidateLocalDeploy")
        self.assertIn("Local deployment is safe to run", output)

    def test_local_deploy_replaces_only_the_skill_directory(self):
        """Install into a temporary user profile and replace its old skill copy."""
        with tempfile.TemporaryDirectory(prefix="valheim-skill-deploy-test-") as temp:
            home = Path(temp) / "profile"
            destination = home / ".agents/skills/valheim-modding"
            destination.mkdir(parents=True)
            (destination / "old-skill-file.txt").write_text("old", encoding="utf-8")
            output = run("dotnet", "msbuild", str(PROJECT), "-t:TestDeployLocal",
                         f"-p:TestHomeDirectory={home}")
            self.assertIn("Installed the Valheim Modding skill", output)
            self.assertTrue((destination / "SKILL.md").is_file())
            self.assertTrue((destination / "README.md").is_file())
            self.assertFalse((destination / "old-skill-file.txt").exists())

    def test_archive_allowlist_excludes_unlisted_files(self):
        """Package from an extracted copy and exclude injected files and caches."""
        with tempfile.TemporaryDirectory(prefix="valheim-skill-test-") as temp:
            root = Path(temp)
            package(SKILL_ROOT, root / "original.zip")
            with ZipFile(root / "original.zip") as archive:
                original = {name: archive.read(name) for name in archive.namelist()}
                archive.extractall(root / "extracted")
            source = root / "extracted/valheim-modding"
            cache = source / TEMPLATE / "obj/private.cache"
            cache.parent.mkdir()
            cache.write_text("not for distribution", encoding="utf-8")
            (source / "unreviewed.txt").write_text("exclude me", encoding="utf-8")
            package(source, root / "repeat.zip")
            with ZipFile(root / "repeat.zip") as archive:
                self.assertEqual(set(archive.namelist()), set(original))
                self.assertEqual({name: archive.read(name) for name in archive.namelist()}, original)
                self.assertNotIn("valheim-modding/unreviewed.txt", archive.namelist())
                self.assertIn("valheim-modding/" + TEMPLATE + ".template.config/template.json", archive.namelist())
                self.assertIn("valheim-modding/README.md", archive.namelist())
                json.loads(archive.read("valheim-modding/" + TEMPLATE + "manifest.json"))

    def test_broken_reference_is_rejected(self):
        """A missing shipped resource must fail even if a source cache exists."""
        with tempfile.TemporaryDirectory(prefix="valheim-skill-test-") as temp:
            root = Path(temp)
            with ZipFile(root / "skill.zip", "w") as archive:
                pass
            source = root / "source"
            shutil.copytree(SKILL_ROOT, source, ignore=shutil.ignore_patterns("obj", "bin", "__pycache__"))
            with (source / "SKILL.md").open("a", encoding="utf-8") as entry:
                entry.write("\n[Broken](references/missing.md)\n")
            self.assertIn("Broken local link", package(source, root / "broken.zip", success=False))

    def test_broken_anchor_is_rejected(self):
        """Keep the task router's section links usable."""
        with tempfile.TemporaryDirectory(prefix="valheim-skill-test-") as temp:
            root = Path(temp)
            source = root / "source"
            shutil.copytree(SKILL_ROOT, source, ignore=shutil.ignore_patterns("obj", "bin", "__pycache__"))
            with (source / "SKILL.md").open("a", encoding="utf-8") as entry:
                entry.write("\n[Broken](references/environment.md#missing-heading)\n")
            self.assertIn("Broken heading link", package(source, root / "broken.zip", success=False))

    def test_personal_path_is_rejected(self):
        """Reject accidental absolute home paths without echoing their contents."""
        with tempfile.TemporaryDirectory(prefix="valheim-skill-test-") as temp:
            root = Path(temp)
            package(SKILL_ROOT, root / "skill.zip")
            with ZipFile(root / "skill.zip") as archive:
                archive.extractall(root)
            source = root / "valheim-modding"
            path = source / "references/sources.md"
            path.write_text("Local file: C:/Users/ExamplePerson/private/file.txt", encoding="utf-8")
            self.assertIn("Personal absolute path", package(source, root / "private.zip", success=False))


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
        package(SKILL_ROOT, cls.root / "skill.zip")
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
