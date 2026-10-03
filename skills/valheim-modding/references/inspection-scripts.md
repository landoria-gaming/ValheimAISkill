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
python scripts/inspect_code.py --game "/path/to/Valheim" decompile
```

`types` lists all supported kinds and filters names without decompiling the whole
game. `type` writes one C# or IL file and reports its absolute path; `--print`
prints the code, and `--query` returns matching lines. Use `rg` on that cached
file when more context is needed. No DLL is executed.

Use `decompile` when a question needs broad searches across multiple classes or
assemblies. It decompiles `assembly_valheim.dll`, `assembly_utils.dll`, and
`assembly_guiutils.dll` into a persistent local C# project, then reports its path.
Search that directory with `rg` rather than decompiling individual types again.
The cache key includes the game version read from the installed `Version` type,
the SHA-256 of each selected assembly, the managed reference DLL stamps, and the
ILSpy version. Its manifest also verifies every generated source file before a
cache hit. A hotfix, changed reference set, ILSpy update, or damaged output gets
a separate extraction; old version folders are retained. This is decompiled
inspection material, not official source code, and must not be committed,
distributed, or treated as runtime behavior proof by itself.

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
With `--tool`, repeated icon and targeted export requests reuse verified local
results without starting AssetRipper or reloading the inputs. `cache_hit` reports
reuse. A `--base-url` service has no verified local tool identity, so these requests
retain the output but always extract again. Search still uses a live session;
its locators must not be reused in another session.

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
  --english-names \
  --output "/chosen/report/valheim-prefabs.md"
```

Only request a bulk inventory when needed; a single icon or recipe uses targeted
inspection. English names come from component fields and the local translation
files in `LocalizationSettings` order, not a guessed conversion of prefab IDs.
Unknown names remain blank. The report states scope and missing data.
Bulk inspection resumes from the persistent cache by default. Optional `--cache`
selects another local metadata file outside repositories; keep it for later runs.

### Static models for Unity Editor

```bash
python scripts/export_model.py wood_stack \
  --game "/path/to/Valheim" --tool "/path/to/AssetRipper.GUI.Free"
```

Use an exact prefab name or catalog path. Optional `--output` must name a **new**
directory outside the game and Git repositories. Otherwise the export is kept in
the [persistent cache](#cache-and-limits). The result includes a `.unitypackage`,
its editable `Assets` tree, import instructions, and local provenance.

- UnityPy selects only the static hierarchy, renderers, LOD groups, meshes,
  materials, and base textures in memory. AssetRipper converts that small selection
  into native Unity assets. The original game bundle is never rewritten.
- Import with **Assets > Import Package > Custom Package** in a separate Unity 6
  Built-in Render Pipeline project. Open the exported prefab or drag it into a
  scene. Prefer the recorded source Unity version or a compatible newer editor.
- The root position is reset to zero; child transforms, mesh data, inactive visual
  variants, and material tint are retained. Game scripts, physics, colliders,
  particles, audio, and gameplay behavior are intentionally absent.
- A supplied diffuse preview shader replaces the compiled game shaders. Only
  `_MainTex` base textures are included; normal, emission, noise, and other maps
  and game-specific effects are omitted and reported. URP/HDRP need a separate
  material conversion. This is not an exact in-game appearance reconstruction.
- This first exporter supports static models whose visual references resolve in
  one serialized collection. Skinned/animated prefabs, external dependencies,
  material variants, and static batches fail explicitly; do not claim they were
  exported. Do not use this version for a Greydwarf character.

Validate a requested export in Unity when available: check meshes, materials,
references, transforms, and visible rendering. The repository's optional
`scripts/test_model_import.py` imports the package into an isolated project and
renders a preview; it does not modify an existing Unity project or run Valheim.
An archive structure check alone does not establish successful Unity import.

## Cache and limits

### Use targeted lookups and caches

For a player question, use the relevant [Wiki article](sources.md#community-reference)
to locate the likely creature, item, recipe, biome, or mechanic. Then inspect only
the matching local code and asset data needed to verify the answer. This avoids
reopening broad sets of bundles and avoids building a full-game database.

Notice when a specific inspection is slow or likely to be repeated. Reuse the
existing persistent, version-keyed caches for decompiled types, prefab catalogs,
icons, and requested asset properties. Offer a narrowly scoped catalog only when
it would help with likely future questions, explain what it contains and any
known time/storage cost, and wait for agreement before a long batch extraction.
Do not propose indexing every bundle or rebuilding a full-game SQLite database.

During an agreed long targeted extraction, keep it low priority when possible and
send brief progress updates at meaningful stages, roughly once a minute when the
interface allows. Report actual phases and completed/total counts; give a
percentage only when its denominator is known. Do not imply a phase percentage
is overall completion or invent a remaining-time estimate. Report completion,
partial coverage, or failure clearly.

### Storage and validity

Reuse inspection results across tasks and agent restarts. Store them under a
persistent per-user data directory, not the OS temporary directory:

| OS | Default cache root |
| --- | --- |
| Windows | `%USERPROFILE%/.cache/valheim-modding` (outside desktop-app sandbox caches) |
| Linux | `$XDG_DATA_HOME/valheim-modding/cache`, or `~/.local/share/valheim-modding/cache` |
| macOS | `~/Library/Application Support/ValheimModdingSkill/cache` |

Set `VALHEIM_SKILL_CACHE` to an absolute directory to override it. Git repositories
are rejected. The cache contains:

- `indexes/`: prefab facts, English names, bulk catalogs, and bundle indexes.
- `code/`: ILSpy type lists and requested C#/IL extracts.
- `images/`: inventory icons and targeted PNG exports.
- `assets/`: targeted JSON properties and other supported asset exports.
- `exports/`: static model packages, kept without automatic reuse.

Do not clear this cache at task completion. Old entries are retained; cleanup is explicit
and targeted. A new model export creates a new directory rather than overwriting
another result. This local storage is durable across sessions, not a backup or a
guarantee against user/disk cleanup.

AssetRipper working files and service logs remain temporary; stopping the
task-owned service does not delete persistent results. Existing temporary results
are not blindly migrated: a first request regenerates a verified persistent entry.
Never commit cached game data or include it in the
skill ZIP. Share only the specifically requested report or permitted export.

Targeted code caches use DLL hashes, reference file stamps, tool version, and script identity.
Full-project code caches use the exact game version, selected assembly hashes,
managed reference stamps, ILSpy version, and a manifest of generated-file hashes.
Asset caches use input paths, sizes, modification times, and script identity.
Targeted exports also include request options and local tool-file stamps. Code,
icon, and targeted-export hits verify output SHA-256 and provenance; damaged or
incomplete entries are regenerated. A normal game update invalidates the affected
cache. For files modified while preserving size and timestamps, use a new cache
location or remove only the confirmed affected entry. Prefab-catalog resume caches
include the manifest hash, bundle stamps, and inspector revision; an explicitly
selected stale cache is rejected rather than silently reused.

These helpers do not install tools automatically, execute game assemblies, export
a reconstructed game project, or promise runtime values unaffected by mods.
The stripped `LocalizationSettings` fallback is checked for the observed Unity 6
layout and fails on unexpected fields. Keep the [manual workflow](assets.md) and
[DLL inspection guide](environment.md#inspect-the-actual-game) as fallbacks.
