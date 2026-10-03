# Reusable Inspection Scripts

Use these helpers before writing another one-off extractor. They inspect local
files without starting Valheim, loading a diagnostic mod, or changing game data.
Run them with Python 3.10+ from this skill's directory. Paths below are placeholders.
The installed-game gate in `SKILL.md` applies before every inspection command,
including commands that could otherwise use cached data or an explicit DLL.

## Setup

- Install the official [ILSpyCMD](https://github.com/icsharpcode/ILSpy) .NET tool
  (`dotnet tool install --global ilspycmd`) only if missing and installation is in scope.
- Download the correct official [AssetRipper](https://github.com/AssetRipper/AssetRipper/releases)
  build for the host. Check its checksum; do not silently update an existing tool.
- For fast asset metadata and sprite processing, install the pinned open-source
  [UnityPy](https://github.com/K0lb3/UnityPy) dependency in an agent-owned temporary
  Python environment: `python -m pip install -r scripts/requirements-assets.txt`.
  ILSpy remains the decompiler; AssetRipper decodes the exported image pixels.
- Pass `--game "/path/to/Valheim"` or set `VALHEIM_PATH`. Client roots
  (`valheim_Data`), dedicated-server roots (`valheim_server_Data`), a data folder,
  or a macOS app bundle are accepted. Pass `--assembly` for a DLL outside the usual layout.

Checked versions: ILSpyCMD 10.1.0.8386, AssetRipper 2.0.0 Free, UnityPy 1.25.2.
Tool changes may require adapting these scripts; these are not necessarily the
latest releases.

## Code: inspect assemblies and types

```bash
python scripts/inspect_code.py --game "/path/to/Valheim" assemblies
python scripts/inspect_code.py --game "/path/to/Valheim" types --query ItemDrop
python scripts/inspect_code.py --game "/path/to/Valheim" type ItemDrop --query GetHoverName
python scripts/inspect_code.py --game "/path/to/Valheim" type Character --il
python scripts/inspect_code.py --game "/path/to/Valheim" --assembly assembly_guiutils.dll type Localization
```

`types` lists all supported kinds and filters names without decompiling the whole
game. `type` writes one C# or IL file and reports its absolute path; `--print`
prints the code, and `--query` returns matching lines. Use `rg` on that temporary
file when more context is needed. No DLL is executed. Full project decompilation
remains an explicit ILSpy operation, not the default for a question.

## Assets: search, inspect, and extract

```bash
python scripts/inspect_assets.py --game "/path/to/Valheim" catalog Wood
python scripts/inspect_assets.py --game "/path/to/Valheim" prefab Wood
python scripts/inspect_assets.py --game "/path/to/Valheim" --tool "/path/to/AssetRipper.GUI.Free" icon Wood
python scripts/inspect_assets.py --game "/path/to/Valheim" --tool "/path/to/AssetRipper.GUI.Free" search --input "/path/to/bundle" --query Recipe_ArrowWood
python scripts/inspect_assets.py --game "/path/to/Valheim" --tool "/path/to/AssetRipper.GUI.Free" export --input "/path/to/resources.assets" --query localization --class TextAsset --id 347 --format text
```

The last ID is an example from the checked build: get the current ID from
`search`, never assume it is stable. On Windows use `AssetRipper.GUI.Free.exe`.
`--tool` starts a hidden loopback service for the command and stops only that
process afterwards. `--base-url http://127.0.0.1:PORT` reuses a **dedicated**
service instead: loading inputs replaces its current session, so do not point
it at another person's active inspection. Repeat `--input` to include required
dependencies. `export` supports JSON, YAML, text, PNG, and supported raw binaries.
Ambiguous names fail instead of silently selecting the first match.

### Inventory icons

`icon Wood` follows the exact prefab's `ItemDrop.m_itemData.m_shared.m_icons`
reference. `--variant 0` is the default; select another index only when it exists.
This is an inventory image, not a 3D render, screenshot, or approximate replacement.
Return the generated PNG inline after opening it for visual verification.

AssetRipper 2.0's image endpoint can return the **whole atlas even for a Sprite**.
The helper extracts the recorded rectangle, handles rectangular packing rotation,
and preserves transparency. It refuses unsupported tight packing, external sprite
atlases, and separate alpha textures rather than returning an incorrect icon.
For these cases, inspect the dependencies and use a verified mesh-aware extractor.
Some prefabs have no inventory icon; report that fact without inventing one.

### Prefab inventory with English names

```bash
python scripts/export_prefab_catalog.py \
  --manifest "/path/to/valheim_Data/StreamingAssets/SoftRef/manifest_extended" \
  --base-url http://127.0.0.1:PORT --game-version VERIFIED_VERSION \
  --cache "/agent/temp/prefab-cache.json" --english-names \
  --output "/chosen/report/valheim-prefabs.md"
```

Only request a bulk inventory when needed; a single icon or recipe uses targeted
inspection. English names come from component fields and the local translation
files in `LocalizationSettings` order, not a guessed conversion of prefab IDs.
Unknown names remain blank. The report states scope and missing data.

## Cache and limits

Generated code, metadata, images, and provenance stay under the operating system's
temporary directory, in `valheim-skill-inspection`; service logs use a separate
`valheim-assetripper-…` directory. Treat these as disposable local data. Never commit
or package them. Share only the specifically requested report or permitted image.

Code caches use DLL hashes, reference file stamps, tool version, and script identity.
Asset caches use input paths, sizes, modification times, and script identity; image
cache hits also verify the PNG hash. A normal game update invalidates the affected
cache. For files modified while preserving size and timestamps, use a fresh temp
location or remove only the confirmed inspection cache. A prefab-catalog resume
cache is tied to its manifest; start a new one after any game update.

These helpers do not install tools automatically, execute game assemblies, export
a reconstructed game project, or promise runtime values unaffected by mods.
The stripped `LocalizationSettings` fallback is checked for the observed Unity 6
layout and fails on unexpected fields. Keep the [manual workflow](assets.md) and
[DLL inspection guide](environment.md#inspect-the-actual-game) as fallbacks.
