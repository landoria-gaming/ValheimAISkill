"""Small AssetRipper 2.0 HTTP adapter with an optional task-owned hidden process."""

from contextlib import contextmanager
import html
import json
from pathlib import Path
import re
import socket
import subprocess
import tempfile
import time
from urllib.parse import parse_qs, urlencode, urlsplit
from urllib.request import Request, urlopen

from inspection_common import stamp


def cache_identity(tool):
    """Identify a local tool build without launching it; external services are unverified."""
    if not tool:
        return None
    executable = Path(tool).resolve(strict=True)
    files = {executable, *executable.parent.glob("*.dll"), *executable.parent.glob("*.json")}
    return [stamp(p) for p in sorted(files) if p.is_file()]


def validate_base(base):
    parsed = urlsplit(base)
    if (parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
            or parsed.username or parsed.password or parsed.query or parsed.fragment
            or parsed.path not in {"", "/"}):
        raise ValueError("Use an HTTP loopback AssetRipper URL without credentials or a path")
    return base.rstrip("/")


def request(base, endpoint, data=None, timeout=180):
    body = urlencode(data).encode() if data is not None else None
    with urlopen(Request(validate_base(base) + endpoint, data=body), timeout=timeout) as response:
        # Refuse an unexpected redirect outside the local service.
        if urlsplit(response.url).netloc != urlsplit(base).netloc:
            raise ValueError("AssetRipper redirected outside the selected service")
        return response.read()


def asset_json(base, locator):
    result = json.loads(request(base, "/Assets/Json?" + urlencode({"Path": json.dumps(locator)})))
    if not isinstance(result, dict):
        raise ValueError("Expected an asset property object")
    return result


def search(base, query):
    page = request(base, "/Search/View?" + urlencode({"q": query})).decode("utf-8")
    entries = []
    for kind, row in re.findall(r'<tr data-class="([^"]+)">(.*?)</tr>', page, re.S):
        match = re.search(r'<a href="(/Assets/View\?[^\"]+)"[^>]*>(.*?)</a>', row)
        if match:
            locator = json.loads(parse_qs(urlsplit(html.unescape(match[1])).query)["Path"][0])
            entries.append({"class": html.unescape(kind), "name": html.unescape(match[2]),
                            "locator": locator})
    return entries


def load(base, paths):
    paths = [Path(p).resolve(strict=True) for p in paths]
    if not paths or any(not p.is_file() for p in paths):
        raise ValueError("Load explicit files, not a whole game directory")
    request(base, "/LoadFile", [("Path", str(p)) for p in paths])


def export(base, locator, format_name):
    endpoints = {"json": "Json", "yaml": "Yaml", "text": "Text", "png": "Image", "binary": "Binary"}
    query = {"Path": json.dumps(locator)}
    if format_name == "png":
        query["Extension"] = "png"
    payload = request(base, "/Assets/" + endpoints[format_name] + "?" + urlencode(query))
    if format_name == "png" and not payload.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("AssetRipper did not return a PNG; check sprite/texture dependencies")
    if format_name == "json":
        json.loads(payload)
    return payload


@contextmanager
def session(base=None, tool=None):
    """Stop only the process started here; never reset or stop another user's service."""
    if base:
        yield validate_base(base)
        return
    if not tool:
        raise ValueError("Pass --tool with the AssetRipper executable or --base-url for a dedicated service")
    executable = Path(tool).resolve(strict=True)
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    base = f"http://127.0.0.1:{port}"
    logs = Path(tempfile.mkdtemp(prefix="valheim-assetripper-"))
    process = None
    try:
        with (logs / "service.log").open("wb") as output:
            process = subprocess.Popen([str(executable), "--headless", "--port", str(port)],
                                       cwd=logs, stdout=output, stderr=subprocess.STDOUT,
                                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            deadline = time.monotonic() + 45
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    raise ValueError(f"AssetRipper exited; inspect {logs / 'service.log'}")
                try:
                    schema = json.loads(request(base, "/openapi.json", timeout=1))
                    if "/LoadFile" not in schema.get("paths", {}):
                        raise ValueError("Unsupported AssetRipper API schema")
                    break
                except OSError:
                    time.sleep(0.2)
            else:
                raise ValueError(f"AssetRipper startup timed out; inspect {logs / 'service.log'}")
            yield base
    finally:
        if process is not None and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=10)
