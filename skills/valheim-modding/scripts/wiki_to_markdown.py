#!/usr/bin/env python3
"""Fetch one Valheim Wiki suggestion through MediaWiki and print article Markdown."""

import argparse
import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urljoin, urlsplit
from urllib.request import Request, urlopen


API_URL = "https://valheim.fandom.com/api.php"
USER_AGENT = "ValheimModdingSkill/1.0 (wiki article reading)"
TIMEOUT_SECONDS = 25
MAX_RESPONSE_BYTES = 8 * 1024 * 1024


class WikiRequestError(Exception):
    """A safe, concise error for network, API, and conversion failures."""


def fetch_article(title):
    """Fetch the rendered article from MediaWiki's parse API, not the web shell."""
    title = title.strip()
    if not title or len(title) > 200 or "\n" in title:
        raise WikiRequestError("Pass one suggestion title between 1 and 200 characters")
    params = urlencode({
        "action": "parse",
        "page": title,
        "prop": "text",
        "format": "json",
        "formatversion": "2",
    })
    request = Request(API_URL + "?" + params,
                      headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            if response.status != 200:
                raise WikiRequestError(f"Wiki article returned HTTP {response.status}")
            payload = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as error:
        raise WikiRequestError(f"Wiki article returned HTTP {error.code}") from None
    except (URLError, TimeoutError, OSError) as error:
        raise WikiRequestError(f"Could not reach the Valheim Wiki: {error}") from None
    if len(payload) > MAX_RESPONSE_BYTES:
        raise WikiRequestError("Wiki article exceeded the 8 MiB safety limit")
    try:
        data = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise WikiRequestError("Wiki article endpoint returned invalid JSON") from None
    if "error" in data:
        info = data["error"].get("info", "unknown MediaWiki error")
        raise WikiRequestError(f"Wiki could not find that suggestion: {info}")
    article = data.get("parse")
    if not isinstance(article, dict) or not isinstance(article.get("text"), str):
        raise WikiRequestError("Wiki response did not contain rendered article HTML")
    canonical_title = article.get("title") or title
    page_url = "https://valheim.fandom.com/wiki/" + quote(
        canonical_title.replace(" ", "_"), safe="()'!,.-_"
    )
    return canonical_title, page_url, article["text"]


def article_to_markdown(html, title, page_url):
    """Convert only article content to Markdown; never persist HTML or output."""
    try:
        from bs4 import BeautifulSoup
        from bs4.element import NavigableString
        from markdownify import markdownify
    except ImportError as error:
        raise WikiRequestError(
            "Markdown conversion needs the optional dependency; install "
            "scripts/requirements-wiki.txt"
        ) from error

    soup = BeautifulSoup(html, "html.parser")
    # MediaWiki's parse API returns article content rather than a full document.
    # Fandom currently wraps it in .mw-parser-output; accept <main> if that changes.
    content = soup.find("main") or soup.select_one(".mw-parser-output")
    if content is None:
        raise WikiRequestError("Could not identify the article's main content")

    for element in content.select(
        "script, style, noscript, .mw-editsection, .reference, .navbox, "
        ".catlinks, .printfooter, .mw-empty-elt, #toc, figure.pi-image"
    ):
        element.decompose()
    for link in content.select("a[href]"):
        target = urljoin("https://valheim.fandom.com", link["href"])
        if urlsplit(target).scheme in {"http", "https"}:
            link["href"] = target
        else:
            link.unwrap()
    for image in content.select("img"):
        image_link = image.find_parent("a")
        label = image.get("alt") or (image_link.get("title", "") if image_link else "")
        if image_link and not image_link.get_text(" ", strip=True):
            item = image_link.find_parent(["li", "td", "th", "p"])
            duplicate_label = item and any(
                link is not image_link and link.get_text(" ", strip=True).casefold() == label.casefold()
                for link in item.find_all("a")
            )
            if duplicate_label:
                image_link.decompose()
            elif label:
                image_link.replace_with(NavigableString(label))
            else:
                image_link.decompose()
        elif label:
            image.replace_with(NavigableString(label))
        else:
            image.decompose()
    # These markers are emitted by Fandom's icon-decorated ingredient lists.
    for text in content.find_all(string=True):
        if "\ufffd" in text:
            text.replace_with(re.sub(r"\ufffd\s*(\d+)\s*\ufffd", r" x\1 ", str(text)).replace("\ufffd", " "))

    markdown = markdownify(str(content), heading_style="ATX", bullets="-")
    markdown = re.sub(r"\ufffd\s*(\d+)\s*\ufffd", r" x\1 ", markdown)
    markdown = markdown.replace("\ufffd", " ")
    markdown = re.sub(r"(?m)^(\s*[-*+]\s+)(\d+)[\xa0 ]+(.+)$", r"\1\3 x\2", markdown)
    markdown = re.sub(r"(?m)^(\s*[-*+]\s+)x(\d+)\s+(.+)$", r"\1\3 x\2", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    if not markdown:
        raise WikiRequestError("The article did not contain readable text")
    label = title.replace("\\", "\\\\").replace("]", "\\]")
    return f"> Source: [{label}]({page_url})\n\n{markdown}\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("suggestion", help="Exact title returned by search_wiki.py")
    args = parser.parse_args()
    try:
        title, page_url, html = fetch_article(args.suggestion)
        print(article_to_markdown(html, title, page_url), end="")
    except WikiRequestError as error:
        parser.exit(1, f"Wiki Markdown conversion failed: {error}\n")


if __name__ == "__main__":
    main()
