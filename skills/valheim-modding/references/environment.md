# Environment

## Supported approach

This toolchain is for mod development only. Gameplay questions and vanilla-game
support need access to the installed game files, not this setup.

Use the [.NET 10 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0),
[VS Code](https://code.visualstudio.com/download) or
[JetBrains Rider](https://www.jetbrains.com/rider/download/), and Bash-compatible scripts.
These tools are available on Windows, macOS, and Linux. Examples below favor Windows.

```text
.NET 10 SDK
    ↓ compiles
DLL targeting net48
    ↓ loaded by
BepInEx 5
    ↓ runs on
Mono bundled with Unity/Valheim
```

.NET Framework 4.8 itself is Windows-only. This build uses reference assemblies
from NuGet; the mod runs on the game's Mono runtime, not the desktop .NET Framework.
Do not assume every net48 API or native dependency is portable.
No Visual Studio desktop workload or Windows Build Tools is required by the template.

## What each task needs

| Task | Required local setup |
| --- | --- |
| Ask about Valheim gameplay, recipes, commands, or a vanilla-game problem | Read access to the installed Valheim game files. No BepInEx profile or developer tools are required. |
| Diagnose a mod problem or inspect BepInEx logs | The game files and, when relevant, access to the user's selected mod-manager profile and logs. |
| Create, build, launch, or test a mod | The game files, selected BepInEx profile, and the build/runtime tools needed by that task. |

Resolve the game directory from an explicit path or `VALHEIM_PATH` when provided.
Otherwise, check the last verified local path, then common Steam libraries and
the standard Xbox location. If multiple installs are accessible, ask which one
to use. After verifying that the managed assembly and game data are readable,
remember the path and assembly fingerprint in the user's persistent skill cache,
outside the repository. Revalidate it on later requests; if it moved or became
inaccessible, ask for the new path. Never put it in the mod, repository, README,
or package. The user needs no developer environment variable for gameplay help.

## Install and isolate a modding profile

Only use this setup for mod development, modded launch, or mod-specific
diagnostics. Do not make it a prerequisite for ordinary gameplay questions or
vanilla-game support.

- Install [Valheim](https://www.valheimgame.com/) through the chosen store.
- Use the player's chosen mod manager. Open-source options include
  [r2modman](https://thunderstore.io/package/ebkr/r2modman/),
  [Gale](https://github.com/Kesomannen/gale) for Windows/Linux (GPL-3.0), and
  [Macheim](https://github.com/lofcgi/macheim) for macOS (MIT).
  Check the selected manager's current store and platform support; do not require
  migration to r2modman.
- Create a profile such as `dev`; install
  [BepInExPack Valheim](https://thunderstore.io/c/valheim/p/denikson/BepInExPack_Valheim/).
- Launch modded once to create config and logs. Keep this profile for development.
- Manual BepInEx installation is an alternative: use the pack's ZIP instructions.
  Do not mix a manual game-root installation with a profile without understanding
  which loader and plugin directory will run.

| Variable | Purpose / Windows example |
| --- | --- |
| `VALHEIM_PATH` | Optional override: game root containing the executable and game data; normally discovered and remembered after first verification |
| Steam default | `%ProgramFiles(x86)%\Steam\steamapps\common\Valheim` |
| Xbox default root | `C:\XboxGames\Valheim`; check whether the executable/data are under `Content` |
| `BEPINEX_PATH` | Optional task-specific path to the selected profile's BepInEx directory; resolve only when the task needs that profile |
| `STEAM_PATH` | Steam client directory containing `Steam.exe`; resolve it independently of the game library |

Resolve paths from the selected manager on the actual machine; the profile paths
below and above are r2modman examples, not shared layouts. Use `%APPDATA%`, not a
personal username, in Windows documentation. Restart the editor/agent after
changing persistent variables.

| Context | Variable syntax |
| --- | --- |
| Windows path fields / cmd | `%APPDATA%` |
| PowerShell | `$env:APPDATA` |
| Git Bash / Bash | `$APPDATA`, `$VALHEIM_PATH` |
| MSBuild | `$(VALHEIM_PATH)`, `$(BepInExPath)` |

Git Bash example for a mod-development session only (no secrets):

```bash
export VALHEIM_PATH='C:/Program Files (x86)/Steam/steamapps/common/Valheim'
export BEPINEX_PATH="$APPDATA/r2modmanPlus-local/Valheim/profiles/dev/BepInEx"
```

On Linux/macOS use the real game and profile paths. The template defaults
`ValheimManagedPath` to `$(ValheimGamePath)/valheim_Data/Managed`.
For a macOS app bundle or another layout, locate `assembly_valheim.dll` and
override `-p:ValheimManagedPath="/actual/path/to/Managed"`.

## Launch the modded Windows client

Follow [Launching](launching.md) to reproduce r2modman's **Start modded** behavior
for the selected store and profile. It covers Steam, Xbox/Game Pass, Doorstop
versions, and the [direct executable alternative](launching.md#direct-executable-alternative).

## Inspect the actual game

Inspect the installed Valheim and Unity DLLs on demand with ILSpy or `ilspycmd`.
Prefer the [reusable code-inspection script](inspection-scripts.md#code-inspect-assemblies-and-types)
for persistent cached type lookup and targeted C#/IL extraction. Manual commands
below are a temporary fallback; prefer the helper for reusable results.
The user does not need to maintain a decompiled source tree. Online snippets are
examples, not API contracts; confirm exact signatures and behavior locally.

1. Read startup versions from `BEPINEX_PATH/LogOutput.log` and Unity's `Player.log`.
2. Inspect `assembly_valheim.dll`, `assembly_utils.dll`, `assembly_guiutils.dll`,
   and needed Unity modules in the game's Managed directory.
3. Read `BEPINEX_PATH/core/BepInEx.dll` and `0Harmony.dll` when needed.
4. Use [ILSpy](https://github.com/icsharpcode/ILSpy) or `ilspycmd` to inspect a type:

```bash
ilspycmd -t Game "$VALHEIM_PATH/valheim_Data/Managed/assembly_valheim.dll"
```

Omit `-o` for a quick read on standard output. When several files must be searched,
create an agent-owned temporary directory outside the repository and decompile
only the needed types there. For example, in Bash:

```bash
VALHEIM_INSPECT_DIR=$(mktemp -d)
ilspycmd -t Game -o "$VALHEIM_INSPECT_DIR" \
  "$VALHEIM_PATH/valheim_Data/Managed/assembly_valheim.dll"
```

On PowerShell, create a uniquely named directory under `[IO.Path]::GetTempPath()`
with `New-Item`, then pass its path with `-o`. Use `ilspycmd --help` for the installed
version's options; `-l c` lists classes and `-p -o <directory>` exports a project
only when a broader investigation needs it. Record the source assembly version
or hash with temporary extracts and discard stale results after game updates.
Do not require a persistent environment variable or source checkout. Adapt the
DLL path for the actual platform and never commit or distribute game DLLs or
decompiled source. A plausible method name is not verification.

For dedicated-server questions, start with matching-version client DLLs for shared
gameplay logic. See [shared code and build differences](architecture.md#shared-client-and-server-code)
before assuming a client-specific implementation also describes the server.
The inspection helpers also accept a server root with `valheim_server_Data`.

Local API baseline checked on 2026-10-03: Valheim 1.0.16, Unity 6000.0.75f1,
and BepInEx 5.4.23.5. These are snapshots, not claims about the latest release.

## Inspect game assets

When DLLs explain the rule but not its values, use [Assets](assets.md) to inspect
prefabs, recipes, translations, or images with AssetRipper. Keep code and asset
findings tied to the same installed game version.

## Generate a project

Use the bundled [mod template](../assets/mod-template/) for new projects only.
It targets `net48` and includes local references, config, and Harmony Validator.
Resolve the installed skill folder to an absolute path, then install its
[local template](https://learn.microsoft.com/en-us/dotnet/core/tools/templates):

```bash
dotnet new install "/path/to/valheim-modding/assets/mod-template"
dotnet new valheim-mod -n FjordGreeting -o FjordGreeting \
  --pluginId org.example.fjordgreeting --modAuthor "Your Name"
cd FjordGreeting
dotnet build -c Release -p:DeployOnBuild=false
```

Use a simple PascalCase project name without spaces or hyphens. Choose a unique
plugin ID. Optional `--modVersion` and `--copyrightYear` set release metadata.
Release defaults and version synchronization are in [Packaging](packaging.md).
The source value `0.1.0` is a template replacement marker, not the generated
default. If copying files manually, replace that marker in mod metadata only;
do not change dependency versions. Use a public author label chosen by the user.

This installs a template in the user's .NET template registry; explain that local
change when doing it. If installation is out of scope, copy and adapt the assets
instead. Never overwrite an existing mod with the starter project.
