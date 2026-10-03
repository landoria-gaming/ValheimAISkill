# Inspect and Extract Unity Assets

Use this reference for prefabs, recipes, localization, textures, and other game
data that DLL inspection alone cannot establish. Work from the user's installed
game version; do not assume a particular bundle layout.

Start with the [reusable scripts](inspection-scripts.md) for prefab lookup,
English display names, and inventory icons. Use the manual API below to investigate
unsupported cases or changed tool versions.

## Choose the input

| Input | Approach |
| --- | --- |
| `.unitypackage` | An editor asset package, not a compiled AssetBundle. Inspect its archive safely or import trusted contents into a separate disposable Unity project. Review scripts before importing. |
| Serialized player files such as `.assets` | Open the relevant files with AssetRipper; preserve nearby resource streams needed for decoding. |
| AssetBundles, including extensionless files | Load the bundle and the required dependencies; names and extensions alone do not identify contents. |
| A readable game catalog or localization file | Inspect it directly first. It may identify exact asset paths and avoid a full game export. |

For Valheim, check whether `StreamingAssets/SoftRef/manifest_extended` exists.
In the checked 1.0.16 installation, this text catalog maps asset IDs to bundles
and original paths. Entries ending in `.prefab` are useful for an inventory.
That catalog is not a list of every runtime object or a guarantee of spawnability.

## Start AssetRipper

Prefer the open-source [AssetRipper](https://github.com/AssetRipper/AssetRipper).
Select an official release for the host OS and architecture; verify its published
checksum when available and its support for the game's Unity version. Keep the
tool and extracted files outside the mod repository. Installation is conditional,
not a requirement for a simple gameplay question.

The following interface was checked against **AssetRipper 2.0.0 Free**. Run
`--help` on the installed release and check its live API schema before automation:

```bash
"$ASSETRIPPER_EXE" --help
"$ASSETRIPPER_EXE" --headless --port "$ASSETRIPPER_PORT"
```

On Windows the executable is `AssetRipper.GUI.Free.exe`. Use a hidden background
process with captured logs for automation; do not open an unwanted console window.
`--headless` suppresses the browser, not the local web service. Keep the service on
loopback: this version binds to `127.0.0.1`. Do not expose it to a LAN or the internet.
Record the PID and stop only the process started for this task when finished.

Set `BASE_URL` to the observed local address. Read `GET /openapi.json` or visit
`/swagger`. Do not invent a nonexistent `--input` or `--export` CLI switch.

## Load and locate

1. Load one relevant file first. The 2.0.0 API accepts form-encoded local paths:

   ```bash
   curl --fail --location --data-urlencode "Path=$ASSET_INPUT" "$BASE_URL/LoadFile"
   ```

   Use `/LoadFolder` for a selected directory; repeated `Path` fields accept
   multiple inputs. Avoid a whole-game load when a catalog or small bundle suffices.
   Watch memory use: compressed texture bundles can expand substantially.
2. Read the import log. A redirected HTTP success does not prove every dependency
   or script was decoded. Missing dependencies require loading the matching files
   or reporting incomplete properties, not treating missing values as zero.
3. Search through `/Search/View?q=QUERY`, then follow the returned asset,
   collection, and bundle links. Search matches names and classes; a GameObject
   with a familiar name may be an animation child rather than the prefab root.
4. For a bundle, inspect its `AssetBundle` object's JSON `m_Container` map. Match
   the original `.prefab` path to its asset reference, then inspect that object.
   Do not equate every GameObject with a prefab or every prefab with a console ID.
5. Keep the exact `Path` locator returned by the tool. It is JSON identifying a
   collection and a path ID, not a filesystem path. IDs can be signed 64-bit values:
   preserve them exactly and do not parse them into an imprecise JavaScript Number.

## Extract information or an image

These are **GET** endpoints from the checked API. URL-encode the observed `Path`
value; never guess collection indices or IDs. `ASSET_PATH` below is the decoded
locator JSON copied from a real asset link, and `ASSET_OUTPUT` is a chosen directory.

| Endpoint | Result |
| --- | --- |
| `/Assets/Json?Path=…` | Serialized properties and references; parse and validate the response |
| `/Assets/Yaml?Path=…` | YAML representation when supported |
| `/Assets/Text?Path=…` | Decoded text for a supported TextAsset, including possible localization data |
| `/Assets/Image?Path=…&Extension=png` | Decoded texture or sprite image |
| `/Assets/Binary?Path=…` | Raw data for supported raw objects, not a universal image export |

```bash
curl --fail --get --data-urlencode "Path=$ASSET_PATH" \
  "$BASE_URL/Assets/Json" --output "$ASSET_OUTPUT/asset.json"
curl --fail --get --data-urlencode "Path=$ASSET_PATH" \
  --data-urlencode "Extension=png" \
  "$BASE_URL/Assets/Image" --output "$ASSET_OUTPUT/image.png"
```

Check the response type and contents; an error can be text rather than valid JSON.
For an image, verify its signature and dimensions and open it for visual inspection.
Preserve transparency. AssetRipper 2.0 can return the whole atlas for a Sprite:
follow the exact reference and extract its recorded rectangle and packing rotation.
The [icon helper](inspection-scripts.md#inventory-icons) does this for supported
rectangular sprites and rejects unsupported layouts. Do not regenerate or approximate an image
when the task is to extract its actual pixels.

For a requested bulk export, `/Export/PrimaryContent` or `/Export/UnityProject`
accepts an output `Path` form field. Use a new empty directory and check disk space;
these are broad exports, not replacements for a targeted asset request.

## Interpret and report

- Cross-reference serialized values with loading code, prefab references, and
  mod overrides. Asset defaults may differ from active runtime values.
- Trace recipe ingredients, counts, stations, and unlock rules. Match localization
  keys to the relevant language; a translated name alone does not prove a mechanic.
- For prefab inventories, retain original path and bundle provenance. Separate
  observed properties from categories inferred from folders. State coverage and
  unreadable dependencies; a catalog-only inventory is not a runtime enumeration.
- Keep inspection read-only. Extract outside the repository; do not overwrite game
  assets, bypass access controls, or silently install a runtime diagnostic mod.
- Share the requested factual report or permitted individual export, not proprietary
  bundles, a reconstructed game project, or full translation tables in a mod or Skill.

API sources: [launcher and routes](https://github.com/AssetRipper/AssetRipper/blob/2.0.0/Source/AssetRipper.GUI.Web/WebApplicationLauncher.cs),
[asset endpoints](https://github.com/AssetRipper/AssetRipper/blob/2.0.0/Source/AssetRipper.GUI.Web/Pages/Assets/AssetAPI.cs),
[command inputs](https://github.com/AssetRipper/AssetRipper/blob/2.0.0/Source/AssetRipper.GUI.Web/Pages/Commands.cs).
