"""Tests for the Valheim Wiki suggestion and Markdown helpers."""

import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

SCRIPTS = Path(__file__).resolve().parents[1] / "src/scripts"
sys.path.insert(0, str(SCRIPTS))

import search_wiki
import wiki_to_markdown
import fetch_wiki_image


class MockResponse(io.BytesIO):
    def __init__(self, payload, status=200):
        super().__init__(payload)
        self.status = status


class WikiSearchTests(unittest.TestCase):
    def test_search_encodes_query_and_returns_suggestion_titles(self):
        payload = json.dumps({
            "query": "onion so",
            "ids": {"Onion Soup": 3416},
            "suggestions": ["Onion Soup"],
        }).encode()
        with patch.object(search_wiki, "urlopen", return_value=MockResponse(payload)) as request:
            result = search_wiki.search(" onion so ")
        params = parse_qs(urlsplit(request.call_args.args[0].full_url).query)
        self.assertEqual(params["query"], ["onion so"])
        self.assertEqual(result["suggestions"][0]["title"], "Onion Soup")
        self.assertEqual(result["suggestions"][0]["page_id"], 3416)
        self.assertEqual(result["suggestions"][0]["url"], "https://valheim.fandom.com/wiki/Onion_Soup")

    def test_blank_query_is_rejected(self):
        with self.assertRaises(search_wiki.WikiRequestError):
            search_wiki.search("  ")


class WikiMarkdownTests(unittest.TestCase):
    def test_fetch_uses_mediawiki_parse_api_and_returns_rendered_content(self):
        payload = json.dumps({"parse": {"title": "Onion Soup", "text": "<main><h1>Soup</h1></main>"}}).encode()
        with patch.object(wiki_to_markdown, "urlopen", return_value=MockResponse(payload)) as request:
            title, url, html = wiki_to_markdown.fetch_article("Onion Soup")
        params = parse_qs(urlsplit(request.call_args.args[0].full_url).query)
        self.assertEqual(params["action"], ["parse"])
        self.assertEqual(params["page"], ["Onion Soup"])
        self.assertEqual(title, "Onion Soup")
        self.assertEqual(url, "https://valheim.fandom.com/wiki/Onion_Soup")
        self.assertEqual(html, "<main><h1>Soup</h1></main>")

    @unittest.skipUnless(importlib.util.find_spec("markdownify") and importlib.util.find_spec("bs4"),
                         "Install optional scripts/requirements-wiki.txt to test conversion")
    def test_conversion_keeps_article_structure_and_drops_page_chrome(self):
        html = """<div class="mw-parser-output"><script>bad()</script>
        <h2>Recipe</h2><p>Make the soup.</p>
        <ul><li><a href="/wiki/Onion">Onion</a> x3</li></ul>
        <table><tr><th>Station</th><th>Level</th></tr>
        <tr><td>Cauldron</td><td>2</td></tr></table>
        <div class="navbox">Unrelated navigation</div></div>"""
        result = wiki_to_markdown.article_to_markdown(
            html, "Onion Soup", "https://valheim.fandom.com/wiki/Onion_Soup"
        )
        self.assertIn("## Recipe", result)
        self.assertRegex(result, r"(?m)^- \[Onion\]\(https://valheim\.fandom\.com/wiki/Onion.*\) x3$")
        self.assertIn("| Cauldron | 2 |", result)
        self.assertNotIn("Unrelated navigation", result)
        self.assertNotIn("bad()", result)

    @unittest.skipUnless(importlib.util.find_spec("markdownify") and importlib.util.find_spec("bs4"),
                         "Install optional scripts/requirements-wiki.txt to test conversion")
    def test_conversion_cleans_icon_only_links_and_fandom_quantity_markers(self):
        html = """<div class="mw-parser-output"><h2>Recipe</h2><ul><li>
        <a href="/wiki/Onion" title="Onion"><img alt="Onion" src="icon.png"/></a>
        �3�<a href="/wiki/Onion" title="Onion">Onion</a>
        </li></ul></div>"""
        result = wiki_to_markdown.article_to_markdown(
            html, "Onion Soup", "https://valheim.fandom.com/wiki/Onion_Soup"
        )
        self.assertRegex(result, r"(?m)^- \[Onion\]\(https://valheim\.fandom\.com/wiki/Onion.*\) x3$")
        self.assertNotIn("icon.png", result)
        self.assertNotIn("\ufffd", result)


