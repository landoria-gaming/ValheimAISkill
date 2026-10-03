#!/usr/bin/env python3
"""Search the Valheim Wiki suggestion endpoint and print matching page titles."""

import argparse
import json
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


API_URL = "https://valheim.fandom.com/wikia.php"
USER_AGENT = "ValheimModdingSkill/1.0 (wiki page discovery)"
TIMEOUT_SECONDS = 20
MAX_RESPONSE_BYTES = 1024 * 1024


class WikiRequestError(Exception):
    """A safe, concise error for network and API failures."""


def search(query):
    """Return suggestions from Fandom without writing the response to disk."""
    query = query.strip()
    if not query or len(query) > 200:
        raise WikiRequestError("Enter a search query between 1 and 200 characters")
    url = API_URL + "?" + urlencode({
        "controller": "UnifiedSearchSuggestions",
        "method": "getSuggestions",
        "query": query,
        "format": "json",
        "scope": "internal",
    })
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            if response.status != 200:
                raise WikiRequestError(f"Wiki search returned HTTP {response.status}")
            payload = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as error:
        raise WikiRequestError(f"Wiki search returned HTTP {error.code}") from None
    except (URLError, TimeoutError, OSError) as error:
        raise WikiRequestError(f"Could not reach the Valheim Wiki: {error}") from None
    if len(payload) > MAX_RESPONSE_BYTES:
        raise WikiRequestError("Wiki search response exceeded the 1 MiB safety limit")
    try:
        data = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise WikiRequestError("Wiki search returned invalid JSON") from None
    titles = data.get("suggestions")
    if not isinstance(titles, list) or any(not isinstance(title, str) for title in titles):
        raise WikiRequestError("Wiki search response has an unexpected format")
    ids = data.get("ids", {})
    return {
        "query": data.get("query", query),
        "suggestions": [
            {
                "title": title,
                "page_id": ids.get(title) if isinstance(ids, dict) else None,
                "url": "https://valheim.fandom.com/wiki/" + quote(
                    title.replace(" ", "_"), safe="()'!,.-_"
                ),
            }
            for title in titles
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Words to search for, for example: 'onion so'")
    args = parser.parse_args()
    try:
        print(json.dumps(search(args.query), ensure_ascii=False, indent=2))
    except WikiRequestError as error:
        parser.exit(1, f"Wiki search failed: {error}\n")


if __name__ == "__main__":
    main()
