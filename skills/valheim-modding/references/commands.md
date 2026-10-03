# Console, Developer Commands, and Debug Mode

Use this reference for command help, with or without cheats. Findings were
checked through ILSpy on 2026-10-03 against the Windows client **1.0.16** identified
in [Architecture](architecture.md#evidence-and-scope). No command was executed in
the game. Recheck the installed command registration and handler after updates
or when mods change them; this is not an exhaustive, version-independent catalog.

## Separate access, permissions, and debug features

| Layer | Checked behavior | What it does not grant |
| --- | --- | --- |
| Console access | `-console` enables the console for that launch; the client also reads the `EnableConsole` preference; the default keyboard binding is F5 | Cheats, server administration, or debug mode |
| Ordinary commands | Commands without `IsCheat` can run without `devcommands`, subject to their own context and handler checks | A promise that the command is harmless or usable in chat |
| `devcommands` | Toggles `Terminal.m_cheat`; `IsCheatsEnabled()` additionally requires an active `ZNet` with `IsServer()` true | Admin rights on a remote host, or automatic enabling of every feature |
| `confirmcheats` | A separate confirmation exists before the first cheat action when the achievement checker reports no existing cheated state | A harmless setup step: running it marks the current character's profile as having used cheats |
| `debugmode` | A cheat command toggling `Player.m_debugMode`; it enables the keyboard shortcuts below when input and cheat checks also pass | Required setup for every developer command, invulnerability, or a universal creative mode |
| Server administrator | Server-side permission checks authorize admin requests from the remote player's platform ID | A local player on a headless server or unrestricted client-side cheat execution |

Console, in-game chat, the dedicated process console, and PowerShell/Bash are not
interchangeable. `Chat.isAllowedCommand` rejects cheat commands in the checked
client. Do not paste OS launch flags as game commands or assume all F5 commands
work through chat. For an authorized launch with `-console`, preserve the selected
profile and other arguments using [Launching](launching.md); do not restart a
running game merely to inspect console settings. Check actual bindings rather
than assuming F5 has not been reassigned. PC observations do not establish Xbox
console UI or controller behavior.

## Commands with and without debug mode

These are lookup starting points, not commands to run automatically. For cheat
rows, the cheat gate, any confirmation, role, and handler prerequisites still
apply even though **`debugmode` is not required**.

| Command or group | Requires `devcommands` in the checked code? | Requires `debugmode`? | Important use or restriction |
| --- | --- | --- | --- |
| `help`, `info`, `ping` | No | No | List available commands, inspect system information, or test the game connection; output depends on context |
| `pos` | No | No | Shows local player coordinates; hidden from the ordinary help list until developer commands are toggled on |
| `kick`, `ban`, `unban`, `banned` | No | No | Network/admin operations; the server validates remote requests, independently of cheats |
| `save` | No | No | Saves local character state and requests a world save; a remote world-save request has its own admin check |
| `god`, `fly`, `nocost` | Yes | No | Separate invulnerability, flight, and placement-cost controls; inspect each handler and local-player requirement |
| `spawn`, `raiseskill`, `goto` | Yes | No | Change items/entities, skills, or position; verify arguments, exact IDs, and target context |
| `debugmode` | Yes | It toggles this mode | Host-side cheat command, not a replacement for the above gates |
| `removedrops`, `killall`, `forcedelete` | Yes | No | Potentially destructive; scope and filters differ, so inspect the actual handler before recommending one |

`help` and autocomplete are filtered by context, secret flags, and visibility
settings. An absent help entry is not proof that the command is unregistered.
Conversely, an entry being listed does not prove the current user can execute its
server-side action. Do not infer permission from a field such as `OnlyAdmin`
alone: inspect the constructor overload, `IsValid`, routing, and handler checks.

### Debug shortcuts in this build

`Player.Update` requires player input, `Player.m_debugMode`, and
`Console.instance.IsCheatsEnabled()` before processing these keys:

| Key | Actual action |
| --- | --- |
| Z | Toggles debug flight through `ToggleDebugFly` |
| B | Toggles no-placement-cost mode through `ToggleNoPlacementCost` |
| K | Invokes `killenemies`; do not describe it as the different `killall` command |
| L | Invokes `removedrops`; warn that this removes dropped items |

Typing `fly` or `nocost` can control those features without enabling the shortcut
mode. `debugmode` and `devcommands` are toggles: repeating one can turn it off.
Turning either off does not automatically undo flight, no-cost, god mode, spawned
objects, skill changes, or saved progress. Check each feature's state and verified
off/reset behavior rather than promising a global reset. Do not disable flight
while the player is high above the ground without warning about the fall.

## Solo, player host, remote client, and dedicated server

- In solo play and a player-hosted world, `ZNet.IsServer()` is true. Thus the
  inspected cheat gate is **not simply a single-player-only test**. Individual
  commands still impose their own conditions.
- On a remote client, local `IsCheatsEnabled()` stays false because it is not the
  host. Printing `Dev commands: True` alone does not prove cheat commands are
  usable. Being in `adminlist.txt` does not change this local test.
- This build can forward commands marked `RemoteCommand` through
  `ZNet.RemoteCommand`; typing `devcommands` as a client also sends that request.
  `RPC_RemoteCommand` checks the sender against the server admin list before
  dispatch. This can affect the server's cheat toggle, not just the requesting
  player's state. Do not recommend repeated toggles as a harmless diagnostic.
- A headless server has no `Player.m_localPlayer`. A command requiring a player,
  camera, HUD, or nearby scene objects may be unsuitable even when a permission
  check passes. Inspect the actual dedicated DLL and handler before claiming
  remote execution works; only the client DLL was available for this review.
- Mods can add commands, change permission checks, and implement remote execution.
  Identify them before attributing behavior to vanilla. Do not install a cheat or
  admin mod just because a vanilla command is unavailable. Steam versus PlayFab
  does not by itself grant console or administrator privileges.

## Diagnose and explain safely

1. Ask only for missing context: exact command and response, where it was entered,
   installed version/mods, local runtime role, and intended outcome.
2. Follow registration -> `IsValid`/`IsCheatsEnabled` -> local or remote dispatch
   -> handler. Unknown command, invalid context, denied admin rights, missing
   player, bad arguments, and cheat confirmation are different failures.
3. Check syntax in the parser, not only the help description. The checked
   `ConsoleEventArgs` splits on spaces; it is not a shell-style quoted-argument
   parser. Prefab IDs and translated names are different. Use game assets to
   resolve an identifier or value only when relevant code and the wiki do not
   answer it, or the user asks for asset-level verification.
4. Explain the failed condition and give the smallest verified example. For a
   normal command, do not tell the player to enable cheats or debug mode first.
5. Before an agreed state-changing action, explain its scope and persistence.
   Use disposable test worlds/characters or a consistent backup for risky changes;
   ask permission before changing saves, permissions, developer settings, or
   shared-world state. A question about a command is not permission to run it.

In this build, cheat actions record `PlayerProfile.m_usedCheats`, and achievement
eligibility also considers world settings, inventory, and modded state. Explain
the game's confirmation and possible achievement/progression impact; do not
silently run `confirmcheats` or bypass achievement checks as a troubleshooting
step. Turning the developer toggle off does not erase the profile's cheat marker.

Evidence: `Terminal.InitTerminal`, `ConsoleCommand` constructors, `ShowCommand`,
`IsValid`, `RunAction`, `IsCheatsEnabled`, `TryRunCommand`; `Console.Awake`/`Update`;
`FejdStartup.ParseArguments`; `ZInput.ResetKBMButtons` console binding;
`Chat.isAllowedCommand`; `Player.Update`, `ToggleDebugFly`, `ToggleNoPlacementCost`;
`ZNet.RPC_RemoteCommand`, `RPC_Kick`, `RPC_Ban`, `RPC_Unban`, `RPC_Save`; and
`Achievements.IsCheatedAtAll`/`CanGetAchievements`. Use the
[ILSpy helpers](inspection-scripts.md#code-inspect-assemblies-and-types) to recheck
only the relevant types. Keep extracted game source out of the skill and repository.
