"""Tests for the Valheim Wiki suggestion and Markdown helpers."""

import importlib.util
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/valheim-modding/scripts"
sys.path.insert(0, str(SCRIPTS))

import search_wiki
import wiki_to_markdown


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


if __name__ == "__main__":
    unittest.main()
