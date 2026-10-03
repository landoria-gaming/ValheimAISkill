"""Read-only inspection helpers with persistent, source-keyed local caches."""

import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def stamp(path):
    path = Path(path).resolve()
    stat = path.stat()
    return [str(path), stat.st_size, stat.st_mtime_ns]


def persistent_cache_root():
    """Keep asset indexes across agent sessions, outside repos and temp cleanup."""
    override = os.environ.get("VALHEIM_SKILL_CACHE")
    if override:
        root = Path(override).expanduser()
    elif sys.platform == "win32":
        # Packaged desktop apps can redirect LOCALAPPDATA to their own sandbox.
        # Use a profile-level path shared by agents and unaffected by app removal.
        root = Path.home() / ".cache/valheim-modding"
    elif sys.platform == "darwin":
        root = Path.home() / "Library/Application Support/ValheimModdingSkill/cache"
    else:
        root = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share")) / "valheim-modding/cache"
    if not root.is_absolute():
        raise ValueError("The persistent cache path must be absolute")
    root = root.resolve()
    if any((p / ".git").exists() for p in (root, *root.parents)):
        raise ValueError("Keep the persistent cache outside Git repositories")
    root.mkdir(parents=True, exist_ok=True)
    return root


def cache_dir(identity, persistent=False, category="indexes"):
    """Separate inputs and script revisions; keep working files temporary."""
    if category not in {"indexes", "code", "images", "assets"}:
        raise ValueError("Unknown cache category")
    key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()[:24]
    root = persistent_cache_root() / category if persistent else Path(tempfile.gettempdir()) / "valheim-skill-inspection"
    path = root / key
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_json(path, data):
    """Commit generated metadata atomically, without partial cache entries."""
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     delete=False, suffix=".tmp") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        staging = Path(stream.name)
    staging.replace(path)


def save_bytes(path, payload):
    path = Path(path)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False, suffix=".tmp") as stream:
        stream.write(payload)
        staging = Path(stream.name)
    staging.replace(path)


def cached_result(path, identity):
    """Incomplete, corrupt, or differently sourced outputs are cache misses."""
    try:
        result = json.loads(path.with_name("provenance.json").read_text(encoding="utf-8"))
        if result.get("source") == identity and result.get("output_sha256") == digest(path):
            return result
    except (OSError, ValueError, AttributeError):
        pass
    return None


def game_data(game):
    """Accept a client/server root, data folder, or macOS app; do not scan home folders."""
    supplied = game or os.environ.get("VALHEIM_PATH")
    if not supplied:
        raise ValueError("Pass --game or set VALHEIM_PATH to the local game installation")
    root = Path(supplied).expanduser().resolve()
    candidates = [root, root / "valheim_Data", root / "valheim_server_Data",
                  root / "Contents/Resources/Data", root / "Valheim.app/Contents/Resources/Data"]
    matches = [p for p in candidates if (p / "Managed/assembly_valheim.dll").is_file()]
    if len(matches) != 1:
        raise ValueError("Valheim is missing or inaccessible. Only installation/directory-access help is allowed; pass the actual game path")
    data = matches[0]
    assets = [data / "resources.assets", data / "StreamingAssets/SoftRef/manifest_extended"]
    available = next((p for p in assets if p.is_file()), None)
    if available is None:
        raise ValueError("Game assets are missing or inaccessible; restore access to the installed Valheim directory first")
    try:
        for path in (data / "Managed/assembly_valheim.dll", available):
            with path.open("rb") as stream:
                stream.read(1)
    except OSError as error:
        raise ValueError("Cannot read the Valheim installation; only installation/directory-access help is allowed") from error
    return data


def print_json(value):
    print(json.dumps(value, ensure_ascii=True, indent=2))
