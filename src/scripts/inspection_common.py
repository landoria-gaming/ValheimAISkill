"""Read-only inspection helpers with persistent, source-keyed local caches."""

import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from datetime import datetime, timezone


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
        root = Path.home() / ".cache/valheim-ai-skill"
    elif sys.platform == "darwin":
        root = Path.home() / "Library/Application Support/ValheimAISkill/cache"
    else:
        root = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share")) / "valheim-ai-skill/cache"
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


def _validate_game_root(supplied):
    """Validate an explicit path without persisting it until read access is proven."""
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


def _remember_game_data(data, source):
    """Store only a verified local installation path outside the repository."""
    cache = persistent_cache_root()
    assembly = data / "Managed/assembly_valheim.dll"
    save_json(cache / "installation.json", {
        "game_data": str(data),
        "game_root": str(data.parent),
        "assembly_sha256": digest(assembly),
        "assembly_stamp": stamp(assembly),
        "source": source,
        "verified_utc": datetime.now(timezone.utc).isoformat(),
    })


def _steam_roots():
    """Return a small set of normal Steam roots and libraries listed by Steam."""
    home = Path.home()
    if sys.platform == "win32":
        roots = [Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)")) / "Steam",
                 Path(os.environ.get("PROGRAMFILES", r"C:\Program Files")) / "Steam"]
        local = os.environ.get("LOCALAPPDATA")
        if local:
            roots.append(Path(local) / "Steam")
    elif sys.platform == "darwin":
        roots = [home / "Library/Application Support/Steam"]
    else:
        roots = [home / ".steam/steam", home / ".local/share/Steam",
                 home / ".var/app/com.valvesoftware.Steam/.local/share/Steam"]

    roots = list(dict.fromkeys(path.expanduser() for path in roots))
    libraries = list(roots)
    for steam_root in roots:
        vdf = steam_root / "steamapps/libraryfolders.vdf"
        try:
            content = vdf.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for value in re.findall(r'"path"\s*"((?:\\.|[^"\\])*)"', content):
            decoded = value.replace("\\\\", "\\").replace("\\\"", '"')
            libraries.append(Path(decoded))
    return list(dict.fromkeys(libraries))


def _discover_game_data():
    """Probe exact common client/server install locations, not arbitrary directories."""
    roots = []
    for steam_root in _steam_roots():
        roots.extend((steam_root / "steamapps/common/Valheim",
                      steam_root / "steamapps/common/Valheim Dedicated Server"))
    if sys.platform == "win32":
        roots.append(Path(os.environ.get("ProgramFiles", r"C:\Program Files")) /
                     "WindowsApps")
        roots.extend((Path(r"C:\XboxGames\Valheim\Content"), Path(r"C:\XboxGames\Valheim")))
    matches = {}
    for root in roots:
        try:
            data = _validate_game_root(root)
            matches[str(data)] = data
        except (OSError, ValueError):
            continue
    return list(matches.values())


def game_data(game):
    """Use an explicit, environment, or remembered game path; never scan home folders."""
    supplied = game or os.environ.get("VALHEIM_PATH")
    source = "argument" if game else "environment"
    if supplied:
        data = _validate_game_root(supplied)
        _remember_game_data(data, source)
        return data

    cache = persistent_cache_root()
    saved_path = cache / "installation.json"
    try:
        saved = json.loads(saved_path.read_text(encoding="utf-8"))
        data = _validate_game_root(saved["game_data"])
        _remember_game_data(data, "remembered")
        return data
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        pass
    discovered = _discover_game_data()
    if len(discovered) == 1:
        _remember_game_data(discovered[0], "discovered")
        return discovered[0]
    if len(discovered) > 1:
        paths = ", ".join(str(path.parent) for path in discovered)
        raise ValueError(f"Found multiple accessible Valheim installations ({paths}); choose one with --game")
    raise ValueError(
        "No accessible Valheim installation was found in the usual Steam or Xbox locations. "
        "Pass --game or set VALHEIM_PATH once so the verified path can be remembered locally; "
        "otherwise only installation/directory-access help is allowed"
    )


def print_json(value):
    print(json.dumps(value, ensure_ascii=True, indent=2))
