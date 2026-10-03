#!/usr/bin/env python3
"""List game DLLs, find types, and inspect C# or IL with ILSpyCMD, without execution."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess

from inspection_common import cache_dir, digest, game_data, print_json, save_json, stamp


def run_ilspy(executable, arguments):
    result = subprocess.run([executable, *arguments], capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=180)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "ILSpyCMD failed")
    return result.stdout


def inspect(assembly, action, type_name=None, il=False, executable="ilspycmd"):
    assembly = Path(assembly).resolve(strict=True)
    tool = shutil.which(executable)
    if not tool:
        raise ValueError("ILSpyCMD is missing. Install the official ilspycmd .NET tool first")
    version = run_ilspy(tool, ["--version"]).strip()
    identity = {"script": digest(__file__), "assembly_sha256": digest(assembly),
                "references": [stamp(p) for p in sorted(assembly.parent.glob("*.dll"))],
                "tool": version, "action": action, "type": type_name, "il": il}
    folder = cache_dir(identity)
    output = folder / ("types.txt" if action == "types" else "type.il" if il else "type.cs")
    hit = output.is_file()
    if not hit:
        if action == "types":
            text = "".join(run_ilspy(tool, ["-l", kind, str(assembly)]) for kind in "cised")
        else:
            args = ["-t", type_name, *(["--ilcode"] if il else [])]
            text = run_ilspy(tool, [*args, "-r", str(assembly.parent), str(assembly)])
        output.write_text(text, encoding="utf-8")
        save_json(folder / "provenance.json", identity)
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
    single = sub.add_parser("type", help="Decompile one exact type into the temporary cache")
    single.add_argument("name")
    single.add_argument("--il", action="store_true")
    single.add_argument("--query", help="Show matching lines from the extracted type")
    single.add_argument("--print", action="store_true", dest="show")
    args = parser.parse_args()
    try:
        explicit = Path(args.assembly) if args.assembly else None
        managed = game_data(args.game) / "Managed"
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
