#!/usr/bin/env python3
"""Fetch a Valheim Fandom image through wsrv.nl into a session cache."""

import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen


PROXY_BASE = "https://wsrv.nl/"
IMAGE_HOST = "static.wikia.nocookie.net"
USER_AGENT = "ValheimModdingSkill/1.0 (wiki image display)"
TIMEOUT_SECONDS = 30
MAX_IMAGE_BYTES = 16 * 1024 * 1024
EXTENSION_RE = re.compile(r"\.(?:png|jpe?g|gif|webp|bmp|tiff?|avif|svg)(?=/|$)", re.I)
MIME_EXTENSIONS = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/bmp": ".bmp",
    "image/tiff": ".tiff",
    "image/avif": ".avif",
    "image/svg+xml": ".svg",
}
MAGIC = {
    ".png": lambda data: data.startswith(b"\x89PNG\r\n\x1a\n"),
    ".jpg": lambda data: data.startswith(b"\xff\xd8\xff"),
    ".gif": lambda data: data.startswith((b"GIF87a", b"GIF89a")),
    ".webp": lambda data: len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP",
    ".bmp": lambda data: data.startswith(b"BM"),
    ".tif": lambda data: data.startswith((b"II*\x00", b"MM\x00*")),
    ".tiff": lambda data: data.startswith((b"II*\x00", b"MM\x00*")),
    ".avif": lambda data: len(data) >= 12 and data[4:8] == b"ftyp" and b"avif" in data[8:32],
    ".svg": lambda data: b"<svg" in data[:1024].lower(),
}


class WikiImageError(Exception):
    """A concise, user-safe image fetch or validation error."""


def validate_image_url(url):
    """Validate a Fandom CDN URL without changing its revision path or query."""
    if not isinstance(url, str) or len(url) > 4096:
        raise WikiImageError("Image URL is missing or too long")
    parts = urlsplit(url.strip())
    if (parts.scheme != "https" or parts.hostname != IMAGE_HOST or
            parts.username or parts.password or parts.port not in (None, 443)):
        raise WikiImageError(f"Expected an HTTPS image from {IMAGE_HOST}")
    if not EXTENSION_RE.search(parts.path):
        raise WikiImageError("Image URL has no supported file extension")
    return urlunsplit(("https", IMAGE_HOST, parts.path, parts.query, ""))


def _cache_root(cache_dir):
    """Require a caller-owned temporary directory for session-only caching."""
    root = Path(cache_dir).expanduser().resolve()
    temp_root = Path(tempfile.gettempdir()).resolve()
    if not root.is_relative_to(temp_root) or root == temp_root:
        raise WikiImageError("The session cache must be a dedicated folder under the OS temp directory")
    for parent in (root, *root.parents):
        if (parent / ".git").exists():
            raise WikiImageError("Keep the wiki image cache outside Git repositories")
        if parent == temp_root:
            break
    root.mkdir(parents=True, exist_ok=True)
    return root


def _valid_image(data, extension):
    check = MAGIC.get(extension)
    return bool(check and check(data))


def _markdown_path(path):
    """Format absolute local paths consistently for Markdown on Windows too."""
    return str(path.resolve()).replace("\\", "/")


def fetch_image(image_url, cache_dir, source_page, alt_text="Wiki image"):
    """Fetch via wsrv.nl, validate, and reuse an image cached by source URL."""
    source_url = validate_image_url(image_url)
    page = urlsplit(source_page)
    if page.scheme != "https" or page.hostname != "valheim.fandom.com":
        raise WikiImageError("Source page must be an HTTPS Valheim Wiki page")
    root = _cache_root(cache_dir)
    key = hashlib.sha256(source_url.encode("utf-8")).hexdigest()

    for extension in set(MIME_EXTENSIONS.values()):
        cached = root / f"{key}{extension}"
        if cached.is_file():
            data = cached.read_bytes()
            if len(data) <= MAX_IMAGE_BYTES and _valid_image(data, extension):
                return _result(source_url, page.geturl(), cached, extension, len(data), True, alt_text)

    source_parts = urlsplit(source_url)
    # wsrv.nl can fetch the Wikia CDN when passed host/path/query as a relative
    # origin, while the HTTPS origin form is rejected by the CDN with HTTP 403.
    proxy_origin = source_parts.netloc + source_parts.path
    if source_parts.query:
        proxy_origin += "?" + source_parts.query
    proxy_url = PROXY_BASE + "?" + urlencode({"url": proxy_origin})
    request = Request(proxy_url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "image/avif,image/webp,image/png,image/jpeg,image/gif,*/*;q=0.5",
    })
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            mime = response.headers.get_content_type().lower()
            extension = MIME_EXTENSIONS.get(mime)
            if not extension:
                raise WikiImageError("Image proxy returned an unsupported content type")
            data = response.read(MAX_IMAGE_BYTES + 1)
    except HTTPError as error:
        raise WikiImageError(f"Image proxy returned HTTP {error.code}") from None
    except (URLError, TimeoutError, OSError) as error:
        raise WikiImageError(f"Could not retrieve the wiki image through wsrv.nl: {error}") from None

    if len(data) > MAX_IMAGE_BYTES:
        raise WikiImageError("Image proxy response exceeded the 16 MiB safety limit")
    if not _valid_image(data, extension):
        raise WikiImageError("Image proxy response did not contain a valid image")

    destination = root / f"{key}{extension}"
    partial = root / f".{key}.part"
    try:
        partial.write_bytes(data)
        partial.replace(destination)
    finally:
        if partial.exists():
            partial.unlink()
    return _result(source_url, page.geturl(), destination, extension, len(data), False, alt_text)


def _result(source_url, source_page, path, extension, size, cache_hit, alt_text):
    label = alt_text.replace("\\", "\\\\").replace("]", "\\]").replace("\n", " ")
    local_path = _markdown_path(path)
    return {
        "source_image": source_url,
        "source_page": source_page,
        "path": local_path,
        "mime_type": next(mime for mime, ext in MIME_EXTENSIONS.items() if ext == extension),
        "size_bytes": size,
        "cache_hit": cache_hit,
        "markdown": f"![{label}](<{local_path}>)",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image_url", help="Image URL copied from the English Valheim Wiki article")
    parser.add_argument("--cache-dir", required=True,
                        help="Dedicated session cache folder under the OS temporary directory")
    parser.add_argument("--source-page", required=True, help="Canonical English Valheim Wiki article URL")
    parser.add_argument("--alt", default="Valheim Wiki image", help="Short image description for Markdown")
    args = parser.parse_args()
    try:
        print(json.dumps(fetch_image(args.image_url, args.cache_dir, args.source_page, args.alt),
                         ensure_ascii=False, indent=2))
    except WikiImageError as error:
        parser.exit(1, f"Wiki image fetch failed: {error}\n")


if __name__ == "__main__":
    main()
