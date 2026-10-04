#!/usr/bin/env python3
"""List game DLLs, find types, and inspect C# or IL with ILSpyCMD, without execution."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import uuid

from inspection_common import (cache_dir, cached_result, digest, game_data,
                               persistent_cache_root, print_json, save_bytes, save_json, stamp)


def run_ilspy(executable, arguments):
    result = subprocess.run([executable, *arguments], capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=180)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "ILSpyCMD failed")
    return result.stdout


def decompiled_version(tool, assembly, managed):
    source = run_ilspy(tool, ["-t", "Version", "-r", str(managed), str(assembly)])
    match = re.search(
        r"CurrentVersion\s*\{\s*get;\s*\}\s*=\s*new GameVersion\(([^)]*)\)", source)
    if not match:
        raise ValueError("Could not read the game version from the Version type in assembly_valheim.dll")
    components = [part.strip() for part in match.group(1).split(",")]
    if not components or any(not part.isdigit() for part in components):
        raise ValueError("The decompiled game version has an unexpected format")
    return ".".join(components)


def _project_manifest(folder, identity):
    manifest_path = folder / "cache_manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("source") != identity:
            return None
        files = manifest.get("files")
        if not isinstance(files, list) or not files:
            return None
        actual = sorted(path.relative_to(folder).as_posix()
                        for path in folder.rglob("*.cs") if path.is_file())
        expected = sorted(entry["path"] for entry in files)
        if actual != expected:
            return None
        for entry in files:
            path = folder / entry["path"]
            if not path.is_file() or path.stat().st_size != entry["bytes"] or digest(path) != entry["sha256"]:
                return None
        return manifest
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        return None


def decompile_project(game, executable="ilspycmd"):
    """Decompile the core game projects once per exact build into persistent storage."""
    data = game_data(game)
    managed = data / "Managed"
    tool = shutil.which(executable)
    if not tool:
        raise ValueError("ILSpyCMD is missing. Install the official ilspycmd .NET tool first")
    tool_version = run_ilspy(tool, ["--version"]).strip()
    names = ["assembly_valheim.dll", "assembly_utils.dll", "assembly_guiutils.dll"]
    assemblies = {name: managed / name for name in names}
    missing = [str(path) for path in assemblies.values() if not path.is_file()]
    if missing:
        raise ValueError("Required Valheim assemblies are missing: " + ", ".join(missing))
    version = decompiled_version(tool, assemblies["assembly_valheim.dll"], managed)
    references = [stamp(path) for path in sorted(managed.glob("*.dll"))]
    identity = {
        "format": "valheim-ilspy-project-v1",
        "game_version": version,
        "assemblies": {name: digest(path) for name, path in assemblies.items()},
        "references": references,
        "ilspy_version": tool_version,
    }
    key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode("utf-8")).hexdigest()[:24]
    cache_base = persistent_cache_root() / "code" / "valheim"
    cache_base.mkdir(parents=True, exist_ok=True)
    target = cache_base / f"{version}-{key}"
    cached = _project_manifest(target, identity)
    if cached:
        return {"game_version": version, "cache_hit": True, "cache_dir": str(target),
                "assemblies": names, "csharp_files": len(cached["files"]),
                "total_bytes": sum(entry["bytes"] for entry in cached["files"])}

    if target.exists():
        # Preserve damaged or incomplete entries for recovery instead of deleting them.
        invalid = cache_base / f"{version}-{key}.invalid-{uuid.uuid4().hex[:8]}"
        target.replace(invalid)
    stage = Path(tempfile.mkdtemp(prefix=f".{version}-{key}-", dir=cache_base))
    try:
        for index, (name, assembly) in enumerate(assemblies.items(), 1):
            output = stage / Path(name).stem
            output.mkdir()
            print(f"Decompiling {name} ({index}/{len(assemblies)})...", flush=True)
            result = subprocess.run(
                [tool, "-p", "--nested-directories", "--disable-updatecheck", "-r",
                 str(managed), "-o", str(output), str(assembly)],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
            if result.returncode:
                raise ValueError(result.stderr.strip() or f"ILSpyCMD failed for {name}")
        files = []
        for path in sorted(stage.rglob("*.cs")):
            if path.is_file():
                files.append({"path": path.relative_to(stage).as_posix(),
                              "bytes": path.stat().st_size, "sha256": digest(path)})
        if not files:
            raise ValueError("ILSpyCMD completed without producing C# source files")
        save_json(stage / "cache_manifest.json", {"source": identity, "files": files})
        stage.replace(target)
    except Exception:
        # Keep failed output in the cache area for diagnosis, but never mark it reusable.
        raise
    finally:
        if stage.exists():
            failed = cache_base / f"{stage.name}.incomplete"
            stage.replace(failed)
    return {"game_version": version, "cache_hit": False, "cache_dir": str(target),
            "assemblies": names, "csharp_files": len(files),
            "total_bytes": sum(entry["bytes"] for entry in files)}


def inspect(assembly, action, type_name=None, il=False, executable="ilspycmd"):
    assembly = Path(assembly).resolve(strict=True)
    tool = shutil.which(executable)
    if not tool:
        raise ValueError("ILSpyCMD is missing. Install the official ilspycmd .NET tool first")
    version = run_ilspy(tool, ["--version"]).strip()
    identity = {"script": digest(__file__), "assembly_sha256": digest(assembly),
                "references": [stamp(p) for p in sorted(assembly.parent.glob("*.dll"))],
                "tool": version, "action": action, "type": type_name, "il": il}
    folder = cache_dir(identity, persistent=True, category="code")
    output = folder / ("types.txt" if action == "types" else "type.il" if il else "type.cs")
    hit = cached_result(output, identity) is not None
    if not hit:
        if action == "types":
            text = "".join(run_ilspy(tool, ["-l", kind, str(assembly)]) for kind in "cised")
        else:
            args = ["-t", type_name, *(["--ilcode"] if il else [])]
            text = run_ilspy(tool, [*args, "-r", str(assembly.parent), str(assembly)])
        save_bytes(output, text.encode("utf-8"))
        save_json(folder / "provenance.json", {"source": identity, "output_sha256": digest(output)})
    return output, hit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game")
    parser.add_argument("--ilspy", default="ilspycmd")
    parser.add_argument("--assembly", help="DLL name in Managed, or an explicit DLL path")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("assemblies", help="List local DLL paths and SHA-256 fingerprints")
    types = sub.add_parser("types", help="List classes, interfaces, structs, enums, delegates")
    types.add_argument("--query", default="")
    single = sub.add_parser("type", help="Decompile one exact type into the persistent local cache")
    single.add_argument("name")
    single.add_argument("--il", action="store_true")
    single.add_argument("--query", help="Show matching lines from the extracted type")
    single.add_argument("--print", action="store_true", dest="show")
    sub.add_parser("decompile", help="Cache the core Valheim C# projects by exact game build")
    args = parser.parse_args()
    try:
        explicit = Path(args.assembly) if args.assembly else None
        managed = game_data(args.game) / "Managed"
        if args.command == "decompile":
            print_json(decompile_project(args.game, args.ilspy))
            return
        if args.command == "assemblies":
            print_json([{"name": p.name, "bytes": p.stat().st_size, "sha256": digest(p)}
                        for p in sorted(managed.glob("*.dll"))])
            return
        assembly = explicit.resolve() if explicit and explicit.is_file() else managed / (args.assembly or "assembly_valheim.dll")
        path, hit = inspect(assembly, args.command, getattr(args, "name", None),
                            getattr(args, "il", False), args.ilspy)
        if args.command == "types" or getattr(args, "show", False):
            text = path.read_text(encoding="utf-8")
            print("\n".join(line for line in text.splitlines() if args.query.casefold() in line.casefold())
                  if args.command == "types" else text)
        else:
            result = {"path": str(path), "cache_hit": hit, "assembly": str(assembly)}
            if args.query:
                result["matches"] = [{"line": n, "text": line} for n, line in
                                     enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
                                     if args.query.casefold() in line.casefold()]
            print_json(result)
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f"Inspection failed: {error}\n")


if __name__ == "__main__":
    main()
