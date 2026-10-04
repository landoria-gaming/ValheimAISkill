# Launch Valheim with the Selected Profile

When the user asks to launch Valheim, default to the equivalent of r2modman's
**Start modded**, not a bare executable or a vanilla Steam launch. Honor an
explicit request for vanilla instead. This is the game client; dedicated-server
startup belongs in [Servers](servers.md).

Starting is never implicit: a build, deployment, test, or troubleshooting request
does not authorize launching the client. Stop, kill, and restart actions also
require an explicit request, as described by the shared process-control rule in
`SKILL.md`.

The store launch route is independent of the session's
[Steam or PlayFab/crossplay backend](architecture.md#steam-and-playfab).

## Resolve the launch context

- Use the known store, OS, installation, and selected mod-manager profile. Ask only
  if the store or profile is ambiguous; do not silently choose the `dev` example.
- The installed-game prerequisite must pass. Also verify the selected profile's
  BepInEx preloader and matching bootstrap files. Do not install or switch loaders
  or enable/disable mods merely because the user requested a launch.
- If Valheim is already running, report it instead of launching a second instance
  or killing it. Starting the client does not authorize loading a world or running
  gameplay commands.
- Prefer the manager's **Start modded** when it can be operated. Otherwise reproduce
  the verified store-specific flow below, with actual paths and argument arrays.
  Do not evaluate a settings string as shell code. Preserve understood extra game
  launch arguments from the selected configuration without exposing secrets.

## What Start modded prepares

The implementation below is specific to r2modman. For Gale or Macheim, prefer
that manager's modded launch and inspect its matching release before reproducing
it manually. Do not assume identical profile paths or bootstrap behavior.

The checked manager validates the game directory, calls `linkProfileFiles`, then
dispatches `startModded` to the platform runner. `ModLinker` synchronizes profile
root loader/support files into the game directory while excluding directories
such as `BepInEx` and `plugins`; the profile preloader is passed by argument.

Therefore, arguments alone do not reproduce a first-time setup. Before a direct
launch, check the bootstrap is already compatible (for example `winhttp.dll` and
Doorstop configuration on Windows). Let the manager handle its normal setup, or
explain any needed repair. Do not blindly copy every profile file, overwrite an
unmanaged installation, request elevation, or delete existing loader files.
Stop and ask if resolving a conflict needs changes outside the requested launch.

## Select the Doorstop arguments

The manager reads `.doorstop_version` from the **profile root**, which is the
parent of `BEPINEX_PATH`. Its checked implementation defaults to v3 when no usable
version marker is present. Verify the installed loader before choosing arguments;
do not assume BepInEx 5 implies a particular Doorstop major version.

| Doorstop | Arguments |
| --- | --- |
| v4 | `--doorstop-enabled true --doorstop-target-assembly <preloader>` |
| v3 | `--doorstop-enable true --doorstop-target <preloader>` |

For this skill's BepInEx 5 profile, confirm that the preloader is
`BEPINEX_PATH/core/BepInEx.Preloader.dll`. Other loader layouts need matching
inspection, not a guessed DLL. Recheck upstream for unsupported/new versions.

## Windows Steam and Xbox launches

Define the [environment variables](environment.md#install-and-isolate-a-modding-profile) in the
current shell. `VALHEIM_PATH` is the resolved game directory, `BEPINEX_PATH` is
the selected profile's `BepInEx` directory, and `STEAM_PATH` is the Steam client
directory (not necessarily the parent of the game library).

PowerShell examples below assume the verified **Doorstop v4 / BepInEx 5** layout.
For v3, substitute the two flag names from the table above. These are execution
examples, not commands to run while merely documenting or inspecting the setup.

```powershell
$valheimModdedArgs = @(
    '--doorstop-enabled', 'true',
    '--doorstop-target-assembly', "$env:BEPINEX_PATH\core\BepInEx.Preloader.dll"
)
```

### Steam

The Windows Steam runner starts **Steam**, which launches Valheim's client app
`892970` with the modded arguments and configured extra game arguments:

```powershell
& "$env:STEAM_PATH\Steam.exe" -applaunch 892970 @valheimModdedArgs
```

Do not substitute dedicated-server app `896660`. A bare `steam://run/892970` URL
does not by itself reproduce this argument-bearing Windows launch. Preserve any
existing Steam launch options and check for conflicting loader arguments.

### Xbox / PC Game Pass

The Windows Xbox runner starts **`gamelaunchhelper.exe`**, with the resolved game
directory as its working directory, and forwards the same modded arguments:

```powershell
Push-Location -LiteralPath $env:VALHEIM_PATH
try {
    & '.\gamelaunchhelper.exe' @valheimModdedArgs
} finally {
    Pop-Location
}
```

Resolve the manager's configured directory first. Its fallback queries
`Get-AppxPackage -Name CoffeeStainStudios.Valheim` for `InstallLocation`, then
resolves the real path. Check that the resulting directory contains the helper;
some layouts place game content under `Content`. Do not assume a fixed drive,
take ownership of WindowsApps, or bypass Xbox licensing. If the helper is missing,
fix the selected path/setup rather than replacing it with the Steam executable.

## Direct executable alternative

The previously supplied command is valid as a **direct-launch alternative** for
the compatible Windows setup, not the default Steam/Xbox manager flow. Use it
only when that route was explicitly selected or verified for the installation.
Run from the game directory, with the bootstrap already prepared.

```bat
"%VALHEIM_PATH%\valheim.exe" --doorstop-enabled true --doorstop-target-assembly "%BEPINEX_PATH%\core\BepInEx.Preloader.dll"
```

In PowerShell, with the v4 argument array defined above:

```powershell
& "$env:VALHEIM_PATH\valheim.exe" @valheimModdedArgs
```

## Other platforms and result checks

Linux/macOS use their platform-specific manager runner, not the Windows commands.
Linux native, Proton, and Flatpak paths differ: wrappers, profile selection,
preloader path translation, and DLL overrides may be required. Prefer the manager
and inspect its matching release before reproducing that launch manually.
Do not persist Steam options or change Proton configuration without agreement.

After a requested launch, confirm a new game process/window and fresh entries in
the selected profile's [BepInEx log](validation.md#read-the-logs), including the
expected plugins. Steam/helper exit success alone does not prove the game or
mod loader started. Report launch failures without repeated blind retries.

## Source evidence

Inspected r2modman **v3.2.20**, commit
`6d7c81ddca175b39f41a328879737d6be7fa1855`, on 2026-10-03. This is a source review,
not a live Steam/Xbox launch test. Match the installed release and current game
metadata when behavior differs.

| Source | What it establishes |
| --- | --- |
| [NavigationMenu](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/components/navigation/NavigationMenu.vue) / [ModLinker](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/r2mm/manager/ModLinker.ts) | Preparation before dispatch and profile-root synchronization |
| [PlatformInterceptorImpl](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/providers/generic/game/platform_interceptor/PlatformInterceptorImpl.ts) / [game metadata](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/assets/data/ecosystem.json) | Store/OS runner selection, Valheim client IDs and loader |
| [BepInExGameInstructions](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/r2mm/launching/instructions/instructions/loader/BepInExGameInstructions.ts) / [UnityDoorstopUtils](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/utils/UnityDoorstopUtils.ts) / [GameInstructionParser](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/r2mm/launching/instructions/GameInstructionParser.ts) | Version-specific flags and profile preloader resolution |
| [SteamGameRunner_Windows](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/r2mm/launching/runners/windows/SteamGameRunner_Windows.ts) | Steam executable, app ID, forwarded arguments |
| [XboxGamePassGameRunner](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/r2mm/launching/runners/windows/XboxGamePassGameRunner.ts) / [Xbox directory resolver](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/providers/generic/game/directory_resolver/win/XboxGamePassDirectoryResolver.ts) | Xbox helper executable, working directory and install lookup |
| [DirectGameRunner](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/r2mm/launching/runners/multiplatform/DirectGameRunner.ts) / [SteamGameRunner_Linux](https://github.com/ebkr/r2modmanPlus/blob/6d7c81ddca175b39f41a328879737d6be7fa1855/src/r2mm/launching/runners/linux/SteamGameRunner_Linux.ts) | Separate direct-executable and Linux launch paths |
