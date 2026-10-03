"""Shared read-only inspection helpers. Generated files stay in a temporary cache."""

import hashlib
import json
import os
from pathlib import Path
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


def cache_dir(identity):
    """Separate inputs and script revisions; never use a project as a cache."""
    key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()[:24]
    path = Path(tempfile.gettempdir()) / "valheim-skill-inspection" / key
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
