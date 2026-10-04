# ValheimMod

Shows a configurable local chat greeting on your first spawn of the session.

## Features

- Choose your greeting or turn it off.
- Only you see the message; it is not sent to other players.
- The greeting runs on the first spawn of a session, not on every respawn.

## Installation

Requires Valheim and BepInEx 5. Install on your client through a compatible mod
manager, or copy the DLL into `BepInEx/plugins/ValheimMod/` in your active profile.
No server installation is needed.

## BepInEx configuration

Run once to create `BepInEx/config/example.valheimmod.cfg`. Edit the file while
Valheim is closed, then launch the game again.

| Section | Setting | Default | Description |
| --- | --- | --- | --- |
| `General` | `Enabled` | `true` | Show the greeting on the first spawn. |
| `General` | `Greeting` | `Hello World` | Local chat message to display. |

## Known limitations

- If chat is unavailable at first spawn, the greeting is skipped and a warning
  is written to the BepInEx log.

<!-- Add a Support section with the real GitHub Issues URL once published. -->
