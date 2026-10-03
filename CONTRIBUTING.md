# Maintain the skill

Edit `skills/valheim-modding/`, the source of truth. Do not edit the installed
copy or ZIP directly. Keep shared rules in `SKILL.md` and task-specific details
in focused references; the source index is for finding links, not repeating rules.

## Check and package

Use Python 3.10+ and the .NET 10 SDK. Run from the repository root:

```bash
python scripts/test_skill.py
python scripts/test_inspection.py
python scripts/package_skill.py
```

The tests check archive reproducibility, unwanted-file exclusion, link failures,
and real template generation for default and custom versions in an isolated .NET
template registry. They do not change the user's registered templates.

The packager validates the source and writes `dist/valheim-modding.zip` from an
explicit file list, including hidden template configuration. It rejects missing
files, broken local links, symlinks, and common absolute personal paths in shipped
text. Add intentional new resources to its file list. These checks are not a full
secret scanner or a substitute for reviewing content.

If Codex's `skill-creator` validator is available, also run its
`scripts/quick_validate.py` against the source folder. That validates skill format,
not the ZIP contents or gameplay.

Inspection tests also need the Python dependencies in
`skills/valheim-modding/scripts/requirements-assets.txt`. They use synthetic
fixtures, not proprietary game files. Live ILSpy and AssetRipper checks use the
local game installation and remain separate from CI.

## Snapshot releases

The GitHub workflow tests the skill on Windows, Linux, and macOS after pushes to
`main`, and validates pull requests without publishing. On success for `main`,
it packages the skill and updates the rolling `snapshot` prerelease and ZIP.
The reserved `snapshot` tag moves to the published commit; stable version tags
are untouched. The workflow uses GitHub's temporary token, not a stored PAT.
Manual dispatch is available; publishing remains restricted to `main`.

## Optional build checks

Set `VALHEIM_PATH` and `BEPINEX_PATH` to a real local installation, then run:

```bash
python scripts/test_skill.py --with-game
```

Set `VALHEIM_MANAGED_PATH` too if the game uses a different Managed layout.
These checks build a generated mod, verify that a normal build does not deploy,
exercise explicit deployment into a temporary directory, reject a missing icon,
and inspect a release ZIP. They never deploy into a live profile or start the game.
All generated projects, build caches, and test icons stay outside this repository.

### Optional model import check

After exporting a static prefab, validate the actual package with an installed,
licensed Unity Editor. This creates a separate temporary Built-in project; it
does not modify an existing project, start Valheim, or install Unity:

```bash
python scripts/test_model_import.py --unity "/path/to/Unity" \
  --package "/local/cache/wood_stack.unitypackage"
```

The test imports the package, checks meshes/materials/references, and renders a
preview. It waits for the import-completed callback before validation. Open the
reported PNG for visual review. The script exits only its own test Editor;
Valheim clients, servers, and other Editor processes are untouched.
Report the tested editor version and render pipeline; do not infer URP/HDRP or
animated-model support from this static test. Generated game assets never enter
CI fixtures, Git, or the skill archive.

Report the OS and SDK used. Test game behavior separately; successful builds do
not establish gameplay or cross-platform compatibility.

## Update an installation

1. Run the checks and rebuild the ZIP from the source folder.
2. Back up an existing installed `valheim-modding` folder outside skill discovery
   locations. Compare it with the source and preserve any intentional local changes.
3. Replace only that installed skill with the ZIP's `valheim-modding` folder.
   Do not merge obsolete files or copy source build caches into the installation.
4. Compare installed files with the archive. Refresh the agent if needed.
5. If `dotnet new` was registered from that installed copy, refresh it with
   `dotnet new install "/absolute/installed/path/assets/mod-template" --force`.

Keep the installation path stable so future template generation uses the updated
files. Do not install a second copy with the same skill name at another scope.

The starter originated in the HowToModValheim examples. It does not require that
repository, private reference bundles, or distributed game assemblies.
