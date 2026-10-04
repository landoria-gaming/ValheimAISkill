#!/usr/bin/env python3
"""Clear the persistent Valheim inspection cache at most once per local day."""

from datetime import date
import os
from pathlib import Path
import shutil
import sys


PRESERVED_FILES = {"last-cleanup.txt", "installation.json"}


def persistent_cache_root():
    """Return the persistent cache path used by the inspection helpers."""
    override = os.environ.get("VALHEIM_SKILL_CACHE")
    if override:
        root = Path(override).expanduser()
    elif sys.platform == "win32":
        root = Path.home() / ".cache/valheim-modding"
    elif sys.platform == "darwin":
        root = Path.home() / "Library/Application Support/ValheimModdingSkill/cache"
    else:
        root = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share")) / "valheim-modding/cache"
    if not root.is_absolute():
        raise ValueError("The persistent cache path must be absolute")
    root = root.resolve()
    if root == Path(root.anchor) or any((parent / ".git").exists() for parent in (root, *root.parents)):
        raise ValueError("Refusing to clean a filesystem root or a Git repository")
    return root


def cleanup(root=None, today=None):
    """Clear cached inspection results and preserve only operational metadata."""
    root = Path(root or persistent_cache_root()).resolve()
    root.mkdir(parents=True, exist_ok=True)
    marker = root / "last-cleanup.txt"
    day = (today or date.today()).isoformat()
    try:
        if marker.is_file() and marker.read_text(encoding="ascii").strip() == day:
            return {"date": day, "skipped": True, "removed": 0}
    except (OSError, UnicodeError):
        pass

    removed = 0
    for entry in root.iterdir():
        if entry.name in PRESERVED_FILES:
            continue
        if entry.is_symlink():
            entry.unlink()
        elif entry.is_dir():
            shutil.rmtree(entry)
        else:
            entry.unlink()
        removed += 1

    staging = root / (".last-cleanup-" + os.urandom(8).hex() + ".tmp")
    try:
        staging.write_text(day + "\n", encoding="ascii")
        os.replace(staging, marker)
    finally:
        try:
            staging.unlink()
        except FileNotFoundError:
            pass
    return {"date": day, "skipped": False, "removed": removed}


def main():
    result = cleanup()
    if result["skipped"]:
        print(f"Persistent cache cleanup already completed on {result['date']}.")
    else:
        print(f"Persistent cache cleanup completed on {result['date']}; removed {result['removed']} cache item(s).")


if __name__ == "__main__":
    main()
