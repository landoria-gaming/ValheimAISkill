# Dedicated Servers

Use this reference only for server or multiplayer work.

- Start from [Landoria's server image](https://github.com/landoria-gaming/valheim-server-image).
  Read its current documentation before choosing image tags, ports, volumes, or commands.
- Prefer Podman to pull and run the OCI image on Linux. It is open source and
  accepts the same container image format. Use Docker when the user selects it
  or the host environment makes it the better-supported option.
- Confirm game version, BepInEx version, deployed plugins, service/container name,
  and where logs and persistent world data live.
- Back up world data before risky migrations or gameplay changes.
- A dedicated server has no local player UI; do not call client chat or popup APIs there.
- Decide which features run on the client, server, or both. Test each role and
  document required matching versions.

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
- Use a `systemd` service for startup, graceful shutdown, and restart policy.
- Stop the server cleanly and back up persistent world data before an update.
- After updating, confirm the game and BepInEx versions, then inspect startup logs.

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
- Shut down gracefully with Ctrl+C or the service's equivalent signal, then verify
  exit. Confirm readiness from startup logs and an actual connection check.

Check its Linux library requirements for the distribution. Its Docker example does
not replace this skill's Podman preference.

## SSH

Connect to the Linux host through SSH using a private key already configured
in the user's profile or an agent-specific key the user chooses to provision.

- Prefer an existing SSH host alias and key agent. Do not ask for private key text.
- Confirm the host and host key; never bypass host verification for convenience.
- Use least-privilege access. Diagnose with logs and service status first.
- Restart the identified service/container only when authorized.
  Warn about interrupting active players.

## Security expectations

Valheim relies heavily on client authority. A server-side mod or matching-mod check
can coordinate cooperative clients, but it cannot make modified clients trustworthy
or guarantee anti-cheat protection. State the limits without using them as a reason
to ignore input validation, ownership checks, or safe server administration.
