# Development

## Project conventions

- Use SDK-style C#, `net48`, and MSBuild through `dotnet`.
- Reference installed game, Unity, BepInEx, and Harmony DLLs with `HintPath`
  and `Private=false`; add only the required assemblies.
- Keep plugin GUID, name, and version constants directly in `Plugin`.
  Do not add a metadata-only class.
- `Plugin` owns startup, shutdown, event subscriptions, and Harmony lifetime.
  Feature classes own behavior; `ModConfigFile` owns config bindings.
- Keep functions at most 40 lines and files under 400 lines. Split by purpose.
- One class per C# file. Add a short English line comment to each class,
  script, and function, including constructors.
- Always use braces for control-flow blocks. Avoid duplicated logic.

These are this starter's conventions. Preserve an existing project's explicit rules.

## First spawn and chat

`Game.m_playerInitialSpawn` is a public static `Action` event in the checked
game version. It fires for the local player's initial spawn in the session, not
every respawn. Verify its declaration and call site in the installed DLL.

- Subscribe in `Plugin.Awake`; unsubscribe in `Plugin.OnDestroy`.
- Keep UI work in the event handler, not startup before the game scene exists.
- `Chat.instance?.AddString("Hello World")` adds a local chat line.
  It is not a broadcast to all players.
- Add the message alongside the normal arrival behavior; do not replace the
  game's shout or patch broad update loops just to detect this event.

The starter demonstrates this with a separate `PlayerSpawnHandler`.

## Harmony

Prefer a public event when it describes the required lifecycle. Otherwise:

- Inspect the exact target type, method, parameters, and ownership in local DLLs.
- When several patch targets can express the same behavior, prefer a public
  method. Patch a private method only as a last resort when no suitable public
  event or public method exists. Document why the private target is necessary;
  treat it as version-sensitive and verify it again after every game update.
- Add a `0Harmony` reference from `$(BepInExPath)/core/0Harmony.dll` with
  `Private=false` when introducing patches. The event-only starter does not need it.
- Specify overload parameter types; use one patch class per file.
- Create `new Harmony(PluginGuid)` and call `PatchAll()` from `Awake`.
  Call `UnpatchSelf()` during teardown; never remove other mods' patches.
- Keep patches scoped to the intended player. A client-only feature must not
  accidentally change every remote `Player` object.
- Use the [Harmony Validator](https://github.com/landoria-gaming/HarmonyValidator)
  NuGet build dependency already included in the template:

```xml
<PackageReference Include="HarmonyValidator" Version="1.0.0" PrivateAssets="all" />
```

NuGet imports its build targets. Do not add a second manual import or ship the
validator in the mod. Review checked, error, and unverified counts.
A project with no Harmony patches correctly reports zero checked targets.
Static validation does not verify gameplay, reflection helpers, or network behavior.

The Unlimited Stamina example needs both consumption and availability handling:
skipping local `Player.RPC_UseStamina(long, float)` avoids spending stamina,
while a postfix on local `Player.HaveStamina(float)` allows actions when the
bar starts empty. Verify these signatures for the installed game. Returning
false from a prefix skips the original method; apply that only to the local player.
This example is not a reason to add stamina patches to unrelated mods.

## Configuration and native UI

Bind settings in `ModConfigFile` with clear descriptions and sensible defaults.
Read `ConfigEntry<T>.Value` where behavior runs. Do not build an extra config
framework for a few settings.

For native confirmation UI, inspect `UnifiedPopup`, `YesNoPopup`,
`FixedPopupBase`, and `MessageHud` in the matching assemblies.

- Wait until `UnifiedPopup.IsAvailable()`.
- Push a `YesNoPopup` with callbacks; pop this prompt when its choice is handled.
- Use `MessageHud.instance?.ShowMessage(MessageHud.MessageType.Center, "Yes")`
  for a local on-screen response; it is separate from the popup itself.
- Prefer the built-in localized button labels when sufficient.
- Custom labels may require version-sensitive private UI details.
  Temporarily swapping shared label fields around `Push` is not a complete
  solution: stack redraws can restore the wrong labels. Handle redraws and
  cleanup for this popup only, and test stacked prompts.
- Never overwrite global localization or unrelated popups to rename two buttons.

## Scope and compatibility

For client, dedicated-server, hosted multiplayer, and single-player detection,
read [Runtime roles](architecture.md#runtime-roles). The same reference explains
RPCs and object ownership; server administration belongs in [Servers](servers.md).

Avoid extra frameworks, broad patches, reflection, and defensive scaffolding
without a concrete need. Use logs and narrowly scoped changes to solve real issues.
