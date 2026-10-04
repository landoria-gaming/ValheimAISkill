# Valheim Modding Skill

An AI agent skill for Valheim: make BepInEx mods, get unstuck in-game, learn the
game's mechanics, and keep a dedicated server running smoothly. It combines
plain-language help for players with practical tools for modders.

## What it knows

| If you want to… | It can help with… |
| --- | --- |
| Make a mod | Plan a feature, choose a mod name, write C# for BepInEx 5, configure settings, and use Harmony when needed. |
| Build and ship a mod | Build and validate it, prepare a Thunderstore package, and help write a clear player-facing README. Publishing is always a separate, permission-based step. |
| Figure out a game problem | Troubleshoot crashes, bugs, commands, and blocked progression using available logs and evidence. It can ask for a screenshot or short video when useful. |
| Get gameplay advice | Look up bosses, enemy weaknesses, weapons, food, crafting recipes, biomes, and game mechanics in the English Valheim Wiki; check local game code when the answer depends on runtime behavior. |
| Explore game files | Use ILSpy and AssetRipper helpers to inspect code, prefabs, item icons, translations, and other assets. |
| Run a dedicated server | Set up and maintain a Windows or Linux server, plan backups and updates, and compare native SteamCMD with container options such as Podman. |

## How to use it

The complete skill lives in this repository's `src/` folder: `SKILL.md`,
references, scripts, and templates stay together there. Copy that folder or extract the
[latest snapshot ZIP](https://github.com/landoria-gaming/ValheimModdingSkill/releases/download/snapshot/valheim-modding.zip)
into your agent's skills folder.

To build the ZIP and install or update the skill for your current user, run this
from the repository root with the .NET SDK installed:

```sh
dotnet msbuild scripts/SkillPackage.proj -t:deploy-local
```

This replaces only `~/.agents/skills/valheim-modding` after preparing the new
copy. On Windows, that path is under your user profile.

| Where you're using it | How to start |
| --- | --- |
| Codex app or CLI | Install `src/` as `valheim-modding` or ask with `$valheim-modding`. For a project-local install, place it in `.agents/skills/valheim-modding/`. |
| VS Code | Use the Codex extension, then select the skill with `$` or `/skills`. |
| JetBrains Rider | Use an AI Assistant that supports Agent Skills; add the `src/` folder in **Settings → Tools → AI Assistant → Skills** if needed. |
| ChatGPT | In a ChatGPT environment that supports skills, select it with `@valheim-modding`. |
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

You can ask gameplay and general support questions without installing Valheim on
the agent's machine. The agent will be clear when it cannot verify an answer
against local game files and can use the English Wiki where appropriate.

For hands-on mod development, the agent needs read access to an installed Valheim
game so it can check the actual assemblies and assets. A BepInEx profile and the
.NET SDK are needed for the parts of the workflow that run or build the mod. See
the [environment guide](references/environment.md).

## Get the skill

The [snapshot release](https://github.com/landoria-gaming/ValheimModdingSkill/releases/tag/snapshot)
is rebuilt after successful pushes to `main`. It's a development snapshot, not
a stable release. See [installation guidance for Codex and ChatGPT](https://learn.chatgpt.com/docs/build-skills)
and [JetBrains AI Assistant](https://www.jetbrains.com/help/ai-assistant/agent-skills.html)
for platform-specific details.

[MIT License](LICENSE)
