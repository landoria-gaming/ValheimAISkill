# Valheim Architecture

A practical map for modding, player support, and server administration, not a
complete API or a stable protocol specification. Inspect only the relevant types
with the [ILSpy helpers](inspection-scripts.md#code-inspect-assemblies-and-types).

## Evidence and scope

Checked on 2026-10-03 against the Windows client reporting Valheim **1.0.16**,
with Unity **6000.0.75f1**. Core findings below come from the installed DLLs, not
from a wiki. Recheck changed methods, assets, and mod overrides after updates.

| Assembly | SHA-256 of the inspected build |
| --- | --- |
| `assembly_valheim.dll` | `96cfc004f7f4a6f30d070bef39eafd79c466a137121c4665a2f19fb9c15c6127` |
| `assembly_utils.dll` | `95810ce36bc0563bd74a45df6df906890653e2eda952939a0bcb6ba73af63640` |

The dedicated-server DLL was not available for this comparison. Dedicated-build
details and actual multiplayer behavior still need validation on the target.
Do not present this inspection as a client/server binary diff or a live test.

## Shared client and server code

Use the working approximation **almost 99% shared code** for the matching-version
client and dedicated server. This is the maintainer's practical description, not
a measured percentage or a guarantee that only one or two classes differ.
Start with accessible client DLLs for common gameplay logic, including when
investigating a Linux server from a Windows machine.

The dedicated server runs **headless**: no player-facing game graphics, HUD, or
local player. A console/log window is not a game UI. Keep rendering, input,
local-player chat, and popup work out of its execution path.

Shared classes do not imply identical compiled method bodies. For example, the
checked client's `ZNet.IsDedicated()` returns a constant `false`; do not copy that
body into a mod or conclude the server implementation must also return false.
Inspect the server DLL when build-specific branches matter. Native libraries,
paths, launch scripts, platform services, and deployed mods may also differ.

## Runtime roles

Classify the **local process**, not the remote server it has joined. First wait
for a valid `ZNet.instance` in the gameplay session. Before that, or during
teardown, report an unknown/not-in-session state rather than defaulting to client.

| Local role | `ZNet.instance.IsServer()` | `ZNet.instance.IsDedicated()` | Additional check |
| --- | --- | --- | --- |
| Remote multiplayer client | `false` | `false` | It joins another host; does not host the world |
| Dedicated server | `true` | `true` in the dedicated build | Headless; verify this build-specific result on the target |
| Player-hosted multiplayer (listen server) | `true` | `false` | `ZNet.IsOpenServer()` is `true` |
| Single-player world | `true` | `false` | `ZNet.IsSinglePlayer` is `true`; open server is `false` |

The three multiplayer roles are distinct, but single-player is an essential
fourth check: **`IsServer()` alone does not mean multiplayer or dedicated**.
In the checked code, `IsSinglePlayer` means server with `!IsOpenServer()`.
`FejdStartup` sets these flags from the host/join choice and the open-server toggle.

- A player host runs world-host logic and local-player presentation in one process.
  For host authority use `IsServer()`; for player presentation exclude dedicated
  mode and wait for the relevant player/UI objects. Do not use `!IsServer()` to
  enable a HUD feature: that would incorrectly exclude the hosting player.
- No connected guests does not make an open host single-player. Peer/player counts
  and the public-listing flag are not role tests.
- A missing `Player.m_localPlayer` is normal while loading or spawning. It is not
  proof of dedicated mode. Likewise, batch mode or a null graphics device alone
  does not establish Valheim's networking role.
- `IsCurrentServerDedicated()` examines remote peer information in the checked
  client; it is not the local-process test. Do not substitute it for `IsDedicated()`.
- Do not cache a role permanently in plugin `Awake`. Re-evaluate for each session
  and clear session state on exit. `ZNet.s_onZNetStart` is a public `Action` hook,
  but fires before world loading/client connection completes. It is not a
  world-ready or player-ready notification.

Local evidence: `ZNet.SetServer`, `IsServer`, `IsDedicated`, `IsOpenServer`,
`IsSinglePlayer`, `IsCurrentServerDedicated`, `Awake`, `Start`, `OnDestroy`, and
their `FejdStartup` call sites. Public mod examples can corroborate usage, but
cannot verify a missing dedicated binary for this exact version.

## Main classes and responsibilities

Unless stated otherwise, these types are in `assembly_valheim.dll`. This is a
navigation map, not a claim that every member is public or safe to patch.

| Class or group | Useful responsibility / starting point |
| --- | --- |
| `FejdStartup` | Menu, world selection, host/join options, and session setup |
| `Game` | Gameplay-session coordination, local player spawning, save timing |
| `ZNet` / `ZNetPeer` | Session roles, peers, handshake, world load/save, permissions |
| `ZNetScene` | Prefab registry and creation/removal of scene instances for network objects |
| `ZNetView` | Component connecting a Unity object to its ZDO, ownership checks, object RPCs |
| `ZDO` / `ZDOID` | Replicated object data and identity, distinct from a Unity instance ID |
| `ZDOMan` | Object database, sector-based synchronization, revisions, persistence |
| `ZRpc` | Registered, typed calls over one peer connection |
| `ZRoutedRpc` | Calls routed to a peer, everybody, or a specific ZDO-backed object |
| `ZPackage` | Binary serialization used by networking and save payloads |
| `ZSteamSocket` / `ZSteamMatchmaking` | Steam transport, discovery/registration, session tickets |
| `ZPlayFabSocket` / `ZPlayFabMatchmaking` | PlayFab Party transport, lobbies, join codes, reconnection |
| `PlayFabManager` | PlayFab login and authentication coordination |
| `World` | World identity, seed, generation version, save paths and metadata |
| `SaveSystem` | Save discovery, sources, generations, backups, moves and restoration |
| `PlayerProfile` | Character file, serialized player data and per-world player data |
| `Player` / `Character` | Player actions; shared health, damage and character behavior |
| `HitData` | Damage types/modifiers and serialized hit information |
| `Inventory` / `ItemDrop` | Inventory contents; item definitions, names, icons and instance data |
| `ObjectDB` / `Recipe` | Item/status-effect lookup and crafting recipes/requirements |
| `Smelter` | Conversion recipes stored separately in `m_conversion` |
| `ZoneSystem` | World zones, location spawning, progression/global keys and world modifiers |
| `Terminal` / `Console` | Command registration, parsing, availability and console presentation |
| `Localization` | Display text and translation lookup (`assembly_guiutils.dll`) |
| `Utils` / `FileHelpers` | Save-root resolution and local/cloud file access (`assembly_utils.dll`) |

## Objects, assets, and lifecycle

A Unity `GameObject` carries components such as `ItemDrop`, `Character`, or
`ZNetView`. Prefabs supply serialized defaults; code interprets those values;
runtime state and mods may change them. A recipe or resistance answer therefore
often needs both the component code and the relevant [asset data](assets.md).

- `ObjectDB` indexes items by stable name hash and holds `m_recipes`. It is not a
  complete catalog of every prefab or processing recipe; check the relevant
  workstation/conversion component too.
- `ZNetScene` maps prefab-name hashes to prefabs and ZDOs to instantiated
  `ZNetView` objects. A saved/replicated ZDO can exist without a loaded Unity object.
  Failure to find a scene instance is not proof the object was deleted.
- Prefab names, translated display names, hashes, and `ZDOID` values are different
  identifiers. Use Valheim's stable hashing where its API expects it, not ordinary
  runtime `string.GetHashCode()` or a translated label.
- BepInEx plugin startup, network startup, world readiness, and local-player spawn
  are different points in time. Check the needed singleton/data at the actual use
  point; the public first-spawn pattern is in [Development](development.md#first-spawn-and-chat).
- Unity objects belong on the game thread. The save path prepares state before
  writing on a worker thread; do not add Unity scene access inside save workers.

## Client-server exchanges

Typical game-message path (transport framing is a separate layer):

```text
Gameplay / object state
    -> ZRoutedRpc or ZDOMan (when routing or replication is needed)
    -> ZRpc -> ZPackage bytes -> ISocket implementation
    -> SteamNetworkingSockets or PlayFab Party -> receiving peer
```

The gameplay payload is **custom binary data**, not JSON, HTTP, or an automatically
negotiated C# object schema. `ZPackage` uses `BinaryWriter`/`BinaryReader` over a
stream. Read types and order must match the writing call site exactly.

| Layer | Checked representation / important constraint |
| --- | --- |
| Primitive payload | Typed writes/reads; vectors and quaternions are component values; strings use the binary writer's encoding/framing |
| Nested package / byte array | Length followed by bytes; compression only where the actual call path applies it |
| `ZDOID` | Signed 64-bit user/session portion followed by an unsigned 32-bit object ID in `ZPackage`; not a Steam account ID |
| Direct RPC | Stable method-name hash followed by parameters in handler order; debug mode can add a method string |
| Routed RPC | Message ID, sender peer ID, target peer ID, target ZDO, method hash, nested parameters; sent through the `RoutedRPC` RPC |
| ZDO synchronization | `ZDOData` includes invalidations, object IDs, ownership/data revisions, owner, position, and serialized ZDO payloads |
| Initial handshake | `ZNet.SendPeerInfo` / `RPC_PeerInfo` exchange version/session details and backend-specific authentication data |

`ZDO.Serialize` and `Deserialize` use flags and typed property collections.
Synchronization is selective by sectors, revisions, and queue budget, not a full
Unity scene export every frame. `ZDO.Save`/`Load` are separate from the network
methods: similar data does not make save and network formats interchangeable.

For a mod RPC, use a unique namespaced name, matching registration/parameter
order, and an explicit payload version when the schema evolves. Validate sender
authority and bounds before acting. Prefer the game's RPC/socket layer over
reimplementing Steam or PlayFab framing. Check the exact serialize/deserialize
pair before adding a type; `ZRpc` does not serialize arbitrary objects for you.

## Steam and PlayFab

`ZNet.m_onlineBackend` selects the session's game transport. Do not infer it from
the user's store, operating system, or whether the host is dedicated.

| Backend | Implementation and operational meaning |
| --- | --- |
| Steamworks | `ZSteamSocket` calls SteamNetworkingSockets; `ZSteamMatchmaking` handles Steam discovery/registration and ticket checks |
| PlayFab / crossplay | `ZPlayFabSocket` uses PlayFab Party data messages; `ZPlayFabMatchmaking` registers/searches lobbies and resolves join codes; `PlayFabManager` coordinates authentication |

PlayFab provides connection services, not an automatic replacement for the
player's world-host process. The same Valheim RPC/ZDO concepts sit above either
transport. Steam services can still appear in a Steam client's logs when the
selected game transport is PlayFab; inspect the actual socket/backend.

The checked PlayFab wrapper also handles sequencing, acknowledgements, recovery,
and conditional compression. Captured transport bytes need not start with a
`ZRpc` method hash. Diagnose discovery, backend login, connection, handshake, and
game-state synchronization as separate stages; listing a server does not prove
a successful world connection. Ports, crossplay join restrictions, and launch
flags are covered once in the [official-guide notes](servers.md#official-server-guide).

## Authority and mod compatibility

The host manages the world and peer session, but individual network objects have
owners, and clients participate in simulation. `ZNetView.IsOwner()` concerns that
object; it is not equivalent to `ZNet.IsServer()` or administrator permission.
Follow the particular feature's RPC and ownership checks before choosing a patch.

A server-only mod cannot assume clients receive its DLL, prefabs, UI, or custom
RPC handlers. Check which machines need the mod and any shared content. Network
version compatibility does not establish mod compatibility. Cooperative config
or matching-mod checks are not a guarantee against modified clients; retain input
validation and explain those limits.

## Saves and storage

Resolve the actual source and path first: local, cloud, legacy, a `-savedir`
override, or a service/container account's storage. `Utils.GetSaveDataPath` and
`FileHelpers` decide the underlying root/provider. Cloud paths can be logical
provider paths rather than files beneath a guessed Steam directory.

| Data | Checked layout / meaning |
| --- | --- |
| Local character | `characters_local/<name>.fch`; `PlayerProfile` stores serialized `Player` data and per-world data |
| Local world, current chunked format | `worlds_local/<world>/` with numbered `_main.*.fwl2`, `_main.*.db2`, `.chunks`, `.chunk`, and `.ok` files |
| Legacy world | Matching `<world>.fwl` metadata and `<world>.db` state; legacy readers still exist |
| Cloud/legacy path variants | `characters/` and `worlds/`; inspect `FileSource` rather than inferring cloud status from a folder name alone |

In the checked build, `ZNet.SaveWorldThread` writes ZDO chunks, world-system state,
metadata, then a completion marker. `World.GetSavePaths()` returns the entire
world directory for a chunked save. **Do not back up only `.db` and `.fwl`, or only
the newest `_main` files, for that format.** Preserve referenced chunks and the
complete consistent save set; do not assemble generations from different saves.

World metadata contains identity, seed and generation information; world state
includes persistent objects, zone/progression data and events. Character state
is separate: a world backup alone does not back up every player's inventory or
character. `PlayerProfile` writes a length-delimited binary package and its
SHA-512 hash to `.fch`; a hash is not encryption. These are versioned game formats,
not generic SQLite databases or JSON files.

For backup/restore, establish a completed save and stop the writer gracefully, or
use a verified consistent snapshot mechanism. Preserve a recovery copy, the game
version and required mods. Restore into an isolated location first. Never test
a binary editor or an older game version against the only copy of a save.
Administration steps stay in [Routine maintenance](servers.md#routine-maintenance).

## How to extend this reference

Keep only findings that change modding or support decisions. Add the inspected
type/method, build evidence, and any unverified part; keep extracted code and
personal paths out of the skill. A local signature check is not a runtime test.
When a change affects roles or networking, test solo, remote client, player-hosted
multiplayer, and dedicated server as applicable, with the relevant backend.
