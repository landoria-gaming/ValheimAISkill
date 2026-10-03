# Dedicated Servers

Help install, configure, maintain, update, back up, and troubleshoot dedicated
servers on Windows or Linux. Preserve an existing deployment unless the user
asks to migrate it. Read [Architecture](architecture.md) for shared client/server
code, runtime-role detection, networking, and save formats.

- For a Linux container deployment, start from
  [Landoria's server image](https://github.com/landoria-gaming/valheim-server-image).
  Read its current documentation before choosing image tags, ports, volumes, or commands.
- Prefer Podman to pull and run the OCI image on Linux. It is open source and
  accepts the same container image format. Use Docker when the user selects it
  or the host environment makes it the better-supported option.
- Confirm game version, BepInEx version, deployed plugins, service/container name,
  and where logs and persistent world data live.
- Decide which features run on the client, server, or both. Test each role and
  document required matching versions.

## Native Windows installation

- Install **Valheim Dedicated Server** from Steam Library's **Tools** category,
  or use Windows SteamCMD with dedicated-server app ID `896660` after checking
  the current guide. Do not install Linux binaries on a native Windows host.
- Copy `start_headless_server.bat` before customizing it. Keep launch settings,
  world data, plugins, and logs separate from Steam-managed files where possible.
  Apply the skill's secret-handling rules to credentials; do not commit them.
- Check the console/startup log and add only the necessary firewall rules for
  the selected backend. Do not disable the firewall to fix a connection failure.
- For unattended startup, agree on Task Scheduler or an appropriate service
  wrapper and a non-administrator account. Enabling automatic startup or invoking
  the service still requires the user's explicit request to start the server. The
  game console executable is not itself a Windows service; the chosen runner must
  support graceful shutdown.

## Native Linux installation

When a container image is not wanted, use SteamCMD to download and update the
Valheim Dedicated Server directly on Linux. SteamCMD is the command-line Steam
client; the dedicated-server application ID is `896660` in the checked setup.
Verify the current ID and Linux requirements before relying on them.

```bash
steamcmd \
  +force_install_dir /opt/valheim \
  +login anonymous \
  +app_update 896660 validate \
  +quit
```

- Run the server under a dedicated unprivileged account, not as root.
- Keep world data, configuration, BepInEx plugins, and logs outside files that
  SteamCMD replaces during an update.
- Install the Linux runtime libraries listed by the current official Valheim
  dedicated-server guide.
- A `systemd` service can provide startup and graceful shutdown. Configure an
  automatic restart policy only when requested, and never invoke `start`, `stop`,
  or `restart` for the Valheim service without an explicit user request.

Use the shared [maintenance checklist](#routine-maintenance) for updates on either OS.

## Official server guide

Read Iron Gate's [dedicated-server guide](https://www.valheimgame.com/support/a-guide-to-dedicated-servers/)
for startup flags and administration. Dated April 2024, it should be checked against
the installed server before applying commands.

- Keep customized launch scripts separate from Steam-managed originals so updates
  do not replace local settings.
- Steam networking uses the chosen port and the next port: 2456–2457 by default.
  Check firewall and router rules for the selected backend.
- Crossplay uses PlayFab relays without router forwarding. Use a join code, server
  list, or public address; local and loopback addresses are not supported there.
- Check world selection, visibility, save/log locations, and backups. A hidden
  listing is not access control. Presets overwrite modifiers; apply overrides last.
- Permissions use `adminlist.txt`, `bannedlist.txt`, and `permittedlist.txt` in the
  save directory, with case-sensitive platform IDs. A nonempty permitted list
  excludes everyone not listed.
- When the user explicitly requests a server start or stop, use the appropriate
  graceful method and verify the result. Confirm readiness from startup logs and
  an actual connection check only after an authorized start.

Check its Linux library requirements for the distribution. Its Docker example does
not replace this skill's Podman preference.

## SSH

Connect to the Linux host through SSH using a private key already configured
in the user's profile or an agent-specific key the user chooses to provision.

- Prefer an existing SSH host alias and key agent. Do not ask for private key text.
- Confirm the host and host key; never bypass host verification for convenience.
- Use least-privilege access. Diagnose with logs and service status first.
- Start, stop, or restart the identified game service/container only when the user
  explicitly requests that action. Diagnosis or maintenance alone is not permission.
  Warn about interrupting active players.

## Routine maintenance

- Check process/service status, startup errors, game/BepInEx/plugin versions,
  free disk space, and backup health before changing the installation.
- For a user-requested update that needs downtime, agree on timing and warn
  connected players. Ask separately before stopping or starting the server if
  those actions were not explicitly requested. Verify a complete backup before
  changes, then check logs and a real player connection after an authorized start.
- Follow the [save-format and backup guidance](architecture.md#saves-and-storage).
  Do not assume copying only `.db` and `.fwl` covers newer chunked saves.
- Keep a recovery copy and test restoration in an isolated location. Do not
  replace a world, remove plugins, or restart an occupied server without agreement.
- Explain [multiplayer authority limits](architecture.md#authority-and-mod-compatibility)
  when proposing server-side enforcement or matching-mod checks.
