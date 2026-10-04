# Valheim AI Skill

An AI agent skill for [Valheim](https://www.valheimgame.com/) that helps you make [BepInEx](https://docs.bepinex.dev/)
mods, get unstuck in-game, learn the game's mechanics, and keep a dedicated
server running smoothly. It combines plain-language help for players with
practical tools for modders.

## What it can help you with

### Create a mod

Plan a feature, agree on a mod name, and build it with C# and [BepInEx 5](https://docs.bepinex.dev/).
The skill favors public game APIs and events, using Harmony patches only when needed.

### Build and prepare a Thunderstore release

Build and validate the mod, prepare its manifest, README, changelog, and ZIP,
and check that the package matches what the code actually does for [Thunderstore](https://thunderstore.io/c/valheim/).
It can explain publishing with the [Thunderstore CLI](https://github.com/thunderstore-io/thunderstore-cli),
but publishing is a separate step that always needs the user's permission.

### Inspect game code and assets

Use [ILSpy](https://github.com/icsharpcode/ILSpy) and
[AssetRipper](https://github.com/AssetRipper/AssetRipper) helpers to inspect
assemblies, prefabs, item icons, translations, and other assets, and export
supported models for [Unity Editor](https://unity.com/download).

### Research trusted online sources

Look up current information in [Valheim's official support pages](https://www.valheimgame.com/support/),
[Iron Gate Studio](https://irongate.se/) resources, and official tool
documentation. Use community pages and mod examples critically. The [English
Valheim Wiki](https://valheim.fandom.com/wiki/Valheim_Wiki) is useful for gameplay content; installed
game code remains the source of truth for executable behavior.

### Set up and maintain a dedicated server

Help with Windows and Linux servers, backups, updates, and access, using the
[official dedicated server guide](https://www.valheimgame.com/support/a-guide-to-dedicated-servers/)
as a starting point, plus SteamCMD and open-source container options such as
[Podman](https://podman.io/).

### Get gameplay and crafting advice

Look up bosses, weaknesses, weapons, food, recipes, biomes, and game mechanics.
Use installed game code for executable behavior; for content not represented in
code, consult the [English Valheim Wiki](https://valheim.fandom.com/wiki/Valheim_Wiki) and label the source.

## Demo

Watch it in action: [Testing Valheim AI Skill with Codex in VS Code](https://youtu.be/2-PucHKb1Cc)

The mod generated is pushed on thunderstore: 
https://thunderstore.io/c/valheim/p/Landoria/HighJump/


## Download and install

Open the [latest pre-release](https://github.com/landoria-gaming/ValheimAISkill/releases/tag/snapshot)
and download **`valheim-ai-skill-1.0-snapshot.zip`** under **Assets**. Extract the
`valheim-ai-skill` folder into your user-wide skills directory:

`~/.agents/skills/valheim-ai-skill/` (Windows:
`%USERPROFILE%\.agents\skills\valheim-ai-skill\`).

See below for installation steps specific to each AI agent.

| Where you're using it | How to install and start |
| --- | --- |
| ChatGPT desktop — Codex mode | Install the extracted `valheim-ai-skill` folder in `~/.agents/skills/valheim-ai-skill/` (see above), then ask Codex to use `$valheim-ai-skill`. |
| Codex CLI | Install in `~/.agents/skills/valheim-ai-skill/` and select it with `$valheim-ai-skill` or `/skills`. |
| VS Code | Install and use the [Codex extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt); install the skill in `~/.agents/skills/valheim-ai-skill/` and select it with `$valheim-ai-skill` or `/skills`. |
| JetBrains Rider | Install the [JetBrains AI Assistant plugin](https://www.jetbrains.com/help/ai-assistant/codex-agent.html), select **Codex** as the agent, then import or add the skill under **Settings → Tools → AI Assistant → Skills**. See [JetBrains skill setup](https://www.jetbrains.com/help/ai-assistant/agent-skills.html). |
| Other compatible agents | See the compatibility list below; install the skill folder and use that agent's skill-selection method. |

### Compatible agents

The Agent Skills format uses a directory containing `SKILL.md` and optional
support files. These agents document support for this format. Installation paths
and activation differ, and features may vary by product or version.

| Agent | Official guidance |
| --- | --- |
| Codex | [Skills](https://developers.openai.com/codex/skills/) |
| Claude Code | [Skills](https://code.claude.com/docs/en/skills) |
| Cursor | [Agent Skills](https://cursor.com/docs/context/skills) |
| GitHub Copilot | [Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| Gemini CLI | [Using Agent Skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md) |
| Goose | [Skills](https://block.github.io/goose/docs/guides/skills/) |
| OpenCode | [Agent Skills](https://opencode.ai/docs/skills) |

Then just ask naturally. For example:

- “Help me make a mod that greets me when I spawn. Let me choose the name first.”
- “Why does this command fail? Here's what I typed and what happened.”
- “What should I bring to fight The Elder? Check its weaknesses and give me a practical plan.”
- “What do I need to craft bronze, and where do I process the materials?”
- “Show me the inventory icon for the Wood prefab.”
- “Help me maintain my dedicated server on Linux and plan safe backups.”

## What you'll need

For hands-on mod development or local code and asset inspection, Valheim must be
installed on the same machine as the agent from [Steam](https://store.steampowered.com/app/892970/Valheim/)
or [Xbox / Microsoft Store](https://www.xbox.com/en-US/games/store/valheim/9NCBL78CG9N7),
and the agent must be able to read the game directory.

## Contact

Having trouble with the skill? [Open an issue on GitHub](https://github.com/landoria-gaming/ValheimAISkill/issues).

[MIT License](LICENSE)
