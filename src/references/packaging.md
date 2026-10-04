# Package and Publish

## Release files

Put these files at the ZIP root. Distinguish Thunderstore's minimum requirements
from the additional files required by this starter's release convention:

| File | Required by | Content |
| --- | --- | --- |
| `manifest.json` | Thunderstore | Name, version, URL, description, dependencies |
| `icon.png` | Thunderstore | PNG, exactly 256 × 256 pixels |
| `README.md` | Thunderstore | Player-facing instructions |
| `CHANGELOG.md` | This starter | Concise release notes |
| `LICENSE` | This starter | Chosen license; MIT is the default for public examples |

Manifest names use letters, numbers, or underscores and are at most 128 characters.
Descriptions are at most 250 characters. Versions use `Major.Minor.Patch`.
Dependencies use `Team-Package-Version`; the website URL may be empty.

The mod DLL belongs under `BepInEx/plugins/<ModName>/`.
Do not wrap everything in another parent directory. Recheck the
[official package rules](https://wiki.thunderstore.io/mods/creating-a-package)
before a public release.

## Player README

For a new package, adapt the bundled [player README template](../assets/readme-template.md).
It reflects the recurring structure of Landoria mod README files but is not a
mandatory outline. Remove irrelevant sections and add a focused section when the
mod needs one.

Start with a one- or two-sentence introduction that explains the player-visible
purpose. Prefer short feature bullets and compact tables for controls, commands,
settings, and compatibility. Include a BepInEx configuration section whenever
settings exist. Keep build and contributor instructions out of the player-facing
Thunderstore README unless players genuinely need them.

When the mod repository is published on GitHub, include a direct GitHub Issues
link for bug reports. Include GitHub Discussions only when the repository uses it.

Put contributor instructions in `DEVELOPMENT.md`, which the starter excludes
from the release ZIP. The starter README demonstrates this player-facing layout.

## Icon

Before creating a new mod icon, ask the player about their preferred subject,
style, colors, and any constraints. Propose several short visual directions and
wait for the player to choose or explicitly approve one. An already stated,
unambiguous choice counts; do not ask the same question again. Do not generate
the artwork or choose a final design on the player's behalf before this agreement.

Then use the agent's image-generation skill or tool when available. A simple
low-poly Viking/Valheim-inspired direction is one option, not an imposed style.
Create original artwork; transparency is optional.
Resize/export to the exact PNG dimensions and inspect readability.
If image generation is unavailable, ask for an icon or another agreed approach.

This design choice applies to creating mod artwork, not to extracting an existing
inventory icon explicitly requested from the game's assets.

The starter deliberately contains no generic branded icon. Building a DLL needs
no icon; packaging requires one. Do not copy another mod's artwork without permission.

## Version consistency

Start a new mod at `1.0.0`. By default, increment the patch number for each
subsequent release: `1.0.1`, `1.0.2`, and so on. Preserve an existing mod's
release history and any version explicitly chosen by the user.

For the initial `1.0.0` changelog entry, use `Initial Version` by default.
Later entries should briefly describe the changes in that release.

Keep these values in sync:

- `Plugin.PluginVersion`.
- `AssemblyFileVersion` and `AssemblyInformationalVersion` in
  `Properties/AssemblyInfo.cs`.
- `manifest.json` → `version_number`.
- The current `CHANGELOG.md` heading and `thunderstore.toml` package version,
  when that publishing configuration exists.

The template uses `AssemblyVersion("Major.Minor.Patch.*")`.
Only the last assembly component varies. This requires `Deterministic=false`;
if reproducibility matters more, use a fixed fourth component instead.

Thunderstore releases are immutable. Publish a new, unused version rather than
trying to replace an existing one. Add a concise changelog entry.

## Build a local package

Use the .NET SDK's MSBuild targets as the default cross-platform path for building,
staging, and creating the release ZIP on Windows, Linux, and macOS. Prefer MSBuild
tasks such as `Copy` and `ZipDirectory` over platform-specific shell archivers
when they meet the packaging needs. Keep the staged file list explicit.

```bash
dotnet msbuild -restore -t:PackageMod -p:Configuration=Release -p:DeployOnBuild=false
```

The starter stages an explicit file list and the mod DLL, then creates
`artifacts/<ModName>.zip`. It checks required files exist; it does not validate
the icon pixels, all metadata, or version consistency for you.

Before calling the package ready:

- Parse the manifest; check field formats, description length, and dependencies.
- Verify the icon is a readable 256 × 256 PNG.
- Compare plugin, assembly, and manifest versions.
- Compare every player-facing README claim with the current code, configuration,
  manifest, and packaged files. Verify features, defaults, controls, commands,
  file paths, dependencies, client/server requirements, network behavior, and
  known limitations. Remove or correct claims that are unsupported, outdated,
  misleading, or contradicted by the implementation.
- Inspect ZIP entries: no secrets, game DLLs, validator DLL, build caches, or source.
- Install the ZIP in a clean profile and test it.

## Publish the verified archive

For an automated publishing workflow, prefer the open-source
[Thunderstore CLI (`tcli`)](https://github.com/thunderstore-io/thunderstore-cli).
Use it to publish the exact archive already built and checked by MSBuild. Install
the CLI with `dotnet tool install --global tcli`, or pin an appropriate version
in a tool manifest for reproducible CI.

Use one packaging path per release: build the DLL, create the ZIP, run the release
checks above, and publish that exact file. With the starter's MSBuild path:

```bash
tcli publish --file "artifacts/<ModName>.zip" --config-path thunderstore.toml
```

This command uploads the package and requires explicit authorization for the
destination, version, and account/team. Do not run it just to test a workflow.
Use `tcli build` instead of MSBuild only when the user requests it or a concrete
project requirement needs its packaging behavior. Inspect and test its resulting
ZIP, then pass that exact ZIP to `publish --file`; do not rebuild after verification.
See the [TCLI command reference](https://github.com/thunderstore-io/thunderstore-cli/wiki).

Keep namespace, package version, communities, and categories in `thunderstore.toml`.
Configure file mappings only when TCLI performs packaging. Check its metadata
against the ZIP manifest before publishing.

## Publishing categories

Retrieve the current [Valheim categories](https://thunderstore.io/api/experimental/community/valheim/category/).
For another community, replace `valheim` in that URL. Read the `slug` fields and
use them under `[publish.categories]` in `thunderstore.toml`, not `manifest.json`.
Do not invent slugs or treat the example below as a permanent list.

Categories are important discovery and compatibility metadata. Select applicable
categories and verify their current slugs immediately before publishing:

- Add `ai-generated` without asking when this skill creates or modifies the mod
  or package. Omit it only for advice that did not change the artifact.
- Add `client-side` for client installations and `server-side` for dedicated
  server installations. Use both when both roles are supported or required;
  explain which installations and matching versions players actually need.
- Add `deep-north-update` only when compatibility has been tested on that update.
  Merely targeting the update is not evidence. If testing is pending, say so.

Example for an AI-assisted mod tested in both roles on Deep North:

```toml
[publish.categories]
valheim = ["ai-generated", "client-side", "server-side", "deep-north-update"]
```

## CI publishing

- Use GitHub Actions when CI is requested; the starter includes no workflow.
- Use a Thunderstore team and an appropriately scoped service account.
- Store the service-account token in the CI secret store and expose it to the
  publish step as `TCLI_AUTH_TOKEN`, following the shared secret-handling rule.
- Trigger publishing from an intentional release, version tag, or protected
  manual workflow. Pull requests and ordinary branch pushes should build and
  validate but must not publish.
- Pin the CLI or action version. TCLI releases can be pre-release software, so
  review changes before upgrading.
- Prefer invoking the official CLI directly. Review third-party publishing
  actions before using them; they are not maintained by Thunderstore.

[LandoriaModActions](https://github.com/landoria-gaming/LandoriaModActions) is a
reference, not a drop-in public dependency: inspect its current inputs and access
requirements first. Do not add a private reference bundle or require
`MOD_REFERENCES_TOKEN` without the user's agreement and access.