class ImageResponse(io.BytesIO):
    def __init__(self, payload, content_type="image/png"):
        super().__init__(payload)
        from email.message import Message
        self.headers = Message()
        self.headers["Content-Type"] = content_type


class WikiImageTests(unittest.TestCase):
    SOURCE_URL = (
        "https://static.wikia.nocookie.net/valheim/images/8/82/Greydwarf.png/"
        "revision/latest/scale-to-width-down/536?cb=123"
    )
    PAGE_URL = "https://valheim.fandom.com/wiki/Greydwarf"
    PNG_BYTES = b"\x89PNG\r\n\x1a\nsynthetic-test-image"

    def test_preserves_revision_suffix_and_query_string(self):
        self.assertEqual(fetch_wiki_image.validate_image_url(self.SOURCE_URL), self.SOURCE_URL)

    def test_rejects_other_hosts_and_non_https_urls(self):
        for url in (
            "https://example.com/image.png",
            "http://static.wikia.nocookie.net/valheim/images/image.png",
            "https://static.wikia.nocookie.net/valheim/images/no-extension/revision/latest",
        ):
            with self.subTest(url=url), self.assertRaises(fetch_wiki_image.WikiImageError):
                fetch_wiki_image.validate_image_url(url)

    def test_uses_proxy_and_reuses_session_cache(self):
        with tempfile.TemporaryDirectory(prefix="valheim-wiki-test-") as cache_dir:
            with patch.object(fetch_wiki_image, "urlopen",
                              return_value=ImageResponse(self.PNG_BYTES)) as request:
                first = fetch_wiki_image.fetch_image(
                    self.SOURCE_URL, cache_dir, self.PAGE_URL, "Greydwarf"
                )
                second = fetch_wiki_image.fetch_image(
                    self.SOURCE_URL, cache_dir, self.PAGE_URL, "Greydwarf"
                )

            proxy = request.call_args.args[0]
            params = parse_qs(urlsplit(proxy.full_url).query)
            self.assertEqual(urlsplit(proxy.full_url).hostname, "wsrv.nl")
            self.assertEqual(params["url"], [
                "static.wikia.nocookie.net/valheim/images/8/82/Greydwarf.png/"
                "revision/latest/scale-to-width-down/536?cb=123"
            ])
            self.assertFalse(first["cache_hit"])
            self.assertTrue(second["cache_hit"])
            self.assertEqual(request.call_count, 1)
            self.assertTrue(Path(first["path"]).is_file())
            self.assertIn("![Greydwarf](<", first["markdown"])
            self.assertNotIn("\\", first["markdown"])

    def test_rejects_non_image_proxy_response(self):
        with tempfile.TemporaryDirectory(prefix="valheim-wiki-test-") as cache_dir:
            with patch.object(fetch_wiki_image, "urlopen",
                              return_value=ImageResponse(b"not an image", "text/html")):
                with self.assertRaisesRegex(fetch_wiki_image.WikiImageError, "unsupported content type"):
                    fetch_wiki_image.fetch_image(self.SOURCE_URL, cache_dir, self.PAGE_URL)

    def test_requires_dedicated_cache_under_system_temp(self):
        with tempfile.TemporaryDirectory(prefix="valheim-wiki-test-") as cache_dir:
            self.assertTrue(Path(fetch_wiki_image._cache_root(cache_dir)).is_dir())
        with self.assertRaisesRegex(fetch_wiki_image.WikiImageError, "under the OS temp"):
            fetch_wiki_image._cache_root(Path(__file__).resolve().parents[1] / "not-a-temp-cache")


if __name__ == "__main__":
    unittest.main()
