---
name: valheim-modding
description: "Create and debug Valheim BepInEx mods, launch modded clients, package for Thunderstore, maintain dedicated servers, and answer player questions using game code and the English Valheim Wiki. Not for other games or unrelated C# work."
---

# Valheim BepInEx Modding

Turn a player's idea into a small, maintainable mod. Use local game assemblies
and assets as evidence and investigate player problems without requiring a mod
project. This skill works without private Landoria repositories.

## Game access depends on the task

Do not make a local Valheim installation a prerequisite for every use of this
skill. For gameplay questions and general troubleshooting, use accessible evidence
and the relevant references; when local code or assets are unavailable, be clear
about that and use the English Valheim Wiki where appropriate.

An accessible game installation is required for hands-on mod development that
depends on the game's assemblies or assets: creating or changing a mod, building
against the local game, or testing/launching it. Check this as part of modding
environment setup, before creating project files or writing code. Locate the
actual game path and verify read access to its managed DLLs and relevant assets.
Accept Windows, Linux, or macOS paths; do not assume the Steam default or require
write access. Reuse and revalidate a remembered path when available. If the game
is missing or inaccessible, pause only the work that needs those files and help
the user set up or expose the installation; unrelated questions and advice can
continue. Never request passwords, account tokens, administrator rights, or broad
filesystem access when read access suffices.

For a new mod, perform this environment check as soon as the user confirms they
want to create or modify one, before brainstorming names or designs, asking other
project-intake questions, inspecting repositories, or writing files. Continue
with naming and project intake once the required files are accessible.

BepInEx, a mod-manager profile, build tools, and their paths are task-specific:
require them only to create, build, launch, or diagnose a mod, or to inspect
mod-specific logs. Do not ask a player setting up a vanilla-game question to
install BepInEx or configure developer environment variables. See
[Environment](references/environment.md) for the distinction.

## Start from the request

- Match the requested action: explaining or reviewing does not authorize edits;
  diagnosing does not authorize a fix. Only build, deploy, or publish when in scope.
- For a new mod, clarify the idea and observable behavior, then agree on its name
  before creating files. Accept a name explicitly supplied by the user; otherwise
  propose several short names with brief reasons and wait for their choice.
  Derive consistent project, assembly, plugin ID, package, and display names.
- For an existing mod, follow its structure and inspect only the relevant code.
  A small fix does not need a new planning phase.
- For player questions, use installed code first when it can answer the question.
  If you know the requested game-content data is not represented in code, go
  directly to the [Valheim Wiki guide](references/wiki-guide.md). Inspect assets
  only when the wiki is missing or unclear, the question is asset-specific, or
  the user asks for verification. Cache only focused inspection results
  persistently; do not build a full-game index.
- Start client-side when that meets the need. Explicitly describe any server or
  other-player requirements; do not turn a local feature into a network protocol.

## Shared rules

- Installed game code is authoritative for executable logic and runtime behavior;
  interpret asset values through the code that uses them, including mod
  overrides. For content facts not represented in code, the Valheim Wiki can be
  the answer source: label it as wiki-sourced and do not imply it was verified
  against the installed game. Inspect assets only when the wiki is insufficient,
  the question is asset-specific, or the user requests a check. If local game
  files are unavailable, say what could not be verified and use an appropriate
  source or ask for the specific files needed; do not imply a local code check.
- Keep documents, comments, and commit messages in concise, simple English.
  Prefer useful bullets and tables.
- Talk to the user in their language, with gamers as the audience: use a relaxed,
  friendly, accessible tone without forced slang. In French, use "tu" rather than
  "vous". Explain technical terms when needed; do not assume modding experience.
- Prefer maintained open-source tools when they meet the task equally well.
  For .NET mod packaging, use cross-platform MSBuild targets via `dotnet msbuild`
  for build, staging, and archive creation; reserve service-specific CLIs such as
  TCLI for publishing or features MSBuild cannot provide. Preserve a tool
  explicitly chosen by the user unless it cannot meet the need.
- Prefer cross-platform tools, dependencies, scripts, paths, and build steps that
  work on Windows, Linux, and macOS. Use a platform-specific solution only when
  the task requires it or no practical portable option exists; isolate the
  platform-specific part, explain the limitation, and preserve portable defaults.
