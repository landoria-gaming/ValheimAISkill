# Valheim BepInEx Modding Skill

## What it does

A skill that helps an AI agent create Valheim mods and help players with the game.
It provides practical knowledge about:

- C# mods with BepInEx 5, configuration, public events, and Harmony patches.
- Reusable ILSpy and AssetRipper scripts for code, prefabs, inventory icons, and translations.
- Building mods, reading logs, and checking behavior in game.
- Explaining bugs, blocked progression, and failing commands using logs and game code.
- Explaining boss weaknesses, strategies, and crafting recipes from verified game data.
- Player-friendly README files, versioning, and Thunderstore packages.
- Dedicated Linux servers with Podman or native SteamCMD.

Designed for Codex, with portable instructions for other agents that support
`SKILL.md`. Support depends on the agent, not just the editor. The skill does not
publish or deploy mods without permission.

## How to use it

**Required:** Valheim must be installed and its game directory readable by the
agent. Otherwise, the skill only helps you install Valheim and grant directory
access; all other tasks remain blocked.

1. Copy the whole `skills/valheim-modding` folder, or extract it from
   [the snapshot ZIP](https://github.com/landoria-gaming/ValheimModdingSkill/releases/download/snapshot/valheim-modding.zip), into your mod project's
   `.agents/skills/valheim-modding/`. Keep all subfolders together.
2. Open that project in your coding agent and select the skill:

   | Environment | Start here |
   | --- | --- |
   | Codex app or CLI | Select `valheim-modding` or mention `$valheim-modding`. |
   | VS Code | Use the Codex extension; select the skill with `$` or `/skills`. |
   | JetBrains Rider | Use Codex in AI Assistant. If needed, add this repository's `skills` folder in **Settings → Tools → AI Assistant → Skills**, then install the skill. |
   | ChatGPT desktop | Find the skill in **Skills** and select it with `@`. On web/mobile, native skill distribution uses plugins; this repository provides a standalone skill, not a plugin. |

3. Describe the mod you want, for example:

   ```text
   Use $valheim-modding to create a mod that greets me in chat on my first spawn.
   Make the greeting configurable. Build it without deploying yet.
   ```

For support, try: "I am stuck in Valheim. Help me understand what is happening
using the logs and game code, without changing my setup."
For gameplay advice: "How can I beat this boss? Check its weaknesses in the game
code and data, and suggest a strategy."
Or ask: "What materials and crafting station do I need to make bronze?"
For an image: "Show me the inventory icon of the Wood prefab."

For ChatGPT, select the skill with `@` instead of using the `$` prefix.
To build locally, the agent needs Valheim, a BepInEx profile, and the .NET SDK;
see [setup instructions](skills/valheim-modding/references/environment.md).

Installation details: [ChatGPT and Codex](https://learn.chatgpt.com/docs/build-skills),
[JetBrains AI Assistant](https://www.jetbrains.com/help/ai-assistant/agent-skills.html).
Other compatible agents use their own skill installation and invocation methods.

The [snapshot release](https://github.com/landoria-gaming/ValheimModdingSkill/releases/tag/snapshot)
is rebuilt after successful pushes to `main`. It is a development build, not a stable release.

[Example prefab inventory](docs/valheim-prefabs.md) · [Maintainer guide](CONTRIBUTING.md) · [MIT license](LICENSE)
