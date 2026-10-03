#!/usr/bin/env python3
"""Validate and package only the reviewed, portable skill resources."""

import argparse
import json
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


REPOSITORY = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPOSITORY / "skills" / "valheim-modding"
TEMPLATE = "assets/mod-template/"
FILES = (
    "SKILL.md", "LICENSE", "agents/openai.yaml",
    "references/environment.md", "references/development.md",
    "references/validation.md", "references/unity.md", "references/assets.md",
    "references/packaging.md", "references/servers.md", "references/sources.md",
    "references/inspection-scripts.md",
    "assets/readme-template.md",
    "scripts/inspection_common.py", "scripts/inspect_code.py",
    "scripts/asset_ripper.py", "scripts/asset_index.py", "scripts/inspect_assets.py",
    "scripts/export_prefab_catalog.py", "scripts/requirements-assets.txt",
    *(TEMPLATE + name for name in (
        ".gitignore", ".template.config/template.json", "ValheimMod.csproj",
        "Plugin.cs", "ModConfigFile.cs", "PlayerSpawnHandler.cs",
        "Properties/AssemblyInfo.cs", "build/Thunderstore.targets",
        "manifest.json", "README.md", "DEVELOPMENT.md", "CHANGELOG.md", "LICENSE",
    )),
)
PLACEHOLDER_LINKS = {"REPOSITORY_ISSUES_URL", "REPOSITORY_DISCUSSIONS_URL"}
PERSONAL_PATH = re.compile(
    r"(?:[A-Za-z]:[/\\](?:Users|Documents and Settings)[/\\]|/(?:Users|home)/)"
    r"[^/\\\s<>]+[/\\]", re.IGNORECASE,
)


def headings(text):
    """Resolve anchors for the simple, unique Markdown headings used here."""
    return {
        re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE)
    }


def validate_links(files):
    """Reject local links that would break after extracting the ZIP."""
    for name, payload in files.items():
        if not name.endswith(".md"):
            continue
        for link in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", payload.decode("utf-8")):
            target = link.strip().strip("<>")
            if name == "assets/readme-template.md" and target in PLACEHOLDER_LINKS:
                continue
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            # Resolve without consulting the filesystem: only shipped files count.
            parts = list(Path(name).parent.parts)
            for part in unquote(parsed.path).split("/") if parsed.path else []:
                if part == "..":
                    if not parts:
                        raise ValueError(f"Link escapes skill: {name}")
                    parts.pop()
                elif part and part != ".":
                    parts.append(part)
            resolved = "/".join(parts) if parsed.path else name
            if resolved not in files:
                if parsed.fragment or not any(p.startswith(resolved + "/") for p in files):
                    raise ValueError(f"Broken local link in {name}: {target}")
            elif parsed.fragment and unquote(parsed.fragment) not in headings(
                files[resolved].decode("utf-8")
            ):
                raise ValueError(f"Broken heading link in {name}: {target}")


def load_sources(root):
    """Read the allowlist, rejecting indirect paths and common personal paths."""
    if root.is_symlink() or getattr(root, "is_junction", lambda: False)():
        raise ValueError("Use a real source directory, not a linked skill root")
    root = root.resolve()
    files = {}
    for name in sorted(FILES):
        path = root / name
        for candidate in (path, *path.parents):
            if candidate == root:
                break
            if candidate.is_symlink() or getattr(candidate, "is_junction", lambda: False)():
                raise ValueError(f"Linked resource is not allowed: {name}")
        if not path.resolve().is_relative_to(root) or not path.is_file():
            raise ValueError(f"Missing or unsafe resource: {name}")
        content = path.read_text(encoding="utf-8-sig")
        if PERSONAL_PATH.search(content):
            raise ValueError(f"Absolute personal path in {name}; use a placeholder")
        files[name] = content.encode("utf-8")
    return files


def validate_sources(files):
    """Check entrypoint, structured templates, and self-contained local links."""
    entry = files["SKILL.md"].decode("utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", entry, re.DOTALL)
    if not frontmatter:
        raise ValueError("SKILL.md needs YAML frontmatter")
    header = frontmatter.group(1)
    if not re.search(r"^name: valheim-modding$", header, re.MULTILINE):
        raise ValueError("Unexpected skill name")
    if not re.search(r"^description: \S.+$", header, re.MULTILINE):
        raise ValueError("Missing skill description")
    for name, payload in files.items():
        if name.endswith(".json"):
            json.loads(payload)
        elif name.endswith(".py"):
            compile(payload, name, "exec")
        elif name.endswith((".csproj", ".targets")):
            ET.fromstring(payload)
    validate_links(files)


def verify_archive(path, files):
    """Check exact archive membership and bytes, including hidden resources."""
    expected = {f"valheim-modding/{name}": data for name, data in files.items()}
    with ZipFile(path) as archive:
        if len(archive.namelist()) != len(expected) or set(archive.namelist()) != set(expected):
            raise ValueError("Archive file list differs from the reviewed source list")
        for name, payload in expected.items():
            if archive.read(name) != payload:
                raise ValueError(f"Archive content mismatch: {name}")


def build_archive(root, destination):
    """Produce a deterministic ZIP and replace the output only after validation."""
    files = load_sources(root)
    validate_sources(files)
    destination = destination.resolve()
    if destination.is_relative_to(root.resolve()):
        raise ValueError("Write the archive outside the skill source folder")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="skill-package-", dir=destination.parent) as staging:
        staged = Path(staging) / destination.name
        with ZipFile(staged, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for name, payload in files.items():
                entry = ZipInfo(f"valheim-modding/{name}", date_time=(1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                entry.compress_type = ZIP_DEFLATED
                archive.writestr(entry, payload, compresslevel=9)
        verify_archive(staged, files)
        staged.replace(destination)
    return len(files)


def main():
    """Expose packaging and read-only source checks to maintainers."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SKILL_ROOT)
    parser.add_argument("--output", type=Path, default=REPOSITORY / "dist/valheim-modding.zip")
    parser.add_argument("--check", action="store_true", help="Validate without writing a ZIP")
    args = parser.parse_args()
    try:
        if args.check:
            files = load_sources(args.source)
            validate_sources(files)
            print(f"Validated {len(files)} skill resources; no files written.")
        else:
            count = build_archive(args.source, args.output)
            print(f"Packaged and verified {count} files: {args.output}")
    except (ValueError, OSError, ET.ParseError) as error:
        parser.exit(1, f"Validation failed: {error}\n")


if __name__ == "__main__":
    main()