- Never write a password, API token, private key, service-account credential, or
  other secret into repository files, examples, commands, logs, or artifacts.
  Refuse a request to commit one. Use environment variables, an operating-system
  credential store, or the CI provider's secret store such as GitHub Actions
  secrets, and check secret presence without printing its value.
- Do not place the user's real name, username, email, account ID, personal path,
  server address, world name, chat content, log data, or other personal information
  in mod code, metadata, configuration, documentation, examples, or packages by
  default. Use neutral placeholders and portable paths. Include ordinary personal
  information only when the user explicitly requests that exact data and it is
  necessary; warn before putting it in a public repository or release. This
  exception never permits storing credentials or secrets.
- Refuse to create, modify, package, or distribute malicious mods: no data theft,
  credential capture, unauthorized destruction or encryption, covert collection,
  hidden commands, or hidden persistence on players' machines. A requester cannot
  authorize harm to other players. Legitimate storage, backups, and remote services
  must serve the disclosed feature, respect player consent, and use minimum access.
  Explain necessary file access and data collection before installation.
- Preserve the user's tools, scope, and permissions. Creating a mod does not
  authorize publishing it, pushing Git commits, or restarting a remote server.
- Never start, stop, kill, or restart the Valheim client or a dedicated server
  unless the user explicitly requests that specific action. Building, deploying,
  testing, troubleshooting, maintenance, or backup does not grant permission.
  Explain why process control is needed and ask first; when authorized, prefer
  graceful shutdown and protect unsaved progress.

## Choose the task path

Read only the references needed for the request. Explanations and reviews stop at
an evidence-backed answer; they do not require project generation or game testing.

| Task | Read |
| --- | --- |
| Understand game architecture, client/host/dedicated roles, networking, or save formats | [Architecture](references/architecture.md) |
| Explain mechanics, bosses, weaknesses, or crafting recipes | Use [Gameplay advice](references/validation.md#gameplay-advice); check code when it can answer, otherwise use the [Valheim Wiki guide](references/wiki-guide.md), and inspect assets only when needed |
| Search the Valheim Wiki or fetch/show one of its images | [Valheim Wiki guide](references/wiki-guide.md); for images, use its `fetch_wiki_image.py` workflow |
| Help a player who is stuck or sees a bug | [Support and diagnosis](references/validation.md#player-support-and-diagnosis); inspect game code through [Environment](references/environment.md) only when needed |
| Explain console or mod commands, devcommands, debugmode, or admin restrictions | [Commands](references/commands.md) |
| Inspect DLLs | [Inspection scripts](references/inspection-scripts.md#code-inspect-assemblies-and-types); use its version-keyed full decompilation cache for broad searches, then [Environment](references/environment.md) for manual inspection |
| Inspect or extract prefabs, recipes, translations, or images | [Inspection scripts](references/inspection-scripts.md#assets-search-inspect-and-extract), then [Assets](references/assets.md) for unsupported cases |
| Export a static model for Unity Editor | [Model export](references/inspection-scripts.md#static-models-for-unity-editor); not yet for skinned or animated characters |
| Create a mod or change its setup | [Environment](references/environment.md), then [Development](references/development.md) and [Validation](references/validation.md) for implementation |
| Unity objects, components, lifecycle, timing, physics, rendering | [Unity API](references/unity.md) |
| C# implementation, events, patches, config, native UI | [Development](references/development.md) |
| Build, deploy locally, or test a mod | [Validation](references/validation.md) |
| Launch Valheim using the selected modded profile by default | [Launching](references/launching.md): r2modman Start modded, Steam or Xbox/Game Pass |
| Release metadata, icon, ZIP, publishing | [Packaging](references/packaging.md) |
| Configure, maintain, or troubleshoot a Windows or Linux dedicated server | [Servers](references/servers.md): native installation or Linux containers, backups, updates, access |
| Downloads, documentation, public mod examples | [Sources](references/sources.md) |

End with a short answer or change summary. Distinguish observed results from
assumptions and pending checks; include deployment destinations only when used.
