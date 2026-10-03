# Valheim Wiki guide

Use the English-language [Valheim Wiki](https://valheim.fandom.com/wiki/Valheim_Wiki)
as a community-maintained secondary reference and page finder for player
questions. The wiki describes itself as approved by Valheim's developers, but it
is not first-party game documentation; use official Iron Gate and Valheim sources
for official statements. Always search and read the English article, even when
the user asks in another language; translate the query to English as needed, then
answer in the user's language. Treat the English wiki as the preferred, most
up-to-date wiki version.

Its main page groups articles into families such as Biomes, Weapons, Food, Armor,
Creatures, Crafting, Building, and How to play. The quick-navigation index also
groups World, Creatures, Food and meads, Weapons, Armor and accessories, Tools,
Buildings, Materials, and Mechanics. Follow the family that best matches the
question, then open a focused English article rather than relying on a broad
overview.

## Find the relevant page

| Question | Page family | Useful details to check |
| --- | --- | --- |
| What lives or grows in a biome? | [Biomes](https://valheim.fandom.com/wiki/Biomes), creatures, materials | Resources, gatherables, creatures, dungeons, points of interest, and progression context |
| How do I fight a creature or boss? | [Creatures](https://valheim.fandom.com/wiki/Creatures) | Biome, internal ID, health, attacks and damage types, resistances, drops, spawning, taming, summoning, and combat notes |
| Which weapon or shield should I use? | [Weapons](https://valheim.fandom.com/wiki/Weapons) | Weapon type, damage by attack, stamina, durability, block/parry values, special attacks, and crafting source |
| What armor or accessory does what? | [Armor](https://valheim.fandom.com/wiki/Armor) | Armor by quality, weight, set effects, movement or status effects, crafting station, and upgrade costs |
| How do I make or obtain an item? | [Crafting](https://valheim.fandom.com/wiki/Crafting), materials, tools, food | Internal ID, source or drops, ingredients, output, station, use, and progression unlocks |
| How does a station or building work? | [Building](https://valheim.fandom.com/wiki/Building), crafting, mechanics | Creation and upgrade recipes, station level, processing steps, fuel, nearby requirements, and building rules |
| How does a game system work? | Mechanics, World, How to play | Rules, multipliers, thresholds, controls, and conditions that point to the relevant code |
| What should I eat? | [Food](https://valheim.fandom.com/wiki/Food) and meads | Ingredients, health/stamina/eitr values, duration, effects, and crafting source |

The family names above are navigation aids, not a promise that every article is
up to date or complete. Use installed code first when the requested fact concerns
executable rules or runtime behavior. When a content fact is known not to be
represented in code, go directly to the relevant wiki page. If the wiki answers
the question, give that answer and identify the wiki as its source; do not imply
it was verified against code or assets. Inspect assets only when the wiki is
missing, ambiguous, or conflicts with another source, when the question is
specifically about an asset, or when the user asks for a recheck. Explain any
known discrepancies and check the article's date or game-version context when
available.

## Search and session cache

Use the helper scripts to search and read pages. Search needs only Python's
standard library; converting an article to Markdown needs the pinned open-source
dependency:

```text
python -m pip install -r scripts/requirements-wiki.txt
python scripts/search_wiki.py "onion so"
python scripts/wiki_to_markdown.py "Onion Soup"
```

Install the dependency in an agent-owned virtual environment, not the system
Python environment. The first command prints matching titles, IDs, and page URLs
as JSON. Copy an exact title into the second command; it prints the article as
Markdown. Both commands use Python's standard library for HTTP and save no wiki
content.

Choose the exact English article title from the search results and pass it to the
Markdown converter. Search calls Fandom's suggestion endpoint; the second script requests
the rendered article through MediaWiki's parse API, extracts `<main>` or Fandom's
`.mw-parser-output` content, and prints Markdown to standard output. It does not
write the page or conversion to disk. Read its output in the current task rather
than redirecting it to a repository file.

The converter is for reading and formatting, not for verifying game facts. Check
tables and unusual page markup in the rendered article when the Markdown looks
incomplete or malformed.

During the current session, keep each fetched article's Markdown available in
working context, keyed by its canonical page URL, and reuse it instead of fetching
or converting the same page again. Fetch it again only if the user asks for a
refresh or the output missed needed content; if extraction looks incomplete, view
the article page as a fallback. This is session-only caching: do not save wiki
pages or converted Markdown to the persistent disk cache or repository by default.

## Display wiki images

Only fetch an article image when it is relevant to the answer and you intend to
show it to the user. Resolve the article's image to its best available source
file (not a tiny thumbnail when a suitable original is linked), then download it
to a temporary, session-local cache and display the local cached copy. Key the
cache by the canonical image URL and reuse that file if the same image is shown
again during the session; do not download it twice unless the user requests a
refresh or the cached file is missing or invalid. Use the platform's supported
local-image display mechanism and an absolute local path. Do not commit the image,
put it in the mod, or retain it in the persistent game-data cache. Keep the source
page or image attribution available when presenting it.

For image URLs hosted on `static.wikia.nocookie.net`, strip the URL at the end of
the actual image filename extension before downloading. Remove any trailing
`/revision/...` path, query string, or fragment after `.png`, `.jpg`, `.jpeg`,
`.gif`, `.webp`, or another recognized image extension. For example, turn
`https://static.wikia.nocookie.net/valheim/images/8/82/Greydwarf.png/revision/latest/scale-to-width-down/536?cb=...`
into `https://static.wikia.nocookie.net/valheim/images/8/82/Greydwarf.png`.
Download that cleaned URL into the session cache, then display the cached file;
do not embed the remote image URL directly in the conversation.
