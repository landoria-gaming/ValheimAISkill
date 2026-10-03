# Valheim Prefab Inventory

Extracted on 2026-10-03 from the local Steam build **Valheim 1.0.16**.

- **5,990 prefab assets**, sorted by root name (or file stem when unavailable).
- All **5,945** prefab records from `valheim_Data/StreamingAssets/SoftRef/manifest_extended` are included.
- AssetRipper **2.0.0 Free** inspected **192** referenced bundles and found **45** additional prefab container entries.
- Root properties were read for **5,988** entries; unavailable values are marked explicitly.
- Verified English display names were found for **2,409** entries using local prefab fields and localization data.
- Source manifest SHA-256: `75d44c508602a0af85e7881bb8f99d3ea9e77f7dd39ff305070fde7a2feb1b64`.

## Reading the table

The folder family is derived from the original asset path, not a verified gameplay role.
Root components counts components attached directly to the root, not all descendants.
Active is the serialized root state, not proof that the object currently exists in a world.
Source identifies the bundle and original asset path; identical names are not merged.

English name uses display-name fields on root components (including ItemDrop, Piece,
Character, and pickable item references). Localization files follow LocalizationSettings
load order. Names are not guessed from prefab identifiers. An em dash means no verified
name was found, not proof that no name exists. Runtime renaming, child-only labels, and
mod overrides are not evaluated. Technical prefabs often have no player-facing name.

This is an inventory of prefab files in the inspected shipping bundles, not console commands
or an enumeration of a running game's objects. It does not include mod-added or dynamically
created prefabs, and does not establish that every listed asset can be spawned. References to
unloaded dependency bundles may remain unresolved. Game version was checked in the local
assembly's Version.CurrentVersion; no save or game file was changed.

## Prefabs

| Prefab / root name | English name | Folder family | Root properties | Source: bundle / asset path |
| --- | --- | --- | --- | --- |
| _AudioManager | — | Systems | 3 components; active: yes | 61c598bb / Assets/Systems/_AudioManager.prefab |
| _BOSS_TELEPORT_TARGET | — | Characters/SeekerQueen | 1 components; active: yes | cd0f218 / Assets/Characters/SeekerQueen/attacks/_BOSS_TELEPORT_TARGET.prefab |
| _Console | — | Systems | 6 components; active: yes | c4210710 / Assets/Systems/_Console.prefab |
| _CultivatorPieceTable | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_CultivatorPieceTable.prefab |
| _DLCManager | — | Systems | 2 components; active: yes | c4210710 / Assets/Systems/_DLCManager.prefab |
| _Environment | — | Systems | 4 components; active: yes | d59cfac / Assets/Systems/_Environment.prefab |
| _eventzone_boss_base | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/_eventzone_boss_base.prefab |
| _FeasterPieceTable | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_FeasterPieceTable.prefab |
| _GameMain | — | Systems | 13 components; active: yes | d59cfac / Assets/Systems/_GameMain.prefab |
| _GoogleAnalytics | — | Systems | 2 components; active: no | c4210710 / Assets/Systems/_GoogleAnalytics.prefab |
| _HammerPieceTable | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_HammerPieceTable.prefab |
| _HoePieceTable | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_HoePieceTable.prefab |
| _LocationList_Ashlands | — | Systems/LocationLists | 2 components; active: yes | d59cfac / Assets/Systems/LocationLists/_LocationList_Ashlands.prefab |
| _LocationList_cp1 | — | Systems/LocationLists | 2 components; active: yes | d59cfac / Assets/Systems/LocationLists/_LocationList_cp1.prefab |
| _LocationList_DeepNorth | — | Systems/LocationLists | 2 components; active: yes | d59cfac / Assets/Systems/LocationLists/_LocationList_DeepNorth.prefab |
| _LocationList_Hildir | — | Systems/LocationLists | 2 components; active: yes | d59cfac / Assets/Systems/LocationLists/_LocationList_Hildir.prefab |
| _LocationList_Mistlands | — | Systems/LocationLists | 2 components; active: yes | d59cfac / Assets/Systems/LocationLists/_LocationList_Mistlands.prefab |
| _LocationList_MountainCaves | — | Systems/LocationLists | 2 components; active: yes | d59cfac / Assets/Systems/LocationLists/_LocationList_MountainCaves.prefab |
| _NetScene | — | Systems | 3 components; active: yes | c4210710 / Assets/Systems/_NetScene.prefab |
| _RoomList | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList.prefab |
| _RoomList_Ashlands | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_Ashlands.prefab |
| _RoomList_Cave | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_Cave.prefab |
| _RoomList_DeepNorth | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_DeepNorth.prefab |
| _RoomList_HalfBurried | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_HalfBurried.prefab |
| _RoomList_Hole | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_Hole.prefab |
| _RoomList_Mistlands | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_Mistlands.prefab |
| _RoomList_MorkHalla | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_MorkHalla.prefab |
| _RoomList_Tower | — | Systems/RoomLists | 2 components; active: yes | d59cfac / Assets/Systems/RoomLists/_RoomList_Tower.prefab |
| _SpawnList_ashlands | — | Systems/SpawnLists | 2 components; active: yes | c4210710 / Assets/Systems/SpawnLists/_SpawnList_ashlands.prefab |
| _SpawnList_base | — | Systems/SpawnLists | 2 components; active: yes | c4210710 / Assets/Systems/SpawnLists/_SpawnList_base.prefab |
| _SpawnList_DeepNorth | — | Systems/SpawnLists | 2 components; active: yes | c4210710 / Assets/Systems/SpawnLists/_SpawnList_DeepNorth.prefab |
| _SpawnList_mistlands | — | Systems/SpawnLists | 2 components; active: yes | c4210710 / Assets/Systems/SpawnLists/_SpawnList_mistlands.prefab |
| _TerrainCompiler | — | Systems | 3 components; active: yes | c4210710 / Assets/Systems/_TerrainCompiler.prefab |
| _Zone | — | Systems | 1 components; active: yes | d59cfac / Assets/Systems/_Zone.prefab |
| _ZoneCtrl | — | Systems | 3 components; active: yes | c4210710 / Assets/Systems/_ZoneCtrl.prefab |
| _ZoneSystem | — | Systems | 2 components; active: yes | d59cfac / Assets/Systems/_ZoneSystem.prefab |
| Abomination | Abomination | Characters/Abomination | 11 components; active: yes | c4210710 / Assets/Characters/Abomination/Abomination.prefab |
| Abomination_attack1 | Swing attack | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/Misc/Abomination_attack1.prefab |
| Abomination_attack2 | Slam attack | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/Misc/Abomination_attack2.prefab |
| Abomination_attack3 | Stub to the ground | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/Misc/Abomination_attack3.prefab |
| Abomination_ragdoll | — | Characters/Abomination | 3 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/Abomination_ragdoll.prefab |
| acacitree | — | world/Props | 1 components; active: yes | d59cfac / Assets/world/Props/vegetation/acacitree.prefab |
| AccessibilityTab | — | UI/prefabs | 6 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/AccessibilityTab.prefab |
| Achievements | — | Scripts/gui | 2 components; active: yes | d59cfac / Assets/Scripts/gui/Achievements/Achievements.prefab |
| Achievements1 | — | Scripts/gui | 2 components; active: yes | d59cfac / Assets/Scripts/gui/Achievements/Achievements1.prefab |
| Acorn | Acorns | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Acorn.prefab |
| altar | — | world/Props | 2 components; active: yes | 1cb6211b / Assets/world/Props/offeraltar/altar.prefab |
| AltBiomes_Erik | — | Systems/AltBiomeLists | 2 components; active: yes | d59cfac / Assets/Systems/AltBiomeLists/AltBiomes_Erik.prefab |
| amb_forgeofpotential_main | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/ForgeOfPotential/amb_forgeofpotential_main.prefab |
| Amber | Amber | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/Amber.prefab |
| AmberPearl | Amber Pearl | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/AmberPearl.prefab |
| ancient_skull | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/ancient_skull.prefab |
| ancientbarkspear_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AncientSpear/ancientbarkspear_projectile.prefab |
| AncientCoin | Ancient Coin | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/AncientCoin.prefab |
| AncientGemstoneBlack | Draumyx | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/AncientGemstoneBlack.prefab |
| AncientGemstoneGreen | Grimvarn | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/AncientGemstoneGreen.prefab |
| AncientGemstoneOrange | Solryth | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/AncientGemstoneOrange.prefab |
| AncientGemstonePurple | Veydris | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/AncientGemstonePurple.prefab |
| AncientSeed | Ancient Seed | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AncientSeed.prefab |
| AncientUpgradeStation | — | world/Locations | 2 components; active: yes | c58d692a / Assets/world/Locations/Mountains/AncientUpgradeStation.prefab |
| aniattach_forge_hammer | — | Characters/Player | 1 components; active: yes | c4210710 / Assets/Characters/Player/fx/aniattach_forge_hammer.prefab |
| aoe_nova | — | Characters/GoblinKing | 3 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/aoe_nova.prefab |
| arbalest_projectile_blackmetal | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/arbalest_projectile_blackmetal.prefab |
| arbalest_projectile_bloodgold | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/arbalest_projectile_bloodgold.prefab |
| arbalest_projectile_bone | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/arbalest_projectile_bone.prefab |
| arbalest_projectile_carapace | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/arbalest_projectile_carapace.prefab |
| arbalest_projectile_charred | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/arbalest_projectile_charred.prefab |
| arbalest_projectile_iron | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/arbalest_projectile_iron.prefab |
| ArmorAshlandsMediumChest | Breastplate of Ask | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorAshlandsMediumChest.prefab |
| ArmorAshlandsMediumlegs | Trousers of Ask | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorAshlandsMediumlegs.prefab |
| ArmorBerserkerChest | Patterns of the Bear | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorBerserkerChest.prefab |
| ArmorBerserkerLegs | Loincloth of the Bear | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorBerserkerLegs.prefab |
| ArmorBerserkerUndeadChest | Vilebone Cage | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorBerserkerUndeadChest.prefab |
| ArmorBerserkerUndeadLegs | Vilebone Drapes | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorBerserkerUndeadLegs.prefab |
| ArmorBronzeChest | Bronze Plate Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorBronzeChest.prefab |
| ArmorBronzeLegs | Bronze Plate Leggings | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorBronzeLegs.prefab |
| ArmorCarapaceChest | Carapace Breastplate | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorCarapaceChest.prefab |
| ArmorCarapaceLegs | Carapace Greaves | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorCarapaceLegs.prefab |
| ArmorDeepNorthHeavyChest | Breastplate of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDeepNorthHeavyChest.prefab |
| ArmorDeepNorthHeavylegs | Trousers of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDeepNorthHeavylegs.prefab |
| ArmorDeepNorthMageChest | Robes of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDeepNorthMageChest.prefab |
| ArmorDeepNorthMagelegs | Trousers of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDeepNorthMagelegs.prefab |
| ArmorDeepNorthMediumChest | Chestpiece of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDeepNorthMediumChest.prefab |
| ArmorDeepNorthMediumlegs | Trousers of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDeepNorthMediumlegs.prefab |
| ArmorDress1 | Plain Brown Dress | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress1.prefab |
| ArmorDress10 | Simple Undyed Dress | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress10.prefab |
| ArmorDress2 | Brown Dress with Shawl | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress2.prefab |
| ArmorDress3 | Brown Dress with Beads | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress3.prefab |
| ArmorDress4 | Plain Blue Dress | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress4.prefab |
| ArmorDress5 | Blue Dress with Shawl | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress5.prefab |
| ArmorDress6 | Blue Dress with Beads | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress6.prefab |
| ArmorDress7 | Plain Yellow Dress | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress7.prefab |
| ArmorDress8 | Yellow Dress with Shawl | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress8.prefab |
| ArmorDress9 | Yellow Dress with Beads | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorDress9.prefab |
| ArmorFenringChest | Fenris Coat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorFenringChest.prefab |
| ArmorFenringLegs | Fenris Leggings | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorFenringLegs.prefab |
| ArmorFlametalChest | Flametal Breastplate | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorFlametalChest.prefab |
| ArmorFlametalLegs | Flametal Greaves | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorFlametalLegs.prefab |
| ArmorGoldHeavyChestUncooked | Cast: Breastplate of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldHeavyChestUncooked.prefab |
| ArmorGoldHeavyHelmetUncooked | Cast: Helmet of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldHeavyHelmetUncooked.prefab |
| ArmorGoldHeavyLegsUncooked | Cast: Trousers of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldHeavyLegsUncooked.prefab |
| ArmorGoldMageChestUncooked | Cast: Robes of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldMageChestUncooked.prefab |
| ArmorGoldMageHelmetUncooked | Cast: Headdress of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldMageHelmetUncooked.prefab |
| ArmorGoldMageLegsUncooked | Cast: Trousers of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldMageLegsUncooked.prefab |
| ArmorGoldMediumChestUncooked | Cast: Chestpiece of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldMediumChestUncooked.prefab |
| ArmorGoldMediumHelmetUncooked | Cast: Hood of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldMediumHelmetUncooked.prefab |
| ArmorGoldMediumLegsUncooked | Cast: Trousers of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ArmorGoldMediumLegsUncooked.prefab |
| ArmorHarvester1 | Harvest Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorHarvester1.prefab |
| ArmorHarvester2 | Harvest Dress | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorHarvester2.prefab |
| ArmorIronChest | Iron Scale Mail | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorIronChest.prefab |
| ArmorIronLegs | Iron Greaves | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorIronLegs.prefab |
| ArmorLeatherChest | Leather Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorLeatherChest.prefab |
| ArmorLeatherLegs | Leather Trousers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorLeatherLegs.prefab |
| ArmorLoxChest | Lox Fur Jacket | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorLoxChest.prefab |
| ArmorLoxLegs | Lox Fur Trousers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorLoxLegs.prefab |
| ArmorMageChest | Eitr-weave Robe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorMageChest.prefab |
| ArmorMageChest_Ashlands | Robes of Embla | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorMageChest_Ashlands.prefab |
| ArmorMageLegs | Eitr-weave Trousers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorMageLegs.prefab |
| ArmorMageLegs_Ashlands | Trousers of Embla | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorMageLegs_Ashlands.prefab |
| ArmorPaddedCuirass | Padded Cuirass | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorPaddedCuirass.prefab |
| ArmorPaddedGreaves | Padded Greaves | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorPaddedGreaves.prefab |
| ArmorRagsChest | Rag Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorRagsChest.prefab |
| ArmorRagsLegs | Rag Trousers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorRagsLegs.prefab |
| ArmorRootChest | Root Harnesk | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorRootChest.prefab |
| ArmorRootLegs | Root Leggings | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorRootLegs.prefab |
| ArmorStand | Armour Stand | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ArmorStand.prefab |
| ArmorStand_Female | Armour Stand | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/ArmorStand_Female.prefab |
| ArmorStand_Male | Armour Stand | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/ArmorStand_Male.prefab |
| ArmorTrollLeatherChest | Troll Leather Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTrollLeatherChest.prefab |
| ArmorTrollLeatherLegs | Troll Leather Trousers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTrollLeatherLegs.prefab |
| ArmorTunic1 | Plain Blue Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic1.prefab |
| ArmorTunic10 | Simple Undyed Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic10.prefab |
| ArmorTunic2 | Blue Tunic with Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic2.prefab |
| ArmorTunic3 | Blue Tunic with Beads | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic3.prefab |
| ArmorTunic4 | Plain Red Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic4.prefab |
| ArmorTunic5 | Red Tunic with Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic5.prefab |
| ArmorTunic6 | Red Tunic with Beads | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic6.prefab |
| ArmorTunic7 | Plain Yellow Tunic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic7.prefab |
| ArmorTunic8 | Yellow Tunic with Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic8.prefab |
| ArmorTunic9 | Yellow Tunic with Beads | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorTunic9.prefab |
| ArmorWolfChest | Wolf Hide Chestpiece | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorWolfChest.prefab |
| ArmorWolfLegs | Wolf Hide Trousers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/ArmorWolfLegs.prefab |
| ArrowBloodGold | Bloodgold Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowBloodGold.prefab |
| ArrowBronze | Bronzehead Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowBronze.prefab |
| ArrowCarapace | Carapace Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowCarapace.prefab |
| ArrowCharred | Charred Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowCharred.prefab |
| ArrowFire | Fire Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowFire.prefab |
| ArrowFlint | Flinthead Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowFlint.prefab |
| ArrowFrost | Frost Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowFrost.prefab |
| ArrowIron | Ironhead Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowIron.prefab |
| ArrowNeedle | Needle Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowNeedle.prefab |
| ArrowObsidian | Obsidian Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowObsidian.prefab |
| ArrowPoison | Poison Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowPoison.prefab |
| ArrowSilver | Silver Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowSilver.prefab |
| ArrowWood | Wood Arrow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/ArrowWood.prefab |
| artisan_ext1 | Artisan Press | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/artisan_ext1.prefab |
| AshCrow | — | Characters/animals | 9 components; active: yes | c4210710 / Assets/Characters/animals/birds/AshCrow.prefab |
| ashland_pot1_green | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/ashland_pot1_green.prefab |
| ashland_pot1_red | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/ashland_pot1_red.prefab |
| ashland_pot2_green | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/ashland_pot2_green.prefab |
| ashland_pot2_red | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/ashland_pot2_red.prefab |
| ashland_pot3_green | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/ashland_pot3_green.prefab |
| ashland_pot3_red | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/ashland_pot3_red.prefab |
| Ashland_Stair | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashland_Stair.prefab |
| Ashland_Steepstair | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashland_Steepstair.prefab |
| Ashlands_Altar | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Altar.prefab |
| Ashlands_Arch1 | Stone Wall 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Arch1.prefab |
| Ashlands_Arch2 | Stone Wall 1x1 | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Arch2.prefab |
| Ashlands_Arch2_Broken1 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Arch2_Broken1.prefab |
| Ashlands_Arch2_Broken2 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Arch2_Broken2.prefab |
| Ashlands_ArchRoof | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_ArchRoof.prefab |
| Ashlands_ArchRoofDamaged | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_ArchRoofDamaged.prefab |
| Ashlands_ArchRoofDamaged_half1 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_ArchRoofDamaged_half1.prefab |
| Ashlands_ArchRoofDamaged_half2 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_ArchRoofDamaged_half2.prefab |
| Ashlands_ArchRoofLong_Damaged | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_ArchRoofLong_Damaged.prefab |
| Ashlands_AshRain | — | Effects/weather | 1 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/Ashlands_AshRain.prefab |
| Ashlands_Boss_Pillar | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Boss_Pillar.prefab |
| Ashlands_Boss_Pillar_Twist_broken1 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Boss_Pillar_Twist_broken1.prefab |
| Ashlands_Boss_Pillar_Twist_broken2 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Boss_Pillar_Twist_broken2.prefab |
| Ashlands_Boss_Pillar_Twist_broken3 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Boss_Pillar_Twist_broken3.prefab |
| Ashlands_CinderRain | — | Effects/weather | 1 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/Ashlands_CinderRain.prefab |
| Ashlands_FaderFX | — | Effects/weather | 1 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/Ashlands_FaderFX.prefab |
| Ashlands_Floor | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Floor.prefab |
| Ashlands_floor_large | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_floor_large.prefab |
| Ashlands_floor_large_fractured | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_floor_large_fractured.prefab |
| Ashlands_Fortress_Floor | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Floor.prefab |
| Ashlands_Fortress_Gate | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Gate.prefab |
| Ashlands_Fortress_Gate_Door | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Gate_Door.prefab |
| Ashlands_Fortress_Wall_Pillar | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_Pillar.prefab |
| Ashlands_Fortress_Wall_Pillar_base | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_Pillar_base.prefab |
| Ashlands_Fortress_Wall_Pillar_base_frac | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_Pillar_base_frac.prefab |
| Ashlands_Fortress_Wall_Pillar_frac | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_Pillar_frac.prefab |
| Ashlands_Fortress_Wall_PillarTop | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_PillarTop.prefab |
| Ashlands_Fortress_Wall_PillarTop_frac | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_PillarTop_frac.prefab |
| Ashlands_Fortress_Wall_PillarTopStone | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_PillarTopStone.prefab |
| Ashlands_Fortress_Wall_PillarTopStone_frac | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_PillarTopStone_frac.prefab |
| Ashlands_Fortress_Wall_Spikes | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Fortress_Wall_Spikes.prefab |
| Ashlands_MeteorShower | — | Effects/weather | 1 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/Ashlands_MeteorShower.prefab |
| Ashlands_Misty | — | Effects/weather | 1 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/Ashlands_Misty.prefab |
| Ashlands_Pillar4 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4.prefab |
| Ashlands_Pillar4_tip | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip.prefab |
| Ashlands_Pillar4_tip2 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip2.prefab |
| Ashlands_Pillar4_tip2_broken1 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip2_broken1.prefab |
| Ashlands_Pillar4_tip2_broken2 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip2_broken2.prefab |
| Ashlands_Pillar4_tip3 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip3.prefab |
| Ashlands_Pillar4_tip3_broken1 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip3_broken1.prefab |
| Ashlands_Pillar4_tip3_broken2 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip3_broken2.prefab |
| Ashlands_Pillar4_tip3_broken3 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip3_broken3.prefab |
| Ashlands_Pillar4_tip_broken1 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip_broken1.prefab |
| Ashlands_Pillar4_tip_broken2 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Pillar4_tip_broken2.prefab |
| Ashlands_PillarBase3_double | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_PillarBase3_double.prefab |
| Ashlands_Ramp | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ramp.prefab |
| Ashlands_rock1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands_rock1.prefab |
| Ashlands_rock2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/Ashlands_rock2.prefab |
| Ashlands_Ruins_Floor_1point5x1point5 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_1point5x1point5.prefab |
| Ashlands_Ruins_Floor_1point5x1point5_broken | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_1point5x1point5_broken.prefab |
| Ashlands_Ruins_Floor_3x3 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_3x3.prefab |
| Ashlands_Ruins_Floor_3x3_broken1 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_3x3_broken1.prefab |
| Ashlands_Ruins_Floor_3x3_broken2 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_3x3_broken2.prefab |
| Ashlands_Ruins_Floor_3x3_broken3 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_3x3_broken3.prefab |
| Ashlands_Ruins_Floor_6x6 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_6x6.prefab |
| Ashlands_Ruins_Floor_6x6_broken1 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_6x6_broken1.prefab |
| Ashlands_Ruins_Floor_6x6_broken2 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Floor_6x6_broken2.prefab |
| Ashlands_Ruins_Ramp | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Ramp.prefab |
| Ashlands_Ruins_Ramp_Upsidedown | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Ramp_Upsidedown.prefab |
| Ashlands_Ruins_TopStone | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_TopStone.prefab |
| Ashlands_Ruins_twist_ArchBig | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_twist_ArchBig.prefab |
| Ashlands_Ruins_twist_PillarBase | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_twist_PillarBase.prefab |
| Ashlands_Ruins_twist_PillarBaseSmall | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_twist_PillarBaseSmall.prefab |
| Ashlands_Ruins_Wall_4x6 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_4x6.prefab |
| Ashlands_Ruins_Wall_Broken3_4x6 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Broken3_4x6.prefab |
| Ashlands_Ruins_Wall_Broken4_4x6 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Broken4_4x6.prefab |
| Ashlands_Ruins_Wall_Broken5_4x6 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Broken5_4x6.prefab |
| Ashlands_Ruins_Wall_Top_wHole | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Top_wHole.prefab |
| Ashlands_Ruins_Wall_Window_4x6_broken2 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Window_4x6_broken2.prefab |
| Ashlands_Ruins_Wall_Window_4x6_broken3 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Window_4x6_broken3.prefab |
| Ashlands_Ruins_Wall_Window_4x6_broken4 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Window_4x6_broken4.prefab |
| Ashlands_Ruins_Wall_Window_4x6_broken5 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Window_4x6_broken5.prefab |
| Ashlands_Ruins_Wall_Window_4x6_broken6 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Window_4x6_broken6.prefab |
| Ashlands_Ruins_Wall_Windows_Broken_4x6 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Ruins_Wall_Windows_Broken_4x6.prefab |
| Ashlands_StairsBroad | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_StairsBroad.prefab |
| Ashlands_storm | — | Effects/weather | 1 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/Ashlands_storm.prefab |
| Ashlands_Wall_2x2 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2.prefab |
| Ashlands_Wall_2x2_cornerL | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_cornerL.prefab |
| Ashlands_Wall_2x2_cornerL_top | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_cornerL_top.prefab |
| Ashlands_Wall_2x2_cornerR | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_cornerR.prefab |
| Ashlands_Wall_2x2_cornerR_top | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_cornerR_top.prefab |
| Ashlands_Wall_2x2_edge | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_edge.prefab |
| Ashlands_Wall_2x2_edge2 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_edge2.prefab |
| Ashlands_Wall_2x2_edge2_top | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_edge2_top.prefab |
| Ashlands_Wall_2x2_edge_top | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_edge_top.prefab |
| Ashlands_Wall_2x2_top | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_Wall_2x2_top.prefab |
| Ashlands_WallBlock | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_WallBlock.prefab |
| Ashlands_WallBlock_1x2x2 | Stone Wall 1x1 | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_WallBlock_1x2x2.prefab |
| Ashlands_WallBlock_base | Stone Wall 1x1 | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/Ashlands_WallBlock_base.prefab |
| AshlandsBranch1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Bushes/AshlandsBranch1.prefab |
| AshlandsBranch2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Bushes/AshlandsBranch2.prefab |
| AshlandsBranch3 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Bushes/AshlandsBranch3.prefab |
| AshlandsBush1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Bushes/AshlandsBush1.prefab |
| AshlandsBush2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Bushes/AshlandsBush2.prefab |
| AshlandsFlash | — | Effects/thunder | 2 components; active: yes | d59cfac / Assets/Effects/thunder/AshlandsFlash.prefab |
| AshlandsTree1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTree1.prefab |
| AshlandsTree3 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTree3.prefab |
| AshlandsTree4 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTree4.prefab |
| AshlandsTree5 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTree5.prefab |
| AshlandsTree6 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTree6.prefab |
| AshlandsTree6_big | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTree6_big.prefab |
| AshlandsTreeLog1 | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTreeLog1.prefab |
| AshlandsTreeLog2 | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTreeLog2.prefab |
| AshlandsTreeLogHalf1 | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTreeLogHalf1.prefab |
| AshlandsTreeLogHalf2 | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTreeLogHalf2.prefab |
| AshlandsTreeStump1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTreeStump1.prefab |
| AshlandsTreeStump2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTreeStump2.prefab |
| AshlandsTreeStump3 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/AshlandsTreeStump3.prefab |
| ashwood_arch_big | Ashwood Arch | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_arch_big.prefab |
| ashwood_arch_bottom | Ashwood Bottom Arch | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_arch_bottom.prefab |
| ashwood_arch_top | Ashwood Top Arch | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_arch_top.prefab |
| ashwood_beam_1m | Ashwood Beam 1 m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_beam_1m.prefab |
| ashwood_beam_2m | Ashwood Beam 2 m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_beam_2m.prefab |
| ashwood_bed | Ashwood Bed | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_bed.prefab |
| ashwood_deco_floor | Ashwood Decorative Floor | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_deco_floor.prefab |
| ashwood_decowall_2x2 | Ashwood Decorative Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_decowall_2x2.prefab |
| ashwood_decowall_divider | Ashwood Divider | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_decowall_divider.prefab |
| ashwood_decowall_tree | Ashwood Decorative Window | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_decowall_tree.prefab |
| ashwood_door | Ashwood Door | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_door.prefab |
| ashwood_floor_1x1 | Ashwood Floor 1x1 | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_floor_1x1.prefab |
| ashwood_floor_2x2 | Ashwood Floor 2x2 | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_floor_2x2.prefab |
| ashwood_halfwall_1x2 | Ashwood Half Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_halfwall_1x2.prefab |
| ashwood_pole_1m | Ashwood Pole 1 m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_pole_1m.prefab |
| ashwood_pole_2m | Ashwood Pole 2 m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_pole_2m.prefab |
| ashwood_quarterwall_1x1 | Ashwood Quarter Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_quarterwall_1x1.prefab |
| ashwood_stair | Ashwood Stair | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_stair.prefab |
| ashwood_wall_2x2 | Ashwood Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_2x2.prefab |
| ashwood_wall_arch | Ashwood Arched Wall | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_arch.prefab |
| ashwood_wall_beam_26 | Ashwood Beam 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_beam_26.prefab |
| ashwood_wall_beam_26_alt | Ashwood Beam 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_beam_26_alt.prefab |
| ashwood_wall_beam_45 | Ashwood Beam 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_beam_45.prefab |
| ashwood_wall_beam_45_alt | Ashwood Beam 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_beam_45_alt.prefab |
| ashwood_wall_beam_67 | Ashwood Beam 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_beam_67.prefab |
| ashwood_wall_cross_26 | Ashwood Roof Cross 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_cross_26.prefab |
| ashwood_wall_cross_26_alt | Ashwood Roof Cross 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_cross_26_alt.prefab |
| ashwood_wall_cross_45 | Ashwood Roof Cross 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_cross_45.prefab |
| ashwood_wall_cross_45_alt | Ashwood Roof Cross 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_cross_45_alt.prefab |
| ashwood_wall_cross_67 | Ashwood Roof Cross 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_cross_67.prefab |
| ashwood_wall_roof_26 | Ashwood Wall 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_roof_26.prefab |
| ashwood_wall_roof_26_upsidedown | Ashwood Wall 26° (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_roof_26_upsidedown.prefab |
| ashwood_wall_roof_45 | Ashwood Wall 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_roof_45.prefab |
| ashwood_wall_roof_45_upsidedown | Ashwood Wall 45° (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_roof_45_upsidedown.prefab |
| ashwood_wall_roof_67_a | Ashwood Wall 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_roof_67_a.prefab |
| ashwood_wall_roof_67_upsidedown | Ashwood Wall 67° (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/ashwood_wall_roof_67_upsidedown.prefab |
| AskBladder | Asksvin Bladder | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AskBladder.prefab |
| AskHide | Asksvin Hide | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AskHide.prefab |
| Asksvin | Asksvin | Characters/Asksvin | 12 components; active: yes | c4210710 / Assets/Characters/Asksvin/Asksvin.prefab |
| Asksvin_Bite | lox bite | Characters/Asksvin | 2 components; active: yes | c4210710 / Assets/Characters/Asksvin/attacks/Asksvin_Bite.prefab |
| asksvin_carrion | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/asksvin_carrion.prefab |
| asksvin_carrion2 | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/asksvin_carrion2.prefab |
| Asksvin_hatchling | Asksvin Hatchling | Characters/Asksvin | 11 components; active: yes | c4210710 / Assets/Characters/Asksvin/Asksvin_hatchling.prefab |
| Asksvin_Headbutt | Dragon claw left | Characters/Asksvin | 3 components; active: yes | c4210710 / Assets/Characters/Asksvin/attacks/Asksvin_Headbutt.prefab |
| Asksvin_Pounce | lox bite | Characters/Asksvin | 2 components; active: yes | c4210710 / Assets/Characters/Asksvin/attacks/Asksvin_Pounce.prefab |
| Asksvin_Turnaround | lox bite | Characters/Asksvin | 2 components; active: yes | c4210710 / Assets/Characters/Asksvin/attacks/Asksvin_Turnaround.prefab |
| AsksvinCarrionNeck | Asksvin Neck | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AsksvinCarrionNeck.prefab |
| AsksvinCarrionPelvic | Asksvin Pelvis | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AsksvinCarrionPelvic.prefab |
| AsksvinCarrionRibcage | Asksvin Ribcage | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AsksvinCarrionRibcage.prefab |
| AsksvinCarrionSkull | Asksvin Skull | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AsksvinCarrionSkull.prefab |
| AsksvinEgg | Asksvin Egg | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/AsksvinEgg.prefab |
| AsksvinMeat | Asksvin Tail | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/AsksvinMeat.prefab |
| aspect_aoe_explosion | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/aspect_aoe_explosion.prefab |
| aspect_aoe_nova | — | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Yagluth/aspect_aoe_nova.prefab |
| Aspect_Bonemass | Aspect of the Writhing Dead | Characters/FrozenKing | 10 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Aspect_Bonemass.prefab |
| aspect_bonemass_aoe | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Bonemass/aspect_bonemass_aoe.prefab |
| aspect_bonemass_attack_aoe | heal | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Bonemass/aspect_bonemass_attack_aoe.prefab |
| aspect_bonemass_attack_punch | slap | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Bonemass/aspect_bonemass_attack_punch.prefab |
| aspect_bonemass_attack_throw | slime throw | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Bonemass/aspect_bonemass_attack_throw.prefab |
| aspect_bonemass_spawn | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Bonemass/aspect_bonemass_spawn.prefab |
| aspect_bonemass_throw_projectile | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Bonemass/aspect_bonemass_throw_projectile.prefab |
| aspect_dragon_bite | Dragon claw left | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Moder/aspect_dragon_bite.prefab |
| aspect_dragon_claw_left | Dragon claw left | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Moder/aspect_dragon_claw_left.prefab |
| aspect_dragon_claw_right | Dragon claw left | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Moder/aspect_dragon_claw_right.prefab |
| aspect_dragon_coldbreath | dragon breath | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Moder/aspect_dragon_coldbreath.prefab |
| aspect_dragon_spit_shotgun | cold ball | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Moder/aspect_dragon_spit_shotgun.prefab |
| aspect_dragon_taunt | scream | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Moder/aspect_dragon_taunt.prefab |
| Aspect_Eikthyr | Aspect of the Lightning Stag | Characters/FrozenKing | 11 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Aspect_Eikthyr.prefab |
| aspect_Eikthyr_antler | StagAttack1 | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Eikthyr/aspect_Eikthyr_antler.prefab |
| aspect_Eikthyr_charge | StagAttack2 | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Eikthyr/aspect_Eikthyr_charge.prefab |
| aspect_Eikthyr_stomp | slap | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Eikthyr/aspect_Eikthyr_stomp.prefab |
| Aspect_Elder | Aspect of the Living Forest | Characters/FrozenKing | 10 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Aspect_Elder.prefab |
| Aspect_Fader | Aspect of the Emerald Flame | Characters/FrozenKing | 12 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Aspect_Fader.prefab |
| aspect_Fader_Bite | Fader Bite | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Bite.prefab |
| aspect_Fader_Claw_Left | Fader Claw Left | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Claw_Left.prefab |
| aspect_Fader_Claw_Right | Fader Claw Right | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Claw_Right.prefab |
| aspect_Fader_Fissure | Fader Fissure | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Fissure.prefab |
| aspect_Fader_Fissure_AOE | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Fissure_AOE.prefab |
| aspect_Fader_Fissure_Spawn | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Fissure_Spawn.prefab |
| aspect_Fader_Flamebreath | Fader Firebreath | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Flamebreath.prefab |
| aspect_Fader_Flamebreath_AOE | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Flamebreath_AOE.prefab |
| aspect_Fader_Spin | Fader Spin | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_Spin.prefab |
| aspect_Fader_WallOfFire | Fader Wall of Fire | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_WallOfFire.prefab |
| aspect_Fader_WallOfFire_AOE | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_WallOfFire_AOE.prefab |
| aspect_Fader_WallOfFire_Spawn | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Fader/aspect_Fader_WallOfFire_Spawn.prefab |
| aspect_gd_king_rootspawn | spawn | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Elder/aspect_gd_king_rootspawn.prefab |
| aspect_gd_king_scream | scream | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Elder/aspect_gd_king_scream.prefab |
| aspect_gd_king_shoot | shaman attack | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Elder/aspect_gd_king_shoot.prefab |
| aspect_gd_king_stomp | jaws | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Elder/aspect_gd_king_stomp.prefab |
| aspect_gdking_root_projectile | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Elder/aspect_gdking_root_projectile.prefab |
| aspect_GoblinKing_Beam | dragon breath | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Yagluth/aspect_GoblinKing_Beam.prefab |
| aspect_GoblinKing_Nova | slap | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Yagluth/aspect_GoblinKing_Nova.prefab |
| aspect_GoblinKing_Taunt | scream | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Yagluth/aspect_GoblinKing_Taunt.prefab |
| Aspect_Moder | Aspect of the Dragon Mother | Characters/FrozenKing | 10 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Aspect_Moder.prefab |
| aspect_projectile_beam | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Yagluth/aspect_projectile_beam.prefab |
| Aspect_SeekerQueen | Aspect of the Crawling Matriarch | Characters/FrozenKing | 11 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Aspect_SeekerQueen.prefab |
| aspect_SeekerQueen_Bite | slap | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Queen/aspect_SeekerQueen_Bite.prefab |
| aspect_SeekerQueen_PierceAOE | slap | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Queen/aspect_SeekerQueen_PierceAOE.prefab |
| aspect_SeekerQueen_projectile_spit | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Queen/aspect_SeekerQueen_projectile_spit.prefab |
| aspect_SeekerQueen_Rush | slap | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Queen/aspect_SeekerQueen_Rush.prefab |
| aspect_SeekerQueen_Slap | slap | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Queen/aspect_SeekerQueen_Slap.prefab |
| aspect_SeekerQueen_Spit | dragon breath | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Queen/aspect_SeekerQueen_Spit.prefab |
| aspect_SeekerQueen_SpitSpawnAbility | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Queen/aspect_SeekerQueen_SpitSpawnAbility.prefab |
| aspect_spawn_roots | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Attacks/Elder/aspect_spawn_roots.prefab |
| Aspect_TentaRoot | Root | Characters/Greydwarf_king | 9 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/Aspect_TentaRoot.prefab |
| Aspect_Yagluth | Aspect of the Twisted Soul | Characters/FrozenKing | 11 components; active: yes | c4210710 / Assets/Characters/FrozenKing/BossAspects/Aspect_Yagluth.prefab |
| AtgeirBlackmetal | Black Metal Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirBlackmetal.prefab |
| AtgeirBronze | Bronze Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirBronze.prefab |
| AtgeirGold | Nord Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirGold.prefab |
| AtgeirGold_BloodLightning | Thunderblood Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirGold_BloodLightning.prefab |
| AtgeirGold_FrostFire | Frostfire Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirGold_FrostFire.prefab |
| AtgeirGoldUncooked | Cast: Nord Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirGoldUncooked.prefab |
| AtgeirHimminAfl | Himminafl | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirHimminAfl.prefab |
| AtgeirIron | Iron Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirIron.prefab |
| AtgeirWood | Wooden Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AtgeirWood.prefab |
| AudioTab | — | UI/prefabs | 6 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/AudioTab.prefab |
| Axe1h_JotunWarrior | Club | Characters/Jotnar | 8 components; active: yes | c4210710 / Assets/Characters/Jotnar/model/weapons/Axe1h_JotunWarrior.prefab |
| Axe1h_JotunWarrior 1 | Club | Characters/Jotnar | 8 components; active: yes | c4210710 / Assets/Characters/Jotnar/model/weapons/Axe1h_JotunWarrior 1.prefab |
| Axe2h_JotunWarrior | Club | Characters/Jotnar | 8 components; active: yes | c4210710 / Assets/Characters/Jotnar/model/weapons/Axe2h_JotunWarrior.prefab |
| AxeBerzerkr | Berserkir Axes | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeBerzerkr.prefab |
| AxeBerzerkrBlood | Bleeding Berserkir Axes | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeBerzerkrBlood.prefab |
| AxeBerzerkrLightning | Thundering Berserkir Axes | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeBerzerkrLightning.prefab |
| AxeBerzerkrNature | Primal Berserkir Axes | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeBerzerkrNature.prefab |
| AxeBlackMetal | Black Metal Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeBlackMetal.prefab |
| AxeBronze | Bronze Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeBronze.prefab |
| AxeEarly | Early Axes | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeEarly.prefab |
| AxeFlint | Flint Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeFlint.prefab |
| AxeGold | Nord Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeGold.prefab |
| AxeGold_BloodLightning | Thunderblood Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeGold_BloodLightning.prefab |
| AxeGold_FrostFire | Frostfire Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeGold_FrostFire.prefab |
| AxeGoldUncooked | Cast: Nord Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeGoldUncooked.prefab |
| AxeHead1 | Curious Axe Head | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AxeHead1.prefab |
| AxeHead2 | Mysterious Axe Head | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/AxeHead2.prefab |
| AxeIron | Iron Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeIron.prefab |
| AxeJotunBane | Jotun Bane | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeJotunBane.prefab |
| AxeStone | Stone Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeStone.prefab |
| AxeWood | Wooden Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/AxeWood.prefab |
| babyseeker_attack | Dragon claw left | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/babyseeker_attack.prefab |
| Back | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/Radial/elements/Back.prefab |
| Backgroundscene | — | world/Menu | 4 components; active: yes | b8689a71 / Assets/world/Menu/Backgroundscene.prefab |
| BakedPoteitr | Baked Poteitr | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BakedPoteitr.prefab |
| BakedPoteitrUncooked | Unbaked Poteitr | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BakedPoteitrUncooked.prefab |
| bar_ancientmetal_stack | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_ancientmetal_stack.prefab |
| bar_blackmetal_stack | Black Metal Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_blackmetal_stack.prefab |
| bar_bronze_stack | Bronze Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_bronze_stack.prefab |
| bar_copper_stack | Copper Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_copper_stack.prefab |
| bar_flametal_stack | Flametal Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_flametal_stack.prefab |
| bar_gold_stack | Bloodgold Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_gold_stack.prefab |
| bar_iron_stack | Iron Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_iron_stack.prefab |
| bar_silver_stack | Silver Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_silver_stack.prefab |
| bar_tin_stack | Tin Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bar_tin_stack.prefab |
| BarberGui | — | UI/prefabs | 7 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/BarberGui.prefab |
| BarberKit | Barber Kit | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BarberKit.prefab |
| Barka | Barka | Characters/Barka | 10 components; active: yes | c4210710 / Assets/Characters/Barka/Barka.prefab |
| Barka_Backslam | Barka Backslam | Characters/Barka | 3 components; active: yes | c4210710 / Assets/Characters/Barka/attacks/Barka_Backslam.prefab |
| Barka_HeavySwing | Dragon claw left | Characters/Barka | 3 components; active: yes | c4210710 / Assets/Characters/Barka/attacks/Barka_HeavySwing.prefab |
| Barka_Ragdoll | — | Characters/Barka | 3 components; active: yes | c4210710 / Assets/Characters/Barka/fx/Barka_Ragdoll.prefab |
| Barka_SlamDrive | Dragon claw left | Characters/Barka | 3 components; active: yes | c4210710 / Assets/Characters/Barka/attacks/Barka_SlamDrive.prefab |
| Barka_WhipFlurry | Dragon claw left | Characters/Barka | 3 components; active: yes | c4210710 / Assets/Characters/Barka/attacks/Barka_WhipFlurry.prefab |
| Barka_WhipSlam | Dragon claw left | Characters/Barka | 3 components; active: yes | c4210710 / Assets/Characters/Barka/attacks/Barka_WhipSlam.prefab |
| BarkaBranch | Frozen Branch | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BarkaBranch.prefab |
| Barley | Barley | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Barley.prefab |
| BarleyFlour | Barley Flour | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BarleyFlour.prefab |
| BarleyWine | Fire Resistance Barley Wine | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BarleyWine.prefab |
| BarleyWineBase | Barley Wine Base: Fire Resistance | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BarleyWineBase.prefab |
| barrell | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/barrell/barrell.prefab |
| barrell_static | — | world/Props | 2 components; active: yes | 17a773de / Assets/world/Props/barrell/barrell_static.prefab |
| BarrelRings | Barrel Hoops | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BarrelRings.prefab |
| Bat | Bat | Characters/Bat | 9 components; active: yes | c4210710 / Assets/Characters/Bat/Bat.prefab |
| bat_melee | Bat melee | Characters/Bat | 5 components; active: yes | c4210710 / Assets/Characters/Bat/Attacks/bat_melee.prefab |
| Bat_Swamp | Bat | Characters/Bat | 9 components; active: yes | c4210710 / Assets/Characters/Bat/Bat_Swamp.prefab |
| BatteringRam | Battering Ram | GameElements/Cart | 13 components; active: yes | c4210710 / Assets/GameElements/Cart/BatteringRam.prefab |
| Battleaxe | Battleaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Battleaxe.prefab |
| BattleaxeBlackmetal | Black Metal Battleaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeBlackmetal.prefab |
| BattleaxeCrystal | Crystal Battleaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeCrystal.prefab |
| BattleaxeGold | Nord Greataxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeGold.prefab |
| BattleaxeGold_BloodLightning | Thunderblood Greataxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeGold_BloodLightning.prefab |
| BattleaxeGold_FrostFire | Frostfire Greataxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeGold_FrostFire.prefab |
| BattleaxeGoldUncooked | Cast: Nord Greataxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeGoldUncooked.prefab |
| BattleaxeSkullSplittur | Skull Splittur | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeSkullSplittur.prefab |
| BattleaxeWood | Wooden Battleaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BattleaxeWood.prefab |
| Beard1 | Majestic | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard1.prefab |
| Beard10 | Top Braid | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard10.prefab |
| Beard11 | Facewarmer | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard11.prefab |
| Beard12 | Royal | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard12.prefab |
| Beard13 | Triplets | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard13.prefab |
| Beard14 | Split Braid | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard14.prefab |
| Beard15 | Mini Braid | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard15.prefab |
| Beard16 | Stonedweller | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard16.prefab |
| Beard17 | Neat | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard17.prefab |
| Beard18 | Jarl Braids | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard18.prefab |
| Beard19 | Bushy | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard19.prefab |
| Beard2 | Twin Braids | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard2.prefab |
| Beard20 | Spiky | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard20.prefab |
| Beard21 | Tidy | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard21.prefab |
| Beard22 | Mustache | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard22.prefab |
| Beard23 | Crumb Catcher | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard23.prefab |
| Beard24 | Waxed | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard24.prefab |
| Beard25 | Trimmed | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard25.prefab |
| Beard26 | Handlebar | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard26.prefab |
| Beard3 | Short | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard3.prefab |
| Beard4 | Straight | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard4.prefab |
| Beard5 | Single Braid | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard5.prefab |
| Beard6 | Loose Braid | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard6.prefab |
| Beard7 | Split Shave | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard7.prefab |
| Beard8 | Thick | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard8.prefab |
| Beard9 | Trobadour | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/Beard9.prefab |
| BeardNone | No Beard | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/beards/BeardNone.prefab |
| bed | Bed | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/bed.prefab |
| bee_aoe | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/beehive/bee_aoe.prefab |
| Beech1 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Beech/Beech1.prefab |
| beech_log | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Beech/logs/beech_log.prefab |
| beech_log_half | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Beech/logs/beech_log_half.prefab |
| Beech_Sapling | Beech sapling | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Beech/Beech_Sapling.prefab |
| Beech_small1 | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/Beech/Beech_small1.prefab |
| Beech_small2 | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/Beech/Beech_small2.prefab |
| Beech_Stub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Beech/Beech_Stub.prefab |
| BeechSeeds | Beech Seeds | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BeechSeeds.prefab |
| Beehive | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/BeeHive/Beehive.prefab |
| Bell | Bell | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/Bell.prefab |
| BellFragment | Bell Fragment | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/BellFragment.prefab |
| BeltStrength | Megingjord | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/utility/BeltStrength.prefab |
| BigBranch | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StumpHut/BigBranch.prefab |
| BigRock | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Rocks/BigRock.prefab |
| Bilebag | Bilebag | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Bilebag.prefab |
| bilebomb_explosion | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/bilebomb_explosion.prefab |
| bilebomb_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/bilebomb_projectile.prefab |
| BiomeFoundMessage | — | UI/prefabs | 4 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/BiomeFoundMessage.prefab |
| Birch1 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Birch/Birch1.prefab |
| Birch1_aut | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Birch/Birch1_aut.prefab |
| Birch2 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Birch/Birch2.prefab |
| Birch2_aut | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Birch/Birch2_aut.prefab |
| Birch_log | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Birch/logs/Birch_log.prefab |
| Birch_log_half | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Birch/logs/Birch_log_half.prefab |
| Birch_Sapling | Birch Sapling | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Birch/Birch_Sapling.prefab |
| BirchSeeds | Birch Seeds | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BirchSeeds.prefab |
| BirchStub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Birch/BirchStub.prefab |
| Bjorn | Bear | Characters/Bjorn | 11 components; active: yes | c4210710 / Assets/Characters/Bjorn/Bjorn.prefab |
| bjorn_bite | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/bjorn_bite.prefab |
| bjorn_claws | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/bjorn_claws.prefab |
| Bjorn_ragdoll | — | Characters/Bjorn | 4 components; active: yes | c4210710 / Assets/Characters/Bjorn/Bjorn_ragdoll.prefab |
| bjorn_slam | slap | Characters/Bjorn | 3 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/bjorn_slam.prefab |
| Bjorn_sleeping | Bear | Characters/Bjorn | 11 components; active: yes | c4210710 / Assets/Characters/Bjorn/Bjorn_sleeping.prefab |
| Bjorn_spiritcaller | — | Characters/Bjorn | 11 components; active: yes | c4210710 / Assets/Characters/Bjorn/Bjorn_spiritcaller.prefab |
| bjorn_swipe_combo | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/bjorn_swipe_combo.prefab |
| bjorn_swipe_l | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/bjorn_swipe_l.prefab |
| bjorn_swipe_r | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/bjorn_swipe_r.prefab |
| BjornHide | Bear Hide | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BjornHide.prefab |
| BjornMeat | Bear Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BjornMeat.prefab |
| BjornPaw | Bear Paw | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BjornPaw.prefab |
| BlackCore | Black Core | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BlackCore.prefab |
| BlackForestLocationMusic | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/BlackForestLocationMusic.prefab |
| blackforge | Black Forge | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackforge.prefab |
| blackforge_ext1 | Black Forge Cooler | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackforge_ext1.prefab |
| blackforge_ext2_vise | Vice | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackforge_ext2_vise.prefab |
| blackforge_ext3_metalcutter | Metal Cutter | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackforge_ext3_metalcutter.prefab |
| blackforge_ext4_gemcutter | Gem Cutter | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackforge_ext4_gemcutter.prefab |
| blackforge_ext5_apron | Smith&#x27;s Aprons | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackforge_ext5_apron.prefab |
| BlackIce_Core | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/BlackIce/BlackIce_Core.prefab |
| BlackIce_Core_combined | — | world/Props | 2 components; active: yes | d59cfac / Assets/world/Props/DeepNorth/BlackIce/BlackIce_Core_combined.prefab |
| BlackIce_Core_outer | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/BlackIce/BlackIce_Core_outer.prefab |
| BlackIce_Start | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/BlackIce/BlackIce_Start.prefab |
| BlackIceShard_01 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/BlackIceShard_01.prefab |
| BlackIceShard_02 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/BlackIceShard_02.prefab |
| BlackMarble | Black Marble | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BlackMarble.prefab |
| blackmarble_1x1 | Black Marble 1x1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_1x1.prefab |
| blackmarble_2x1x1 | Black Marble 2x1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_2x1x1.prefab |
| blackmarble_2x2_enforced | Enforced Black Marble | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_2x2_enforced.prefab |
| blackmarble_2x2x1 | Black Marble 2x2x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_2x2x1.prefab |
| blackmarble_2x2x2 | Black Marble 2x2x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_2x2x2.prefab |
| blackmarble_altar_crystal | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_altar_crystal.prefab |
| blackmarble_altar_crystal_broken | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_altar_crystal_broken.prefab |
| blackmarble_arch | Black Marble Arch | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_arch.prefab |
| blackmarble_base_1 | Black Marble Plinth | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_base_1.prefab |
| blackmarble_base_2 | Black Marble Wide Plinth | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_base_2.prefab |
| blackmarble_basecorner | Black Marble Plinth Corner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_basecorner.prefab |
| blackmarble_column_1 | Black Marble Column Small | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_column_1.prefab |
| blackmarble_column_2 | Black Marble Column Wide | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_column_2.prefab |
| blackmarble_column_3 | Black Marble Column Tall | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_column_3.prefab |
| blackmarble_creep_4x1x1 | Black Marble 2x2x1 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/marblepieces_creep_boss_destructable/blackmarble_creep_4x1x1.prefab |
| blackmarble_creep_4x2x1 | Black Marble 2x2x1 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/marblepieces_creep_boss_destructable/blackmarble_creep_4x2x1.prefab |
| blackmarble_creep_slope_inverted_1x1x2 | Black Marble Cornice | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/marblepieces_creep_boss_destructable/blackmarble_creep_slope_inverted_1x1x2.prefab |
| blackmarble_creep_slope_inverted_2x2x1 | Black Marble Cornice | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/marblepieces_creep_boss_destructable/blackmarble_creep_slope_inverted_2x2x1.prefab |
| blackmarble_creep_stair | Black Marble Stair | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/marblepieces_creep_boss_destructable/blackmarble_creep_stair.prefab |
| blackmarble_floor | Black Marble Floor | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_floor.prefab |
| blackmarble_floor_large | Black Marble Floor 4x4 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_floor_large.prefab |
| blackmarble_floor_triangle | Black Marble Floor Triangle | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_floor_triangle.prefab |
| blackmarble_head01 | Bronze Head 1 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_head01.prefab |
| blackmarble_head02 | Bronze Head 2 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_head02.prefab |
| blackmarble_head_big01 | Black Marble Large Head 1 | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_head_big01.prefab |
| blackmarble_head_big02 | Black Marble Large Head 2 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_head_big02.prefab |
| blackmarble_out_1 | Black Marble Cornice | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_out_1.prefab |
| blackmarble_out_2 | Black Marble Cornice Wide | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_out_2.prefab |
| blackmarble_outcorner | Black Marble Cornice Corner | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_outcorner.prefab |
| blackmarble_pile | Black Marble Pile | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_pile.prefab |
| blackmarble_post01 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_post01.prefab |
| blackmarble_slope_1x2 | Black Marble Slope | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_slope_1x2.prefab |
| blackmarble_slope_inverted_1x2 | Black Marble Slope (Inverted) | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_slope_inverted_1x2.prefab |
| blackmarble_stair | Black Marble Stair | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_stair.prefab |
| blackmarble_stair_corner | Black Marble Stair Right | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_stair_corner.prefab |
| blackmarble_stair_corner_left | Black Marble Stair Left | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_stair_corner_left.prefab |
| blackmarble_tile_floor_1x1 | Black Marble Floor Tile Small | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_tile_floor_1x1.prefab |
| blackmarble_tile_floor_2x2 | Black Marble Floor Tile Large | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_tile_floor_2x2.prefab |
| blackmarble_tile_wall_1x1 | Black Marble Wall Tile Small | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_tile_wall_1x1.prefab |
| blackmarble_tile_wall_2x2 | Black Marble Wall Tile Large | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_tile_wall_2x2.prefab |
| blackmarble_tile_wall_2x4 | Black Marble Wall Tile Tall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackmarble_tile_wall_2x4.prefab |
| blackmarble_tip | Black Marble Quarter Spire | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/blackmarble_tip.prefab |
| BlackMetal | Black Metal | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BlackMetal.prefab |
| BlackMetalScrap | Black Metal Scrap | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BlackMetalScrap.prefab |
| BlackSoup | Black Soup | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BlackSoup.prefab |
| Blackwood | Ashwood | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Blackwood.prefab |
| blackwood_stack | Ashwood Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/blackwood_stack.prefab |
| blastfurnace | Blast Furnace | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/blastfurnace.prefab |
| Blob | Blob | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/Blob.prefab |
| blob_aoe | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/misc/old/blob_aoe.prefab |
| blob_attack_aoe | fart | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/misc/blob_attack_aoe.prefab |
| blob_frost_attack_aoe | fart | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/misc/blob_frost_attack_aoe.prefab |
| BlobAspect | Blob | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/BlobAspect.prefab |
| BlobElite | Oozer | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/BlobElite.prefab |
| blobelite_attack_aoe | fart | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/misc/blobelite_attack_aoe.prefab |
| BlobFrost | Frost Blob | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/BlobFrost.prefab |
| BlobLava | Lava Blob | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/BlobLava.prefab |
| blobLava_attack_aoe | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/misc/blobLava_attack_aoe.prefab |
| BlobLava_explosion | — | Characters/Blob | 4 components; active: yes | c4210710 / Assets/Characters/Blob/BlobLava_explosion.prefab |
| BlobMork | Shapeless Pulp | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/BlobMork.prefab |
| blobmork_attack_aoe | fart | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/misc/blobmork_attack_aoe.prefab |
| BlobMorkBig | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/BlobMorkBig.prefab |
| BlobMorkMini | Tiny Pulp | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/BlobMorkMini.prefab |
| BlobTar | Growth | Characters/Blob | 10 components; active: yes | c4210710 / Assets/Characters/Blob/BlobTar.prefab |
| blobtar_attack | fireballattack | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/misc/blobtar_attack.prefab |
| blobtar_projectile_tarball | — | Characters/Blob | 4 components; active: yes | c4210710 / Assets/Characters/Blob/misc/blobtar_projectile_tarball.prefab |
| BlobVial | Corked Vial | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/BlobVial.prefab |
| Bloodbag | Bloodbag | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Bloodbag.prefab |
| BloodGoldKey | Intricate Key | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/BloodGoldKey.prefab |
| BloodPudding | Blood Pudding | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BloodPudding.prefab |
| Blueberries | Blueberries | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Blueberries.prefab |
| BlueberryBush | Blueberries | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Bush01/BlueberryBush.prefab |
| Boar | Boar | Characters/Boar | 12 components; active: yes | c4210710 / Assets/Characters/Boar/Boar.prefab |
| boar_base_attack | boar attack1 | Characters/Boar | 3 components; active: yes | c4210710 / Assets/Characters/Boar/attacks/boar_base_attack.prefab |
| Boar_piggy | Piggy | Characters/Boar | 9 components; active: yes | c4210710 / Assets/Characters/Boar/Boar_piggy.prefab |
| boar_ragdoll | — | Characters/Boar | 4 components; active: yes | c4210710 / Assets/Characters/Boar/fx/boar_ragdoll.prefab |
| Boar_spiritcaller | — | Characters/Boar | 10 components; active: yes | c4210710 / Assets/Characters/Boar/Boar_spiritcaller.prefab |
| BoarJerky | Boar Jerky | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BoarJerky.prefab |
| BogWitch | — | Characters/BogWitch | 5 components; active: yes | c4210710 / Assets/Characters/BogWitch/BogWitch.prefab |
| BogWitch_Amulet | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Amulet.prefab |
| bogwitch_barrel | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/bogwitch_barrel.prefab |
| BogWitch_Camp | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Camp.prefab |
| BogWitch_Cauldron | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Cauldron.prefab |
| BogWitch_Fire_Pit | Campfire; Fire | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/BogWitchHut/BogWitch_Fire_Pit.prefab |
| BogWitch_Hut | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Hut.prefab |
| BogWitch_Ladder | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Ladder.prefab |
| BogWitch_Leech | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Leech.prefab |
| BogWitch_Stump1 | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Stump1.prefab |
| BogWitch_Stump2 | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Stump2.prefab |
| BogWitch_Table | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Table.prefab |
| BogWitch_Talisman1 | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Talisman1.prefab |
| BogWitch_Talisman2 | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Talisman2.prefab |
| BogWitch_Talisman3 | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Talisman3.prefab |
| BogWitch_Thistles | — | world/Props | 2 components; active: yes | 3e896e5d / Assets/world/Props/BogWitchHut/BogWitch_Thistles.prefab |
| BogWitchKvastur | Kvastur | Characters/Kvastur | 9 components; active: yes | c4210710 / Assets/Characters/Kvastur/BogWitchKvastur.prefab |
| BogWitchKvastur_attack | jaws | Characters/Kvastur | 3 components; active: yes | c4210710 / Assets/Characters/Kvastur/BogWitchKvastur_attack.prefab |
| BoltBlackmetal | Black Metal Bolt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BoltBlackmetal.prefab |
| BoltBloodGold | Bloodgold Bolt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BoltBloodGold.prefab |
| BoltBone | Bone Bolt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BoltBone.prefab |
| BoltCarapace | Carapace Bolt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BoltCarapace.prefab |
| BoltCharred | Charred Bolt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BoltCharred.prefab |
| BoltIron | Iron Bolt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BoltIron.prefab |
| bomb_lastboss_ice_explosion | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombDynamite/bomb_lastboss_ice_explosion.prefab |
| BombBile | Bile Bomb | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombBile.prefab |
| BombBlob_Frost | Blob Bomb: Frost | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombBlob_Frost.prefab |
| BombBlob_Frost_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/BombBlob_Frost_projectile.prefab |
| BombBlob_Lava | Blob Bomb: Lava | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombBlob_Lava.prefab |
| BombBlob_Lava_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/BombBlob_Lava_projectile.prefab |
| BombBlob_Morkhalla | Blob Bomb: Pulp | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombBlob_Morkhalla.prefab |
| BombBlob_Morkhalla_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/BombBlob_Morkhalla_projectile.prefab |
| BombBlob_Poison | Blob Bomb: Poison | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombBlob_Poison.prefab |
| BombBlob_Poison_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/BombBlob_Poison_projectile.prefab |
| BombBlob_PoisonElite | Blob Bomb: Elite Poison | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombBlob_PoisonElite.prefab |
| BombBlob_PoisonElite_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/BombBlob_PoisonElite_projectile.prefab |
| BombBlob_Tar | Blob Bomb: Tar | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombBlob_Tar.prefab |
| BombBlob_Tar_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/BombBlob_Tar_projectile.prefab |
| BombDynamite | Ember Charge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombDynamite.prefab |
| bombdynamite_explosion | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombDynamite/bombdynamite_explosion.prefab |
| bombdynamite_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombDynamite/bombdynamite_projectile.prefab |
| BombLava | Basalt Bomb | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombLava.prefab |
| BombOoze | Ooze Bomb | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombOoze.prefab |
| BombSiege | Explosive Payload | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombSiege.prefab |
| BombSmoke | Smoke Bomb | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BombSmoke.prefab |
| bone_stack | Bone Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/bone_stack.prefab |
| BoneFragments | Bone Fragments | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BoneFragments.prefab |
| Bonemass | Bonemass | Characters/Bonemass | 10 components; active: yes | c4210710 / Assets/Characters/Bonemass/Bonemass.prefab |
| Bonemass | — | world/Locations | 4 components; active: yes | cd230c7f / Assets/world/Locations/Swamp/Bonemass.prefab |
| bonemass_aoe | — | Characters/Bonemass | 4 components; active: yes | c4210710 / Assets/Characters/Bonemass/misc/bonemass_aoe.prefab |
| bonemass_attack_aoe | heal | Characters/Bonemass | 3 components; active: yes | c4210710 / Assets/Characters/Bonemass/misc/bonemass_attack_aoe.prefab |
| bonemass_attack_punch | slap | Characters/Bonemass | 3 components; active: yes | c4210710 / Assets/Characters/Bonemass/misc/bonemass_attack_punch.prefab |
| bonemass_attack_spawn | heal | Characters/Bonemass | 3 components; active: yes | c4210710 / Assets/Characters/Bonemass/misc/bonemass_attack_spawn.prefab |
| bonemass_attack_throw | slime throw | Characters/Bonemass | 3 components; active: yes | c4210710 / Assets/Characters/Bonemass/misc/bonemass_attack_throw.prefab |
| bonemass_spawn | — | Characters/Bonemass | 2 components; active: yes | c4210710 / Assets/Characters/Bonemass/misc/bonemass_spawn.prefab |
| bonemass_throw_projectile | — | Characters/Bonemass | 4 components; active: yes | c4210710 / Assets/Characters/Bonemass/misc/bonemass_throw_projectile.prefab |
| BonemawSerpent | Bonemaw | Characters/BonemawSerpent | 10 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/BonemawSerpent.prefab |
| BonemawSerpent_bite | Serpent bite | Characters/BonemawSerpent | 3 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/attacks/BonemawSerpent_bite.prefab |
| BonemawSerpent_breath | Fallen Valkyrie Poison Breath | Characters/BonemawSerpent | 3 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/attacks/BonemawSerpent_breath.prefab |
| BonemawSerpent_breath_aoe | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/attacks/BonemawSerpent_breath_aoe.prefab |
| BonemawSerpent_projectile | — | Characters/BonemawSerpent | 4 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/attacks/BonemawSerpent_projectile.prefab |
| BonemawSerpent_ram | Serpent bite | Characters/BonemawSerpent | 3 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/attacks/BonemawSerpent_ram.prefab |
| BonemawSerpent_spit | bonemaw spit | Characters/BonemawSerpent | 3 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/attacks/BonemawSerpent_spit.prefab |
| BonemawSerpent_taunt | Serpent Taunt | Characters/BonemawSerpent | 3 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/attacks/BonemawSerpent_taunt.prefab |
| BoneMawSerpentMeat | Bonemaw Meat | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BoneMawSerpentMeat.prefab |
| BonemawSerpentScale | Bonemaw Scale | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BonemawSerpentScale.prefab |
| BonemawSerpentTooth | Bonemaw Tooth | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BonemawSerpentTooth.prefab |
| BonePileSpawner | — | Characters/Skeleton | 6 components; active: yes | c4210710 / Assets/Characters/Skeleton/BonePileSpawner.prefab |
| BonePileSpawner_swamp | — | Characters/Skeleton | 6 components; active: yes | c4210710 / Assets/Characters/Skeleton/BonePileSpawner_swamp.prefab |
| bonfire | Bonfire; Fire | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/bonfire.prefab |
| BossStone_Bonemass | Sacrificial Stone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/BossStone_Bonemass.prefab |
| BossStone_DragonQueen | Sacrificial Stone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/BossStone_DragonQueen.prefab |
| BossStone_Eikthyr | Sacrificial Stone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/BossStone_Eikthyr.prefab |
| BossStone_Fader | Sacrificial Stone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/BossStone_Fader.prefab |
| BossStone_TheElder | Sacrificial Stone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/BossStone_TheElder.prefab |
| BossStone_TheQueen | Sacrificial Stone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/BossStone_TheQueen.prefab |
| BossStone_Yagluth | Sacrificial Stone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/BossStone_Yagluth.prefab |
| Bow | Crude Bow | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Bow.prefab |
| bow_projectile | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile.prefab |
| bow_projectile_bloodgold | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_bloodgold.prefab |
| bow_projectile_bronze | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_bronze.prefab |
| bow_projectile_carapace | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_carapace.prefab |
| bow_projectile_charred | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_charred.prefab |
| bow_projectile_fire | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_fire.prefab |
| bow_projectile_flint | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_flint.prefab |
| bow_projectile_frost | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_frost.prefab |
| bow_projectile_iron | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_iron.prefab |
| bow_projectile_needle | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_needle.prefab |
| bow_projectile_obsidian | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_obsidian.prefab |
| bow_projectile_poison | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_poison.prefab |
| bow_projectile_silver | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/bow_projectile_silver.prefab |
| BowAshlands | Ash Fang | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowAshlands.prefab |
| BowAshlandsBlood | Blood Fang | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowAshlandsBlood.prefab |
| BowAshlandsRoot | Root Fang | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowAshlandsRoot.prefab |
| BowAshlandsStorm | Storm Fang | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowAshlandsStorm.prefab |
| BowDraugrFang | Draugr Fang | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowDraugrFang.prefab |
| BowFineWood | Finewood Bow | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowFineWood.prefab |
| BowGold | Nord Bow | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowGold.prefab |
| BowGold_BloodLightning | Thunderblood Bow | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowGold_BloodLightning.prefab |
| BowGold_FrostFire | Frostfire Bow | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowGold_FrostFire.prefab |
| BowGoldUncooked | Cast: Nord Bow | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowGoldUncooked.prefab |
| BowHuntsman | Huntsman Bow | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowHuntsman.prefab |
| BowSpineSnap | Spinesnap | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/BowSpineSnap.prefab |
| Bread | Bread | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Bread.prefab |
| BreadDough | Bread Dough | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BreadDough.prefab |
| Bronze | Bronze | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Bronze.prefab |
| BronzeNails | Bronze Nails | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BronzeNails.prefab |
| BronzeScrap | Scrap Bronze | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/BronzeScrap.prefab |
| bronzespear_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BronzeSpear/bronzespear_projectile.prefab |
| bucket | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/bucket.prefab |
| BugMeat | Seeker Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/BugMeat.prefab |
| BuildPieceSelectButton | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/BuildUI/BuildPieceSelectButton.prefab |
| BuildUITagButton | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/BuildUI/BuildUITagButton.prefab |
| BuildUIV2 | — | UI/prefabs | 4 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/BuildUI/BuildUIV2.prefab |
| burn | Cultivate | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/burn.prefab |
| Bush01 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Bush01/Bush01.prefab |
| Bush01_deepnorth | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Bush01/Bush01_deepnorth.prefab |
| Bush01_heath | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Bush01/Bush01_heath.prefab |
| Bush02_en | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Bush01/Bush02_en.prefab |
| ButtonBinding | — | UI/prefabs | 2 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/ButtonBinding.prefab |
| Candle_resin | Resin Candle | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Candle_resin.prefab |
| Candle_resin_bogwitch | Resin Candle | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/Candle_resin_bogwitch.prefab |
| CandleWick | Candle Wick | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CandleWick.prefab |
| CapeAsh | Ashen Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeAsh.prefab |
| CapeAsksvin | Asksvin Cloak | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeAsksvin.prefab |
| CapeDeepNorth | Moose Hide Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeDeepNorth.prefab |
| CapeDeepNorthMage | Cape of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeDeepNorthMage.prefab |
| CapeDeerHide | Deer Hide Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeDeerHide.prefab |
| CapeFeather | Feather Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeFeather.prefab |
| CapeLinen | Linen Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeLinen.prefab |
| CapeLox | Lox Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeLox.prefab |
| CapeOdin | Cape of Oden | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeOdin.prefab |
| CapeTest | CAPE TEST | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeTest.prefab |
| CapeTrollHide | Troll Hide Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeTrollHide.prefab |
| CapeWolf | Wolf Fur Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/CapeWolf.prefab |
| Captions_DirectionIndicators | — | UI/prefabs | 2 components; active: yes | d59cfac / Assets/UI/prefabs/Captions_DirectionIndicators.prefab |
| Carapace | Carapace | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Carapace.prefab |
| CargoCrate | Cargo | GameElements/Ships | 8 components; active: yes | c4210710 / Assets/GameElements/Ships/CargoCrate.prefab |
| Carrot | Carrot | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Carrot.prefab |
| CarrotSeeds | Carrot Seeds | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CarrotSeeds.prefab |
| CarrotSoup | Carrot Soup | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CarrotSoup.prefab |
| Cart | Cart | GameElements/Cart | 12 components; active: yes | c4210710 / Assets/GameElements/Cart/Cart.prefab |
| CastleKit_braided_box01 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/CastleKit_braided_box01.prefab |
| CastleKit_brazier | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/CastleKit_brazier.prefab |
| CastleKit_decal_clawmarks | — | world/Props | 5 components; active: yes | 81cff51 / Assets/world/Props/Caverocks/CastleKit_decal_clawmarks.prefab |
| CastleKit_decal_dirt | — | world/Props | 4 components; active: yes | b8e0b1f0 / Assets/world/Props/CastleBuildingKit/CastleKit_decal_dirt.prefab |
| CastleKit_decal_fenrir_blood | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/CastleKit_decal_fenrir_blood.prefab |
| CastleKit_decal_straw | — | world/Props | 5 components; active: yes | 86715016 / Assets/world/Props/CastleBuildingKit/CastleKit_decal_straw.prefab |
| CastleKit_groundtorch | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/CastleKit_groundtorch.prefab |
| CastleKit_groundtorch_blue | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/CastleKit_groundtorch_blue.prefab |
| CastleKit_groundtorch_green | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/CastleKit_groundtorch_green.prefab |
| CastleKit_groundtorch_unlit | Standing Wood Torch | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/CastleKit_groundtorch_unlit.prefab |
| CastleKit_metal_groundtorch_unlit | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Caverocks/CastleKit_metal_groundtorch_unlit.prefab |
| CastleKit_pot03 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/CastleKit_pot03.prefab |
| Catapult | Catapult | GameElements/Cart | 13 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult.prefab |
| Catapult_ammo | Grausten Payload | GameElements/Cart | 7 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult_ammo.prefab |
| Catapult_Ammo_BloodGold | Bloodgold Payload | GameElements/Cart | 7 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult_Ammo_BloodGold.prefab |
| Catapult_Ammo_BloodGold_Projectile | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult_Ammo_BloodGold_Projectile.prefab |
| Catapult_Ammo_BloodGold_Projectile_AOE | — | GameElements/Cart | 3 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult_Ammo_BloodGold_Projectile_AOE.prefab |
| Catapult_Ammo_Projectile | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult_Ammo_Projectile.prefab |
| Catapult_Ammo_Projectile_AOE | — | GameElements/Cart | 3 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult_Ammo_Projectile_AOE.prefab |
| Catapult_projectile | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult_projectile.prefab |
| cauldron_ext1_spice | Spice Rack | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/cauldron_ext1_spice.prefab |
| cauldron_ext3_butchertable | Butcher&#x27;s Table | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/cauldron_ext3_butchertable.prefab |
| cauldron_ext4_pots | Pots and Pans | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/cauldron_ext4_pots.prefab |
| cauldron_ext5_mortarandpestle | Mortar and Pestle | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/cauldron_ext5_mortarandpestle.prefab |
| cauldron_ext6_rollingpins | Rolling Pins and Cutting Boards | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/cauldron_ext6_rollingpins.prefab |
| cauldron_ext7_smoker | Smoker | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/cauldron_ext7_smoker.prefab |
| cave_dome_bottom_lake | — | world/Rooms | 2 components; active: yes | dfbc4c92 / Assets/world/Rooms/cave/cave_dome_bottom_lake.prefab |
| caverock_cornerwall | — | world/Props | 4 components; active: yes | 972cbe15 / Assets/world/Props/Caverocks/caverock_cornerwall.prefab |
| caverock_curvedrock | — | world/Props | 3 components; active: yes | 46faf1c / Assets/world/Props/Caverocks/caverock_curvedrock.prefab |
| caverock_curvedrock | — | world/Props | 2 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/caverock_curvedrock.prefab |
| caverock_curvedwallbig | — | world/Props | 3 components; active: yes | 56e56554 / Assets/world/Props/Caverocks/caverock_curvedwallbig.prefab |
| caverock_curvedwallbig_extra | — | world/Props | 3 components; active: yes | a8945b7c / Assets/world/Props/Caverocks/caverock_curvedwallbig_extra.prefab |
| caverock_floorbig | — | world/Props | 3 components; active: yes | c126c945 / Assets/world/Props/Caverocks/caverock_floorbig.prefab |
| caverock_floorsmall | — | world/Props | 3 components; active: yes | 47d0845d / Assets/world/Props/Caverocks/caverock_floorsmall.prefab |
| caverock_floorsmall | — | world/Props | 2 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/caverock_floorsmall.prefab |
| caverock_flowstone | — | world/Props | 2 components; active: yes | 4f83a87c / Assets/world/Props/Caverocks/caverock_flowstone.prefab |
| caverock_ice_pillar_wall | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_pillar_wall.prefab |
| caverock_ice_stalagmite | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_stalagmite.prefab |
| caverock_ice_stalagmite_broken | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_stalagmite_broken.prefab |
| caverock_ice_stalagmite_destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_stalagmite_destruction.prefab |
| caverock_ice_stalagtite | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_stalagtite.prefab |
| caverock_ice_stalagtite_destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_stalagtite_destruction.prefab |
| caverock_ice_stalagtite_falling | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_stalagtite_falling.prefab |
| caverock_ice_wall_destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/caverock_ice_wall_destruction.prefab |
| caverock_pillar | — | world/Props | 3 components; active: yes | 59dd5f98 / Assets/world/Props/Caverocks/caverock_pillar.prefab |
| caverock_pillar | — | world/Props | 2 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/caverock_pillar.prefab |
| caverock_ramp | — | world/Props | 2 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/caverock_ramp.prefab |
| caverock_rockbun | — | world/Props | 3 components; active: yes | 533b16e1 / Assets/world/Props/Caverocks/caverock_rockbun.prefab |
| caverock_stairs | — | world/Props | 3 components; active: yes | 9a66ea63 / Assets/world/Props/Caverocks/caverock_stairs.prefab |
| caverock_stairs | — | world/Props | 2 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/caverock_stairs.prefab |
| caverock_stalagmite | — | world/Props | 2 components; active: yes | 4f83a87c / Assets/world/Props/Caverocks/caverock_stalagmite.prefab |
| caverock_stalagtite | — | world/Props | 2 components; active: yes | 4f83a87c / Assets/world/Props/Caverocks/caverock_stalagtite.prefab |
| CC Entry | — | UI/prefabs | 4 components; active: yes | d59cfac / Assets/UI/prefabs/CC Entry.prefab |
| CelestialFeather | Celestial Feather | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CelestialFeather.prefab |
| CeramicPlate | Ceramic Plate | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CeramicPlate.prefab |
| Chain | Chain | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Chain.prefab |
| ChainLightning | Lightning | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/ChainLightning/ChainLightning.prefab |
| ChainLightningRed | Lightning | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/ChainLightning/ChainLightningRed.prefab |
| charcoal_kiln | Charcoal Kiln | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/charcoal_kiln.prefab |
| CharcoalResin | Charcoal Resin | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CharcoalResin.prefab |
| Charred_altar_bellfragment | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/Charred_altar_bellfragment.prefab |
| Charred_Archer | Charred Marksman | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Archer.prefab |
| Charred_Archer_Fader | Summoned Charred Warrior | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Archer_Fader.prefab |
| charred_bow | Bow | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow.prefab |
| charred_bow_Fader | Bow | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow_Fader.prefab |
| charred_bow_Fader_projectile | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow_Fader_projectile.prefab |
| charred_bow_projectile | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow_projectile.prefab |
| charred_bow_volley | Bow | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow_volley.prefab |
| charred_bow_volley_Fader | Bow | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow_volley_Fader.prefab |
| charred_bow_volley_Fader_projectile | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow_volley_Fader_projectile.prefab |
| charred_bow_volley_projectile | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_bow_volley_projectile.prefab |
| Charred_Breastplate | Iron plate armor | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Armor/Charred_Breastplate.prefab |
| charred_dyrnwyn_greatsword_feint | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_dyrnwyn_greatsword_feint.prefab |
| charred_dyrnwyn_greatsword_swing | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_dyrnwyn_greatsword_swing.prefab |
| charred_dyrnwyn_greatsword_thrust | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_dyrnwyn_greatsword_thrust.prefab |
| charred_dyrnwyn_greatsword_thrustfeint | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_dyrnwyn_greatsword_thrustfeint.prefab |
| charred_fader_greatsword_feint | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_fader_greatsword_feint.prefab |
| charred_fader_greatsword_swing | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_fader_greatsword_swing.prefab |
| charred_fader_greatsword_thrust | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_fader_greatsword_thrust.prefab |
| charred_fader_greatsword_thrustfeint | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_fader_greatsword_thrustfeint.prefab |
| charred_fireball_aoe | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_fireball_aoe.prefab |
| charred_fireball_projectile | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_fireball_projectile.prefab |
| charred_greatsword_feint | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_greatsword_feint.prefab |
| charred_greatsword_swing | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_greatsword_swing.prefab |
| charred_greatsword_thrust | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_greatsword_thrust.prefab |
| charred_greatsword_thrustfeint | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_greatsword_thrustfeint.prefab |
| Charred_Helmet | Iron plate armor | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Armor/Charred_Helmet.prefab |
| Charred_HipCloth | Iron plate armor | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Armor/Charred_HipCloth.prefab |
| Charred_Mage | Charred Warlock | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Mage.prefab |
| Charred_MageCloths | Iron plate armor | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Armor/Charred_MageCloths.prefab |
| charred_magestaff_fire | Bow | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_magestaff_fire.prefab |
| charred_magestaff_summon | Bow | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_magestaff_summon.prefab |
| charred_magestaff_summoncharred | — | Characters/TheCharred | 2 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_magestaff_summoncharred.prefab |
| Charred_Melee | Charred Warrior | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Melee.prefab |
| Charred_Melee_Dyrnwyn | &lt;color=orange&gt;Lord Reto&lt;/color&gt; | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Melee_Dyrnwyn.prefab |
| Charred_Melee_Fader | Summoned Charred Warrior | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Melee_Fader.prefab |
| Charred_Melee_Ragdoll | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/effects/Charred_Melee_Ragdoll.prefab |
| charred_shieldgenerator | Shield Generator | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/charred_shieldgenerator.prefab |
| Charred_Twitcher | Charred Twitcher | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Twitcher.prefab |
| charred_twitcher_projectile | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_twitcher_projectile.prefab |
| charred_twitcher_scratch_l | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_twitcher_scratch_l.prefab |
| charred_twitcher_scratch_r | Charred Sword | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_twitcher_scratch_r.prefab |
| Charred_Twitcher_Summoned | Summoned Twitcher | Characters/TheCharred | 11 components; active: yes | c4210710 / Assets/Characters/TheCharred/Charred_Twitcher_Summoned.prefab |
| charred_twitcher_throw | Bow | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Weapons/charred_twitcher_throw.prefab |
| CharredBanner1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CharredBanners/CharredBanner1.prefab |
| CharredBanner2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CharredBanners/CharredBanner2.prefab |
| CharredBanner3 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CharredBanners/CharredBanner3.prefab |
| CharredBone | Charred Bone | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CharredBone.prefab |
| CharredCogwheel | Charred Cogwheel | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CharredCogwheel.prefab |
| CharredFortress | — | world/Locations | 2 components; active: yes | b51de604 / Assets/world/Locations/Ashlands/CharredFortress.prefab |
| Charredfortress_LOD | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/Charredfortress_LOD.prefab |
| Charredskull | Charred Skull | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Charredskull.prefab |
| Chest | Container | 3rd party/A_piece_of_nature | 6 components; active: yes | c4210710 / Assets/3rd party/A_piece_of_nature/Chest.prefab |
| chest_hildir1 | Hildir&#x27;s Brass Chest | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/chest_hildir1.prefab |
| chest_hildir1_incamp | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/chest_hildir1_incamp.prefab |
| chest_hildir2 | Hildir&#x27;s Silver Chest | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/chest_hildir2.prefab |
| chest_hildir2_incamp | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/chest_hildir2_incamp.prefab |
| chest_hildir3 | Hildir&#x27;s Bronze Chest | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/chest_hildir3.prefab |
| chest_hildir3_incamp | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/chest_hildir3_incamp.prefab |
| Chicken | Chicken | Characters/Chicken | 10 components; active: yes | c4210710 / Assets/Characters/Chicken/Chicken.prefab |
| ChickenEgg | Egg | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ChickenEgg.prefab |
| ChickenMeat | Chicken Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ChickenMeat.prefab |
| Chitin | Chitin | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Chitin.prefab |
| Cinder | — | world/SmokeFire | 6 components; active: yes | c4210710 / Assets/world/SmokeFire/Cinder.prefab |
| Cinder_campfire | — | world/SmokeFire | 6 components; active: yes | c4210710 / Assets/world/SmokeFire/Cinder_campfire.prefab |
| CinderSky | — | world/SmokeFire | 6 components; active: yes | c4210710 / Assets/world/SmokeFire/CinderSky.prefab |
| CinderStorm | — | world/SmokeFire | 6 components; active: yes | c4210710 / Assets/world/SmokeFire/CinderStorm.prefab |
| CinematicsManager | — | Systems | 4 components; active: yes | c4210710 / Assets/Systems/CinematicsManager.prefab |
| Circle_section | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/station_marker/Circle_section.prefab |
| cliff_ashlands1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_ashlands1.prefab |
| cliff_ashlands1_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_ashlands1_frac.prefab |
| cliff_ashlands2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_ashlands2.prefab |
| cliff_ashlands2_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_ashlands2_frac.prefab |
| cliff_ashlands3_Arch_1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_ashlands3_Arch_1.prefab |
| cliff_ashlands4 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands4.prefab |
| cliff_ashlands4_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands4_frac.prefab |
| cliff_ashlands5 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands5.prefab |
| cliff_ashlands6 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands6.prefab |
| cliff_ashlands6_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands6_frac.prefab |
| cliff_ashlands7_HalfArch | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands7_HalfArch.prefab |
| cliff_ashlands7_HalfArch_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands7_HalfArch_frac.prefab |
| cliff_ashlands8 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands8.prefab |
| cliff_ashlands_Arch_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlands_Arch_frac.prefab |
| cliff_ashlandsflowrock_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/cliff_ashlandsflowrock_frac.prefab |
| cliff_mistlands1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_mistlands1.prefab |
| cliff_mistlands1_creep | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_mistlands1_creep.prefab |
| cliff_mistlands1_creep_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_mistlands1_creep_frac.prefab |
| cliff_mistlands1_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_mistlands1_frac.prefab |
| cliff_mistlands2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_mistlands2.prefab |
| cliff_mistlands2_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/cliff_mistlands2_frac.prefab |
| ClosedCaptions | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/ClosedCaptions.prefab |
| cloth_hanging_door | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/cloth_hanging_door.prefab |
| cloth_hanging_door_double | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/cloth_hanging_door_double.prefab |
| cloth_hanging_long | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/cloth_hanging_long.prefab |
| Cloudberry | Cloudberries | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Cloudberry.prefab |
| CloudberryBush | Cloudberries | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/CloudberryBush/CloudberryBush.prefab |
| CloudStorageWarningPopup | — | UI/prefabs | 3 components; active: no | c4210710 / Assets/UI/prefabs/CloudStorageWarningPopup.prefab |
| Club | Club | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Club.prefab |
| clutter_shrub_large | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/old/clutter_shrub_large.prefab |
| Coal | Coal | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Coal.prefab |
| coal_pile | Coal Pile | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/coal_pile.prefab |
| Coins | Coins | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/Coins.prefab |
| Connection | — | world/dungeon | 2 components; active: yes | 4099323b / Assets/world/dungeon/Misc/Connection.prefab |
| Connection_Entrance | — | world/dungeon | 2 components; active: yes | 25493c19 / Assets/world/dungeon/Misc/Connection_Entrance.prefab |
| CookedAsksvinMeat | Cooked Asksvin Tail | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedAsksvinMeat.prefab |
| CookedBjornMeat | Cooked Bear Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedBjornMeat.prefab |
| CookedBoneMawSerpentMeat | Cooked Bonemaw Meat | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedBoneMawSerpentMeat.prefab |
| CookedBugMeat | Cooked Seeker Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedBugMeat.prefab |
| CookedChickenMeat | Cooked Chicken Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedChickenMeat.prefab |
| CookedDeerMeat | Cooked Deer Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedDeerMeat.prefab |
| CookedEgg | Cooked Egg | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedEgg.prefab |
| CookedHareMeat | Cooked Hare Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedHareMeat.prefab |
| CookedLoxMeat | Cooked Lox Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedLoxMeat.prefab |
| CookedMeat | Cooked Boar Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedMeat.prefab |
| CookedMooseMeat | Cooked Moose Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedMooseMeat.prefab |
| CookedSealBlubber | Cooked Seal Blubber | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedSealBlubber.prefab |
| CookedVoltureMeat | Cooked Volture Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedVoltureMeat.prefab |
| CookedWolfMeat | Cooked Wolf Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/CookedWolfMeat.prefab |
| Copper | Copper | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Copper.prefab |
| CopperOre | Copper Ore | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CopperOre.prefab |
| CopperScrap | Copper Scrap | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CopperScrap.prefab |
| CreepProp_drops | — | world/Props | 3 components; active: yes | 32899a32 / Assets/world/Props/Dvergr/CreepProp_drops.prefab |
| CreepProp_egg_hanging01 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/CreepProp_egg_hanging01.prefab |
| CreepProp_egg_hanging02 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/CreepProp_egg_hanging02.prefab |
| CreepProp_entrance1 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/CreepProp_entrance1.prefab |
| CreepProp_entrance2 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/CreepProp_entrance2.prefab |
| CreepProp_FloorCover01 | — | world/Props | 2 components; active: yes | 9329ce20 / Assets/world/Props/Dvergr/CreepProp_FloorCover01.prefab |
| CreepProp_hanging01 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/CreepProp_hanging01.prefab |
| CreepProp_pillar01 | — | world/Props | 2 components; active: yes | dab1039c / Assets/world/Props/Dvergr/CreepProp_pillar01.prefab |
| CreepProp_pillarhalf01 | — | world/Props | 2 components; active: yes | 71eb4fba / Assets/world/Props/Dvergr/CreepProp_pillarhalf01.prefab |
| CreepProp_pillarhalf02 | — | world/Props | 2 components; active: yes | 721410fe / Assets/world/Props/Dvergr/CreepProp_pillarhalf02.prefab |
| CreepProp_wall01 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/CreepProp_wall01.prefab |
| CrossbowArbalest | Arbalest | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowArbalest.prefab |
| CrossbowGold | Nord Crossbow | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowGold.prefab |
| CrossbowGold_BloodLightning | Thunderblood Crossbow | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowGold_BloodLightning.prefab |
| CrossbowGold_FrostFire | Frostfire Crossbow | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowGold_FrostFire.prefab |
| CrossbowGoldUncooked | Cast: Nord Crossbow | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowGoldUncooked.prefab |
| CrossbowRipper | Ripper | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowRipper.prefab |
| CrossbowRipperBlood | Wound Ripper | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowRipperBlood.prefab |
| CrossbowRipperLightning | Storm Ripper | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowRipperLightning.prefab |
| CrossbowRipperNature | Root Ripper | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/CrossbowRipperNature.prefab |
| Crow | — | Characters/animals | 9 components; active: yes | c4210710 / Assets/Characters/animals/birds/Crow.prefab |
| CrownJewel | Crown Jewel | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CrownJewel.prefab |
| crypt_hangingchain | — | world/dungeon | 4 components; active: yes | 297ec008 / Assets/world/dungeon/Crypt/crypt_hangingchain.prefab |
| crypt_hangingskeleton | — | world/dungeon | 4 components; active: yes | f88b6302 / Assets/world/dungeon/Crypt/crypt_hangingskeleton.prefab |
| crypt_rock | — | world/dungeon | 6 components; active: yes | 8aa1d8f2 / Assets/world/dungeon/Crypt/crypt_rock.prefab |
| crypt_skeleton_chest | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Chests/crypt_skeleton_chest.prefab |
| crypt_skeleton_laying | — | world/dungeon | 4 components; active: yes | dfbc4c92 / Assets/world/dungeon/Crypt/crypt_skeleton_laying.prefab |
| CryptKey | Swamp Key | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/CryptKey.prefab |
| Crystal | Crystal | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Crystal.prefab |
| crystal_wall_1x1 | Crystal Wall 1x1 | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/crystal_wall_1x1.prefab |
| cultivate | Cultivate | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/cultivate.prefab |
| cultivate_v2 | Cultivate | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/cultivate_v2.prefab |
| Cultivator | Cultivator | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/tools/Cultivator.prefab |
| CuredSquirrelHamstring | Cured Squirrel Hamstring | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/CuredSquirrelHamstring.prefab |
| DamageText | — | UI/prefabs | 5 components; active: no | d59cfac / Assets/UI/prefabs/IngameGui/DamageText.prefab |
| Dandelion | Dandelion | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Dandelion.prefab |
| darkwood_arch | Darkwood Arch | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_arch.prefab |
| darkwood_beam | Darkwood Beam 2 m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_beam.prefab |
| darkwood_beam4x4 | Darkwood Beam 4 m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_beam4x4.prefab |
| darkwood_beam_26 | Darkwood Beam 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_beam_26.prefab |
| darkwood_beam_45 | Darkwood Beam 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_beam_45.prefab |
| darkwood_beam_67 | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_beam_67.prefab |
| darkwood_decowall | Carved Darkwood Divider | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_decowall.prefab |
| darkwood_gate | Darkwood Gate | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_gate.prefab |
| darkwood_pole | Darkwood Pole 2m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_pole.prefab |
| darkwood_pole4 | Darkwood Pole 4m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_pole4.prefab |
| darkwood_raven | Raven Adornment | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_raven.prefab |
| darkwood_roof | Shingle Roof 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof.prefab |
| darkwood_roof_45 | Shingle Roof 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_45.prefab |
| darkwood_roof_67 | Shingle Roof 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_67.prefab |
| darkwood_roof_icorner | Shingle Roof Inner Corner 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_icorner.prefab |
| darkwood_roof_icorner_45 | Shingle Roof Inner Corner 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_icorner_45.prefab |
| darkwood_roof_icorner_67 | Shingle Roof Inner Corner 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_icorner_67.prefab |
| darkwood_roof_ocorner | Shingle Roof Outer Corner 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_ocorner.prefab |
| darkwood_roof_ocorner_45 | Shingle Roof Outer Corner 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_ocorner_45.prefab |
| darkwood_roof_ocorner_67 | Shingle Roof Outer Corner 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_ocorner_67.prefab |
| darkwood_roof_top | Shingle Roof Ridge 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_top.prefab |
| darkwood_roof_top_45 | Shingle Roof Ridge 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_top_45.prefab |
| darkwood_roof_top_67 | Shingle Roof Ridge 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_roof_top_67.prefab |
| darkwood_wolf | Wolf Adornment | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/darkwood_wolf.prefab |
| dead_deer | — | Characters/Deer | 4 components; active: yes | c4210710 / Assets/Characters/Deer/fx/dead_deer.prefab |
| DeadSpeak_Base | — | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/_res/DeadSpeak_Base.prefab |
| Deathsquito | Deathsquito | Characters/Deathsquito | 9 components; active: yes | c4210710 / Assets/Characters/Deathsquito/Deathsquito.prefab |
| Deathsquito_sting | Wraith melee | Characters/Deathsquito | 5 components; active: yes | c4210710 / Assets/Characters/Deathsquito/attacks/Deathsquito_sting.prefab |
| deepnorth_lantern_standing | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/deepnorth_lantern_standing.prefab |
| Deer | Deer | Characters/Deer | 10 components; active: yes | c4210710 / Assets/Characters/Deer/Deer.prefab |
| deer_ragdoll | — | Characters/Deer | 4 components; active: yes | c4210710 / Assets/Characters/Deer/fx/deer_ragdoll.prefab |
| Deer_White | — | Characters/Deer | 10 components; active: yes | c4210710 / Assets/Characters/Deer/Deer_White.prefab |
| DeerGodExplosion | — | Characters/Deer | 3 components; active: yes | c4210710 / Assets/Characters/Deer/misc/DeerGodExplosion.prefab |
| DeerHide | Deer Hide | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/DeerHide.prefab |
| DeerMeat | Deer Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/DeerMeat.prefab |
| DeerStew | Deer Stew | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/DeerStew.prefab |
| Demister | Wisplight | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/utility/Demister.prefab |
| demister_ball | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/demister/demister_ball.prefab |
| DG_AshlandRuins | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_AshlandRuins.prefab |
| DG_Cave | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_Cave.prefab |
| DG_DvergrBoss | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_DvergrBoss.prefab |
| DG_DvergrTown | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_DvergrTown.prefab |
| DG_ForestCrypt | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_ForestCrypt.prefab |
| DG_FortressRuins | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_FortressRuins.prefab |
| DG_GoblinCamp | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_GoblinCamp.prefab |
| DG_HalfBurried_ForestCrypt | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_HalfBurried_ForestCrypt.prefab |
| DG_Hildir_Cave | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_Hildir_Cave.prefab |
| DG_Hildir_ForestCrypt | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/DG_Hildir_ForestCrypt.prefab |
| DG_Hildir_PlainsFortress | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_Hildir_PlainsFortress.prefab |
| DG_Hole | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_Hole.prefab |
| DG_MeadowsFarm | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_MeadowsFarm.prefab |
| DG_MeadowsVillage | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_MeadowsVillage.prefab |
| DG_MorkHalla | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_MorkHalla.prefab |
| DG_NorthVillage | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_NorthVillage.prefab |
| DG_SunkenCrypt | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/DG_SunkenCrypt.prefab |
| digg | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/digg.prefab |
| digg_blobLavaExplosion | — | Characters/Blob | 2 components; active: yes | c4210710 / Assets/Characters/Blob/digg_blobLavaExplosion.prefab |
| digg_bombdynamite | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/digg_bombdynamite.prefab |
| digg_siegebomb | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/digg_siegebomb.prefab |
| digg_UnstableLavaRock | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/digg_UnstableLavaRock.prefab |
| digg_v2 | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/digg_v2.prefab |
| digg_v3 | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/digg_v3.prefab |
| dirtfloor | — | world/Props | 2 components; active: yes | 61c47e63 / Assets/world/Props/DirtWalls/dirtfloor.prefab |
| dirtfloorflat | — | world/Props | 2 components; active: yes | 678f4045 / Assets/world/Props/DirtWalls/dirtfloorflat.prefab |
| dirtwall | — | world/Props | 1 components; active: yes | 75196655 / Assets/world/Props/DirtWalls/dirtwall.prefab |
| DN_Bossroom | — | world/Locations | 2 components; active: yes | e06fccc7 / Assets/world/Locations/DeepNorth/DN_Bossroom.prefab |
| drag_item | — | UI/prefabs | 1 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/drag_item.prefab |
| Dragon | Moder | Characters/Dragon | 10 components; active: yes | c4210710 / Assets/Characters/Dragon/Dragon.prefab |
| dragon_bite | Dragon claw left | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/dragon_bite.prefab |
| dragon_claw_left | Dragon claw left | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/dragon_claw_left.prefab |
| dragon_claw_right | Dragon claw left | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/dragon_claw_right.prefab |
| dragon_coldbreath | dragon breath | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/dragon_coldbreath.prefab |
| dragon_coldbreath_OLD | dragon breath | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/dragon_coldbreath_OLD.prefab |
| dragon_ice_projectile | — | Characters/Dragon | 4 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/misc/dragon_ice_projectile.prefab |
| dragon_spit_shotgun | cold ball | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/dragon_spit_shotgun.prefab |
| dragon_taunt | scream | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/dragon_taunt.prefab |
| DragonEgg | Dragon Egg | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/DragonEgg.prefab |
| dragoneggcup | Offering Bowl | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/offeraltar/dragoneggcup.prefab |
| Dragonqueen | — | world/Locations | 4 components; active: yes | fac4ecb7 / Assets/world/Locations/Mountains/Dragonqueen.prefab |
| DragonTear | Dragon Tear | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/DragonTear.prefab |
| DrakeLorestone | — | world/Locations | 2 components; active: yes | d9afdb37 / Assets/world/Locations/Mountains/DrakeLorestone.prefab |
| DrakeNest01 | — | world/Locations | 2 components; active: yes | 86c8ff36 / Assets/world/Locations/Mountains/DrakeNest01.prefab |
| Draugr | Draugr | Characters/Draugr | 11 components; active: yes | c4210710 / Assets/Characters/Draugr/Draugr.prefab |
| draugr_arrow | Ironhead arrow | Characters/Draugr | 7 components; active: yes | c4210710 / Assets/Characters/Draugr/weapons/draugr_arrow.prefab |
| draugr_axe | Dragur axe | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/weapons/draugr_axe.prefab |
| draugr_bow | Bow | Characters/Draugr | 7 components; active: yes | c4210710 / Assets/Characters/Draugr/weapons/draugr_bow.prefab |
| draugr_bow_projectile | — | Characters/Draugr | 4 components; active: yes | c4210710 / Assets/Characters/Draugr/weapons/draugr_bow_projectile.prefab |
| Draugr_Elite | Draugr Elite | Characters/Draugr | 11 components; active: yes | c4210710 / Assets/Characters/Draugr/Draugr_Elite.prefab |
| Draugr_elite_ragdoll | — | Characters/Draugr | 4 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/Draugr_elite_ragdoll.prefab |
| Draugr_Elite_sleeping | Draugr Elite | Characters/Draugr | 11 components; active: yes | c4210710 / Assets/Characters/Draugr/Draugr_Elite_sleeping.prefab |
| Draugr_ragdoll | — | Characters/Draugr | 4 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/Draugr_ragdoll.prefab |
| Draugr_Ranged | Draugr | Characters/Draugr | 11 components; active: yes | c4210710 / Assets/Characters/Draugr/Draugr_Ranged.prefab |
| Draugr_ranged_ragdoll | — | Characters/Draugr | 4 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/Draugr_ranged_ragdoll.prefab |
| Draugr_Ranged_sleeping | Draugr | Characters/Draugr | 11 components; active: yes | c4210710 / Assets/Characters/Draugr/Draugr_Ranged_sleeping.prefab |
| Draugr_sleeping | Draugr | Characters/Draugr | 11 components; active: yes | c4210710 / Assets/Characters/Draugr/Draugr_sleeping.prefab |
| draugr_sword | Dragur axe | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/weapons/draugr_sword.prefab |
| DreamTexts | — | Systems | 2 components; active: yes | d59cfac / Assets/Systems/DreamTexts.prefab |
| dungeon_forestcrypt_door | Wood Door | world/dungeon | 7 components; active: yes | c4210710 / Assets/world/dungeon/doors/dungeon_forestcrypt_door.prefab |
| dungeon_queen_door | Dvergr Vault | world/dungeon | 4 components; active: yes | c4210710 / Assets/world/dungeon/doors/dungeon_queen_door.prefab |
| dungeon_sunkencrypt_irongate | Iron Gate | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/doors/dungeon_sunkencrypt_irongate.prefab |
| dungeon_sunkencrypt_irongate_rusty | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/doors/dungeon_sunkencrypt_irongate_rusty.prefab |
| dust_particles | — | world/dungeon | 3 components; active: yes | 25d8bae1 / Assets/world/dungeon/effects/dust_particles.prefab |
| Dverger | Dvergr Rogue; Dvergr | Characters/Dverger | 12 components; active: yes | c4210710 / Assets/Characters/Dverger/Dverger.prefab |
| dverger_demister | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dverger_demister.prefab |
| dverger_demister_broken | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dverger_demister_broken.prefab |
| dverger_demister_large | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dverger_demister_large.prefab |
| dverger_demister_ruins | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dverger_demister_ruins.prefab |
| dverger_guardstone | Ward | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dverger_guardstone.prefab |
| Dverger_melee | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/Dverger_melee.prefab |
| Dverger_meleeAshlands | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/Dverger_meleeAshlands.prefab |
| Dverger_meleeDeepNorth | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/Dverger_meleeDeepNorth.prefab |
| Dverger_ragdoll | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/Dverger_ragdoll.prefab |
| DvergerArbalest | Arbalest | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerArbalest.prefab |
| DvergerArbalest_projectile | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerArbalest_projectile.prefab |
| DvergerArbalest_shoot | Arbalest | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerArbalest_shoot.prefab |
| DvergerArbalest_shootAshlands | Arbalest | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerArbalest_shootAshlands.prefab |
| DvergerArbalest_shootDeepNorth | Arbalest | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerArbalest_shootDeepNorth.prefab |
| DvergerAshlands | Dvergr Rogue; Dvergr | Characters/Dverger | 12 components; active: yes | c4210710 / Assets/Characters/Dverger/DvergerAshlands.prefab |
| DvergerDeepNorth | Imprisoned Dvergr; Dvergr | Characters/Dverger | 12 components; active: yes | c4210710 / Assets/Characters/Dverger/DvergerDeepNorth.prefab |
| DvergerHairFemale | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerHairFemale.prefab |
| DvergerHairFemale_Redhair | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerHairFemale_Redhair.prefab |
| DvergerHairMale | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerHairMale.prefab |
| DvergerHairMale_Redbeard | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerHairMale_Redbeard.prefab |
| DvergerMage | Dvergr Mage; Dvergr | Characters/Dverger | 12 components; active: yes | c4210710 / Assets/Characters/Dverger/DvergerMage.prefab |
| DvergerMageFire | Dvergr Mage; Dvergr | Characters/Dverger | 12 components; active: yes | c4210710 / Assets/Characters/Dverger/DvergerMageFire.prefab |
| DvergerMageIce | Dvergr Mage; Dvergr | Characters/Dverger | 12 components; active: yes | c4210710 / Assets/Characters/Dverger/DvergerMageIce.prefab |
| DvergerMageSupport | Dvergr Mage; Dvergr | Characters/Dverger | 12 components; active: yes | c4210710 / Assets/Characters/Dverger/DvergerMageSupport.prefab |
| DvergerMistile | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerMistile.prefab |
| DvergerMistile_spawn | — | Characters/Dverger | 2 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerMistile_spawn.prefab |
| DvergerStaffBlocker | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffBlocker.prefab |
| DvergerStaffBlocker_blockCircle | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffBlocker_blockCircle.prefab |
| DvergerStaffBlocker_blockCircleBig | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffBlocker_blockCircleBig.prefab |
| DvergerStaffBlocker_blockHemisphere | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffBlocker_blockHemisphere.prefab |
| DvergerStaffBlocker_blockU | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffBlocker_blockU.prefab |
| DvergerStaffBlocker_blockWall | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffBlocker_blockWall.prefab |
| DvergerStaffBlocker_projectile | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffBlocker_projectile.prefab |
| DvergerStaffFire | Club | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerStaffFire.prefab |
| DvergerStaffFire_clusterbomb | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffFire_clusterbomb.prefab |
| DvergerStaffFire_clusterbomb_aoe | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffFire_clusterbomb_aoe.prefab |
| DvergerStaffFire_clusterbomb_projectile | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffFire_clusterbomb_projectile.prefab |
| DvergerStaffFire_fire_aoe | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffFire_fire_aoe.prefab |
| DvergerStaffFire_fireball | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffFire_fireball.prefab |
| DvergerStaffFire_fireball_projectile | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffFire_fireball_projectile.prefab |
| DvergerStaffHeal | Club | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerStaffHeal.prefab |
| DvergerStaffHeal_aoe | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffHeal_aoe.prefab |
| DvergerStaffHeal_heal | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffHeal_heal.prefab |
| DvergerStaffIce | Club | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerStaffIce.prefab |
| DvergerStaffIce_icebolt | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffIce_icebolt.prefab |
| DvergerStaffIce_projectile | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffIce_projectile.prefab |
| DvergerStaffNova | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffNova.prefab |
| DvergerStaffNova_aoe | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffNova_aoe.prefab |
| DvergerStaffSupport | Club | Characters/Dverger | 8 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerStaffSupport.prefab |
| DvergerStaffSupport_aoe | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffSupport_aoe.prefab |
| DvergerStaffSupport_buff | Club | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/DvergerStaffSupport_buff.prefab |
| DvergerSuitArbalest | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerSuitArbalest.prefab |
| DvergerSuitArbalest_Ashlands | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerSuitArbalest_Ashlands.prefab |
| DvergerSuitFire | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerSuitFire.prefab |
| DvergerSuitIce | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerSuitIce.prefab |
| DvergerSuitSupport | Iron plate armor | Characters/Dverger | 7 components; active: yes | c4210710 / Assets/Characters/Dverger/Gear/DvergerSuitSupport.prefab |
| DvergerTest | Haldor | Characters/Dverger | 13 components; active: yes | c4210710 / Assets/Characters/Dverger/DvergerTest.prefab |
| dvergr_new_bossroom_ENTRANCE02 | — | world/Rooms | 2 components; active: yes | cd0f218 / Assets/world/Rooms/mistlands/dvergr_new_bossroom_ENTRANCE02.prefab |
| DvergrKey | Sealbreaker | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/DvergrKey.prefab |
| DvergrKeyFragment | Sealbreaker Fragment | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/DvergrKeyFragment.prefab |
| DvergrNeedle | Dvergr Extractor | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/DvergrNeedle.prefab |
| dvergrprops_banner | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_banner.prefab |
| dvergrprops_barrel | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_barrel.prefab |
| dvergrprops_bed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_bed.prefab |
| dvergrprops_chair | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_chair.prefab |
| dvergrprops_crate | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_crate.prefab |
| dvergrprops_crate_ashlands | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_crate_ashlands.prefab |
| dvergrprops_crate_long | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_crate_long.prefab |
| dvergrprops_curtain | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_curtain.prefab |
| dvergrprops_hooknchain | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_hooknchain.prefab |
| dvergrprops_lantern | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_lantern.prefab |
| dvergrprops_lantern_standing | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_lantern_standing.prefab |
| dvergrprops_pickaxe | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_pickaxe.prefab |
| dvergrprops_shelf | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_shelf.prefab |
| dvergrprops_stool | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_stool.prefab |
| dvergrprops_table | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_table.prefab |
| dvergrprops_wood_beam | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_wood_beam.prefab |
| dvergrprops_wood_floor | Wood Floor 2x2 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_wood_floor.prefab |
| dvergrprops_wood_pole | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_wood_pole.prefab |
| dvergrprops_wood_stair | Wood Stairs | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_wood_stair.prefab |
| dvergrprops_wood_stake | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_wood_stake.prefab |
| dvergrprops_wood_stakewall | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_wood_stakewall.prefab |
| dvergrprops_wood_wall | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrprops_wood_wall.prefab |
| dvergrrock_curvedrock | — | world/Props | 2 components; active: yes | 8b54bda2 / Assets/world/Props/Dvergr/dvergrrock_curvedrock.prefab |
| dvergrrock_floorbig | — | world/Props | 2 components; active: yes | 5e1fdd1d / Assets/world/Props/Dvergr/dvergrrock_floorbig.prefab |
| dvergrrock_floorsmall | — | world/Props | 2 components; active: yes | 4bf9770f / Assets/world/Props/Dvergr/dvergrrock_floorsmall.prefab |
| dvergrrock_rockbun | — | world/Props | 2 components; active: yes | 434e44c0 / Assets/world/Props/Dvergr/dvergrrock_rockbun.prefab |
| dvergrtown_1x1x1 | — | world/Props | 2 components; active: yes | e62655a / Assets/world/Props/Dvergr/marblepieces/dvergrtown_1x1x1.prefab |
| dvergrtown_2x2x1 | — | world/Props | 2 components; active: yes | 52840833 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_2x2x1.prefab |
| dvergrtown_2x2x2 | — | world/Props | 2 components; active: yes | 20204d04 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_2x2x2.prefab |
| dvergrtown_2x2x2_enforced | — | world/Props | 2 components; active: yes | 13d4dc / Assets/world/Props/Dvergr/marblepieces/dvergrtown_2x2x2_enforced.prefab |
| dvergrtown_4x2x1 | — | world/Props | 2 components; active: yes | 7e8754f6 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_4x2x1.prefab |
| dvergrtown_arch | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_arch.prefab |
| dvergrtown_base | — | world/Props | 2 components; active: yes | 13d4dc / Assets/world/Props/Dvergr/marblepieces/dvergrtown_base.prefab |
| dvergrtown_column_3 | — | world/Props | 1 components; active: yes | cd0f218 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_column_3.prefab |
| dvergrtown_creep_door | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_creep_door.prefab |
| dvergrtown_floor_large | — | world/Props | 2 components; active: yes | d054aa3 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_floor_large.prefab |
| dvergrtown_gate | — | world/Props | 2 components; active: yes | 5c1b7f34 / Assets/world/Props/Dvergr/dvergrtown_gate.prefab |
| dvergrtown_gate_corner | — | world/Props | 2 components; active: yes | b698d7ef / Assets/world/Props/Dvergr/dvergrtown_gate_corner.prefab |
| dvergrtown_gate_stair | — | world/Props | 2 components; active: yes | 54a2a18d / Assets/world/Props/Dvergr/dvergrtown_gate_stair.prefab |
| dvergrtown_head01 | — | world/Props | 2 components; active: yes | e4944bb4 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_head01.prefab |
| dvergrtown_head02 | — | world/Props | 2 components; active: yes | b67d58a8 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_head02.prefab |
| dvergrtown_metal_wall_2x2 | — | world/Props | 3 components; active: yes | 4415392a / Assets/world/Props/Dvergr/marblepieces/dvergrtown_metal_wall_2x2.prefab |
| dvergrtown_secretdoor | Hidden Door | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/Sliding_door/dvergrtown_secretdoor.prefab |
| dvergrtown_slidingdoor | Old Dvergr Gate | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/Sliding_door/dvergrtown_slidingdoor.prefab |
| dvergrtown_slope_1x1x2 | — | world/Props | 2 components; active: yes | 2fc8af8e / Assets/world/Props/Dvergr/marblepieces/dvergrtown_slope_1x1x2.prefab |
| dvergrtown_slope_inverted_1x1x2 | — | world/Props | 1 components; active: yes | d6daa696 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_slope_inverted_1x1x2.prefab |
| dvergrtown_stair | — | world/Props | 2 components; active: yes | f40f2391 / Assets/world/Props/Dvergr/marblepieces/dvergrtown_stair.prefab |
| dvergrtown_stair_corner | — | world/Props | 2 components; active: yes | f6398d9e / Assets/world/Props/Dvergr/marblepieces/dvergrtown_stair_corner.prefab |
| dvergrtown_stair_corner_wood_left | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_stair_corner_wood_left.prefab |
| dvergrtown_stair_long | — | world/Props | 2 components; active: yes | 652c02be / Assets/world/Props/Dvergr/dvergrtown_stair_long.prefab |
| dvergrtown_tip_1x1x2 | — | world/Props | 2 components; active: yes | 5842aa8d / Assets/world/Props/Dvergr/marblepieces/dvergrtown_tip_1x1x2.prefab |
| dvergrtown_wall_large | — | world/Props | 2 components; active: yes | b99bd33a / Assets/world/Props/Dvergr/dvergrtown_wall_large.prefab |
| dvergrtown_wall_w_loophole | — | world/Props | 2 components; active: yes | 2b5df0d / Assets/world/Props/Dvergr/dvergrtown_wall_w_loophole.prefab |
| dvergrtown_wood_beam | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_beam.prefab |
| dvergrtown_wood_crane | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_crane.prefab |
| dvergrtown_wood_pole | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_pole.prefab |
| dvergrtown_wood_stake | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_stake.prefab |
| dvergrtown_wood_stakewall | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_stakewall.prefab |
| dvergrtown_wood_support | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_support.prefab |
| dvergrtown_wood_wall01 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_wall01.prefab |
| dvergrtown_wood_wall02 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_wall02.prefab |
| dvergrtown_wood_wall03 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/dvergrtown_wood_wall03.prefab |
| DyrnwynBladeFragment | Dyrnwyn Blade Fragment | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/DyrnwynBladeFragment.prefab |
| DyrnwynHiltFragment | Dyrnwyn Hilt Fragment | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/DyrnwynHiltFragment.prefab |
| DyrnwynTipFragment | Dyrnwyn Tip Fragment | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/DyrnwynTipFragment.prefab |
| Ectoplasm | Ectoplasm | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Ectoplasm.prefab |
| Eikthyr | Eikthyr | Characters/Eikthyr | 11 components; active: yes | c4210710 / Assets/Characters/Eikthyr/Eikthyr.prefab |
| Eikthyr_antler | StagAttack1 | Characters/Eikthyr | 2 components; active: yes | c4210710 / Assets/Characters/Eikthyr/attacks/Eikthyr_antler.prefab |
| Eikthyr_charge | StagAttack2 | Characters/Eikthyr | 2 components; active: yes | c4210710 / Assets/Characters/Eikthyr/attacks/Eikthyr_charge.prefab |
| Eikthyr_flegs_OLD | StagAttack1 | Characters/Eikthyr | 2 components; active: yes | c4210710 / Assets/Characters/Eikthyr/attacks/Eikthyr_flegs_OLD.prefab |
| eikthyr_ragdoll | — | Characters/Eikthyr | 3 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/eikthyr_ragdoll.prefab |
| Eikthyr_stomp | slap | Characters/Eikthyr | 3 components; active: yes | c4210710 / Assets/Characters/Eikthyr/attacks/Eikthyr_stomp.prefab |
| Eikthyrnir | — | world/Locations | 2 components; active: yes | b3a2b0f3 / Assets/world/Locations/Meadows/Eikthyrnir.prefab |
| Eitr | Refined Eitr | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Eitr.prefab |
| eitrrefinery | Eitr Refinery | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/eitrrefinery.prefab |
| Elaking | Elaking | Characters/Elaking | 11 components; active: yes | c4210710 / Assets/Characters/Elaking/Elaking.prefab |
| Elaking_AttackClaw | jaws | Characters/Elaking | 3 components; active: yes | c4210710 / Assets/Characters/Elaking/attacks/Elaking_AttackClaw.prefab |
| Elaking_AttackJump | Charred Sword | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/attacks/Elaking_AttackJump.prefab |
| Elaking_AttackLantern | Torch | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/Elaking_AttackLantern.prefab |
| Elaking_Ragdoll | — | Characters/Elaking | 3 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/Elaking_Ragdoll.prefab |
| elaking_trashpile | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/TheHole/elaking_trashpile.prefab |
| elaking_trashpile_destruction | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/TheHole/elaking_trashpile_destruction.prefab |
| ElakingHairBundle | Elaking Hair Bundle | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/ElakingHairBundle.prefab |
| ElakingLantern | Elaking | Characters/Elaking | 12 components; active: yes | c4210710 / Assets/Characters/Elaking/ElakingLantern.prefab |
| ElakingMole | Eyeless One | Characters/ElakingMole | 11 components; active: yes | c4210710 / Assets/Characters/ElakingMole/ElakingMole.prefab |
| ElakingMole_AttackClaw | jaws | Characters/ElakingMole | 3 components; active: yes | c4210710 / Assets/Characters/ElakingMole/attacks/ElakingMole_AttackClaw.prefab |
| ElakingMole_AttackClaw2 | jaws | Characters/ElakingMole | 3 components; active: yes | c4210710 / Assets/Characters/ElakingMole/attacks/ElakingMole_AttackClaw2.prefab |
| ElakingMole_AttackSandcloud | StagAttack2 | Characters/ElakingMole | 2 components; active: yes | c4210710 / Assets/Characters/ElakingMole/attacks/ElakingMole_AttackSandcloud.prefab |
| ElakingMole_Ragdoll | — | Characters/ElakingMole | 3 components; active: yes | c4210710 / Assets/Characters/ElakingMole/fx/ElakingMole_Ragdoll.prefab |
| ElakingMole_Sandcloud_Projectile | — | Characters/ElakingMole | 4 components; active: yes | c4210710 / Assets/Characters/ElakingMole/attacks/ElakingMole_Sandcloud_Projectile.prefab |
| ElderBark | Ancient Bark | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/ElderBark.prefab |
| Emote | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/Radial/elements/Emote.prefab |
| Empty | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/Radial/elements/Empty.prefab |
| Enemy_Barka_Attack_BackSlam | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Attack/Enemy_Barka_Attack_BackSlam.prefab |
| Enemy_Barka_Attack_HeavyImpact | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Attack/Enemy_Barka_Attack_HeavyImpact.prefab |
| Enemy_Barka_Attack_HeavySwings | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Attack/Enemy_Barka_Attack_HeavySwings.prefab |
| Enemy_Barka_Attack_SlamDrive | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Attack/Enemy_Barka_Attack_SlamDrive.prefab |
| Enemy_Barka_Attack_WhipFlurry | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Attack/Enemy_Barka_Attack_WhipFlurry.prefab |
| Enemy_Barka_Attack_WhipSlam | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Attack/Enemy_Barka_Attack_WhipSlam.prefab |
| Enemy_Barka_Death | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Death/Enemy_Barka_Death.prefab |
| Enemy_Barka_Death_Debris | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Death/Enemy_Barka_Death_Debris.prefab |
| Enemy_Barka_Footstep | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Footsteps/Enemy_Barka_Footstep.prefab |
| Enemy_Barka_Hurt | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Hurt/Enemy_Barka_Hurt.prefab |
| Enemy_Barka_Idle | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Idle/Enemy_Barka_Idle.prefab |
| Enemy_Barka_Movement | — | Characters/Barka | 4 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Footsteps/Enemy_Barka_Movement.prefab |
| Enemy_Barka_Verse_Death | — | Characters/Barka | 5 components; active: yes | c4210710 / Assets/Characters/Barka/fx/sfx/Death/Enemy_Barka_Verse_Death.prefab |
| EnemyHud | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/EnemyHud.prefab |
| Entrails | Entrails | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Entrails.prefab |
| EventSystem | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/EventSystem.prefab |
| eventzone_bonemass | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/eventzone_bonemass.prefab |
| eventzone_eikthyr | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/eventzone_eikthyr.prefab |
| eventzone_fader | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/eventzone_fader.prefab |
| eventzone_gdking | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/eventzone_gdking.prefab |
| eventzone_goblinking | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/eventzone_goblinking.prefab |
| eventzone_moder | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/eventzone_moder.prefab |
| eventzone_queen | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/eventzone_queen.prefab |
| EvilHeart_Forest | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/EvilHeart/EvilHeart_Forest.prefab |
| EvilHeart_Swamp | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/EvilHeart/EvilHeart_Swamp.prefab |
| ExteriorGateway | — | GameElements/InteriorStuff | 3 components; active: yes | 64010dc9 / Assets/GameElements/InteriorStuff/ExteriorGateway.prefab |
| Eyescream | Eyescream | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Eyescream.prefab |
| Fader | Fader | Characters/Fader | 12 components; active: yes | c4210710 / Assets/Characters/Fader/Fader.prefab |
| fader_bellholder | Bell Holder | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fader_bellholder.prefab |
| Fader_Bite | Fader Bite | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Bite.prefab |
| Fader_Claw_Left | Fader Claw Left | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Claw_Left.prefab |
| Fader_Claw_Right | Fader Claw Right | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Claw_Right.prefab |
| Fader_DroppedFire_AOE | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_DroppedFire_AOE.prefab |
| Fader_Fissure | Fader Fissure | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Fissure.prefab |
| Fader_Fissure_AOE | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Fissure_AOE.prefab |
| Fader_Fissure_Intense | Fader Fissure | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Fissure_Intense.prefab |
| Fader_Fissure_Spawn | — | Characters/Fader | 2 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Fissure_Spawn.prefab |
| Fader_Flamebreath | Fader Firebreath | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Flamebreath.prefab |
| Fader_Flamebreath_AOE | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Flamebreath_AOE.prefab |
| Fader_Jump | Fader Jump | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Jump.prefab |
| Fader_Jump_AOE | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Jump_AOE.prefab |
| Fader_Jump_Left | Fader Jump | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Jump_Left.prefab |
| Fader_Jump_Right | Fader Jump | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Jump_Right.prefab |
| Fader_Meteors | spawn | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Meteors.prefab |
| Fader_Meteors_Intense | spawn | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Meteors_Intense.prefab |
| Fader_MeteorSmash_AOE | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_MeteorSmash_AOE.prefab |
| Fader_Roar | Fader Roar | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Roar.prefab |
| Fader_Roar_Intense | Fader Roar | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Roar_Intense.prefab |
| Fader_Roar_Projectile | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Roar_Projectile.prefab |
| Fader_Roar_Spawn | — | Characters/Fader | 2 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Roar_Spawn.prefab |
| Fader_Spin | Fader Spin | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Spin.prefab |
| Fader_Taunt | Fader Taunt | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_Taunt.prefab |
| Fader_WallOfFire | Fader Wall of Fire | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_WallOfFire.prefab |
| Fader_WallOfFire_AOE | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_WallOfFire_AOE.prefab |
| Fader_WallOfFire_Spawn | — | Characters/Fader | 2 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/Fader_WallOfFire_Spawn.prefab |
| FaderDrop | Kindled Ribs | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/FaderDrop.prefab |
| FaderEmber | Embers | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FaderEmber.prefab |
| FaderLocation | — | world/Locations | 2 components; active: yes | 1080ee37 / Assets/world/Locations/Ashlands/FaderLocation.prefab |
| FallenValkyrie | Fallen Valkyrie | Characters/FallenValkyrie | 9 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/FallenValkyrie.prefab |
| fallenvalkyrie_claws | Fallen Valkyrie Claws | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_claws.prefab |
| fallenvalkyrie_feather_projectile | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_feather_projectile.prefab |
| fallenvalkyrie_poisonbreath | Fallen Valkyrie Poison Breath | Characters/FallenValkyrie | 3 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_poisonbreath.prefab |
| fallenvalkyrie_poisonbreath_aoe | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_poisonbreath_aoe.prefab |
| FallenValkyrie_projectile_explosion | — | Characters/FallenValkyrie | 3 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/FallenValkyrie_projectile_explosion.prefab |
| fallenvalkyrie_screech | Fallen Valkyrie Claws | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_screech.prefab |
| fallenvalkyrie_spin | Fallen Valkyrie Aoe Spin | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_spin.prefab |
| fallenvalkyrie_spit | cold ball | Characters/FallenValkyrie | 3 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_spit.prefab |
| fallenvalkyrie_spit_projectile | — | Characters/FallenValkyrie | 4 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_spit_projectile.prefab |
| fallenvalkyrie_swoopattack | Fallen Valkyrie swooping | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_swoopattack.prefab |
| fallenvalkyrie_taunt | Fallen Valkyrie Claws | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_taunt.prefab |
| fallenvalkyrie_wingspin | Fallen Valkyrie Wingspin | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/attacks/fallenvalkyrie_wingspin.prefab |
| FallenWarrior | Fallen Warrior; Haldor | Characters/FallenWarrior | 13 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/FallenWarrior.prefab |
| FavCategoryCheck | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/BuildUI/FavCategoryCheck.prefab |
| FeastAshlands | Ashlands Gourmet Bowl | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastAshlands.prefab |
| FeastAshlands_Material | Ashlands Gourmet Bowl | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastAshlands_Material.prefab |
| FeastBlackforest | Black Forest Buffet Platter | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastBlackforest.prefab |
| FeastBlackforest_Material | Black Forest Buffet Platter | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastBlackforest_Material.prefab |
| FeastDeepNorth | Northern Morning Fare | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastDeepNorth.prefab |
| FeastDeepNorth_Material | Northern Morning Fare | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastDeepNorth_Material.prefab |
| Feaster | Serving Tray | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/tools/Feaster.prefab |
| FeastMeadows | Whole Roasted Meadow Boar | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastMeadows.prefab |
| FeastMeadows_Material | Whole Roasted Meadow Boar | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastMeadows_Material.prefab |
| FeastMistlands | Mushrooms Galore á la Mistlands | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastMistlands.prefab |
| FeastMistlands_Material | Mushrooms Galore á la Mistlands | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastMistlands_Material.prefab |
| FeastMountains | Hearty Mountain Logger&#x27;s Stew | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastMountains.prefab |
| FeastMountains_Material | Hearty Mountain Logger&#x27;s Stew | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastMountains_Material.prefab |
| FeastOceans | Sailor&#x27;s Bounty | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastOceans.prefab |
| FeastOceans_Material | Sailor&#x27;s Bounty | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastOceans_Material.prefab |
| FeastPlains | Plains Pie Picnic | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastPlains.prefab |
| FeastPlains_Material | Plains Pie Picnic | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastPlains_Material.prefab |
| FeastSwamps | Swamp Dweller&#x27;s Delight | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/FeastSwamps.prefab |
| FeastSwamps_Material | Swamp Dweller&#x27;s Delight | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FeastSwamps_Material.prefab |
| Feathers | Feathers | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Feathers.prefab |
| Feedback | — | UI/prefabs | 7 components; active: yes | c4210710 / Assets/UI/prefabs/Feedback.prefab |
| Fenring | Fenring | Characters/Fenring | 10 components; active: yes | c4210710 / Assets/Characters/Fenring/Fenring.prefab |
| Fenring_attack_claw | claw | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_claw.prefab |
| Fenring_attack_fireclaw | claw | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_fireclaw.prefab |
| Fenring_attack_fireclaw_double | claw | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_fireclaw_double.prefab |
| Fenring_attack_flames | Fenring cultist flames | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_flames.prefab |
| Fenring_attack_flames_aoe | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_flames_aoe.prefab |
| Fenring_attack_frost | Fenring cultist frost | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_frost.prefab |
| Fenring_attack_frost_aoe | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_frost_aoe.prefab |
| Fenring_attack_iceclaw | claw | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_iceclaw.prefab |
| Fenring_attack_iceclaw_double | claw | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_iceclaw_double.prefab |
| Fenring_attack_IceNova | Club | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_IceNova.prefab |
| Fenring_attack_jump | claw | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_attack_jump.prefab |
| Fenring_Cultist | Cultist | Characters/Fenring | 10 components; active: yes | c4210710 / Assets/Characters/Fenring/Fenring_Cultist.prefab |
| Fenring_Cultist_Hildir | &lt;color=orange&gt;Geirrhafa&lt;/color&gt; | Characters/Fenring | 10 components; active: yes | c4210710 / Assets/Characters/Fenring/Fenring_Cultist_Hildir.prefab |
| Fenring_Cultist_Hildir_nochest | &lt;color=orange&gt;Geirrhafa&lt;/color&gt; | Characters/Fenring | 10 components; active: yes | c4210710 / Assets/Characters/Fenring/Fenring_Cultist_Hildir_nochest.prefab |
| Fenring_cultist_ragdoll | — | Characters/Fenring | 4 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/Fenring_cultist_ragdoll.prefab |
| Fenring_cultist_ragdoll_hildir | — | Characters/Fenring | 4 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/Fenring_cultist_ragdoll_hildir.prefab |
| Fenring_ragdoll | — | Characters/Fenring | 4 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/Fenring_ragdoll.prefab |
| Fenring_taunt | scream | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/Fenring_taunt.prefab |
| FenringIceNova_aoe | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/attacks/FenringIceNova_aoe.prefab |
| fenrirhide_hanging | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Caverocks/fenrirhide_hanging.prefab |
| fenrirhide_hanging_door | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Caverocks/fenrirhide_hanging_door.prefab |
| fermenter | Fermenter | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/fermenter.prefab |
| FernAshlands | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/FernAshlands.prefab |
| FernFiddleHeadAshlands | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Ashlands/FernFiddleHeadAshlands.prefab |
| fi_vil_cath_decor_swords_cross | — | world/Props | 5 components; active: yes | 1cb6211b / Assets/world/Props/CryptKit/fi_vil_cath_decor_swords_cross.prefab |
| fi_vil_shield05_a | — | world/Props | 5 components; active: yes | 46989d29 / Assets/world/Props/CryptKit/fi_vil_shield05_a.prefab |
| Fiddleheadfern | Fiddlehead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Fiddleheadfern.prefab |
| FierySvinstew | Fiery Svinstew | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FierySvinstew.prefab |
| FimbulLocation01 | — | world/Locations | 2 components; active: yes | d59cfac / Assets/world/Locations/DeepNorth/FimbulLocation01.prefab |
| FimbulvinterOrb | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/Fimbulvinter/FimbulvinterOrb.prefab |
| FimbulvinterOrb_start | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/Fimbulvinter/FimbulvinterOrb_start.prefab |
| FineWood | Finewood | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FineWood.prefab |
| FirCone | Fir Cone | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FirCone.prefab |
| FirConeFrost | Timberwood Cone | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FirConeFrost.prefab |
| Fire | — | world/SmokeFire | 8 components; active: yes | c4210710 / Assets/world/SmokeFire/Fire.prefab |
| fire_pit | Campfire; Fire | GameElements/Pieces | 8 components; active: yes | c4210710 / Assets/GameElements/Pieces/fire_pit.prefab |
| fire_pit_haldor | Campfire; Fire | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/fire_pit_haldor.prefab |
| fire_pit_hildir | Campfire; Fire | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/fire_pit_hildir.prefab |
| fire_pit_iron | Iron Fire Pit; Fire | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/fire_pit_iron.prefab |
| FireFlies | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/FireFlies.prefab |
| FireHole | — | world/Locations | 2 components; active: yes | 3303f8a1 / Assets/world/Locations/Misc/FireHole.prefab |
| FireworksRocket_Blue | Blue Fireworks | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FireworksRocket_Blue.prefab |
| FireworksRocket_Cyan | Cyan Fireworks | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FireworksRocket_Cyan.prefab |
| FireworksRocket_Green | Green Fireworks | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FireworksRocket_Green.prefab |
| FireworksRocket_Purple | Purple Fireworks | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FireworksRocket_Purple.prefab |
| FireworksRocket_Red | Red Fireworks | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FireworksRocket_Red.prefab |
| FireworksRocket_White | Basic Fireworks | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FireworksRocket_White.prefab |
| FireworksRocket_Yellow | Yellow Fireworks | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FireworksRocket_Yellow.prefab |
| FirTree | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree.prefab |
| FirTree_big | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/FirTree_big.prefab |
| FirTree_Big_log | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/FirTree/logs/FirTree_Big_log.prefab |
| FirTree_big_log_half | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/FirTree/logs/FirTree_big_log_half.prefab |
| FirTree_Big_plantable_Stub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_Big_plantable_Stub.prefab |
| FirTree_big_Sapling | Timberwood Sapling | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/FirTree_big_Sapling.prefab |
| FirTree_log | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/FirTree/logs/FirTree_log.prefab |
| FirTree_log_half | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/FirTree/logs/FirTree_log_half.prefab |
| FirTree_oldLog | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_oldLog.prefab |
| FirTree_oldLog_deepnorth | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_oldLog_deepnorth.prefab |
| FirTree_Sapling | Fir Sapling | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_Sapling.prefab |
| FirTree_small | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_small.prefab |
| FirTree_small_dead | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_small_dead.prefab |
| FirTree_Snow_log | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/FirTree/logs/FirTree_Snow_log.prefab |
| FirTree_Snow_log_half | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/FirTree/logs/FirTree_Snow_log_half.prefab |
| FirTree_Snow_Stub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_Snow_Stub.prefab |
| FirTree_Stub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/FirTree/FirTree_Stub.prefab |
| Fish1 | Perch | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish1.prefab |
| Fish10 | Northern Salmon | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish10.prefab |
| Fish11 | Magmafish | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish11.prefab |
| Fish12 | Pufferfish | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish12.prefab |
| Fish2 | Pike | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish2.prefab |
| Fish3 | Tuna | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish3.prefab |
| Fish4_cave | Tetra | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish4_cave.prefab |
| Fish5 | Trollfish | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish5.prefab |
| Fish6 | Giant Herring | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish6.prefab |
| Fish7 | Grouper | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish7.prefab |
| Fish8 | Coral Cod | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish8.prefab |
| Fish9 | Anglerfish | Characters/animals | 8 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Fish9.prefab |
| FishAndBread | Fish &#x27;n&#x27; Bread | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FishAndBread.prefab |
| FishAndBreadUncooked | Uncooked Fish &#x27;n&#x27; Bread | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishAndBreadUncooked.prefab |
| FishAnglerRaw | Raw Fish | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FishAnglerRaw.prefab |
| FishCooked | Cooked Fish | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FishCooked.prefab |
| FishingBait | Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBait.prefab |
| FishingBaitAshlands | Hot Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitAshlands.prefab |
| FishingBaitCave | Cold Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitCave.prefab |
| FishingBaitDeepNorth | Frosty Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitDeepNorth.prefab |
| FishingBaitForest | Mossy Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitForest.prefab |
| FishingBaitMistlands | Misty Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitMistlands.prefab |
| FishingBaitOcean | Heavy Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitOcean.prefab |
| FishingBaitPlains | Stingy Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitPlains.prefab |
| FishingBaitSwamp | Sticky Fishing Bait | GameElements/Items | 10 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FishingBaitSwamp.prefab |
| FishingRod | Fishing Rod | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/tools/FishingRod.prefab |
| FishingRodFloat | — | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/tools/_res/FishingRod/FishingRodFloat.prefab |
| FishingRodFloatProjectile | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/tools/_res/FishingRod/FishingRodFloatProjectile.prefab |
| FishRaw | Raw Fish | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FishRaw.prefab |
| FishSoup | Fish Soup | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FishSoup.prefab |
| FishWraps | Fish Wraps | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FishWraps.prefab |
| FistBjornClaw | Paws of the Bear | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/FistBjornClaw.prefab |
| FistBjornUndeadClaw | Vilebone Maulclaws | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/FistBjornUndeadClaw.prefab |
| FistFenrirClaw | Flesh Rippers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/FistFenrirClaw.prefab |
| FistGold | Nord Knucklechains | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/FistGold.prefab |
| FistGold_BloodLightning | Thunderblood Knucklechains | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/FistGold_BloodLightning.prefab |
| FistGold_FrostFire | Frostfire Knucklechains | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/FistGold_FrostFire.prefab |
| FistGoldUncooked | Cast: Nord Knucklechains | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/FistGoldUncooked.prefab |
| Flametal | Ancient Metal | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Flametal.prefab |
| flametal_gate | Flametal Gate | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/flametal_gate.prefab |
| FlametalNew | Flametal | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FlametalNew.prefab |
| FlametalOre | Glowing Metal Ore | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FlametalOre.prefab |
| FlametalOreNew | Flametal Ore | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FlametalOreNew.prefab |
| FlametalRockstand | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Flametal/model/FlametalRockstand.prefab |
| FlametalRockstand_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Flametal/model/FlametalRockstand_frac.prefab |
| Flash | — | Effects/thunder | 2 components; active: yes | d59cfac / Assets/Effects/thunder/Flash.prefab |
| Flax | Flax | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Flax.prefab |
| Flies | — | Effects | 2 components; active: yes | c4210710 / Assets/Effects/Flies.prefab |
| Flint | Flint | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Flint.prefab |
| flint_pile | Flint Pile | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/flint_pile.prefab |
| flintspear_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/spear/flintspear_projectile.prefab |
| flying_core | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Mistlands/flying_core.prefab |
| ForceField | — | Characters/TraderHaldor | 3 components; active: yes | c4210710 / Assets/Characters/TraderHaldor/ForceField.prefab |
| forestcrypt_chamber_hildir | — | world/Rooms | 2 components; active: yes | 577352c9 / Assets/world/Rooms/rooms/forestcrypt_chamber_hildir.prefab |
| forestcrypt_new_BurialChamber02 | — | world/Rooms | 2 components; active: yes | c27cce3a / Assets/world/Rooms/rooms/forestcrypt_new_BurialChamber02.prefab |
| forestcrypt_Stairs1 | — | world/Rooms | 2 components; active: yes | 75196655 / Assets/world/Rooms/rooms/forestcrypt_Stairs1.prefab |
| forge | Forge | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/forge.prefab |
| forge_ext1 | Forge Bellows | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/forge_ext1.prefab |
| forge_ext2 | Anvils | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/forge_ext2.prefab |
| forge_ext3 | Grinding Wheel | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/forge_ext3.prefab |
| forge_ext4 | Smith&#x27;s Anvil | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/forge_ext4.prefab |
| forge_ext5 | Forge Cooler | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/forge_ext5.prefab |
| forge_ext6 | Forge Tool Rack | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/forge_ext6.prefab |
| FragrantBundle | Fragrant Bundle | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FragrantBundle.prefab |
| FreezeGland | Freeze Gland | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FreezeGland.prefab |
| FreshSeaweed | Fresh Seaweed | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FreshSeaweed.prefab |
| FrostCavesShrineReveal | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/FrostCavesShrineReveal.prefab |
| FrostCore | Frostcore | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/FrostCore.prefab |
| FrostWisp | — | Characters/Frostwisp | 9 components; active: yes | c4210710 / Assets/Characters/Frostwisp/FrostWisp.prefab |
| FrostWisp_Storm | — | Characters/Frostwisp | 5 components; active: yes | c4210710 / Assets/Characters/Frostwisp/FrostWisp_Storm.prefab |
| Frostwood | Timberwood | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Frostwood.prefab |
| FrozenFuel | Liquid Frost | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/FrozenFuel.prefab |
| FrozenGD | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Frozen/FrozenGD.prefab |
| FrozenKing | Kall Fimbulbringer | Characters/FrozenKing | 11 components; active: yes | c4210710 / Assets/Characters/FrozenKing/FrozenKing.prefab |
| FrozenKing_ChainFlurry | FrozenKing ChainFlurry | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainFlurry.prefab |
| FrozenKing_ChainRush | FrozenKing ChainRush | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainRush.prefab |
| FrozenKing_ChainSlam_L | FrozenKing ChainSlam L | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainSlam_L.prefab |
| FrozenKing_ChainSlam_L_double | FrozenKing ChainSlam L double | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainSlam_L_double.prefab |
| FrozenKing_ChainSlam_R | FrozenKing ChainSlam R | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainSlam_R.prefab |
| FrozenKing_ChainSlam_R_double | FrozenKing ChainSlam R double | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainSlam_R_double.prefab |
| FrozenKing_ChainSweep_L | FrozenKing ChainSweep L | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainSweep_L.prefab |
| FrozenKing_ChainSweep_R | FrozenKing ChainSweep R | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainSweep_R.prefab |
| FrozenKing_ChainWhirl | FrozenKing ChainWhirl | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_ChainWhirl.prefab |
| FrozenKing_DoubleSweep | FrozenKing DoubleSweep | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_DoubleSweep.prefab |
| FrozenKing_p2 | Kall Fimbulbringer | Characters/FrozenKing | 9 components; active: yes | c4210710 / Assets/Characters/FrozenKing/FrozenKing_p2.prefab |
| FrozenKing_P2_Projectile_Bonemass | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Projectile_Bonemass.prefab |
| FrozenKing_P2_Projectile_Eikthyr | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Projectile_Eikthyr.prefab |
| FrozenKing_P2_Projectile_Elder | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Projectile_Elder.prefab |
| FrozenKing_P2_Projectile_Fader | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Projectile_Fader.prefab |
| FrozenKing_P2_Projectile_Moder | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Projectile_Moder.prefab |
| FrozenKing_P2_Projectile_Queen | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Projectile_Queen.prefab |
| FrozenKing_P2_Projectile_Yagluth | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Projectile_Yagluth.prefab |
| FrozenKing_P2_Spawn_Bonemass | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Spawn_Bonemass.prefab |
| FrozenKing_P2_Spawn_Eikthyr | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Spawn_Eikthyr.prefab |
| FrozenKing_P2_Spawn_Elder | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Spawn_Elder.prefab |
| FrozenKing_P2_Spawn_Fader | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Spawn_Fader.prefab |
| FrozenKing_P2_Spawn_Moder | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Spawn_Moder.prefab |
| FrozenKing_P2_Spawn_Queen | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Spawn_Queen.prefab |
| FrozenKing_P2_Spawn_Yagluth | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Spawn_Yagluth.prefab |
| FrozenKing_P2_Summon_Bonemass | Fader Roar | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Summon_Bonemass.prefab |
| FrozenKing_P2_Summon_Eikthyr | Fader Roar | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Summon_Eikthyr.prefab |
| FrozenKing_P2_Summon_Elder | Fader Roar | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Summon_Elder.prefab |
| FrozenKing_P2_Summon_Fader | Fader Roar | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Summon_Fader.prefab |
| FrozenKing_P2_Summon_Moder | Fader Roar | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Summon_Moder.prefab |
| FrozenKing_P2_Summon_Queen | Fader Roar | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Summon_Queen.prefab |
| FrozenKing_P2_Summon_Yagluth | Fader Roar | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_P2_Summon_Yagluth.prefab |
| FrozenKing_p3 | Kall Fimbulbringer | Characters/FrozenKing | 11 components; active: yes | c4210710 / Assets/Characters/FrozenKing/FrozenKing_p3.prefab |
| FrozenKing_P3_ChainSlam_L_double | FrozenKing ChainSlam L double | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_P3_ChainSlam_L_double.prefab |
| FrozenKing_P3_ChainSlam_R_double | FrozenKing ChainSlam R double | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_P3_ChainSlam_R_double.prefab |
| FrozenKing_P3_ChainWhirl | FrozenKing ChainWhirl | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_P3_ChainWhirl.prefab |
| FrozenKing_Punch_AOE | FrozenKing Punch AOE | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_Punch_AOE.prefab |
| FrozenKing_SpikeRain | spawn | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_SpikeRain.prefab |
| FrozenKing_Summon | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Phase 2/FrozenKing_Summon.prefab |
| FrozenKing_tendrilspawn | spawn | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/FrozenKing_tendrilspawn.prefab |
| FrozenKingDrop | Sacrificial Blood | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/FrozenKingDrop.prefab |
| frozenship | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/frozenship.prefab |
| frozenship02 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/frozenship02.prefab |
| frozenship03 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/frozenship03.prefab |
| FrozenSkeleton_Pose1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Frozen/FrozenSkeleton_Pose1.prefab |
| FrozenSkeleton_Pose2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Frozen/FrozenSkeleton_Pose2.prefab |
| Frysling | Frysling | Characters/Frysling | 9 components; active: yes | c4210710 / Assets/Characters/Frysling/Frysling.prefab |
| frysling_snowball_attack | fireballattack | Characters/Frysling | 3 components; active: yes | c4210710 / Assets/Characters/Frysling/attacks/frysling_snowball_attack.prefab |
| frysling_snowball_projectile | — | Characters/Frysling | 4 components; active: yes | c4210710 / Assets/Characters/Frysling/attacks/frysling_snowball_projectile.prefab |
| fuling_trap | Trap | Characters/Traps | 6 components; active: yes | c4210710 / Assets/Characters/Traps/fuling_trap.prefab |
| fuling_turret | Ballista | Characters/Traps | 6 components; active: yes | c4210710 / Assets/Characters/Traps/fuling_turret.prefab |
| FW_ArmorBronzeChest | Bronze Plate Tunic | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorBronzeChest.prefab |
| FW_ArmorBronzeLegs | Bronze Plate Leggings | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorBronzeLegs.prefab |
| FW_ArmorFenringChest | Fenris Coat | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorFenringChest.prefab |
| FW_ArmorFenringLegs | Fenris Leggings | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorFenringLegs.prefab |
| FW_ArmorMageChest | Eitr-weave Robe | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorMageChest.prefab |
| FW_ArmorMageChest_Ashlands | Robes of Embla | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorMageChest_Ashlands.prefab |
| FW_ArmorMageLegs | Eitr-weave Trousers | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorMageLegs.prefab |
| FW_ArmorMageLegs_Ashlands | Trousers of Embla | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorMageLegs_Ashlands.prefab |
| FW_ArmorPaddedCuirass | Padded Cuirass | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorPaddedCuirass.prefab |
| FW_ArmorPaddedGreaves | Padded Greaves | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorPaddedGreaves.prefab |
| FW_ArmorTrollLeatherChest | Troll Leather Tunic | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorTrollLeatherChest.prefab |
| FW_ArmorTrollLeatherLegs | Troll Leather Trousers | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ArmorTrollLeatherLegs.prefab |
| FW_AxeBronze | Bronze Axe | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_AxeBronze.prefab |
| FW_BattleaxeCrystal | Crystal Battleaxe | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_BattleaxeCrystal.prefab |
| FW_BowDraugrFang | Draugr Fang | Characters/FallenWarrior | 9 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_BowDraugrFang.prefab |
| FW_CapeLinen | Linen Cape | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_CapeLinen.prefab |
| FW_CapeTrollHide | Troll Hide Cape | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_CapeTrollHide.prefab |
| FW_CapeWolf | Wolf Fur Cape | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_CapeWolf.prefab |
| FW_HelmetBronze | Bronze Helmet | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_HelmetBronze.prefab |
| FW_KnifeSilver | Silver Knife | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_KnifeSilver.prefab |
| FW_KnifeSkollAndHati | Skoll and Hati | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_KnifeSkollAndHati.prefab |
| FW_ShieldBlackmetalTower | Black Metal Tower Shield | Characters/FallenWarrior | 8 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_ShieldBlackmetalTower.prefab |
| FW_StaffFireball | Staff of Embers | Characters/FallenWarrior | 8 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_StaffFireball.prefab |
| FW_StaffLightning | Dundr | Characters/FallenWarrior | 8 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_StaffLightning.prefab |
| FW_SwordBlackmetal | Black Metal Sword | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/FW_SwordBlackmetal.prefab |
| fx_Abomination_arise | — | Characters/Abomination | 4 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_arise.prefab |
| fx_Abomination_arise_end | — | Characters/Abomination | 4 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_arise_end.prefab |
| fx_Abomination_attack1 | — | Characters/Abomination | 4 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack1.prefab |
| fx_Abomination_attack1_start | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack1_start.prefab |
| fx_Abomination_attack1_trailon | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack1_trailon.prefab |
| fx_Abomination_attack2 | — | Characters/Abomination | 6 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack2.prefab |
| fx_Abomination_attack2_lift | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack2_lift.prefab |
| fx_Abomination_attack2_start | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack2_start.prefab |
| fx_Abomination_attack3 | — | Characters/Abomination | 6 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack3.prefab |
| fx_Abomination_attack3_start | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack3_start.prefab |
| fx_Abomination_attack_hit | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_attack_hit.prefab |
| fx_Abomination_footstep_run | — | Characters/Abomination | 3 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_footstep_run.prefab |
| fx_Abomination_footstep_walk | — | Characters/Abomination | 3 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/fx_Abomination_footstep_walk.prefab |
| fx_Adrenaline1 | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_Adrenaline1.prefab |
| fx_altar_charred_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/crystal/fx_altar_charred_destruction.prefab |
| fx_altar_crystal_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/crystal/fx_altar_crystal_destruction.prefab |
| fx_ArmorStand_pick | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ArmorStand/Fx/fx_ArmorStand_pick.prefab |
| fx_ArtisanPress_Poof | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ArtisanExtension/fx/fx_ArtisanPress_Poof.prefab |
| fx_ashvine_destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Vines_Ashlands/fx/fx_ashvine_destruction.prefab |
| fx_ashvine_leaf_puff | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Vines_Ashlands/fx/fx_ashvine_leaf_puff.prefab |
| fx_asksvin_footstep_run | — | Characters/Asksvin | 4 components; active: yes | c4210710 / Assets/Characters/Asksvin/fx/fx_asksvin_footstep_run.prefab |
| fx_asksvin_footstep_walk | — | Characters/Asksvin | 4 components; active: yes | c4210710 / Assets/Characters/Asksvin/fx/fx_asksvin_footstep_walk.prefab |
| fx_asksvin_pet | — | Characters/Asksvin | 3 components; active: yes | c4210710 / Assets/Characters/Asksvin/fx/fx_asksvin_pet.prefab |
| fx_asksvin_soothed | — | Characters/Asksvin | 3 components; active: yes | c4210710 / Assets/Characters/Asksvin/fx/fx_asksvin_soothed.prefab |
| fx_asksvin_tamed | — | Characters/Asksvin | 3 components; active: yes | c4210710 / Assets/Characters/Asksvin/fx/fx_asksvin_tamed.prefab |
| fx_aspect_death | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_aspect_death.prefab |
| fx_babyseeker_death | — | Characters/Seeker | 5 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/fx_babyseeker_death.prefab |
| fx_babyseeker_hurt | — | Characters/Seeker | 5 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/fx_babyseeker_hurt.prefab |
| fx_backstab | — | Characters/character_effects | 3 components; active: yes | c4210710 / Assets/Characters/character_effects/fx_backstab.prefab |
| fx_BarkaMoveFrost | — | Characters/Barka | 3 components; active: yes | c4210710 / Assets/Characters/Barka/fx/fx_BarkaMoveFrost.prefab |
| fx_bat_death | — | Characters/Bat | 5 components; active: yes | c4210710 / Assets/Characters/Bat/fx/fx_bat_death.prefab |
| fx_bat_hit | — | Characters/Bat | 5 components; active: yes | c4210710 / Assets/Characters/Bat/fx/fx_bat_hit.prefab |
| fx_batteringram_fire | — | GameElements/Cart | 4 components; active: yes | c4210710 / Assets/GameElements/Cart/fx/fx_batteringram_fire.prefab |
| fx_bjorn_death | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/fx/fx_bjorn_death.prefab |
| fx_bjorn_hit | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/fx/fx_bjorn_hit.prefab |
| fx_blastfurnace_blast | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/BlastFurnace/fx/fx_blastfurnace_blast.prefab |
| fx_blobLava_explosion | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSiege/fx/fx_blobLava_explosion.prefab |
| fx_blobtar_tarball_hit | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/fx_blobtar_tarball_hit.prefab |
| fx_block_camshake | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_block_camshake.prefab |
| fx_bloodweapon_hit | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Niedhogg/vfx/fx_bloodweapon_hit.prefab |
| fx_boar_footstep_walk | — | Characters/Boar | 4 components; active: yes | c4210710 / Assets/Characters/Boar/fx/fx_boar_footstep_walk.prefab |
| fx_boar_pet | — | Characters/Boar | 3 components; active: yes | c4210710 / Assets/Characters/Boar/fx/fx_boar_pet.prefab |
| fx_Bonemass_aoe_start | — | Characters/Bonemass | 6 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/fx_Bonemass_aoe_start.prefab |
| fx_BonemawSerpent_poisonbreath | — | Characters/BonemawSerpent | 4 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/fx/fx_BonemawSerpent_poisonbreath.prefab |
| fx_BonemawSerpent_Spit_Hit | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/fx/fx_BonemawSerpent_Spit_Hit.prefab |
| fx_BonfireFlames | — | Effects/Fire | 3 components; active: yes | c4210710 / Assets/Effects/Fire/fx_BonfireFlames.prefab |
| fx_BonfireFlames_Low | — | Effects/Fire | 3 components; active: yes | c4210710 / Assets/Effects/Fire/fx_BonfireFlames_Low.prefab |
| fx_BonusYield | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/fx_BonusYield.prefab |
| fx_bossstone_activate_Bonemass | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_bossstone_activate_Bonemass.prefab |
| fx_bossstone_activate_DragonQueen | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_bossstone_activate_DragonQueen.prefab |
| fx_bossstone_activate_Eikthyr | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_bossstone_activate_Eikthyr.prefab |
| fx_bossstone_activate_TheElder | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_bossstone_activate_TheElder.prefab |
| fx_bossstone_activate_Yagluth | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_bossstone_activate_Yagluth.prefab |
| fx_bossstone_attach | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_bossstone_attach.prefab |
| fx_Brazier_flames | — | Effects/Fire | 1 components; active: yes | c4210710 / Assets/Effects/Fire/fx_Brazier_flames.prefab |
| fx_candle_addfuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Candle/fx/fx_candle_addfuel.prefab |
| fx_candle_off | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Candle/fx/fx_candle_off.prefab |
| fx_candle_on | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Candle/fx/fx_candle_on.prefab |
| fx_chainlightning_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/ChainLightning/fx_chainlightning_hit.prefab |
| fx_chainlightning_spread | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/ChainLightning/fx_chainlightning_spread.prefab |
| fx_chainlightning_spread_red | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/ChainLightning/fx_chainlightning_spread_red.prefab |
| fx_charred_chestglow | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/effects/fx_charred_chestglow.prefab |
| fx_charred_death | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/effects/fx_charred_death.prefab |
| fx_charred_eyeglow | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/effects/fx_charred_eyeglow.prefab |
| fx_charred_firestaff_chargeup | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/effects/fx_charred_firestaff_chargeup.prefab |
| fx_charred_hit | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/effects/fx_charred_hit.prefab |
| fx_charred_summoned_death | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/effects/fx_charred_summoned_death.prefab |
| fx_CharredStone_Destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/TwitcherSpawner/fx/fx_CharredStone_Destruction.prefab |
| fx_CharredStone_Gibs | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/TwitcherSpawner/fx/fx_CharredStone_Gibs.prefab |
| fx_chicken_birth | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/fx/fx_chicken_birth.prefab |
| fx_chicken_death | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/fx/fx_chicken_death.prefab |
| fx_chicken_lay_egg | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/fx/fx_chicken_lay_egg.prefab |
| fx_chicken_pet | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/fx/fx_chicken_pet.prefab |
| fx_Cinder_hit | — | world/SmokeFire | 3 components; active: yes | c4210710 / Assets/world/SmokeFire/fx_Cinder_hit.prefab |
| fx_Cinder_storm_hit | — | world/SmokeFire | 3 components; active: yes | c4210710 / Assets/world/SmokeFire/fx_Cinder_storm_hit.prefab |
| fx_CinderFire_Burn | — | world/SmokeFire | 3 components; active: yes | c4210710 / Assets/world/SmokeFire/fx_CinderFire_Burn.prefab |
| fx_clusterbombstaff_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_clusterbombstaff_hit.prefab |
| fx_clusterbombstaff_splinter_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_clusterbombstaff_splinter_hit.prefab |
| fx_creature_tamed | — | Characters/character_effects | 3 components; active: yes | c4210710 / Assets/Characters/character_effects/fx_creature_tamed.prefab |
| fx_crit | — | Characters/character_effects | 3 components; active: yes | c4210710 / Assets/Characters/character_effects/fx_crit.prefab |
| fx_crystal_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/crystal/fx_crystal_destruction.prefab |
| fx_damage_camshake | — | Characters/Player | 3 components; active: yes | b8689a71 / Assets/Characters/Player/audio/fx_damage_camshake.prefab |
| fx_deadspeak_vo | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/_res/fx/fx_deadspeak_vo.prefab |
| fx_deathsquito_hit | — | Characters/Deathsquito | 5 components; active: yes | c4210710 / Assets/Characters/Deathsquito/fx/fx_deathsquito_hit.prefab |
| fx_deatsquito_death | — | Characters/Deathsquito | 5 components; active: yes | c4210710 / Assets/Characters/Deathsquito/fx/fx_deatsquito_death.prefab |
| fx_dragon_land | — | Characters/Dragon | 4 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/fx_dragon_land.prefab |
| fx_drown | — | Characters/Player | 3 components; active: yes | c4210710 / Assets/Characters/Player/fx/fx_drown.prefab |
| fx_Dverger_death | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_Dverger_death.prefab |
| fx_Dverger_hit | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_Dverger_hit.prefab |
| fx_DvergerMage_Fire_hit | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Fire_hit.prefab |
| fx_DvergerMage_Fire_start | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Fire_start.prefab |
| fx_DvergerMage_Ice_hit | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Ice_hit.prefab |
| fx_DvergerMage_Mistile_attack | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Mistile_attack.prefab |
| fx_DvergerMage_Mistile_die | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Mistile_die.prefab |
| fx_DvergerMage_MistileSpawn | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_MistileSpawn.prefab |
| fx_DvergerMage_Nova_ring | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Nova_ring.prefab |
| fx_DvergerMage_Nova_start | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Nova_start.prefab |
| fx_DvergerMage_Support_hit | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Support_hit.prefab |
| fx_DvergerMage_Support_start | — | Characters/Dverger | 4 components; active: yes | c4210710 / Assets/Characters/Dverger/Fx/fx_DvergerMage_Support_start.prefab |
| fx_dynamite_explosion | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombDynamite/fx/fx_dynamite_explosion.prefab |
| fx_Eat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_Eat.prefab |
| fx_Eat_Black | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_Eat_Black.prefab |
| fx_Eat_Blue | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_Eat_Blue.prefab |
| fx_Eat_Green | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_Eat_Green.prefab |
| fx_Eat_Orange | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_Eat_Orange.prefab |
| fx_Eat_Red | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_Eat_Red.prefab |
| fx_Eat_Yellow | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_Eat_Yellow.prefab |
| fx_egg_splash | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/SeekerEgg/fx/fx_egg_splash.prefab |
| fx_eikthyr_forwardshockwave | — | Characters/Eikthyr | 4 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/fx_eikthyr_forwardshockwave.prefab |
| fx_eikthyr_stomp | — | Characters/Eikthyr | 6 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/fx_eikthyr_stomp.prefab |
| fx_ElakingMole_Sandcloud | — | Characters/ElakingMole | 3 components; active: yes | c4210710 / Assets/Characters/ElakingMole/fx/fx_ElakingMole_Sandcloud.prefab |
| fx_ElakingMole_Wakeup | — | Characters/ElakingMole | 3 components; active: yes | c4210710 / Assets/Characters/ElakingMole/fx/fx_ElakingMole_Wakeup.prefab |
| fx_ember_rain | — | Effects/weather | 4 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/fx_ember_rain.prefab |
| fx_Fader_AttackGlint | — | Characters/Fader | 1 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_AttackGlint.prefab |
| fx_Fader_Bite | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_Bite.prefab |
| fx_fader_chestfire | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_fader_chestfire.prefab |
| fx_fader_clawattack | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_fader_clawattack.prefab |
| fx_Fader_CorpseExplosion | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_CorpseExplosion.prefab |
| fx_fader_firebreath | — | Characters/Fader | 1 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_fader_firebreath.prefab |
| fx_Fader_Fissure_Prespawn | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_Fissure_Prespawn.prefab |
| fx_fader_footstep_ground | — | Characters/Fader | 3 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_fader_footstep_ground.prefab |
| fx_fader_meteor_hit | — | Characters/Fader | 6 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_fader_meteor_hit.prefab |
| fx_fader_meteorsmash | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_fader_meteorsmash.prefab |
| fx_Fader_Ragdoll | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_Ragdoll.prefab |
| fx_Fader_Roar | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_Roar.prefab |
| fx_Fader_Roar_Projectile_Hit | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_Roar_Projectile_Hit.prefab |
| fx_Fader_Spin | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/fx/fx_Fader_Spin.prefab |
| fx_Fading_Bellfragment_Beam | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/crystal/fx_Fading_Bellfragment_Beam.prefab |
| fx_fallenfalkyrie_spin | — | Characters/FallenValkyrie | 4 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/fx/fx_fallenfalkyrie_spin.prefab |
| fx_fallenvalkyrie_death | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/fx/fx_fallenvalkyrie_death.prefab |
| fx_fallenvalkyrie_poisonbreath | — | Characters/FallenValkyrie | 3 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/fx/fx_fallenvalkyrie_poisonbreath.prefab |
| fx_FallenValkyrie_projectile_explosion | — | Characters/FallenValkyrie | 4 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/fx/fx_FallenValkyrie_projectile_explosion.prefab |
| fx_FeastAshlandsEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastAshlandsEat.prefab |
| fx_FeastBlackForestEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastBlackForestEat.prefab |
| fx_FeastMeadowsEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastMeadowsEat.prefab |
| fx_FeastMistlandsEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastMistlandsEat.prefab |
| fx_FeastMountainsEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastMountainsEat.prefab |
| fx_FeastOceansEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastOceansEat.prefab |
| fx_FeastPlainsEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastPlainsEat.prefab |
| fx_FeastSmall | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastSmall.prefab |
| fx_FeastSwampsEat | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastSwampsEat.prefab |
| fx_FeastTemplate | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FeastTemplate.prefab |
| fx_fenring_burning_hand | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_burning_hand.prefab |
| fx_fenring_burning_hand_long | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_burning_hand_long.prefab |
| fx_fenring_flames | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_flames.prefab |
| fx_fenring_frost | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_frost.prefab |
| fx_fenring_frost_hand | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_frost_hand.prefab |
| fx_fenring_frost_hand_aoestart | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_frost_hand_aoestart.prefab |
| fx_fenring_frost_hand_long | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_frost_hand_long.prefab |
| fx_fenring_icenova | — | Characters/Fenring | 4 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/fx_fenring_icenova.prefab |
| fx_fimbulvinter_meteor_hit | — | Characters/GoblinKing | 6 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_fimbulvinter_meteor_hit.prefab |
| fx_fireball_staff_explosion | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_fireball_staff_explosion.prefab |
| fx_fireskeleton_nova | — | Characters/Skeleton | 4 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/fx_fireskeleton_nova.prefab |
| fx_flametalnode_destruction | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/fx/fx_flametalnode_destruction.prefab |
| fx_float_hitwater | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/tools/_res/FishingRod/fx/fx_float_hitwater.prefab |
| fx_float_nibble | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/tools/_res/FishingRod/fx/fx_float_nibble.prefab |
| fx_FoodSteam | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FoodSteam.prefab |
| fx_FoodSteam_Small | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/fx_FoodSteam_Small.prefab |
| fx_footstep_ash_jog | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ash_jog.prefab |
| fx_footstep_ash_land | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ash_land.prefab |
| fx_footstep_ash_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ash_run.prefab |
| fx_footstep_ash_walk | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ash_walk.prefab |
| fx_footstep_climb | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_climb.prefab |
| fx_footstep_dverger_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_dverger_run.prefab |
| fx_footstep_grass_jog | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_grass_jog.prefab |
| fx_footstep_grass_land | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_grass_land.prefab |
| fx_footstep_grass_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_grass_run.prefab |
| fx_footstep_ground_climb | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ground_climb.prefab |
| fx_footstep_ice_land | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ice_land.prefab |
| fx_footstep_ice_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ice_run.prefab |
| fx_footstep_ice_walk | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_ice_walk.prefab |
| fx_footstep_jog | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_jog.prefab |
| fx_footstep_mud_jog | — | Characters/character_effects | 2 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_mud_jog.prefab |
| fx_footstep_mud_run | — | Characters/character_effects | 2 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_mud_run.prefab |
| fx_footstep_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_run.prefab |
| fx_footstep_snow_deep_run | — | Characters/character_effects | 2 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_snow_deep_run.prefab |
| fx_footstep_snow_jog | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_snow_jog.prefab |
| fx_footstep_snow_land | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_snow_land.prefab |
| fx_footstep_snow_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_snow_run.prefab |
| fx_footstep_snow_verydeep_run | — | Characters/character_effects | 2 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_snow_verydeep_run.prefab |
| fx_footstep_snow_walk | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_snow_walk.prefab |
| fx_footstep_stone_jog | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_stone_jog.prefab |
| fx_footstep_stone_land | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_stone_land.prefab |
| fx_footstep_stone_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_stone_run.prefab |
| fx_footstep_tar | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_tar.prefab |
| fx_footstep_water | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_water.prefab |
| fx_footstep_wood_jog | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_wood_jog.prefab |
| fx_footstep_wood_land | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_wood_land.prefab |
| fx_footstep_wood_run | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/footsteps/fx_footstep_wood_run.prefab |
| fx_forge_hammer | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/fx/fx_forge_hammer.prefab |
| fx_frostcloud | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_frostcloud.prefab |
| fx_frostfoundry_addfuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostFoundry/vfx/fx_frostfoundry_addfuel.prefab |
| fx_frostfoundry_additem | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostFoundry/vfx/fx_frostfoundry_additem.prefab |
| fx_frozenking_aspectspawn | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_aspectspawn.prefab |
| fx_frozenking_chain_fury | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chain_fury.prefab |
| fx_frozenking_chain_fury_ascending | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chain_fury_ascending.prefab |
| fx_frozenking_chain_ground_impact_1 | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chain_ground_impact_1.prefab |
| fx_frozenking_chain_ground_impact_2 | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chain_ground_impact_2.prefab |
| fx_frozenking_chain_rush | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chain_rush.prefab |
| fx_frozenking_chain_rush_impact | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chain_rush_impact.prefab |
| fx_frozenking_chain_sparks | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chain_sparks.prefab |
| fx_frozenking_chainwhirl | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_chainwhirl.prefab |
| fx_frozenking_punch_aoe | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_punch_aoe.prefab |
| fx_frozenking_spikerain_hit | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_spikerain_hit.prefab |
| fx_frozenking_spikerain_summoning | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_spikerain_summoning.prefab |
| fx_frozenking_spikesmash | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_spikesmash.prefab |
| fx_frozenking_spin | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_spin.prefab |
| fx_frozenking_tendrils_summoning | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_tendrils_summoning.prefab |
| fx_frozenking_tendrilspawn | — | Characters/FrozenKing | 6 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_frozenking_tendrilspawn.prefab |
| fx_gdking_rootspawn | — | Characters/Greydwarf_king | 6 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/fx_gdking_rootspawn.prefab |
| fx_gjall_death | — | Characters/Gjall | 6 components; active: yes | c4210710 / Assets/Characters/Gjall/fx/fx_gjall_death.prefab |
| fx_gjall_egg_splat | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/fx/fx_gjall_egg_splat.prefab |
| fx_gjall_taunt | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/fx/fx_gjall_taunt.prefab |
| fx_goblinbrute_groundslam | — | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/fx_goblinbrute_groundslam.prefab |
| fx_goblinking_beam_hit | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_beam_hit.prefab |
| fx_goblinking_death | — | Characters/GoblinKing | 6 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_death.prefab |
| fx_goblinking_groundpunch | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_groundpunch.prefab |
| fx_goblinking_hit | — | Characters/GoblinKing | 5 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_hit.prefab |
| fx_goblinking_meteor_hit | — | Characters/GoblinKing | 6 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_meteor_hit.prefab |
| fx_goblinking_nova | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_nova.prefab |
| fx_goblinking_nova_hand | — | Characters/GoblinKing | 1 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_nova_hand.prefab |
| fx_goblinking_vo_beamstart | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_vo_beamstart.prefab |
| fx_goblinking_vo_meteors1 | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_vo_meteors1.prefab |
| fx_goblinking_vo_meteors2 | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_vo_meteors2.prefab |
| fx_goblinking_vo_nova | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_vo_nova.prefab |
| fx_goblinking_vo_wakeup | — | Characters/GoblinKing | 5 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/fx_goblinking_vo_wakeup.prefab |
| fx_GoblinShieldBreak | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_GoblinShieldBreak.prefab |
| fx_GoblinShieldHit | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_GoblinShieldHit.prefab |
| fx_GP_Activation | — | GameElements/StatusEffects | 6 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_GP_Activation.prefab |
| fx_GP_Player | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_GP_Player.prefab |
| fx_GP_Stone | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/fx_GP_Stone.prefab |
| fx_greenroots_projectile_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/fx/fx_greenroots_projectile_hit.prefab |
| fx_guardstone_activate | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/guardstone/fx_guardstone_activate.prefab |
| fx_guardstone_deactivate | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/guardstone/fx_guardstone_deactivate.prefab |
| fx_guardstone_permitted_add | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/guardstone/fx_guardstone_permitted_add.prefab |
| fx_guardstone_permitted_removed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/guardstone/fx_guardstone_permitted_removed.prefab |
| fx_guardstone_shield | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/guardstone/fx_guardstone_shield.prefab |
| fx_hare_death | — | Characters/Hare | 5 components; active: yes | c4210710 / Assets/Characters/Hare/Fx/fx_hare_death.prefab |
| fx_hen_death | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/fx/fx_hen_death.prefab |
| fx_hen_love | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/fx/fx_hen_love.prefab |
| fx_HildirChest_Unlock | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/Effects/fx_HildirChest_Unlock.prefab |
| fx_himminafl_aoe | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/HimminAfl/fx/fx_himminafl_aoe.prefab |
| fx_himminafl_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/HimminAfl/fx/fx_himminafl_hit.prefab |
| fx_hit_camshake | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_hit_camshake.prefab |
| fx_hit_camshake_knife | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_hit_camshake_knife.prefab |
| fx_HotGround | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/fx_HotGround.prefab |
| fx_hottub_addwood | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/HotTub/fx/fx_hottub_addwood.prefab |
| fx_icefloor_destruction | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Caverocks/fx/fx_icefloor_destruction.prefab |
| fx_iceshard_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_iceshard_hit.prefab |
| fx_iceshard_launch | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_iceshard_launch.prefab |
| fx_IceShelf_Damage | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/IceShelf/fx/fx_IceShelf_Damage.prefab |
| fx_icicle_destruction | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Caverocks/fx/fx_icicle_destruction.prefab |
| fx_Immobilize | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_Immobilize.prefab |
| fx_introLand | — | Characters/Player | 2 components; active: yes | c4210710 / Assets/Characters/Player/fx/fx_introLand.prefab |
| fx_invupgrade | — | Characters/Player | 2 components; active: yes | c4210710 / Assets/Characters/Player/fx/fx_invupgrade.prefab |
| fx_ItemSparkles | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_ItemSparkles.prefab |
| fx_jelly_pickup | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/RoyalJelly/fx/fx_jelly_pickup.prefab |
| fx_jotunbane_hit | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/axe/fx/fx_jotunbane_hit.prefab |
| fx_jotunbane_swing | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/axe/fx/fx_jotunbane_swing.prefab |
| fx_JotunWitch_Death | — | Characters/Jotnar | 3 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/fx_JotunWitch_Death.prefab |
| fx_JotunWitch_Dodge | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/fx/fx_JotunWitch_Dodge.prefab |
| fx_JotunWitch_Flying | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/fx_JotunWitch_Flying.prefab |
| fx_JotunWitch_LightningBolt_Charge | — | Characters/Jotnar | 4 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/fx/fx_JotunWitch_LightningBolt_Charge.prefab |
| fx_JotunWitch_LightningBolt_Explosion | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/fx/fx_JotunWitch_LightningBolt_Explosion.prefab |
| fx_JotunWitch_LightningBolt_Trigger | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/fx/fx_JotunWitch_LightningBolt_Trigger.prefab |
| fx_JotunWitch_MagicBlast | — | Characters/Jotnar | 3 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/fx/fx_JotunWitch_MagicBlast.prefab |
| fx_JotunWitch_MagicBlast_Charge | — | Characters/Jotnar | 4 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/fx/fx_JotunWitch_MagicBlast_Charge.prefab |
| fx_jute_carpet_blue_destruction | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/fx_jute_carpet_blue_destruction.prefab |
| fx_jute_carpet_red_destruction | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/fx_jute_carpet_red_destruction.prefab |
| fx_land | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/land/fx_land.prefab |
| fx_land_tar | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/land/fx_land_tar.prefab |
| fx_land_water | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/land/fx_land_water.prefab |
| fx_lavabomb_explosion | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombLava/fx/fx_lavabomb_explosion.prefab |
| fx_lavabubbling | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/fx_lavabubbling.prefab |
| fx_lavasplash_large | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/fx_lavasplash_large.prefab |
| fx_lavasplash_medium | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/fx_lavasplash_medium.prefab |
| fx_lavasplash_small | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/fx_lavasplash_small.prefab |
| fx_leviathan_leave | — | Characters/Leviathan | 4 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/fx_leviathan_leave.prefab |
| fx_leviathan_reaction | — | Characters/Leviathan | 4 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/fx_leviathan_reaction.prefab |
| fx_leviathanLava_leave | — | Characters/Leviathan | 4 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/fx_leviathanLava_leave.prefab |
| fx_leviathanLava_reaction | — | Characters/Leviathan | 4 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/fx_leviathanLava_reaction.prefab |
| fx_Lightning | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_Lightning.prefab |
| fx_Lightning_red | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_Lightning_red.prefab |
| fx_lightningstaff_charge | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/fx/fx_lightningstaff_charge.prefab |
| fx_lightningstaffprojectile_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_lightningstaffprojectile_hit.prefab |
| fx_lightningweapon_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Niedhogg/vfx/fx_lightningweapon_hit.prefab |
| fx_lox_death | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/fx_lox_death.prefab |
| fx_lox_footstep | — | Characters/Lox | 4 components; active: yes | c4210710 / Assets/Characters/Lox/fx/fx_lox_footstep.prefab |
| fx_lox_footstep_run | — | Characters/Lox | 4 components; active: yes | c4210710 / Assets/Characters/Lox/fx/fx_lox_footstep_run.prefab |
| fx_lox_hit | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/fx_lox_hit.prefab |
| fx_lox_pet | — | Characters/Lox | 3 components; active: yes | c4210710 / Assets/Characters/Lox/fx/fx_lox_pet.prefab |
| fx_lox_tamed | — | Characters/Lox | 3 components; active: yes | c4210710 / Assets/Characters/Lox/fx/fx_lox_tamed.prefab |
| fx_loxcalf_death | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/fx_loxcalf_death.prefab |
| fx_moose_birth | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/fx_moose_birth.prefab |
| fx_moose_death | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/fx_moose_death.prefab |
| fx_moose_hit | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/fx_moose_hit.prefab |
| fx_morgen_death | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/fx/fx_morgen_death.prefab |
| fx_morgen_drool | — | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/fx/fx_morgen_drool.prefab |
| fx_morgen_footstep_default | — | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/fx/fx_morgen_footstep_default.prefab |
| fx_morgen_footstep_run | — | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/fx/fx_morgen_footstep_run.prefab |
| fx_morgen_hit | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/fx/fx_morgen_hit.prefab |
| fx_morgen_roll | — | Characters/Morgen | 6 components; active: yes | c4210710 / Assets/Characters/Morgen/fx/fx_morgen_roll.prefab |
| fx_morgen_swipe | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/fx/fx_morgen_swipe.prefab |
| fx_morgenhole_ceilingdrops | — | Effects | 3 components; active: yes | a8945b7c / Assets/Effects/fx_morgenhole_ceilingdrops.prefab |
| fx_morgenhole_mist | — | Effects | 3 components; active: yes | a8945b7c / Assets/Effects/fx_morgenhole_mist.prefab |
| fx_natureweapon_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Niedhogg/vfx/fx_natureweapon_hit.prefab |
| fx_oven_add_food | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/fx_oven_add_food.prefab |
| fx_oven_add_wood | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/fx_oven_add_wood.prefab |
| fx_oven_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/fx_oven_produce.prefab |
| fx_perfectdodge | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_perfectdodge.prefab |
| fx_pheromonebomb_explode | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/fx_pheromonebomb_explode.prefab |
| fx_portal_connected | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/portal/fx/fx_portal_connected.prefab |
| fx_portal_stone_connected | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/portal/fx/fx_portal_stone_connected.prefab |
| fx_Potion_fireresist | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_Potion_fireresist.prefab |
| fx_Potion_frostresist | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_Potion_frostresist.prefab |
| fx_Puke | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/fx_Puke.prefab |
| fx_Queen_BurrowDown | — | Characters/SeekerQueen | 4 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/fx/fx_Queen_BurrowDown.prefab |
| fx_Queen_BurrowUp | — | Characters/SeekerQueen | 4 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/fx/fx_Queen_BurrowUp.prefab |
| fx_Queen_Death | — | Characters/SeekerQueen | 6 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/fx/fx_Queen_Death.prefab |
| fx_queendoor_bolt | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/doors/QueenDoor/fx_queendoor_bolt.prefab |
| fx_queendoor_centerplate | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/doors/QueenDoor/fx_queendoor_centerplate.prefab |
| fx_queendoor_slidestart | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/doors/QueenDoor/fx_queendoor_slidestart.prefab |
| fx_QueenPierceGround | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/fx/fx_QueenPierceGround.prefab |
| fx_radiation_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/eitr/fx_radiation_hit.prefab |
| fx_raven_despawn | — | Characters/Raven | 2 components; active: yes | c4210710 / Assets/Characters/Raven/fx/fx_raven_despawn.prefab |
| fx_redlightning_burst | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_redlightning_burst.prefab |
| fx_redlightning_launch | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_redlightning_launch.prefab |
| fx_refinery_addfuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Destilireitr/fx/fx_refinery_addfuel.prefab |
| fx_refinery_addtissue | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Destilireitr/fx/fx_refinery_addtissue.prefab |
| fx_refinery_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Destilireitr/fx/fx_refinery_destroyed.prefab |
| fx_refinery_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Destilireitr/fx/fx_refinery_produce.prefab |
| fx_RootAshlands | — | Effects | 2 components; active: yes | c4210710 / Assets/Effects/fx_RootAshlands.prefab |
| fx_seeker_death | — | Characters/Seeker | 5 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/fx_seeker_death.prefab |
| fx_seeker_footstep_default | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/fx_seeker_footstep_default.prefab |
| fx_seeker_hurt | — | Characters/Seeker | 5 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/fx_seeker_hurt.prefab |
| fx_seeker_melee_hit | — | Characters/Seeker | 6 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/fx_seeker_melee_hit.prefab |
| fx_seeker_spawn | — | Characters/SeekerQueen | 3 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/spawnhole/fx_seeker_spawn.prefab |
| fx_seekerbrute_death | — | Characters/SeekerBrute | 6 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/fx/fx_seekerbrute_death.prefab |
| fx_seekerbrute_footstep_default | — | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/fx/fx_seekerbrute_footstep_default.prefab |
| fx_seekerbrute_footstep_ground | — | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/fx/fx_seekerbrute_footstep_ground.prefab |
| fx_shaman_fireball_expl | — | Characters/GoblinShaman | 5 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/fx_shaman_fireball_expl.prefab |
| fx_shaman_protect | — | Characters/GoblinShaman | 3 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/fx_shaman_protect.prefab |
| fx_shield_start | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_shield_start.prefab |
| fx_shield_start_frost | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_shield_start_frost.prefab |
| fx_ShieldCharge_1 | — | Effects/shieldcharges | 3 components; active: yes | c4210710 / Assets/Effects/shieldcharges/fx_ShieldCharge_1.prefab |
| fx_ShieldCharge_2 | — | Effects/shieldcharges | 3 components; active: yes | c4210710 / Assets/Effects/shieldcharges/fx_ShieldCharge_2.prefab |
| fx_ShieldCharge_3 | — | Effects/shieldcharges | 3 components; active: yes | c4210710 / Assets/Effects/shieldcharges/fx_ShieldCharge_3.prefab |
| fx_ShieldCharge_4 | — | Effects/shieldcharges | 3 components; active: yes | c4210710 / Assets/Effects/shieldcharges/fx_ShieldCharge_4.prefab |
| fx_ShieldCharge_5 | — | Effects/shieldcharges | 3 components; active: yes | c4210710 / Assets/Effects/shieldcharges/fx_ShieldCharge_5.prefab |
| fx_shieldgenerator_attack | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/fx_shieldgenerator_attack.prefab |
| fx_shieldgenerator_domehit | — | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/fx_shieldgenerator_domehit.prefab |
| fx_siegebomb_explosion | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSiege/fx/fx_siegebomb_explosion.prefab |
| fx_skeleton_pet | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/fx_skeleton_pet.prefab |
| fx_sledge_demolisher_hit | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Demolisher/fx/fx_sledge_demolisher_hit.prefab |
| fx_slide | — | Characters/character_effects | 2 components; active: yes | c4210710 / Assets/Characters/character_effects/fx_slide.prefab |
| fx_snow_wall_break | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/fx_snow_wall_break.prefab |
| fx_snowshovel | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/fx_snowshovel.prefab |
| fx_snowwalkpiece | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/fx_snowwalkpiece.prefab |
| fx_StaffShield_Break | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/shield/fx_StaffShield_Break.prefab |
| fx_StaffShield_Hit | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/shield/fx_StaffShield_Hit.prefab |
| fx_stone_L_destroyed | — | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_stone_L_destroyed.prefab |
| fx_stone_R_destroyed | — | Characters/FrozenKing | 3 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_stone_R_destroyed.prefab |
| fx_summon_skeleton | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_summon_skeleton.prefab |
| fx_summon_skeleton_spawn | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_summon_skeleton_spawn.prefab |
| fx_summon_spirit_spawn | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_summon_spirit_spawn.prefab |
| fx_summon_start | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_summon_start.prefab |
| fx_summon_troll | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_summon_troll.prefab |
| fx_summon_twitcher_spawn | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/fx_summon_twitcher_spawn.prefab |
| fx_sw_addflax | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/SpinningWheel/fx/fx_sw_addflax.prefab |
| fx_sw_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/SpinningWheel/fx/fx_sw_produce.prefab |
| fx_swing_camshake | — | Effects | 3 components; active: yes | c4210710 / Assets/Effects/fx_swing_camshake.prefab |
| fx_tar_bubbles | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Tar/fx/fx_tar_bubbles.prefab |
| fx_tendril_death | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/fx_tendril_death.prefab |
| fx_tentaroot_death | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/fx_tentaroot_death.prefab |
| fx_tick_death | — | Characters/Tick | 5 components; active: yes | c4210710 / Assets/Characters/Tick/Fx/fx_tick_death.prefab |
| fx_TickBloodHit | — | Characters/Tick | 5 components; active: yes | c4210710 / Assets/Characters/Tick/Fx/fx_TickBloodHit.prefab |
| fx_tombstone_destroyed | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/fx/fx_tombstone_destroyed.prefab |
| fx_Torch_Basic | — | Effects/Fire | 3 components; active: yes | c4210710 / Assets/Effects/Fire/fx_Torch_Basic.prefab |
| fx_Torch_Blue | — | Effects/Fire | 3 components; active: yes | c4210710 / Assets/Effects/Fire/fx_Torch_Blue.prefab |
| fx_Torch_Carried | — | Effects/Fire | 3 components; active: yes | c4210710 / Assets/Effects/Fire/fx_Torch_Carried.prefab |
| fx_Torch_Green | — | Effects/Fire | 3 components; active: yes | c4210710 / Assets/Effects/Fire/fx_Torch_Green.prefab |
| fx_Torch_Morkhalla | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/fx_Torch_Morkhalla.prefab |
| fx_totem_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/fx_totem_destroyed.prefab |
| fx_trap_arm | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Trap/fx_trap_arm.prefab |
| fx_trap_trigger | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Trap/fx_trap_trigger.prefab |
| fx_troll_love | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/fx/fx_troll_love.prefab |
| fx_TrollUndead_Gibs | — | Characters/TrollSkeleton | 4 components; active: yes | c4210710 / Assets/Characters/TrollSkeleton/vfx/fx_TrollUndead_Gibs.prefab |
| fx_turret_addammo | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/fx/fx_turret_addammo.prefab |
| fx_turret_fire | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/fx/fx_turret_fire.prefab |
| fx_turret_newtarget | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/fx/fx_turret_newtarget.prefab |
| fx_turret_notarget | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/fx/fx_turret_notarget.prefab |
| fx_turret_reload | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/fx/fx_turret_reload.prefab |
| fx_turret_warmup | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/fx/fx_turret_warmup.prefab |
| fx_unbjorn_death | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/fx/fx_unbjorn_death.prefab |
| fx_unbjorn_hit | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/fx/fx_unbjorn_hit.prefab |
| fx_unstablelavarock_explosion | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/fx/fx_unstablelavarock_explosion.prefab |
| fx_UpgradeStation_Fail | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/fx_UpgradeStation_Fail.prefab |
| fx_UpgradeStation_Success | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/fx_UpgradeStation_Success.prefab |
| fx_vinegreen_destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Vines_Green/fx/fx_vinegreen_destruction.prefab |
| fx_vines_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Vines/fx/fx_vines_hit.prefab |
| fx_WaterImpact_Big | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/fx_WaterImpact_Big.prefab |
| fx_wolf_footstep_snow_run | — | Characters/Wolf | 4 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/fx_wolf_footstep_snow_run.prefab |
| fx_wolf_pet | — | Characters/Wolf | 3 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/fx_wolf_pet.prefab |
| fx_writhan_explosion | — | Characters/Writhan | 6 components; active: yes | c4210710 / Assets/Characters/Writhan/attacks/fx_writhan_explosion.prefab |
| GamepadFeatures | — | Systems | 4 components; active: yes | c4210710 / Assets/Systems/GamepadFeatures.prefab |
| GamepadMap | — | UI/prefabs | 3 components; active: yes | c4210710 / Assets/UI/prefabs/GamepadMap.prefab |
| GamepadTab | — | UI/prefabs | 6 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/GamepadTab.prefab |
| GameplayTab | — | UI/prefabs | 6 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/GameplayTab.prefab |
| gas_flame | — | world/Props | 2 components; active: yes | 3303f8a1 / Assets/world/Props/gas_flame.prefab |
| Gateway | — | GameElements/InteriorStuff | 3 components; active: yes | 3e5986a6 / Assets/GameElements/InteriorStuff/Gateway.prefab |
| gd_king | The Elder | Characters/Greydwarf_king | 10 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/gd_king.prefab |
| gd_king_punch | jaws | Characters/Greydwarf_king | 3 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/gd_king_punch.prefab |
| gd_king_rootspawn | spawn | Characters/Greydwarf_king | 3 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/gd_king_rootspawn.prefab |
| gd_king_scream | scream | Characters/Greydwarf_king | 3 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/gd_king_scream.prefab |
| gd_king_shoot | shaman attack | Characters/Greydwarf_king | 3 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/gd_king_shoot.prefab |
| gd_king_stomp | jaws | Characters/Greydwarf_king | 3 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/gd_king_stomp.prefab |
| GDKing | — | world/Locations | 3 components; active: yes | 5f09202f / Assets/world/Locations/BlackForest/GDKing.prefab |
| gdking_Ragdoll | — | Characters/Greydwarf_king | 3 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/gdking_Ragdoll.prefab |
| gdking_root_projectile | — | Characters/Greydwarf_king | 4 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/gdking_root_projectile.prefab |
| GemstoneBlue | Iolite | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/GemstoneBlue.prefab |
| GemstoneGreen | Jade | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/GemstoneGreen.prefab |
| GemstoneRed | Bloodstone | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/GemstoneRed.prefab |
| GenericMoldUncooked | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/GenericMoldUncooked.prefab |
| Ghost | Ghost | Characters/Ghost | 11 components; active: yes | c4210710 / Assets/Characters/Ghost/Ghost.prefab |
| Ghost_attack | jaws | Characters/Ghost | 3 components; active: yes | c4210710 / Assets/Characters/Ghost/misc/Ghost_attack.prefab |
| Ghost_old | The Void | Characters/Ghost | 11 components; active: yes | c4210710 / Assets/Characters/Ghost/Ghost_old.prefab |
| Ghost_sleeping | Ghost | Characters/Ghost | 11 components; active: yes | c4210710 / Assets/Characters/Ghost/Ghost_sleeping.prefab |
| Ghost_Void | The Void | Characters/Ghost | 11 components; active: yes | c4210710 / Assets/Characters/Ghost/Ghost_Void.prefab |
| GhostSkull | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/misc/GhostSkull.prefab |
| giant_arm | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_arm.prefab |
| giant_brain | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_brain.prefab |
| giant_brain_frac | Soft Tissue | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_brain_frac.prefab |
| giant_helmet1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_helmet1.prefab |
| giant_helmet1_destruction | Ancient Armour | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_helmet1_destruction.prefab |
| giant_helmet2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_helmet2.prefab |
| giant_helmet2_destruction | Ancient Armour | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_helmet2_destruction.prefab |
| giant_ribs | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_ribs.prefab |
| giant_ribs_frac | Petrified Bone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_ribs_frac.prefab |
| giant_skull | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_skull.prefab |
| giant_skull_frac | Petrified Bone | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_skull_frac.prefab |
| giant_sword1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_sword1.prefab |
| giant_sword1_destruction | Ancient Sword | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_sword1_destruction.prefab |
| giant_sword2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_sword2.prefab |
| giant_sword2_destruction | Ancient Sword | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/giant_sword2_destruction.prefab |
| GiantBloodSack | Blood Clot | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/GiantBloodSack.prefab |
| Gjall | Gjall | Characters/Gjall | 9 components; active: yes | c4210710 / Assets/Characters/Gjall/Gjall.prefab |
| gjall_attack_egg | egg drop | Characters/Gjall | 3 components; active: yes | c4210710 / Assets/Characters/Gjall/attacks/gjall_attack_egg.prefab |
| gjall_attack_shake | gjall shake | Characters/Gjall | 3 components; active: yes | c4210710 / Assets/Characters/Gjall/attacks/gjall_attack_shake.prefab |
| gjall_attack_spit | gjall spit | Characters/Gjall | 3 components; active: yes | c4210710 / Assets/Characters/Gjall/attacks/gjall_attack_spit.prefab |
| gjall_attack_taunt | gjall taunt | Characters/Gjall | 3 components; active: yes | c4210710 / Assets/Characters/Gjall/attacks/gjall_attack_taunt.prefab |
| gjall_egg_projectile | — | Characters/Gjall | 4 components; active: yes | c4210710 / Assets/Characters/Gjall/attacks/gjall_egg_projectile.prefab |
| gjall_egg_spawn | — | Characters/Gjall | 2 components; active: yes | c4210710 / Assets/Characters/Gjall/attacks/gjall_egg_spawn.prefab |
| gjall_spit_projectile | — | Characters/Gjall | 4 components; active: yes | c4210710 / Assets/Characters/Gjall/attacks/gjall_spit_projectile.prefab |
| GlowingMushroom | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/mushrooms/GlowingMushroom.prefab |
| GlowWorm | Luminous Larva | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/GlowWorm.prefab |
| Goblin | Fuling | Characters/Goblin | 12 components; active: yes | c4210710 / Assets/Characters/Goblin/Goblin.prefab |
| goblin_banner | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_banner.prefab |
| goblin_bed | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_bed.prefab |
| Goblin_DN_Dragdoll | — | Characters/Goblin | 4 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/Goblin_DN_Dragdoll.prefab |
| Goblin_Dragdoll | — | Characters/Goblin | 4 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/Goblin_Dragdoll.prefab |
| goblin_fence | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_fence.prefab |
| Goblin_Gem | Riktig Fuling | Characters/Goblin | 12 components; active: yes | c4210710 / Assets/Characters/Goblin/Goblin_Gem.prefab |
| goblin_pole | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_pole.prefab |
| goblin_pole_small | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_pole_small.prefab |
| goblin_roof_45d | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_roof_45d.prefab |
| goblin_roof_45d_corner | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_roof_45d_corner.prefab |
| goblin_roof_cap | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_roof_cap.prefab |
| goblin_stairs | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_stairs.prefab |
| goblin_stepladder | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_stepladder.prefab |
| goblin_strawpile | — | world/dungeon | 4 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_strawpile.prefab |
| goblin_totempole | Fuling Totem | world/dungeon | 7 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_totempole.prefab |
| goblin_trashpile | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_trashpile.prefab |
| goblin_trashpile_destruction | — | world/dungeon | 3 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_trashpile_destruction.prefab |
| goblin_woodwall_1m | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_woodwall_1m.prefab |
| goblin_woodwall_2m | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_woodwall_2m.prefab |
| goblin_woodwall_2m_ribs | — | world/dungeon | 6 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/goblin_woodwall_2m_ribs.prefab |
| GoblinArcher | Fuling | Characters/Goblin | 12 components; active: yes | c4210710 / Assets/Characters/Goblin/GoblinArcher.prefab |
| GoblinArmband | Iron plate armor | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinArmband.prefab |
| GoblinBrute | Fuling Berserker | Characters/GoblinBrute | 11 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/GoblinBrute.prefab |
| GoblinBrute_ArmGuard | Iron plate armor | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/misc/GoblinBrute_ArmGuard.prefab |
| GoblinBrute_Attack | Brute sword | Characters/GoblinBrute | 7 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/attacks/GoblinBrute_Attack.prefab |
| GoblinBrute_Backbones | Iron plate armor | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/misc/GoblinBrute_Backbones.prefab |
| GoblinBrute_ExecutionerCap | Iron plate armor | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/misc/GoblinBrute_ExecutionerCap.prefab |
| GoblinBrute_Hildir | &lt;color=orange&gt;Thungr&lt;/color&gt; | Characters/GoblinBruteBros | 11 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/GoblinBrute_Hildir.prefab |
| GoblinBrute_Hildir_ragdoll | — | Characters/GoblinBruteBros | 4 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/fx/GoblinBrute_Hildir_ragdoll.prefab |
| GoblinBrute_HipCloth | Iron plate armor | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/misc/GoblinBrute_HipCloth.prefab |
| GoblinBrute_LegBones | Iron plate armor | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/misc/GoblinBrute_LegBones.prefab |
| GoblinBrute_ragdoll | — | Characters/GoblinBrute | 4 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/GoblinBrute_ragdoll.prefab |
| GoblinBrute_RageAttack | Brute sword | Characters/GoblinBrute | 7 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/attacks/GoblinBrute_RageAttack.prefab |
| GoblinBrute_ShoulderGuard | Iron plate armor | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/misc/GoblinBrute_ShoulderGuard.prefab |
| GoblinBrute_Taunt | Brute taunt | Characters/GoblinBrute | 7 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/attacks/GoblinBrute_Taunt.prefab |
| GoblinBruteBros | &lt;color=orange&gt;Zil &amp; Thungr&lt;/color&gt; | Characters/GoblinBruteBros | 11 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/GoblinBruteBros.prefab |
| GoblinBruteBros_Attack | Brute sword | Characters/GoblinBrute | 7 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/attacks/GoblinBruteBros_Attack.prefab |
| GoblinBruteBros_nochest | &lt;color=orange&gt;Zil &amp; Thungr&lt;/color&gt; | Characters/GoblinBruteBros | 11 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/GoblinBruteBros_nochest.prefab |
| GoblinBruteBros_RageAttack | Brute sword | Characters/GoblinBrute | 7 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/attacks/GoblinBruteBros_RageAttack.prefab |
| GoblinClub | Club | Characters/Goblin | 8 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinClub.prefab |
| GoblinClubDeepNorth | Club | Characters/Goblin | 8 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinClubDeepNorth.prefab |
| GoblinDeepNorth | Captive Fuling | Characters/Goblin | 12 components; active: yes | c4210710 / Assets/Characters/Goblin/GoblinDeepNorth.prefab |
| GoblinHelmet | Iron plate armor | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinHelmet.prefab |
| GoblinKing | Yagluth | Characters/GoblinKing | 11 components; active: yes | c4210710 / Assets/Characters/GoblinKing/GoblinKing.prefab |
| GoblinKing | — | world/Locations | 2 components; active: yes | 32fd94e5 / Assets/world/Locations/Heath/GoblinKing.prefab |
| GoblinKing_Beam | dragon breath | Characters/GoblinKing | 3 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/GoblinKing_Beam.prefab |
| GoblinKing_Meteors | spawn | Characters/GoblinKing | 3 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/GoblinKing_Meteors.prefab |
| GoblinKing_Nova | slap | Characters/GoblinKing | 3 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/GoblinKing_Nova.prefab |
| GoblinKing_ragdoll | — | Characters/GoblinKing | 3 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/GoblinKing_ragdoll.prefab |
| GoblinKing_Taunt | scream | Characters/GoblinKing | 3 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/GoblinKing_Taunt.prefab |
| goblinking_totemholder | Offering Bowl | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/offeraltar/goblinking_totemholder.prefab |
| GoblinLegband | Iron plate armor | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinLegband.prefab |
| GoblinLoin | Iron plate armor | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinLoin.prefab |
| GoblinShaman | Fuling Shaman | Characters/GoblinShaman | 12 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/GoblinShaman.prefab |
| GoblinShaman_attack_fireball | fireballattack | Characters/GoblinShaman | 3 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/attacks/GoblinShaman_attack_fireball.prefab |
| GoblinShaman_attack_fireball_hildir | fireballattack | Characters/GoblinBruteBros | 3 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/attacks/GoblinShaman_attack_fireball_hildir.prefab |
| GoblinShaman_attack_poke | Club | Characters/GoblinShaman | 8 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/attacks/GoblinShaman_attack_poke.prefab |
| GoblinShaman_attack_protect | heal | Characters/GoblinShaman | 3 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/attacks/GoblinShaman_attack_protect.prefab |
| GoblinShaman_attack_protect_hildir | heal | Characters/GoblinBruteBros | 3 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/attacks/GoblinShaman_attack_protect_hildir.prefab |
| GoblinShaman_Headdress_antlers | Club | Characters/GoblinShaman | 8 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/misc/GoblinShaman_Headdress_antlers.prefab |
| GoblinShaman_Headdress_feathers | Club | Characters/GoblinShaman | 8 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/misc/GoblinShaman_Headdress_feathers.prefab |
| GoblinShaman_Hildir | &lt;color=orange&gt;Zil&lt;/color&gt; | Characters/GoblinBruteBros | 12 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/GoblinShaman_Hildir.prefab |
| GoblinShaman_Hildir_nochest | &lt;color=orange&gt;Zil&lt;/color&gt; | Characters/GoblinBruteBros | 12 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/GoblinShaman_Hildir_nochest.prefab |
| GoblinShaman_Hildir_ragdoll | — | Characters/GoblinBruteBros | 4 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/fx/GoblinShaman_Hildir_ragdoll.prefab |
| GoblinShaman_projectile_fireball | — | Characters/GoblinShaman | 4 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/attacks/GoblinShaman_projectile_fireball.prefab |
| GoblinShaman_protect_aoe | — | Characters/GoblinShaman | 5 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/attacks/GoblinShaman_protect_aoe.prefab |
| GoblinShaman_ragdoll | — | Characters/GoblinShaman | 4 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/GoblinShaman_ragdoll.prefab |
| GoblinShaman_Staff_Bones | Club | Characters/GoblinShaman | 8 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/misc/GoblinShaman_Staff_Bones.prefab |
| GoblinShaman_Staff_Feathers | Club | Characters/GoblinShaman | 8 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/misc/GoblinShaman_Staff_Feathers.prefab |
| GoblinShaman_Staff_Hildir | Club | Characters/GoblinBruteBros | 8 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/GoblinShaman_Staff_Hildir.prefab |
| GoblinShoulders | Iron plate armor | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinShoulders.prefab |
| GoblinSpear | Flint spear | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinSpear.prefab |
| GoblinSpear_projectile | — | Characters/Goblin | 4 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinSpear_projectile.prefab |
| GoblinSpearDeepNorth | Flint spear | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinSpearDeepNorth.prefab |
| GoblinSpearDeepNorth_projectile | — | Characters/Goblin | 4 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinSpearDeepNorth_projectile.prefab |
| GoblinSword | Bronze sword | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinSword.prefab |
| GoblinSwordDeepNorth | Bronze sword | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinSwordDeepNorth.prefab |
| GoblinTorch | Torch | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinTorch.prefab |
| GoblinTorchDeepNorth | Torch | Characters/Goblin | 7 components; active: yes | c4210710 / Assets/Characters/Goblin/misc/GoblinTorchDeepNorth.prefab |
| GoblinTotem | Fuling Totem | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/GoblinTotem.prefab |
| Gold | Bloodgold | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Gold.prefab |
| GoldOre | Petrified Tissue | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/GoldOre.prefab |
| goldvein | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/goldvein.prefab |
| goldvein_frac | Petrified Gammeltroll | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/goldvein_frac.prefab |
| GraphicsTab | — | UI/prefabs | 7 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/GraphicsTab.prefab |
| GrapplingHook | Grappling Hook | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/GrapplingHook.prefab |
| GrapplingPoint | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/GrapplingHook/GrapplingPoint.prefab |
| GrapplingPointSecondary | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/GrapplingHook/GrapplingPointSecondary.prefab |
| grasscross_heath_green | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/old/grasscross_heath_green.prefab |
| Grausten | Grausten | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Grausten.prefab |
| grausten_pile | Grausten Pile | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/grausten_pile.prefab |
| GraveStone_Broken_CharredTwitcherNest | — | Characters/TheCharred | 6 components; active: yes | c4210710 / Assets/Characters/TheCharred/GraveStone_Broken_CharredTwitcherNest.prefab |
| GraveStone_Broken_World | — | Characters/TheCharred | 6 components; active: yes | c4210710 / Assets/Characters/TheCharred/GraveStone_Broken_World.prefab |
| GraveStone_CharredFaderLocation | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/GraveStone_CharredFaderLocation.prefab |
| GraveStone_CharredTwitcherNest | — | Characters/TheCharred | 6 components; active: yes | c4210710 / Assets/Characters/TheCharred/GraveStone_CharredTwitcherNest.prefab |
| GraveStone_Elite_Broken_CharredTwitcherNest | — | Characters/TheCharred | 6 components; active: yes | c4210710 / Assets/Characters/TheCharred/GraveStone_Elite_Broken_CharredTwitcherNest.prefab |
| GraveStone_Elite_CharredTwitcherNest | — | Characters/TheCharred | 6 components; active: yes | c4210710 / Assets/Characters/TheCharred/GraveStone_Elite_CharredTwitcherNest.prefab |
| Greydwarf | Greydwarf | Characters/GreyDwarf | 10 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Greydwarf.prefab |
| Greydwarf_attack | jaws | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_attack.prefab |
| Greydwarf_attack_frozen | jaws | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_attack_frozen.prefab |
| Greydwarf_Elite | Greydwarf Brute | Characters/GreyDwarf | 10 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Greydwarf_Elite.prefab |
| Greydwarf_elite_attack | jaws | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_elite_attack.prefab |
| Greydwarf_elite_ragdoll | — | Characters/GreyDwarf | 4 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/Greydwarf_elite_ragdoll.prefab |
| Greydwarf_Frozen | Greydwarf | Characters/GreyDwarf | 10 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Greydwarf_Frozen.prefab |
| Greydwarf_ragdoll | — | Characters/GreyDwarf | 4 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/Greydwarf_ragdoll.prefab |
| Greydwarf_ragdoll_frozen | — | Characters/GreyDwarf | 4 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/Greydwarf_ragdoll_frozen.prefab |
| Greydwarf_Root | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GreyDwarfSpawner/Greydwarf_Root.prefab |
| Greydwarf_Shaman | Greydwarf Shaman | Characters/GreyDwarf | 10 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Greydwarf_Shaman.prefab |
| Greydwarf_shaman_attack | shaman attack | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_shaman_attack.prefab |
| Greydwarf_shaman_attack_frozen | shaman attack | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_shaman_attack_frozen.prefab |
| Greydwarf_Shaman_Frozen | Greydwarf Shaman | Characters/GreyDwarf | 10 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Greydwarf_Shaman_Frozen.prefab |
| Greydwarf_shaman_heal | heal | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_shaman_heal.prefab |
| Greydwarf_shaman_heal_frozen | heal | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_shaman_heal_frozen.prefab |
| Greydwarf_Shaman_ragdoll | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/Greydwarf_Shaman_ragdoll.prefab |
| Greydwarf_Shaman_ragdoll_frozen | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/Greydwarf_Shaman_ragdoll_frozen.prefab |
| Greydwarf_Surprise | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/Greydwarf_Surprise.prefab |
| Greydwarf_throw | throw stone | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_throw.prefab |
| Greydwarf_throw_frozen | throw stone | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_throw_frozen.prefab |
| Greydwarf_throw_projectile | — | Characters/GreyDwarf | 4 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_throw_projectile.prefab |
| Greydwarf_throw_projectile_frozen | — | Characters/GreyDwarf | 4 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greydwarf_throw_projectile_frozen.prefab |
| GreydwarfEye | Greydwarf Eye | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/GreydwarfEye.prefab |
| GreydwarfSurprise | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/misc/GreydwarfSurprise.prefab |
| Greyling | Greyling | Characters/GreyDwarf | 10 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Greyling.prefab |
| Greyling_attack | jaws | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/Greyling_attack.prefab |
| Greyling_ragdoll | — | Characters/GreyDwarf | 4 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/Greyling_ragdoll.prefab |
| Group | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/Radial/elements/Group.prefab |
| guard_stone | Ward | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/guard_stone.prefab |
| guard_stone_test | Guard stone | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/guardstone/oldmodel/guard_stone_test.prefab |
| Guck | Guck | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Guck.prefab |
| GuckSack | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/GuckSack/GuckSack.prefab |
| GuckSack_small | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/GuckSack/GuckSack_small.prefab |
| GUIButton | — | UI/GUI | 5 components; active: yes | c4210710 / Assets/UI/GUI/GUIButton.prefab |
| GUIButtonWithKeyHint | — | UI/GUI | 6 components; active: yes | c4210710 / Assets/UI/GUI/GUIButtonWithKeyHint.prefab |
| GuidePoint | — | Characters/Raven | 2 components; active: yes | c4210710 / Assets/Characters/Raven/GuidePoint.prefab |
| GUIDropDown | — | UI/GUI | 4 components; active: yes | c4210710 / Assets/UI/GUI/GUIDropDown.prefab |
| GUIInputField | — | UI/GUI | 4 components; active: yes | 8d5dbad8 / Assets/UI/GUI/GUIInputField.prefab |
| GUISlider | — | UI/GUI | 3 components; active: yes | c4210710 / Assets/UI/GUI/GUISlider.prefab |
| GUISliderWithLabel | — | UI/GUI | 3 components; active: yes | c4210710 / Assets/UI/GUI/GUISliderWithLabel.prefab |
| GUISliderWithLabelAndValue | — | UI/GUI | 3 components; active: yes | c4210710 / Assets/UI/GUI/GUISliderWithLabelAndValue.prefab |
| GUIStepper | — | UI/GUI | 3 components; active: yes | c4210710 / Assets/UI/GUI/GUIStepper.prefab |
| GUITabButton | — | UI/GUI | 5 components; active: yes | c4210710 / Assets/UI/GUI/GUITabButton.prefab |
| GUITabButtonWithKeyHint | — | UI/GUI | 5 components; active: yes | c4210710 / Assets/UI/GUI/GUITabButtonWithKeyHint.prefab |
| GUIText | — | UI/GUI | 3 components; active: yes | c4210710 / Assets/UI/GUI/GUIText.prefab |
| GUIToggle | — | UI/GUI | 3 components; active: yes | c4210710 / Assets/UI/GUI/GUIToggle.prefab |
| GUIToggleWithLabel | — | UI/GUI | 3 components; active: yes | c4210710 / Assets/UI/GUI/GUIToggleWithLabel.prefab |
| Hair1 | Windswept | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair1.prefab |
| Hair10 | Side Swept | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair10.prefab |
| Hair10_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair10_2.prefab |
| Hair11 | Long Braid | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair11.prefab |
| Hair11_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair11_2.prefab |
| Hair11_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair11_3.prefab |
| Hair12 | Matronly | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair12.prefab |
| Hair12_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair12_2.prefab |
| Hair13 | Twin Braids | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair13.prefab |
| Hair13_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair13_2.prefab |
| Hair13_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair13_3.prefab |
| Hair14 | Speed Demon | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair14.prefab |
| Hair14_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair14_2.prefab |
| Hair15 | Pulled Back Curls | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair15.prefab |
| Hair15_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair15_2.prefab |
| Hair15_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair15_3.prefab |
| Hair16 | Gathered Braids | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair16.prefab |
| Hair16_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair16_2.prefab |
| Hair17 | Neat Braids | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair17.prefab |
| Hair17_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair17_2.prefab |
| Hair18 | Royal Braids | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair18.prefab |
| Hair18_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair18_2.prefab |
| Hair19 | Painter Curls | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair19.prefab |
| Hair2 | High Ponytail | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair2.prefab |
| Hair20 | Tidy Curls | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair20.prefab |
| Hair21 | Twin Buns | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair21.prefab |
| Hair21_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair21_2.prefab |
| Hair22 | Single Bun | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair22.prefab |
| Hair22_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair22_2.prefab |
| Hair23 | Short Curls | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair23.prefab |
| Hair24 | Shaved and Braided | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair24.prefab |
| Hair24_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair24_2.prefab |
| Hair24_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair24_3.prefab |
| Hair25 | Knot | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair25.prefab |
| Hair26 | Short Locs | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair26.prefab |
| Hair27 | Strength Braids | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair27.prefab |
| Hair27_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair27_2.prefab |
| Hair27_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair27_3.prefab |
| Hair28 | Merchant&#x27;s Braid | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair28.prefab |
| Hair28_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair28_2.prefab |
| Hair28_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair28_3.prefab |
| Hair29 | Tucked Back | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair29.prefab |
| Hair29_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair29_2.prefab |
| Hair3 | Pigtails | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair3.prefab |
| Hair30 | Loose Waves | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair30.prefab |
| Hair30_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair30_2.prefab |
| Hair30_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair30_3.prefab |
| Hair31 | Gathered Locs | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair31.prefab |
| Hair31_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair31_2.prefab |
| Hair31_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair31_3.prefab |
| Hair32 | Mullet | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair32.prefab |
| Hair32_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair32_2.prefab |
| Hair32_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair32_3.prefab |
| Hair33 | Vinland Shave | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair33.prefab |
| Hair33_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair33_2.prefab |
| Hair34 | Castellan | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair34.prefab |
| Hair34_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair34_2.prefab |
| Hair34_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair34_3.prefab |
| Hair35 | Champion | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair35.prefab |
| Hair35_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair35_2.prefab |
| Hair35_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair35_3.prefab |
| Hair36 | Chronicler | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair36.prefab |
| Hair36_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair36_2.prefab |
| Hair36_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair36_3.prefab |
| Hair37 | Sunbringer | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair37.prefab |
| Hair37_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair37_2.prefab |
| Hair37_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair37_3.prefab |
| Hair38 | Masculine | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair38.prefab |
| Hair38_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair38_2.prefab |
| Hair38_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair38_3.prefab |
| Hair3_2 | Pigtails | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair3_2.prefab |
| Hair3_3 | Pigtails | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair3_3.prefab |
| Hair4 | Low Ponytail | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair4.prefab |
| Hair4_2 | Pigtails | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair4_2.prefab |
| Hair4_3 | Pigtails | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair4_3.prefab |
| Hair5 | Short | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair5.prefab |
| Hair5_2 | Pigtails | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair5_2.prefab |
| Hair6 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair6.prefab |
| Hair6_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair6_2.prefab |
| Hair6_3 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair6_3.prefab |
| Hair7 | Dragonslayer | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair7.prefab |
| Hair7_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair7_2.prefab |
| Hair8 | Parted | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair8.prefab |
| Hair8_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair8_2.prefab |
| Hair9 | Old One-Eye | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair9.prefab |
| Hair9_2 | Long and Loose | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/Hair9_2.prefab |
| HairNone | No Hair | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/customizations/hairs/HairNone.prefab |
| Haldor | Haldor | Characters/TraderHaldor | 5 components; active: yes | c4210710 / Assets/Characters/TraderHaldor/Haldor.prefab |
| HalfBurried_ForestCrypt | — | world/Locations | 2 components; active: yes | 9ab8cd61 / Assets/world/Locations/BlackForest/HalfBurried_ForestCrypt.prefab |
| halfBurried_forestcrypt_Bend3 | — | world/Rooms | 2 components; active: yes | 9ab8cd61 / Assets/world/Rooms/halfBurriedCrypt/halfBurried_forestcrypt_Bend3.prefab |
| halfBurried_forestcrypt_Corridor4 | — | world/Rooms | 2 components; active: yes | 9ab8cd61 / Assets/world/Rooms/halfBurriedCrypt/halfBurried_forestcrypt_Corridor4.prefab |
| Halstein | Halstein | Characters/Lox | 3 components; active: yes | 17a773de / Assets/Characters/Lox/Halstein.prefab |
| Hammer | Hammer | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/tools/Hammer.prefab |
| Hammer | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/Radial/elements/Hammer.prefab |
| hanging_hairstrands | Fenris Hair | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/hanging_hairstrands.prefab |
| Hanging_RoyalJelly | — | world/Props | 2 components; active: yes | 40a174b9 / Assets/world/Props/Dvergr/Hanging_RoyalJelly.prefab |
| HardAntler | Hard Antler | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/HardAntler.prefab |
| Hare | Hare | Characters/Hare | 10 components; active: yes | c4210710 / Assets/Characters/Hare/Hare.prefab |
| Hare_ragdoll | — | Characters/Hare | 4 components; active: yes | c4210710 / Assets/Characters/Hare/Fx/Hare_ragdoll.prefab |
| HareMeat | Hare Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/HareMeat.prefab |
| Hatchling | Drake | Characters/Hatchling | 9 components; active: yes | c4210710 / Assets/Characters/Hatchling/Hatchling.prefab |
| hatchling_cold_projectile | — | Characters/Hatchling | 4 components; active: yes | c4210710 / Assets/Characters/Hatchling/attacks/hatchling_cold_projectile.prefab |
| Hatchling_ragdoll | — | Characters/Hatchling | 4 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/Hatchling_ragdoll.prefab |
| hatchling_spit_cold | cold ball | Characters/Hatchling | 3 components; active: yes | c4210710 / Assets/Characters/Hatchling/attacks/hatchling_spit_cold.prefab |
| HatefulBlood | Malicious Blood | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/HatefulBlood.prefab |
| HealthUpgrade_Bonemass | Bonemass heart | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/HealthUpgrade_Bonemass.prefab |
| HealthUpgrade_GDKing | Elder heart | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/HealthUpgrade_GDKing.prefab |
| hearth | Hearth; Fire | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/hearth.prefab |
| HeathRockPillar | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/HeathRockPillar/HeathRockPillar.prefab |
| HeathRockPillar_frac | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/HeathRockPillar/HeathRockPillar_frac.prefab |
| HelmetAshlandsMediumHood | Hood of Ask | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetAshlandsMediumHood.prefab |
| HelmetBerserkerHood | Headdress of the Bear | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetBerserkerHood.prefab |
| HelmetBerserkerUndead | Vilebone Visage | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetBerserkerUndead.prefab |
| HelmetBronze | Bronze Helmet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetBronze.prefab |
| HelmetCarapace | Carapace Helmet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetCarapace.prefab |
| HelmetCelebration | Celebratory Cap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetCelebration.prefab |
| HelmetCrownofValheim | Crown of Valheim | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetCrownofValheim.prefab |
| HelmetDNHeavy | Helmet of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetDNHeavy.prefab |
| HelmetDNMage | Headdress of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetDNMage.prefab |
| HelmetDNMediumHood | Hood of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetDNMediumHood.prefab |
| HelmetDrake | Drake Helmet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetDrake.prefab |
| HelmetDverger | Dverger Circlet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetDverger.prefab |
| HelmetFenring | Fenris Hood | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetFenring.prefab |
| HelmetFishingHat | Fishing Hat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetFishingHat.prefab |
| HelmetFlametal | Flametal Helmet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetFlametal.prefab |
| HelmetHat1 | Blue Tied Headscarf | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat1.prefab |
| HelmetHat10 | Simple Purple Cap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat10.prefab |
| HelmetHat2 | Green Twisted Headscarf | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat2.prefab |
| HelmetHat3 | Brown Fur Cap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat3.prefab |
| HelmetHat4 | Extravagant Green Cap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat4.prefab |
| HelmetHat5 | Simple Red Cap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat5.prefab |
| HelmetHat6 | Yellow Tied Headscarf | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat6.prefab |
| HelmetHat7 | Red Twisted Headscarf | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat7.prefab |
| HelmetHat8 | Grey Fur Cap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat8.prefab |
| HelmetHat9 | Extravagant Orange Cap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetHat9.prefab |
| HelmetIron | Iron Helmet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetIron.prefab |
| HelmetLeather | Leather Helmet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetLeather.prefab |
| HelmetLox | Lox Fur Hood | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetLox.prefab |
| HelmetMage | Eitr-weave Hood | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetMage.prefab |
| HelmetMage_Ashlands | Hood of Embla | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetMage_Ashlands.prefab |
| HelmetMidsummerCrown | Midsummer Crown | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetMidsummerCrown.prefab |
| HelmetOdin | Hood of Oden | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetOdin.prefab |
| HelmetPadded | Padded Helmet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetPadded.prefab |
| HelmetPointyHat | Pointy Hat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetPointyHat.prefab |
| HelmetRoot | Root Mask | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetRoot.prefab |
| HelmetRootCrown | Crown of Roots | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetRootCrown.prefab |
| HelmetStrawHat | Straw Hat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetStrawHat.prefab |
| HelmetSweatBand | Headband | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetSweatBand.prefab |
| HelmetTrollLeather | Troll Leather Hood | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetTrollLeather.prefab |
| HelmetYule | Yule Hat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/helmets/HelmetYule.prefab |
| Hen | Hen | Characters/Chicken | 12 components; active: yes | c4210710 / Assets/Characters/Chicken/Hen.prefab |
| highstone | — | world/Props | 3 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/highstone.prefab |
| highstone | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/highstone.prefab |
| highstone_2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/highstone_2.prefab |
| highstone_2_frac | Rock | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/highstone_2_frac.prefab |
| highstone_frac | Rock | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/highstone_frac.prefab |
| Hildir | Hildir | Characters/Hildir | 5 components; active: yes | c4210710 / Assets/Characters/Hildir/Hildir.prefab |
| hildir_barrel | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_barrel.prefab |
| Hildir_camp | — | world/Locations | 2 components; active: yes | d9b97a3d / Assets/world/Locations/Meadows/Hildir_camp.prefab |
| hildir_carpet | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_carpet.prefab |
| hildir_clothesrack1 | — | world/Props | 3 components; active: yes | 4a06e3ee / Assets/world/Props/HildirWagon/hildir_clothesrack1.prefab |
| hildir_clothesrack2 | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_clothesrack2.prefab |
| hildir_clothesrack3 | — | world/Props | 3 components; active: yes | 4a06e3ee / Assets/world/Props/HildirWagon/hildir_clothesrack3.prefab |
| hildir_divan | — | world/Props | 2 components; active: yes | 4a06e3ee / Assets/world/Props/HildirWagon/hildir_divan.prefab |
| hildir_divan1 | Divan | world/Props | 3 components; active: yes | 4a06e3ee / Assets/world/Props/HildirWagon/hildir_divan1.prefab |
| hildir_fabricsroll1 | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_fabricsroll1.prefab |
| hildir_fabricsroll2 | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_fabricsroll2.prefab |
| hildir_flowergirland | — | world/Props | 1 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_flowergirland.prefab |
| hildir_hatstand | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_hatstand.prefab |
| hildir_hatstand1 | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_hatstand1.prefab |
| hildir_hatstand2 | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_hatstand2.prefab |
| hildir_lantern | — | world/Props | 2 components; active: yes | 4a06e3ee / Assets/world/Props/HildirWagon/hildir_lantern.prefab |
| hildir_maptable | Hildir&#x27;s Map Table | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_maptable.prefab |
| Hildir_plainsfortress_wood_beam | — | world/Props | 2 components; active: yes | e9d8ba5e / Assets/world/Props/Dvergr/Hildir_plainsfortress_wood_beam.prefab |
| Hildir_plainsfortress_wood_floor | — | world/Props | 2 components; active: yes | 5b5d26ec / Assets/world/Props/Dvergr/Hildir_plainsfortress_wood_floor.prefab |
| hildir_table | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_table.prefab |
| hildir_table1 | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_table1.prefab |
| hildir_table2 | — | world/Props | 3 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_table2.prefab |
| hildir_tent | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_tent.prefab |
| hildir_tent2 | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_tent2.prefab |
| hildir_wagon | — | world/Props | 2 components; active: yes | d9b97a3d / Assets/world/Props/HildirWagon/hildir_wagon.prefab |
| HildirKey_forestcrypt | Hildir&#x27;s Brass Key | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/HildirKey_forestcrypt.prefab |
| HildirKey_mountaincave | Hildir&#x27;s Silver Key | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/HildirKey_mountaincave.prefab |
| HildirKey_plainsfortress | Hildir&#x27;s Bronze Key | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/HildirKey_plainsfortress.prefab |
| HildirsLox | — | Characters/Lox | 3 components; active: yes | d9b97a3d / Assets/Characters/Lox/HildirsLox.prefab |
| Hive | — | Characters/Hive | 10 components; active: yes | c4210710 / Assets/Characters/Hive/Hive.prefab |
| hive_attack_aoe | heal | Characters/Hive | 3 components; active: yes | c4210710 / Assets/Characters/Hive/Attacks/hive_attack_aoe.prefab |
| hive_attack_punch | slap | Characters/Hive | 3 components; active: yes | c4210710 / Assets/Characters/Hive/Attacks/hive_attack_punch.prefab |
| hive_attack_ranged | dragon breath | Characters/Hive | 3 components; active: yes | c4210710 / Assets/Characters/Hive/Attacks/hive_attack_ranged.prefab |
| hive_attack_throw | slime throw | Characters/Hive | 3 components; active: yes | c4210710 / Assets/Characters/Hive/Attacks/hive_attack_throw.prefab |
| hive_spawn | — | Characters/Hive | 2 components; active: yes | c4210710 / Assets/Characters/Hive/Attacks/hive_spawn.prefab |
| hive_throw_projectile | — | Characters/Hive | 4 components; active: yes | c4210710 / Assets/Characters/Hive/Attacks/hive_throw_projectile.prefab |
| Hoe | Hoe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/tools/Hoe.prefab |
| hole_destructableDoor | — | world/Rooms | 1 components; active: yes | c4210710 / Assets/world/Rooms/hole/hole_destructableDoor.prefab |
| hole_destructableDoor1 | — | world/Rooms | 1 components; active: yes | c4210710 / Assets/world/Rooms/hole/hole_destructableDoor1.prefab |
| hole_destructableDoor2 | — | world/Rooms | 1 components; active: yes | c4210710 / Assets/world/Rooms/hole/hole_destructableDoor2.prefab |
| HoleRock_curved1 | — | world/Props | 3 components; active: yes | 37adb48e / Assets/world/Props/TheHole/HoleRock_curved1.prefab |
| HoleRock_curved2 | — | world/Props | 3 components; active: yes | aca3b9a5 / Assets/world/Props/TheHole/HoleRock_curved2.prefab |
| HoleRock_curved2wHole | — | world/Props | 3 components; active: yes | 49d6ffbf / Assets/world/Props/TheHole/HoleRock_curved2wHole.prefab |
| HoleRock_floor1 | — | world/Props | 3 components; active: yes | a372362 / Assets/world/Props/TheHole/HoleRock_floor1.prefab |
| HoleRock_opening1 | — | world/Props | 3 components; active: yes | d80eaa12 / Assets/world/Props/TheHole/HoleRock_opening1.prefab |
| HoleRock_opening_znet | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/TheHole/HoleRock_opening_znet.prefab |
| HoleRock_root1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/TheHole/HoleRock_root1.prefab |
| HoleRock_root1_destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/TheHole/HoleRock_root1_destruction.prefab |
| HoleRock_rootBush1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/TheHole/HoleRock_rootBush1.prefab |
| HoleRock_rootFloor1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/TheHole/HoleRock_rootFloor1.prefab |
| HoleRock_rootWall1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/TheHole/HoleRock_rootWall1.prefab |
| HoleRock_rootWall1_destruction | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/TheHole/HoleRock_rootWall1_destruction.prefab |
| HoleRock_small1 | — | world/Props | 3 components; active: yes | 13c174a / Assets/world/Props/TheHole/HoleRock_small1.prefab |
| HoleRock_small1_hole | — | world/Props | 3 components; active: yes | 2fe48ee2 / Assets/world/Props/TheHole/HoleRock_small1_hole.prefab |
| Honey | Honey | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Honey.prefab |
| HoneyGlazedChicken | Honey Glazed Chicken | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/HoneyGlazedChicken.prefab |
| HoneyGlazedChickenUncooked | Uncooked Honey Glazed Chicken | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/HoneyGlazedChickenUncooked.prefab |
| Hook | Hook | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Hook.prefab |
| horizontal_web | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/webs/horizontal_web.prefab |
| HotKeyElement | — | UI/prefabs | 2 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/HotKeyElement.prefab |
| HotSpring3 | — | world/Locations | 2 components; active: yes | 98c14cfe / Assets/world/Locations/DeepNorth/HotSpring3.prefab |
| HouseFire | — | world/SmokeFire | 8 components; active: yes | c4210710 / Assets/world/SmokeFire/HouseFire.prefab |
| HudMessage | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/HudMessage.prefab |
| HugeRoot1 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/SwampTree/HugeRoot1.prefab |
| HugeStone1 | — | world/Props | 1 components; active: yes | d59cfac / Assets/world/Props/HugeStone1.prefab |
| Hugin | Hugin | Characters/Raven | 2 components; active: yes | c4210710 / Assets/Characters/Raven/Hugin.prefab |
| Ice | Ice | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Ice.prefab |
| ice1 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice/ice1.prefab |
| Ice_floor | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Caverocks/Ice_floor.prefab |
| Ice_floor_fractured | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Caverocks/Ice_floor_fractured.prefab |
| ice_rock1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/ice_rock1.prefab |
| ice_rock1_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/ice_rock1_frac.prefab |
| Ice_ship_1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/Ice_ship_1.prefab |
| Ice_ship_2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/Ice_ship_2.prefab |
| Ice_ship_3 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/Ice_ship_3.prefab |
| Ice_ship_4 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/Ice_ship_4.prefab |
| Ice_ship_5 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/Ice_ship_5.prefab |
| Ice_ship_6 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/Ice_ship_6.prefab |
| Ice_ship_7 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FrozenShips/Ice_ship_7.prefab |
| IceBlocker | — | Characters/Dragon | 4 components; active: yes | c4210710 / Assets/Characters/Dragon/attacks/misc/IceBlocker.prefab |
| icelake | — | world/Props | 3 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/BossRoom/icelake.prefab |
| IcePond_rock | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/IcePond_rock.prefab |
| IcePond_rock_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/IcePond_rock_frac.prefab |
| IceShard_01 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/IceShard_01.prefab |
| IceShard_02 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/IceShard_02.prefab |
| IceShard_03 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/IceShard_03.prefab |
| IceShard_04 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/IceShard_04.prefab |
| IceShard_05 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/IceShard_05.prefab |
| IceShard_06 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Ice_FimbulWinter/IceShard_06.prefab |
| IceShelf_01 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_01.prefab |
| IceShelf_02 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_02.prefab |
| IceShelf_03 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_03.prefab |
| IceShelf_04 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_04.prefab |
| IceShelf_05 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_05.prefab |
| IceShelf_06 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_06.prefab |
| IceShelf_07 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_07.prefab |
| IceShelf_08 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_08.prefab |
| IceShelf_09 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_09.prefab |
| IceShelf_10 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/IceShelf/IceShelf_10.prefab |
| IceShoes | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/utility/IceShoes.prefab |
| IceShore | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/IceShore.prefab |
| IceShore_1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/IceShore_1.prefab |
| IceShore_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/IceShore_frac.prefab |
| IceShoreShard | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/IceShoreShard.prefab |
| IceSkates | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/utility/IceSkates.prefab |
| IceSpike01 | — | world/Props | 5 components; active: yes | 86c8ff36 / Assets/world/Props/DrakeNest/IceSpike01.prefab |
| IceSpike02 | — | world/Props | 5 components; active: yes | 86c8ff36 / Assets/world/Props/DrakeNest/IceSpike02.prefab |
| IceWall | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/IceWall.prefab |
| imp_fireball_attack | fireballattack | Characters/Surtling | 3 components; active: yes | c4210710 / Assets/Characters/Surtling/misc/imp_fireball_attack.prefab |
| Imp_fireball_projectile | — | Characters/Surtling | 4 components; active: yes | c4210710 / Assets/Characters/Surtling/misc/Imp_fireball_projectile.prefab |
| incinerator | Obliterator | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/incinerator.prefab |
| IngameGui | — | UI/prefabs | 3 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui.prefab |
| IngameGui_Achievements | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_Achievements.prefab |
| IngameGui_Chat | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_Chat.prefab |
| IngameGui_Chat_box | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_Chat_box.prefab |
| IngameGui_ConnectionPanel | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_ConnectionPanel.prefab |
| IngameGui_HUD | — | UI/prefabs | 7 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_HUD.prefab |
| IngameGui_HUD_HoveredPieceAuthor | — | UI/prefabs | 1 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_HUD_HoveredPieceAuthor.prefab |
| IngameGui_HUD_Minimap | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_HUD_Minimap.prefab |
| IngameGui_Inventory | — | UI/prefabs | 7 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_Inventory.prefab |
| IngameGui_JoinCodeOverlay | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_JoinCodeOverlay.prefab |
| IngameGui_Menu | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_Menu.prefab |
| IngameGui_Store_Screen | — | UI/prefabs | 6 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_Store_Screen.prefab |
| IngameGui_TextInput | — | UI/prefabs | 8 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_TextInput.prefab |
| IngameGui_TextViewer | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_TextViewer.prefab |
| IngameGui_Trophies | — | UI/prefabs | 4 components; active: no | d59cfac / Assets/UI/prefabs/IngameGui/IngameGui_Trophies.prefab |
| instanced_ashlands_grass_long | — | world/Props | 2 components; active: yes | d59cfac / Assets/world/Props/ground_clutter/instanced_ashlands_grass_long.prefab |
| instanced_ashlands_grass_short | — | world/Props | 2 components; active: yes | d59cfac / Assets/world/Props/ground_clutter/instanced_ashlands_grass_short.prefab |
| instanced_forest_groundcover | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_forest_groundcover.prefab |
| instanced_forest_groundcover_brown | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_forest_groundcover_brown.prefab |
| instanced_forest_groundcover_snow | — | world/Props | 2 components; active: yes | d59cfac / Assets/world/Props/ground_clutter/instanced_forest_groundcover_snow.prefab |
| instanced_heathflowers | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_heathflowers.prefab |
| instanced_heathgrass | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_heathgrass.prefab |
| instanced_meadows_grass | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_meadows_grass.prefab |
| instanced_meadows_grass_short | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_meadows_grass_short.prefab |
| instanced_mistlands_grass_short | — | world/Props | 2 components; active: yes | d59cfac / Assets/world/Props/ground_clutter/instanced_mistlands_grass_short.prefab |
| instanced_mistlands_rockplant | — | world/Props | 2 components; active: yes | d59cfac / Assets/world/Props/ground_clutter/instanced_mistlands_rockplant.prefab |
| instanced_ormbunke | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_ormbunke.prefab |
| instanced_shrub | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_shrub.prefab |
| instanced_small_rock1 | — | world/Props | 2 components; active: yes | d59cfac / Assets/world/Props/ground_clutter/instanced_small_rock1.prefab |
| instanced_swamp_grass | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_swamp_grass.prefab |
| instanced_swamp_ormbunke | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_swamp_ormbunke.prefab |
| instanced_vass | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_vass.prefab |
| instanced_waterlilies | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/instanced_waterlilies.prefab |
| InteriorEnvironmentZone | — | GameElements/InteriorStuff | 3 components; active: yes | ba621cac / Assets/GameElements/InteriorStuff/InteriorEnvironmentZone.prefab |
| InteriorEnvironmentZoneForce | — | GameElements/InteriorStuff | 3 components; active: yes | 6c120cb / Assets/GameElements/InteriorStuff/InteriorEnvironmentZoneForce.prefab |
| InventoryElement | — | UI/prefabs | 10 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/InventoryElement.prefab |
| InventoryInfo | — | UI/prefabs | 4 components; active: yes | d59cfac / Assets/UI/prefabs/Radial/InventoryInfo.prefab |
| InventoryTooltip | — | UI/prefabs | 1 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/InventoryTooltip.prefab |
| Iron | Iron | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Iron.prefab |
| iron_floor_1x1 | Cage Floor 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/iron_floor_1x1.prefab |
| iron_floor_1x1_v2 | Cage Floor 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/iron_floor_1x1_v2.prefab |
| iron_floor_2x2 | Cage Floor 2x2 | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/iron_floor_2x2.prefab |
| iron_grate | Iron Gate | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/iron_grate.prefab |
| iron_wall_1x1 | Cage Wall 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/iron_wall_1x1.prefab |
| iron_wall_1x1_rusty | Cage Wall 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/iron_wall_1x1_rusty.prefab |
| iron_wall_2x2 | Cage Wall 2x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/iron_wall_2x2.prefab |
| IronNails | Iron Nails | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/IronNails.prefab |
| IronOre | Iron Ore | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/IronOre.prefab |
| Ironpit | Iron Pit | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Ironpit.prefab |
| IronScrap | Scrap Iron | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/IronScrap.prefab |
| Item | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/Radial/elements/Item.prefab |
| ItemSets | — | Systems | 2 components; active: yes | d59cfac / Assets/Systems/ItemSets.prefab |
| itemstand | Item Stand | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/itemstand.prefab |
| itemstandh | Item Stand | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/itemstandh.prefab |
| JotunHairFemale | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairFemale.prefab |
| JotunHairMale | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale.prefab |
| JotunHairMale2 | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale2.prefab |
| JotunHairMale3 | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale3.prefab |
| JotunHairMale4 | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale4.prefab |
| JotunHairMale5 | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale5.prefab |
| JotunHairMale6 | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale6.prefab |
| JotunHairMale7 | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale7.prefab |
| JotunHairMale8 | Iron plate armor | Characters/Jotnar | 7 components; active: yes | c4210710 / Assets/Characters/Jotnar/gear/JotunHairMale8.prefab |
| JotunWarrior | Krigen | Characters/Jotnar | 11 components; active: yes | c4210710 / Assets/Characters/Jotnar/JotunWarrior.prefab |
| JotunWarrior1HAxe_attack_cleave | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior1HAxe_attack_cleave.prefab |
| JotunWarrior1HAxe_attack_dodge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior1HAxe_attack_dodge.prefab |
| JotunWarrior1HAxe_attack_dodger | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior1HAxe_attack_dodger.prefab |
| JotunWarrior1HAxe_attack_slash | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior1HAxe_attack_slash.prefab |
| JotunWarrior1HAxe_attack_slashdw | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior1HAxe_attack_slashdw.prefab |
| JotunWarrior2HAxe_attack_charge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HAxe_attack_charge.prefab |
| JotunWarrior2HAxe_attack_cleave | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HAxe_attack_cleave.prefab |
| JotunWarrior2HAxe_attack_dodge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HAxe_attack_dodge.prefab |
| JotunWarrior2HAxe_attack_slash | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HAxe_attack_slash.prefab |
| JotunWarrior2HSword_attack_charge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HSword_attack_charge.prefab |
| JotunWarrior2HSword_attack_cleave | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HSword_attack_cleave.prefab |
| JotunWarrior2HSword_attack_dodge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HSword_attack_dodge.prefab |
| JotunWarrior2HSword_attack_slash | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior2HSword_attack_slash.prefab |
| JotunWarrior_attack_charge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior_attack_charge.prefab |
| JotunWarrior_attack_cleave | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior_attack_cleave.prefab |
| JotunWarrior_attack_dodge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior_attack_dodge.prefab |
| JotunWarrior_attack_slash | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior_attack_slash.prefab |
| JotunWarrior_attack_sword | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWarrior_attack_sword.prefab |
| JotunWarrior_Ragdoll | — | Characters/Jotnar | 4 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/JotunWarrior_Ragdoll.prefab |
| JotunWarriorDualWield | Krigen | Characters/Jotnar | 11 components; active: yes | c4210710 / Assets/Characters/Jotnar/JotunWarriorDualWield.prefab |
| JotunWarriorSword2h | Club | Characters/Jotnar | 8 components; active: yes | c4210710 / Assets/Characters/Jotnar/model/weapons/JotunWarriorSword2h.prefab |
| JotunWitch | Hexen | Characters/Jotnar | 11 components; active: yes | c4210710 / Assets/Characters/Jotnar/JotunWitch.prefab |
| JotunWitch_attack_dodge | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWitch_attack_dodge.prefab |
| JotunWitch_attack_dodge2 | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWitch_attack_dodge2.prefab |
| JotunWitch_attack_dodge_down | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWitch_attack_dodge_down.prefab |
| JotunWitch_attack_dodge_up | Charred Sword | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWitch_attack_dodge_up.prefab |
| JotunWitch_attack_lightningbolt | fireballattack | Characters/Jotnar | 3 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWitch_attack_lightningbolt.prefab |
| JotunWitch_attack_magicblast | StagAttack2 | Characters/Jotnar | 2 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWitch_attack_magicblast.prefab |
| JotunWitch_projectile_lightningbolt | — | Characters/Jotnar | 4 components; active: yes | c4210710 / Assets/Characters/Jotnar/attacks/JotunWitch_projectile_lightningbolt.prefab |
| jute_carpet | Red Jute Carpet | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/jute_carpet.prefab |
| jute_carpet_blue | Blue Jute Carpet | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/jute_carpet_blue.prefab |
| JuteBlue | Blue Jute | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/JuteBlue.prefab |
| JuteRed | Red Jute | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/JuteRed.prefab |
| Kale | Kale | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Kale.prefab |
| KaleChips | Kale Chips | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/KaleChips.prefab |
| KaleChipsUncooked | Raw Kale Chips | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/KaleChipsUncooked.prefab |
| KaleSeeds | Kale Seeds | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/KaleSeeds.prefab |
| Karve | Karve | GameElements/Ships | 10 components; active: yes | c4210710 / Assets/GameElements/Ships/Karve.prefab |
| KeyboardMouseTab | — | UI/prefabs | 6 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/KeyboardMouseTab.prefab |
| KeyHint | — | UI/GUI | 2 components; active: yes | c4210710 / Assets/UI/GUI/KeyHint.prefab |
| KeyHintsBase | — | UI/prefabs | 2 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/KeyHintsBase.prefab |
| KeysGoldUncooked | Cast: Intricate Key | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/KeysGoldUncooked.prefab |
| KnifeBlackMetal | Black Metal Knife | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeBlackMetal.prefab |
| KnifeButcher | Butcher Knife | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeButcher.prefab |
| KnifeChitin | Abyssal Razor | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeChitin.prefab |
| KnifeCopper | Copper Knife | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeCopper.prefab |
| KnifeFlint | Flint Knife | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeFlint.prefab |
| KnifeGold | Nord Dagger | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeGold.prefab |
| KnifeGold_BloodLightning | Thunderblood Dagger | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeGold_BloodLightning.prefab |
| KnifeGold_FrostFire | Frostfire Dagger | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeGold_FrostFire.prefab |
| KnifeGoldUncooked | Cast: Nord Dagger | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeGoldUncooked.prefab |
| KnifeSilver | Silver Knife | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeSilver.prefab |
| KnifeSkollAndHati | Skoll and Hati | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeSkollAndHati.prefab |
| KnifeVoid | Voidcaller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeVoid.prefab |
| KnifeWood | Wooden Knife | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/KnifeWood.prefab |
| Lantern | Dvergr Lantern | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Lantern.prefab |
| Lantern_DN | Salvaged Lantern | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Lantern_DN.prefab |
| Lantern_hooded | Hooded Lantern | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Lantern_hooded.prefab |
| LargeBone | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/LargeBone.prefab |
| LargeBone_half01 | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/LargeBone_half01.prefab |
| LargeBone_half02 | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/LargeBone_half02.prefab |
| Larva | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Larva.prefab |
| LastBossGate | — | world/Props | 3 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate.prefab |
| LastBossGate_Chain | — | world/Props | 3 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_Chain.prefab |
| LastBossGate_Chain2 | — | world/Props | 3 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_Chain2.prefab |
| LastBossGate_Floorstone | — | world/Props | 3 components; active: yes | c58d692a / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_Floorstone.prefab |
| LastBossGate_InternalGate | — | world/Props | 2 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_InternalGate.prefab |
| LastBossGate_Pillar | — | world/Props | 3 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_Pillar.prefab |
| LastBossGate_Pillarbase | — | world/Props | 3 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_Pillarbase.prefab |
| LastBossGate_Rotator | — | world/Props | 2 components; active: yes | e06fccc7 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_Rotator.prefab |
| LastBossGate_RuneTile | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/LastBossGate/LastBossGate_RuneTile.prefab |
| lavabomb_explosion | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombLava/lavabomb_explosion.prefab |
| lavabomb_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombLava/lavabomb_projectile.prefab |
| lavabomb_rock1 | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombLava/lavabomb_rock1.prefab |
| LavaRock | — | Characters/LavaRock | 5 components; active: yes | c4210710 / Assets/Characters/LavaRock/LavaRock.prefab |
| lavarock_ashlands1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/lavarock_ashlands1.prefab |
| LeatherScraps | Leather Scraps | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/LeatherScraps.prefab |
| Leatherstraps | Leather Straps | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Leatherstraps.prefab |
| Leech | Leech | Characters/Leech | 9 components; active: yes | c4210710 / Assets/Characters/Leech/Leech.prefab |
| Leech_BiteAttack | jaws | Characters/Leech | 3 components; active: yes | c4210710 / Assets/Characters/Leech/attacks/Leech_BiteAttack.prefab |
| Leech_cave | Leech | Characters/Leech | 9 components; active: yes | c4210710 / Assets/Characters/Leech/Leech_cave.prefab |
| LevelTerrain | — | world | 2 components; active: yes | d59cfac / Assets/world/LevelTerrain.prefab |
| Leviathan | — | Characters/Leviathan | 7 components; active: yes | c4210710 / Assets/Characters/Leviathan/Leviathan.prefab |
| LeviathanLava | Flametal Ore | Characters/Leviathan | 8 components; active: yes | c4210710 / Assets/Characters/Leviathan/LeviathanLava.prefab |
| lightningAOE | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/incinerator/lightningAOE.prefab |
| LinenThread | Linen Thread | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/LinenThread.prefab |
| Lingonberry | Lingonberries | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Lingonberry.prefab |
| LingonberryBush | Lingonberries | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Lingon/LingonberryBush.prefab |
| Lingondricka | Lingonberry Juice | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Lingondricka.prefab |
| LoadingGUI | — | UI/prefabs | 1 components; active: yes | d59cfac / Assets/UI/prefabs/LoadingGUI.prefab |
| LoadingGUI_Connecting | — | UI/prefabs | 6 components; active: no | d59cfac / Assets/UI/prefabs/LoadingGUI_Connecting.prefab |
| LoadingGUI_Password | — | UI/prefabs | 7 components; active: no | d59cfac / Assets/UI/prefabs/LoadingGUI_Password.prefab |
| LoadingIndicator | — | UI/prefabs | 2 components; active: yes | 9ac395d7 / Assets/UI/prefabs/LoadingIndicator.prefab |
| LocationProxy | — | Systems | 3 components; active: yes | c4210710 / Assets/Systems/LocationProxy.prefab |
| LongPressRadial | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/LongPressRadial.prefab |
| loot_chest_stone | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/loot_chest_stone.prefab |
| loot_chest_wood | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/loot_chest_wood.prefab |
| loot_deepNorth_Granary | Barrel | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/loot_deepNorth_Granary.prefab |
| loot_deepNorth_TimberHall | Barrel | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/loot_deepNorth_TimberHall.prefab |
| LootSpawner_pineforest | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/loot/LootSpawner_pineforest.prefab |
| Lox | Lox | Characters/Lox | 13 components; active: yes | c4210710 / Assets/Characters/Lox/Lox.prefab |
| lox_bite | lox bite | Characters/Lox | 2 components; active: yes | c4210710 / Assets/Characters/Lox/attacks/lox_bite.prefab |
| Lox_Calf | Lox Calf | Characters/Lox | 10 components; active: yes | c4210710 / Assets/Characters/Lox/Lox_Calf.prefab |
| lox_ragdoll | — | Characters/Lox | 4 components; active: yes | c4210710 / Assets/Characters/Lox/fx/lox_ragdoll.prefab |
| lox_ribs | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/lox_ribs.prefab |
| lox_stomp | slap | Characters/Lox | 3 components; active: yes | c4210710 / Assets/Characters/Lox/attacks/lox_stomp.prefab |
| lox_stomp_aoe_OLD | — | Characters/Lox | 3 components; active: yes | c4210710 / Assets/Characters/Lox/attacks/lox_stomp_aoe_OLD.prefab |
| loxcalf_ragdoll | — | Characters/Lox | 4 components; active: yes | c4210710 / Assets/Characters/Lox/fx/loxcalf_ragdoll.prefab |
| LoxMeat | Lox Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/LoxMeat.prefab |
| LoxPelt | Lox Pelt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/LoxPelt.prefab |
| LoxPie | Lox Meat Pie | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/LoxPie.prefab |
| LoxPieUncooked | Unbaked Lox Pie | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/LoxPieUncooked.prefab |
| LuredFaderEmber | Embers | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FaderFire/LuredFaderEmber.prefab |
| LuredWisp | Wisp | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/WispLure/LuredWisp.prefab |
| MaceBronze | Bronze Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceBronze.prefab |
| MaceEldner | Flametal Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceEldner.prefab |
| MaceEldnerBlood | Bloodgeon | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceEldnerBlood.prefab |
| MaceEldnerLightning | Storm Star | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceEldnerLightning.prefab |
| MaceEldnerNature | Klossen | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceEldnerNature.prefab |
| MaceGold | Nord Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceGold.prefab |
| MaceGold_BloodLightning | Thunderblood Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceGold_BloodLightning.prefab |
| MaceGold_FrostFire | Frostfire Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceGold_FrostFire.prefab |
| MaceGoldUncooked | Cast: Nord Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceGoldUncooked.prefab |
| MaceIron | Iron Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceIron.prefab |
| MaceNeedle | Porcupine | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceNeedle.prefab |
| MaceSilver | Frostner | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceSilver.prefab |
| MaceWood | Wooden Mace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/MaceWood.prefab |
| MagicallyStuffedShroom | Stuffed Mushroom | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MagicallyStuffedShroom.prefab |
| MagicallyStuffedShroomUncooked | Uncooked Stuffed Mushroom | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MagicallyStuffedShroomUncooked.prefab |
| Mandible | Mandible | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Mandible.prefab |
| MapPin | — | UI/map | 3 components; active: yes | d59cfac / Assets/UI/map/MapPin.prefab |
| MapPinName | — | UI/map | 2 components; active: yes | d59cfac / Assets/UI/map/MapPinName.prefab |
| MarinatedGreens | Marinated Greens | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MarinatedGreens.prefab |
| marker01 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Waymarkers/marker01.prefab |
| marker02 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Waymarkers/marker02.prefab |
| MashedMeat | Mashed Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MashedMeat.prefab |
| MeadBaseBugRepellent | Mead Base: Anti-Sting | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseBugRepellent.prefab |
| MeadBaseBzerker | Mead base: Berserkir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseBzerker.prefab |
| MeadBaseEitrLingering | Mead Base: Lingering Eitr | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseEitrLingering.prefab |
| MeadBaseEitrMinor | Mead Base: Minor Eitr | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseEitrMinor.prefab |
| MeadBaseFrostResist | Mead Base: Frost Resistance | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseFrostResist.prefab |
| MeadBaseHasty | Mead base: Ratatosk | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseHasty.prefab |
| MeadBaseHealthLingering | Mead Base: Lingering Health | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseHealthLingering.prefab |
| MeadBaseHealthMajor | Mead Base: Major Healing | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseHealthMajor.prefab |
| MeadBaseHealthMedium | Mead Base: Medium Healing | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseHealthMedium.prefab |
| MeadBaseHealthMinor | Mead Base: Minor Healing | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseHealthMinor.prefab |
| MeadBaseLightFoot | Mead Base: Lightfoot | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseLightFoot.prefab |
| MeadBasePoisonResist | Mead Base: Poison Resistance | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBasePoisonResist.prefab |
| MeadBaseStaminaLingering | Mead Base: Lingering Stamina | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseStaminaLingering.prefab |
| MeadBaseStaminaMedium | Mead Base: Medium Stamina | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseStaminaMedium.prefab |
| MeadBaseStaminaMinor | Mead Base: Minor Stamina | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseStaminaMinor.prefab |
| MeadBaseStrength | Mead Base: Troll Endurance | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseStrength.prefab |
| MeadBaseSwimmer | Mead Base: Vananidir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseSwimmer.prefab |
| MeadBaseTamer | Mead Base: Animal Whispers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseTamer.prefab |
| MeadBaseTasty | Mead Base: Tasty | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBaseTasty.prefab |
| MeadBugRepellent | Anti-Sting Concoction | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBugRepellent.prefab |
| MeadBzerker | Berserkir Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadBzerker.prefab |
| MeadEitrLingering | Lingering Eitr Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadEitrLingering.prefab |
| MeadEitrMinor | Minor Eitr Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadEitrMinor.prefab |
| MeadFrostResist | Frost Resistance Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadFrostResist.prefab |
| MeadHasty | Tonic of Ratatosk | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadHasty.prefab |
| MeadHealthLingering | Lingering Healing Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadHealthLingering.prefab |
| MeadHealthMajor | Major Healing Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadHealthMajor.prefab |
| MeadHealthMedium | Medium Healing Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadHealthMedium.prefab |
| MeadHealthMinor | Minor Healing Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadHealthMinor.prefab |
| MeadLightfoot | Lightfoot Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadLightfoot.prefab |
| MeadPoisonResist | Poison Resistance Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadPoisonResist.prefab |
| MeadStaminaLingering | Lingering Stamina Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadStaminaLingering.prefab |
| MeadStaminaMedium | Medium Stamina Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadStaminaMedium.prefab |
| MeadStaminaMinor | Minor Stamina Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadStaminaMinor.prefab |
| MeadStrength | Mead of Troll Endurance | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadStrength.prefab |
| MeadSwimmer | Draught of Vananidir | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadSwimmer.prefab |
| MeadTamer | Brew of Animal Whispers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadTamer.prefab |
| MeadTasty | Tasty Mead | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadTasty.prefab |
| MeadTrollPheromones | Love Potion | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeadTrollPheromones.prefab |
| MeatballsMashedPoteitr | Meatballs and Poteitr | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeatballsMashedPoteitr.prefab |
| MeatPlatter | Meat Platter | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MeatPlatter.prefab |
| MeatPlatterUncooked | Uncooked Meat Platter | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MeatPlatterUncooked.prefab |
| MechanicalSpring | Mechanical Spring | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MechanicalSpring.prefab |
| MemorialCoal | Memorial Coal | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MemorialCoal.prefab |
| memorialsite_offering | — | world/Props | 1 components; active: yes | 25830207 / Assets/world/Props/MemorialStones/memorialsite_offering.prefab |
| MemorialStone_Large | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/MemorialStones/MemorialStone_Large.prefab |
| MemorialStone_Medium | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/MemorialStones/MemorialStone_Medium.prefab |
| MemorialStone_Small | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/MemorialStones/MemorialStone_Small.prefab |
| menu_bush | — | world/Menu | 3 components; active: yes | b8689a71 / Assets/world/Menu/menu_bush.prefab |
| Menu_fir | — | world/Menu | 2 components; active: yes | b8689a71 / Assets/world/Menu/Menu_fir.prefab |
| Menu_greydwarf | — | world/Menu | 1 components; active: yes | f1709814 / Assets/world/Menu/Menu_greydwarf.prefab |
| Menu_Greydwarf_Elite | — | world/Menu | 1 components; active: yes | b8689a71 / Assets/world/Menu/Menu_Greydwarf_Elite.prefab |
| Menu_greydwarf_george | — | world/Menu | 1 components; active: yes | 3e896e5d / Assets/world/Menu/Menu_greydwarf_george.prefab |
| Menu_PineTree | — | world/Menu | 2 components; active: yes | b8689a71 / Assets/world/Menu/Menu_PineTree.prefab |
| Menu_Seal | — | world/Menu | 1 components; active: yes | b8689a71 / Assets/world/Menu/Menu_Seal.prefab |
| Menu_Seeker | — | world/Menu | 1 components; active: yes | b8689a71 / Assets/world/Menu/Menu_Seeker.prefab |
| Menu_SmallStone | — | world/Menu | 4 components; active: yes | b8689a71 / Assets/world/Menu/Menu_SmallStone.prefab |
| Menu_Twitcher | — | world/Menu | 1 components; active: yes | b8689a71 / Assets/world/Menu/Menu_Twitcher.prefab |
| MenuEntryButton | — | UI/prefabs | 7 components; active: yes | c4210710 / Assets/UI/prefabs/MenuEntryButton.prefab |
| MenuFire | — | world/Menu | 3 components; active: yes | b8689a71 / Assets/world/Menu/MenuFire.prefab |
| MenuRock | — | world/Menu | 4 components; active: yes | b8689a71 / Assets/world/Menu/MenuRock.prefab |
| MenuZone | — | world/Menu | 1 components; active: yes | b8689a71 / Assets/world/Menu/MenuZone.prefab |
| metalbar_1x2 | Black Marble 1x1x1 | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/marble/metalbar_1x2.prefab |
| MinceMeatSauce | Minced Meat Sauce | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MinceMeatSauce.prefab |
| MineRock_Copper | Copper vein | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/MineRock_Copper.prefab |
| MineRock_Iron | Iron vein | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/MineRock_Iron.prefab |
| MineRock_Meteorite | Flametal Ore | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/MineRock_Meteorite.prefab |
| MineRock_Obsidian | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/MineRock/MineRock_Obsidian.prefab |
| MineRock_Stone | Rock | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/MineRock_Stone.prefab |
| MineRock_Tin | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/MineRock/MineRock_Tin.prefab |
| MistArea | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Mistlands/MistArea.prefab |
| MistArea_edge | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Mistlands/MistArea_edge.prefab |
| MistArea_small | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Mistlands/MistArea_small.prefab |
| MisthareSupreme | Misthare Supreme | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MisthareSupreme.prefab |
| MisthareSupremeUncooked | Uncooked Misthare Supreme | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MisthareSupremeUncooked.prefab |
| Mistile | Mistile | Characters/Dverger | 9 components; active: yes | c4210710 / Assets/Characters/Dverger/Mistile.prefab |
| Mistile_kamikaze | Mistile Kamikaze | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/Attacks/Mistile_kamikaze.prefab |
| Mistlands_DvergrBossEntrance1 | — | world/Locations | 2 components; active: yes | ba621cac / Assets/world/Locations/Mistlands/Mistlands_DvergrBossEntrance1.prefab |
| MistlandsFlash | — | Effects/thunder | 2 components; active: yes | d59cfac / Assets/Effects/thunder/MistlandsFlash.prefab |
| mistvolume | — | Effects | 2 components; active: yes | c4210710 / Assets/Effects/mistvolume.prefab |
| MoldArmorGoldChest | Mould: Breastplate of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorGoldChest.prefab |
| MoldArmorGoldHelmet | Mould: Helmet of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorGoldHelmet.prefab |
| MoldArmorGoldLegs | Mould: Trousers of the Protector | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorGoldLegs.prefab |
| MoldArmorMageChest | Mould: Robes of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorMageChest.prefab |
| MoldArmorMageHelmet | Mould: Headdress of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorMageHelmet.prefab |
| MoldArmorMageLegs | Mould: Trousers of the Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorMageLegs.prefab |
| MoldArmormediumChest | Mould: Chestpiece of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmormediumChest.prefab |
| MoldArmorMediumHelmet | Mould: Hood of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorMediumHelmet.prefab |
| MoldArmorMediumLegs | Mould: Trousers of the Vanguard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldArmorMediumLegs.prefab |
| MoldAtgeir | Mould: Nord Atgeir | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldAtgeir.prefab |
| MoldAxe | Mould: Nord Axe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldAxe.prefab |
| MoldAxe2H | Mould: Nord Greataxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldAxe2H.prefab |
| MoldBow | Mould: Nord Bow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldBow.prefab |
| MoldCrossbow | Mould: Nord Crossbow | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldCrossbow.prefab |
| MoldFistweapon | Mould: Nord Knucklechains | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldFistweapon.prefab |
| MoldKeys | Mould: Intricate Key | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldKeys.prefab |
| MoldKnife | Mould: Nord Dagger | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldKnife.prefab |
| MoldMace | Mould: Nord Mace | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldMace.prefab |
| MoldMace2H | Mould: Nord Sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldMace2H.prefab |
| MoldShieldBuckler | Mould: Nord Buckler | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldShieldBuckler.prefab |
| MoldShieldRound | Mould: Nord Shield | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldShieldRound.prefab |
| MoldShieldTower | Mould: Nord Greatshield | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldShieldTower.prefab |
| MoldSmallParts | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldSmallParts.prefab |
| MoldSpear | Mould: Nord Spear | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldSpear.prefab |
| MoldStafffrostorbs | Mould: Northern Vengeance | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldStafffrostorbs.prefab |
| MoldStaffOrbofAhri | Mould: Echo Spike | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldStaffOrbofAhri.prefab |
| MoldStaffspiritcaller | Mould: Spirit Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldStaffspiritcaller.prefab |
| MoldStaffthunderblood | Mould: Lightning Strike | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldStaffthunderblood.prefab |
| MoldSword | Mould: Nord Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldSword.prefab |
| MoldSword2H | Mould: Nord Greatsword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoldSword2H.prefab |
| MoleClaws | Long Claws | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MoleClaws.prefab |
| MoltenCore | Molten Core | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MoltenCore.prefab |
| Moose | Moose | Characters/moose | 13 components; active: yes | c4210710 / Assets/Characters/moose/Moose.prefab |
| Moose_calf | Moose Calf | Characters/moose | 10 components; active: yes | c4210710 / Assets/Characters/moose/Moose_calf.prefab |
| Moose_Calf_Ragdoll | — | Characters/moose | 4 components; active: yes | c4210710 / Assets/Characters/moose/fx/Moose_Calf_Ragdoll.prefab |
| moose_hooves | moose horns | Characters/moose | 2 components; active: yes | c4210710 / Assets/Characters/moose/attacks/moose_hooves.prefab |
| moose_horns | moose horns | Characters/moose | 2 components; active: yes | c4210710 / Assets/Characters/moose/attacks/moose_horns.prefab |
| moose_horns_sweep | moose horns | Characters/moose | 2 components; active: yes | c4210710 / Assets/Characters/moose/attacks/moose_horns_sweep.prefab |
| Moose_Ragdoll | — | Characters/moose | 4 components; active: yes | c4210710 / Assets/Characters/moose/fx/Moose_Ragdoll.prefab |
| Moose_spiritcaller | — | Characters/moose | 11 components; active: yes | c4210710 / Assets/Characters/moose/Moose_spiritcaller.prefab |
| MooseHide | Moose Hide | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MooseHide.prefab |
| MooseKebab | Meat In Bread | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MooseKebab.prefab |
| MooseMeat | Moose Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MooseMeat.prefab |
| MooseSinew | Moose Sinew | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MooseSinew.prefab |
| Morgen | Morgen | Characters/Morgen | 10 components; active: yes | c4210710 / Assets/Characters/Morgen/Morgen.prefab |
| Morgen_bite | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_bite.prefab |
| Morgen_bodyslam | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_bodyslam.prefab |
| Morgen_NonSleeping | Morgen | Characters/Morgen | 10 components; active: yes | c4210710 / Assets/Characters/Morgen/Morgen_NonSleeping.prefab |
| Morgen_roll_left | Morgen Roll Left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_roll_left.prefab |
| Morgen_roll_right | Morgen Roll Right | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_roll_right.prefab |
| Morgen_swipe_1 | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_swipe_1.prefab |
| Morgen_swipe_2 | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_swipe_2.prefab |
| Morgen_swipe_3 | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_swipe_3.prefab |
| Morgen_swipe_4 | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_swipe_4.prefab |
| Morgen_swipe_5 | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_swipe_5.prefab |
| Morgen_swipe_6 | Dragon claw left | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/attacks/Morgen_swipe_6.prefab |
| MorgenHeart | Morgen Heart | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MorgenHeart.prefab |
| morgenhole_pile | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/morgenhole_pile.prefab |
| MorgenSinew | Morgen Sinew | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/MorgenSinew.prefab |
| MorkBorg | — | world/Locations | 2 components; active: yes | eac409ee / Assets/world/Locations/DeepNorth/MorkBorg.prefab |
| Morkborg_gate | Gates of Mörkhalla | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkborg_gate.prefab |
| Morkhalla_balcony_long | — | world/Props | 2 components; active: yes | 9ac7091b / Assets/world/Props/Morkhalla/Morkhalla_balcony_long.prefab |
| Morkhalla_balcony_short | — | world/Props | 2 components; active: yes | 34805ae5 / Assets/world/Props/Morkhalla/Morkhalla_balcony_short.prefab |
| Morkhalla_Banner1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Banner1.prefab |
| Morkhalla_Banner2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Banner2.prefab |
| Morkhalla_Bedroll1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Bedroll1.prefab |
| Morkhalla_Bedroll2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Bedroll2.prefab |
| Morkhalla_Bench | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Bench.prefab |
| Morkhalla_Block | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Block.prefab |
| Morkhalla_BoundingWall_20_broken | — | world/Props | 2 components; active: yes | b4732293 / Assets/world/Props/Morkhalla/Morkhalla_BoundingWall_20_broken.prefab |
| Morkhalla_bridge01 | — | world/Props | 1 components; active: yes | 230feefe / Assets/world/Props/Morkhalla/Morkhalla_bridge01.prefab |
| Morkhalla_bridge01_broken_random | — | world/Props | 1 components; active: yes | 46f936fb / Assets/world/Props/Morkhalla/Morkhalla_bridge01_broken_random.prefab |
| Morkhalla_bridge01_wide_broken_random | — | world/Props | 1 components; active: yes | f478e36e / Assets/world/Props/Morkhalla/Morkhalla_bridge01_wide_broken_random.prefab |
| Morkhalla_bridge02 | — | world/Props | 1 components; active: yes | 230feefe / Assets/world/Props/Morkhalla/Morkhalla_bridge02.prefab |
| Morkhalla_bridge02_broken_random | — | world/Props | 1 components; active: yes | 46f936fb / Assets/world/Props/Morkhalla/Morkhalla_bridge02_broken_random.prefab |
| Morkhalla_bridge03 | — | world/Props | 1 components; active: yes | 72fdb1de / Assets/world/Props/Morkhalla/Morkhalla_bridge03.prefab |
| Morkhalla_bridge03_broken_random | — | world/Props | 1 components; active: yes | 46f936fb / Assets/world/Props/Morkhalla/Morkhalla_bridge03_broken_random.prefab |
| Morkhalla_bridge_davinci | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_bridge_davinci.prefab |
| Morkhalla_bridge_stair01 | — | world/Props | 2 components; active: yes | 7678af9f / Assets/world/Props/Morkhalla/Morkhalla_bridge_stair01.prefab |
| Morkhalla_bridge_stair01_broken | — | world/Props | 2 components; active: yes | 17fcf274 / Assets/world/Props/Morkhalla/Morkhalla_bridge_stair01_broken.prefab |
| Morkhalla_bridge_wood01 | — | world/Props | 1 components; active: yes | 230feefe / Assets/world/Props/Morkhalla/Morkhalla_bridge_wood01.prefab |
| Morkhalla_bridge_wood01_broken | — | world/Props | 1 components; active: yes | 46f936fb / Assets/world/Props/Morkhalla/Morkhalla_bridge_wood01_broken.prefab |
| Morkhalla_bridge_wood02 | — | world/Props | 2 components; active: yes | 46f936fb / Assets/world/Props/Morkhalla/Morkhalla_bridge_wood02.prefab |
| Morkhalla_bridgeBrokenRandom | — | world/Props | 2 components; active: yes | 46f936fb / Assets/world/Props/Morkhalla/Morkhalla_bridgeBrokenRandom.prefab |
| Morkhalla_bridgeWholeRandom | — | world/Props | 2 components; active: yes | 230feefe / Assets/world/Props/Morkhalla/Morkhalla_bridgeWholeRandom.prefab |
| Morkhalla_Chain | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Chain.prefab |
| Morkhalla_ChainLink | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_ChainLink.prefab |
| Morkhalla_ChestAncient | Ancient Chest | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_ChestAncient.prefab |
| Morkhalla_coal_pile_memorial | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_coal_pile_memorial.prefab |
| Morkhalla_Drawbridge | Drawbridge | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Drawbridge.prefab |
| morkhalla_entrance02 | — | world/Rooms | 2 components; active: yes | 72fdb1de / Assets/world/Rooms/morkhalla/morkhalla_entrance02.prefab |
| Morkhalla_Eye1 | Draumyx | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Eye1.prefab |
| Morkhalla_Eye2 | Grimvarn | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Eye2.prefab |
| Morkhalla_Eye3 | Solryth | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Eye3.prefab |
| Morkhalla_Eye4 | Veydris | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Eye4.prefab |
| Morkhalla_Eye5_gemstone | Iolite | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Eye5_gemstone.prefab |
| Morkhalla_Eye6_gemstone | Jade | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Eye6_gemstone.prefab |
| Morkhalla_Eye7_gemstone | Bloodstone | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Eye7_gemstone.prefab |
| Morkhalla_firepit | Campfire; Fire | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_firepit.prefab |
| morkhalla_floor03_tall | — | world/Rooms | 2 components; active: yes | 17fcf274 / Assets/world/Rooms/morkhalla/morkhalla_floor03_tall.prefab |
| Morkhalla_Floor_20 | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Floor_20.prefab |
| Morkhalla_Floor_20_2 | — | world/Props | 2 components; active: yes | 9ac7091b / Assets/world/Props/Morkhalla/Morkhalla_Floor_20_2.prefab |
| Morkhalla_Floor_20_broken | — | world/Props | 2 components; active: yes | 412e6904 / Assets/world/Props/Morkhalla/Morkhalla_Floor_20_broken.prefab |
| Morkhalla_Floor_20_broken2 | — | world/Props | 1 components; active: yes | a6f8a9b8 / Assets/world/Props/Morkhalla/Morkhalla_Floor_20_broken2.prefab |
| Morkhalla_Floor_20_broken3 | — | world/Props | 1 components; active: yes | cefb9193 / Assets/world/Props/Morkhalla/Morkhalla_Floor_20_broken3.prefab |
| Morkhalla_Floor_20_wHole | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Floor_20_wHole.prefab |
| Morkhalla_Floor_2x2 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Floor_2x2.prefab |
| Morkhalla_Floor_4x4 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4.prefab |
| Morkhalla_Floor_4x4_broken01 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_broken01.prefab |
| Morkhalla_Floor_4x4_broken02 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_broken02.prefab |
| Morkhalla_Floor_4x4_hole01 | — | world/Props | 1 components; active: yes | 35ec0b07 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole01.prefab |
| Morkhalla_Floor_4x4_hole02 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole02.prefab |
| Morkhalla_Floor_4x4_hole03 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole03.prefab |
| Morkhalla_Floor_4x4_hole04 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole04.prefab |
| Morkhalla_Floor_4x4_hole05 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole05.prefab |
| Morkhalla_Floor_4x4_hole06 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole06.prefab |
| Morkhalla_Floor_4x4_hole07 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole07.prefab |
| Morkhalla_Floor_4x4_hole08 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole08.prefab |
| Morkhalla_Floor_4x4_hole09 | — | world/Props | 1 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_4x4_hole09.prefab |
| Morkhalla_Floor_RandomHole | — | world/Props | 2 components; active: yes | f18fba97 / Assets/world/Props/Morkhalla/Morkhalla_Floor_RandomHole.prefab |
| Morkhalla_GateDoor | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_GateDoor.prefab |
| Morkhalla_GateDoor02 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_GateDoor02.prefab |
| Morkhalla_GateDoor03 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_GateDoor03.prefab |
| Morkhalla_giant_railing | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_giant_railing.prefab |
| Morkhalla_giant_railing_corner | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_giant_railing_corner.prefab |
| Morkhalla_giant_railing_deco | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_giant_railing_deco.prefab |
| Morkhalla_giant_railing_half | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_giant_railing_half.prefab |
| Morkhalla_giant_railing_single | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_giant_railing_single.prefab |
| Morkhalla_giant_railing_torch | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_giant_railing_torch.prefab |
| Morkhalla_giant_railing_torch_unlit | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_giant_railing_torch_unlit.prefab |
| Morkhalla_jotun_gate | Gates of Mörkhalla | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_jotun_gate.prefab |
| Morkhalla_MetalBar | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_MetalBar.prefab |
| Morkhalla_MetalPillar | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_MetalPillar.prefab |
| Morkhalla_RandomDoor | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_RandomDoor.prefab |
| Morkhalla_RandomEye | — | world/Props | 2 components; active: yes | 8f4977e8 / Assets/world/Props/Morkhalla/Morkhalla_RandomEye.prefab |
| Morkhalla_RandomLoot | — | world/Props | 2 components; active: yes | 8f4977e8 / Assets/world/Props/Morkhalla/Morkhalla_RandomLoot.prefab |
| Morkhalla_RandomRailDeco | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_RandomRailDeco.prefab |
| Morkhalla_RandomRubble | — | world/Props | 2 components; active: yes | a4db9b07 / Assets/world/Props/Morkhalla/Morkhalla_RandomRubble.prefab |
| Morkhalla_RandomSpawner | — | world/Props | 2 components; active: yes | 11b3f7ee / Assets/world/Props/Morkhalla/Morkhalla_RandomSpawner.prefab |
| Morkhalla_RandomWallDeco | — | world/Props | 2 components; active: yes | cf401443 / Assets/world/Props/Morkhalla/Morkhalla_RandomWallDeco.prefab |
| Morkhalla_Rubble1 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rubble1.prefab |
| Morkhalla_Rubble1_fall | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rubble1_fall.prefab |
| Morkhalla_Rubble2 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rubble2.prefab |
| Morkhalla_Rubble2_fall | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rubble2_fall.prefab |
| Morkhalla_Rubble3 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rubble3.prefab |
| Morkhalla_Rubble4 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rubble4.prefab |
| Morkhalla_Rubble_Destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rubble_Destroyed.prefab |
| Morkhalla_Rubble_mix | — | world/Props | 1 components; active: yes | a4db9b07 / Assets/world/Props/Morkhalla/Morkhalla_Rubble_mix.prefab |
| Morkhalla_rubble_trashpile | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_rubble_trashpile.prefab |
| Morkhalla_rubble_trashpile_destruction | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_rubble_trashpile_destruction.prefab |
| Morkhalla_Rug_corner | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rug_corner.prefab |
| Morkhalla_Rug_end1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rug_end1.prefab |
| Morkhalla_Rug_end2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rug_end2.prefab |
| Morkhalla_Rug_middle | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rug_middle.prefab |
| Morkhalla_Rug_stair | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Rug_stair.prefab |
| Morkhalla_Stairs_12 | — | world/Props | 1 components; active: yes | 8f4977e8 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_12.prefab |
| Morkhalla_Stairs_12_2 | — | world/Props | 1 components; active: yes | e72af72 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_12_2.prefab |
| Morkhalla_Stairs_12_railing | — | world/Props | 1 components; active: yes | 5d6de0f8 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_12_railing.prefab |
| Morkhalla_Stairs_giant | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Stairs_giant.prefab |
| Morkhalla_Stairs_giant_base | — | world/Props | 2 components; active: yes | 8f4977e8 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_giant_base.prefab |
| Morkhalla_Stairs_giant_railing | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_giant_railing.prefab |
| Morkhalla_Stairs_giant_short | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_giant_short.prefab |
| Morkhalla_Stairs_giant_short_broken1 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_giant_short_broken1.prefab |
| Morkhalla_Stairs_giant_short_broken2 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Stairs_giant_short_broken2.prefab |
| Morkhalla_Statue | — | world/Props | 2 components; active: yes | 9ac7091b / Assets/world/Props/Morkhalla/Morkhalla_Statue.prefab |
| Morkhalla_Statue2 | — | world/Props | 2 components; active: yes | 9ac7091b / Assets/world/Props/Morkhalla/Morkhalla_Statue2.prefab |
| Morkhalla_Statue_base | — | world/Props | 2 components; active: yes | 9ac7091b / Assets/world/Props/Morkhalla/Morkhalla_Statue_base.prefab |
| Morkhalla_Statue_random_rubble | — | world/Props | 1 components; active: yes | 1940dcc2 / Assets/world/Props/Morkhalla/Morkhalla_Statue_random_rubble.prefab |
| Morkhalla_Statue_random_standing | — | world/Props | 1 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Statue_random_standing.prefab |
| Morkhalla_StatuePieceArmL | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceArmL.prefab |
| Morkhalla_StatuePieceArmL_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceArmL_big.prefab |
| Morkhalla_StatuePieceArmR | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceArmR.prefab |
| Morkhalla_StatuePieceArmR_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceArmR_big.prefab |
| Morkhalla_StatuePieceFace | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceFace.prefab |
| Morkhalla_StatuePieceFace_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceFace_big.prefab |
| Morkhalla_StatuePieceFeet | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceFeet.prefab |
| Morkhalla_StatuePieceFeet_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceFeet_big.prefab |
| Morkhalla_StatuePieceHorn | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceHorn.prefab |
| Morkhalla_StatuePieceHorn2 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceHorn2.prefab |
| Morkhalla_StatuePieceHorn2_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceHorn2_big.prefab |
| Morkhalla_StatuePieceHorn_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceHorn_big.prefab |
| Morkhalla_StatuePieceLegs | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceLegs.prefab |
| Morkhalla_StatuePieceLegs_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceLegs_big.prefab |
| Morkhalla_StatuePieceSword | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceSword.prefab |
| Morkhalla_StatuePieceSword_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceSword_big.prefab |
| Morkhalla_StatuePieceTorso | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceTorso.prefab |
| Morkhalla_StatuePieceTorso_big | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatuePieceTorso_big.prefab |
| Morkhalla_StatueSword | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatueSword.prefab |
| Morkhalla_StatueSword_hanging | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_StatueSword_hanging.prefab |
| Morkhalla_Stonepile | Black Marble Pile | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Stonepile.prefab |
| Morkhalla_StonePillar | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_StonePillar.prefab |
| Morkhalla_StonePillar_broken_bottom | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_StonePillar_broken_bottom.prefab |
| Morkhalla_StonePillar_broken_top | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_StonePillar_broken_top.prefab |
| Morkhalla_StonePillarSupport | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_StonePillarSupport.prefab |
| Morkhalla_Stool | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Stool.prefab |
| Morkhalla_Table | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Table.prefab |
| Morkhalla_Trainingdummy1 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Trainingdummy1.prefab |
| Morkhalla_Trainingdummy2 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_Trainingdummy2.prefab |
| Morkhalla_Wall | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Wall.prefab |
| Morkhalla_Wall_20 | — | world/Props | 2 components; active: yes | cf401443 / Assets/world/Props/Morkhalla/Morkhalla_Wall_20.prefab |
| Morkhalla_Wall_20_broken | — | world/Props | 2 components; active: yes | d07b7355 / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_broken.prefab |
| Morkhalla_Wall_20_broken2 | — | world/Props | 2 components; active: yes | 4c93b92c / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_broken2.prefab |
| Morkhalla_Wall_20_broken3 | — | world/Props | 2 components; active: yes | b7cad132 / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_broken3.prefab |
| Morkhalla_Wall_20_broken3_2 | — | world/Props | 2 components; active: yes | eac409ee / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_broken3_2.prefab |
| Morkhalla_Wall_20_broken4 | — | world/Props | 1 components; active: yes | 4e093e6d / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_broken4.prefab |
| Morkhalla_Wall_20_broken5 | — | world/Props | 1 components; active: yes | eac409ee / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_broken5.prefab |
| Morkhalla_Wall_20_pillars | — | world/Props | 2 components; active: yes | 3c3d232e / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_pillars.prefab |
| Morkhalla_Wall_20_stair | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_stair.prefab |
| Morkhalla_Wall_20_wGate | — | world/Props | 2 components; active: yes | d2449ee7 / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_wGate.prefab |
| Morkhalla_Wall_20_wGate2 | — | world/Props | 2 components; active: yes | a4db9b07 / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_wGate2.prefab |
| Morkhalla_Wall_20_wGate3 | — | world/Props | 2 components; active: yes | 9d8b40a8 / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_wGate3.prefab |
| Morkhalla_Wall_20_wGate_Entrance | — | world/Props | 2 components; active: yes | 9ac7091b / Assets/world/Props/Morkhalla/Morkhalla_Wall_20_wGate_Entrance.prefab |
| Morkhalla_Wall_broken_center | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Wall_broken_center.prefab |
| Morkhalla_Wall_broken_left | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Wall_broken_left.prefab |
| Morkhalla_Wall_broken_right | — | world/Props | 2 components; active: yes | 57bdadfd / Assets/world/Props/Morkhalla/Morkhalla_Wall_broken_right.prefab |
| Morkhalla_Wall_half | — | world/Props | 2 components; active: yes | bf5bd33e / Assets/world/Props/Morkhalla/Morkhalla_Wall_half.prefab |
| Morkhalla_WallChain1 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_WallChain1.prefab |
| Morkhalla_WeaponStand | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_WeaponStand.prefab |
| morkhalla_web_corner | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/morkhalla_web_corner.prefab |
| morkhalla_web_horisontal | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/morkhalla_web_horisontal.prefab |
| morkhalla_web_tunnel | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/morkhalla_web_tunnel.prefab |
| Morkhalla_WoodBoards | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_WoodBoards.prefab |
| Morkhalla_woodboards_Destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/Morkhalla_woodboards_Destroyed.prefab |
| MountainGraveStone01 | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/MountainGrave/MountainGraveStone01.prefab |
| MountainKit_brazier | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/MountainKit_brazier.prefab |
| MountainKit_brazier_blue | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Caverocks/MountainKit_brazier_blue.prefab |
| MountainKit_brazier_purple | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/MountainKit_brazier_purple.prefab |
| mountainkit_chair | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Caverocks/mountainkit_chair.prefab |
| MountainKit_int_floor | — | world/Props | 4 components; active: yes | 3c0435af / Assets/world/Props/Caverocks/MountainKit_int_floor.prefab |
| MountainKit_int_floor_2x2 | — | world/Props | 4 components; active: yes | d023f9eb / Assets/world/Props/Caverocks/MountainKit_int_floor_2x2.prefab |
| MountainKit_int_wall_2x4 | — | world/Props | 3 components; active: yes | 9214f153 / Assets/world/Props/Caverocks/MountainKit_int_wall_2x4.prefab |
| MountainKit_int_wall_4x2 | — | world/Props | 3 components; active: yes | f8dff913 / Assets/world/Props/Caverocks/MountainKit_int_wall_4x2.prefab |
| MountainKit_int_wall_4x4 | — | world/Props | 3 components; active: yes | 81cff51 / Assets/world/Props/Caverocks/MountainKit_int_wall_4x4.prefab |
| mountainkit_table | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Caverocks/mountainkit_table.prefab |
| MountainKit_wood_gate | Wood Gate | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Caverocks/MountainKit_wood_gate.prefab |
| mud_road | Level Ground | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/mud_road.prefab |
| mud_road_v2 | Level Ground | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/mud_road_v2.prefab |
| mudfloor | — | world/Props | 1 components; active: yes | 9be62d21 / Assets/world/Props/DirtWalls/mudfloor.prefab |
| mudpile | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MudPile/mudpile.prefab |
| mudpile2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MudPile/mudpile2.prefab |
| mudpile2_frac | Muddy Scrap Pile | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/MudPile/mudpile2_frac.prefab |
| mudpile_beacon | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/MudPile/mudpile_beacon.prefab |
| mudpile_frac | Muddy Scrap Pile | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/MudPile/mudpile_frac.prefab |
| mudpile_old | Muddy Scrap Pile | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/MudPile/mudpile_old.prefab |
| Munin | Munin | Characters/Raven | 2 components; active: yes | c4210710 / Assets/Characters/Raven/Munin.prefab |
| Mushroom | Mushroom | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Mushroom.prefab |
| MushroomBlue | Blue Mushroom | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MushroomBlue.prefab |
| MushroomBzerker | Toadstool | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MushroomBzerker.prefab |
| MushroomJotunPuffs | Jotun Puffs | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MushroomJotunPuffs.prefab |
| MushroomMagecap | Magecap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MushroomMagecap.prefab |
| MushroomOmelette | Mushroom Omelette | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MushroomOmelette.prefab |
| MushroomSmokePuff | Smoke Puff | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MushroomSmokePuff.prefab |
| MushroomYellow | Yellow Mushroom | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/MushroomYellow.prefab |
| Music_Ashlands_Fortress | — | Audio/Music | 3 components; active: yes | b51de604 / Assets/Audio/Music/Locations/Music_Ashlands_Fortress.prefab |
| Music_Ashlands_Ruins | — | Audio/Music | 3 components; active: yes | aaa02a16 / Assets/Audio/Music/Locations/Music_Ashlands_Ruins.prefab |
| Music_Ashlands_Ruins 2 | — | Audio/Music | 3 components; active: yes | 498f98bd / Assets/Audio/Music/Locations/Music_Ashlands_Ruins 2.prefab |
| Music_Ashlands_Ruins 3 | — | Audio/Music | 3 components; active: yes | b7d80aaf / Assets/Audio/Music/Locations/Music_Ashlands_Ruins 3.prefab |
| Music_BogWitch | — | Audio/Music | 3 components; active: yes | 3e896e5d / Assets/Audio/Music/Locations/Music_BogWitch.prefab |
| Music_DN_Memorial | — | Audio/Music | 3 components; active: yes | 25830207 / Assets/Audio/Music/Locations/Music_DN_Memorial.prefab |
| Music_DN_Village | — | Audio/Music | 3 components; active: yes | b53e4ad5 / Assets/Audio/Music/Locations/Music_DN_Village.prefab |
| Music_DvergrExcavationSite | — | Audio/Music | 3 components; active: yes | 3957cfd4 / Assets/Audio/Music/Locations/Music_DvergrExcavationSite.prefab |
| Music_DvergrTower | — | Audio/Music | 3 components; active: yes | 7660d748 / Assets/Audio/Music/Locations/Music_DvergrTower.prefab |
| Music_FrostCavesSanctum | — | Audio/Music | 2 components; active: yes | 4eaf74a8 / Assets/Audio/Music/Locations/Music_FrostCavesSanctum.prefab |
| Music_FulingCamp | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/Music_FulingCamp.prefab |
| Music_GreydwarfCamp | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/Music_GreydwarfCamp.prefab |
| Music_Haldor | — | Audio/Music | 3 components; active: yes | 84b014f6 / Assets/Audio/Music/Locations/Music_Haldor.prefab |
| Music_Hildir | — | Audio/Music | 3 components; active: yes | d9b97a3d / Assets/Audio/Music/Locations/Music_Hildir.prefab |
| Music_MeadowsVillageFarm | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/Music_MeadowsVillageFarm.prefab |
| Music_MountainCottage | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/Music_MountainCottage.prefab |
| Music_SealedTower | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/Music_SealedTower.prefab |
| Music_StoneHenge | — | Audio/Music | 4 components; active: yes | c4210710 / Assets/Audio/Music/Locations/Music_StoneHenge.prefab |
| Neck | Neck | Characters/Neck | 9 components; active: yes | c4210710 / Assets/Characters/Neck/Neck.prefab |
| Neck_BiteAttack | jaws | Characters/Neck | 3 components; active: yes | c4210710 / Assets/Characters/Neck/attacks/Neck_BiteAttack.prefab |
| Neck_Ragdoll | — | Characters/Neck | 4 components; active: yes | c4210710 / Assets/Characters/Neck/fx/Neck_Ragdoll.prefab |
| NeckTail | Neck Tail | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/NeckTail.prefab |
| NeckTailGrilled | Grilled Neck Tail | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/NeckTailGrilled.prefab |
| Needle | Needle | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Needle.prefab |
| NestRock | — | world/Props | 3 components; active: yes | 86c8ff36 / Assets/world/Props/DrakeNest/NestRock.prefab |
| NornThread | Nornathread | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/NornThread.prefab |
| NorthMemorialPlace | — | world/Locations | 2 components; active: yes | 25830207 / Assets/world/Locations/DeepNorth/NorthMemorialPlace.prefab |
| NorthVillage | — | world/Locations | 2 components; active: yes | b53e4ad5 / Assets/world/Locations/DeepNorth/NorthVillage.prefab |
| Oak1 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/oak/Oak1.prefab |
| Oak_log | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/oak/logs/Oak_log.prefab |
| Oak_log_half | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/oak/logs/Oak_log_half.prefab |
| Oak_Sapling | Oak Sapling | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/oak/Oak_Sapling.prefab |
| OakStub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/oak/OakStub.prefab |
| Oat | Oats | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Oat.prefab |
| OatFlour | Oat Flour | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/OatFlour.prefab |
| OatmealLingonberryJam | Oatmeal | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/OatmealLingonberryJam.prefab |
| OatMilk | Oat Milk | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/OatMilk.prefab |
| OatSeeds | Oat Seeds | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/OatSeeds.prefab |
| Obsidian | Obsidian | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Obsidian.prefab |
| obsidian_pile | Obsidian Pile | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/obsidian_pile.prefab |
| odin | — | Characters/Odin | 7 components; active: yes | c4210710 / Assets/Characters/Odin/odin.prefab |
| offeraltar_bonemass | — | world/Props | 3 components; active: yes | cd230c7f / Assets/world/Props/offeraltar/offeraltar_bonemass.prefab |
| offeraltar_deer | Mystical Altar | world/Props | 3 components; active: yes | b3a2b0f3 / Assets/world/Props/offeraltar/offeraltar_deer.prefab |
| offeraltar_dragon | Sacrificial Altar | world/Props | 3 components; active: yes | fac4ecb7 / Assets/world/Props/offeraltar/offeraltar_dragon.prefab |
| offeraltar_fader | Altar of The Emerald Flame | world/Props | 2 components; active: yes | 1080ee37 / Assets/world/Props/offeraltar/offeraltar_fader.prefab |
| offeraltar_FrozenKing | Strange Bowl | world/Props | 3 components; active: yes | e06fccc7 / Assets/world/Props/offeraltar/offeraltar_FrozenKing.prefab |
| offeraltar_FrozenKing_bossroom | Strange Bowl | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/offeraltar/offeraltar_FrozenKing_bossroom.prefab |
| offeraltar_gdking | — | world/Props | 2 components; active: yes | 5f09202f / Assets/world/Props/offeraltar/offeraltar_gdking.prefab |
| offeraltar_goblinking | Mystical Altar | world/Props | 2 components; active: yes | 32fd94e5 / Assets/world/Props/offeraltar/offeraltar_goblinking.prefab |
| offeraltar_memorialsite | Ancient Altar | world/Props | 4 components; active: yes | 25830207 / Assets/world/Props/offeraltar/offeraltar_memorialsite.prefab |
| offeraltar_queen | Hive seat | world/Props | 3 components; active: yes | cd0f218 / Assets/world/Props/offeraltar/offeraltar_queen.prefab |
| OLD_PSGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/OLD_PSGamepadMap.prefab |
| OLD_wood_roof | Wood roof | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/OLD_wood_roof.prefab |
| OLD_wood_roof_icorner | Wood roof icorner | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/OLD_wood_roof_icorner.prefab |
| OLD_wood_roof_ocorner | Wood roof ocorner | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/OLD_wood_roof_ocorner.prefab |
| OLD_wood_roof_top | Wood roof ridge | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/OLD_wood_roof_top.prefab |
| OLD_wood_wall_roof | Wood wall roof | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/OLD_wood_wall_roof.prefab |
| Onion | Onion | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Onion.prefab |
| OnionSeeds | Onion Seeds | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/OnionSeeds.prefab |
| OnionSoup | Onion Soup | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/OnionSoup.prefab |
| Ooze | Ooze | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Ooze.prefab |
| oozebomb_explosion | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/oozebomb_explosion.prefab |
| oozebomb_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/oozebomb_projectile.prefab |
| OozeMork | Dead Pulp | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/OozeMork.prefab |
| OrbFrostFire | Frostfire Essence | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/OrbFrostFire.prefab |
| OrbThunderBlood | Thunderblood Essence | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/OrbThunderBlood.prefab |
| ormbunke_green_medium | — | world/Props | 1 components; active: yes | d59cfac / Assets/world/Props/vegetation/ormbunke/ormbunke_green_medium.prefab |
| OvenPancake | Oven Pancake | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/OvenPancake.prefab |
| OvenPancakeUncooked | Oven Pancake Batter | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/OvenPancakeUncooked.prefab |
| Pancakes | Pancakes | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Pancakes.prefab |
| path | Pathen | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/path.prefab |
| path_v2 | Pathen | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/path_v2.prefab |
| paved_road | Paved Road | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/paved_road.prefab |
| paved_road_v2 | Paved Road | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/paved_road_v2.prefab |
| Pickable_Ashstone | Grausten | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Ashstone.prefab |
| Pickable_Barley | Barley | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Barley.prefab |
| Pickable_Barley_Wild | Barley | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Barley_Wild.prefab |
| Pickable_BlackCoreStand | Black Core | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_BlackCoreStand.prefab |
| Pickable_BogIronOre | Bog Iron | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_BogIronOre.prefab |
| Pickable_Branch | Branch | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Branch.prefab |
| Pickable_Branch_Snow | Branch | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Branch_Snow.prefab |
| Pickable_Carrot | Carrot | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Carrot.prefab |
| Pickable_Charredskull | Charred Skull | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Charredskull.prefab |
| Pickable_Dandelion | Dandelion | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Dandelion.prefab |
| Pickable_DolmenTreasure | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_DolmenTreasure.prefab |
| Pickable_DragonEgg | Dragon Egg | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_DragonEgg.prefab |
| Pickable_DvergerThing | Turnip | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_DvergerThing.prefab |
| Pickable_DvergrLantern | Dvergr Lantern | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_DvergrLantern.prefab |
| Pickable_DvergrMineTreasure | Coin Pile | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_DvergrMineTreasure.prefab |
| Pickable_DvergrStein | Dvergr Tankard | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_DvergrStein.prefab |
| Pickable_Fiddlehead | Fiddlehead | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Fiddlehead.prefab |
| Pickable_Fishingrod | Fishing Rod | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Fishingrod.prefab |
| Pickable_Flax | Flax | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Flax.prefab |
| Pickable_Flax_Wild | Flax | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Flax_Wild.prefab |
| Pickable_Flint | Flint | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Flint.prefab |
| Pickable_ForestCryptRandom | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_ForestCryptRandom.prefab |
| Pickable_ForestCryptRemains01 | Skeletal Remains | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_ForestCryptRemains01.prefab |
| Pickable_ForestCryptRemains02 | Skeletal Remains | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_ForestCryptRemains02.prefab |
| Pickable_ForestCryptRemains03 | Skeletal Remains | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_ForestCryptRemains03.prefab |
| Pickable_ForestCryptRemains04 | Skeletal Remains | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_ForestCryptRemains04.prefab |
| Pickable_FrostCoreHanger | Frostcore | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_FrostCoreHanger.prefab |
| Pickable_GlowWorm | Luminous Larva | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_GlowWorm.prefab |
| Pickable_Hairstrands01 | Fenris Hair | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Hairstrands01.prefab |
| Pickable_Hairstrands02 | Fenris Hair | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Hairstrands02.prefab |
| Pickable_HardRockOffspring | Stone | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_HardRockOffspring.prefab |
| Pickable_Item | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Item.prefab |
| Pickable_Kale | Kale | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Kale.prefab |
| Pickable_MeatPile | Meat Pile | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_MeatPile.prefab |
| Pickable_Meteorite | Meteorite | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Meteorite.prefab |
| Pickable_MoltenCoreStand | Molten Core | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_MoltenCoreStand.prefab |
| Pickable_MorkHallaTreasure | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_MorkHallaTreasure.prefab |
| Pickable_MorkHallaTreasure_Group | — | GameElements/Items | 1 components; active: yes | 11b3f7ee / Assets/GameElements/Items/pickables/Pickable_MorkHallaTreasure_Group.prefab |
| Pickable_MountainCaveCrystal | Crystal | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_MountainCaveCrystal.prefab |
| Pickable_MountainCaveObsidian | Obsidian | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_MountainCaveObsidian.prefab |
| Pickable_MountainCaveRandom | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_MountainCaveRandom.prefab |
| Pickable_MountainRemains01_buried | Skeletal Remains | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_MountainRemains01_buried.prefab |
| Pickable_Mushroom | Mushroom | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Mushroom.prefab |
| Pickable_Mushroom_blue | Blue Mushroom | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Mushroom_blue.prefab |
| Pickable_Mushroom_JotunPuffs | Jotun Puffs | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Mushroom_JotunPuffs.prefab |
| Pickable_Mushroom_Magecap | Magecap | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Mushroom_Magecap.prefab |
| Pickable_Mushroom_yellow | Yellow Mushroom | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Mushroom_yellow.prefab |
| Pickable_Oat | Oat Seeds | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Oat.prefab |
| Pickable_Obsidian | Obsidian | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Obsidian.prefab |
| Pickable_Onion | Onion | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Onion.prefab |
| Pickable_Pot_Shard | Pot Shard | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Pot_Shard.prefab |
| Pickable_Poteitr | Poteitr | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Poteitr.prefab |
| Pickable_RandomFood | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_RandomFood.prefab |
| Pickable_RoyalJelly | Royal Jelly | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_RoyalJelly.prefab |
| Pickable_SeedCarrot | Carrot Seeds | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SeedCarrot.prefab |
| Pickable_SeedKale | Kale Seeds | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SeedKale.prefab |
| Pickable_SeedOnion | Onion Seeds | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SeedOnion.prefab |
| Pickable_SeedTurnip | Turnip Seeds | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SeedTurnip.prefab |
| Pickable_SmokePuff | Smoke Puff | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SmokePuff.prefab |
| Pickable_Snowball | Snowball | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Snowball.prefab |
| Pickable_Stone | Stone | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Stone.prefab |
| Pickable_StoneRock | Rock | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_StoneRock.prefab |
| Pickable_SulfurRock | Sulfur Rock | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SulfurRock.prefab |
| Pickable_SunkenCryptRandom | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SunkenCryptRandom.prefab |
| Pickable_SurtlingCoreStand | Surtling Core | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_SurtlingCoreStand.prefab |
| Pickable_Swordpiece1 | Dyrnwyn Hilt Fragment | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Swordpiece1.prefab |
| Pickable_Swordpiece2 | Dyrnwyn Blade Fragment | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Swordpiece2.prefab |
| Pickable_Swordpiece3 | Dyrnwyn Tip Fragment | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Swordpiece3.prefab |
| Pickable_Tar | Tar | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Tar.prefab |
| Pickable_TarBig | Tar | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_TarBig.prefab |
| Pickable_Thistle | Thistle | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Thistle.prefab |
| Pickable_Tin | Tin Ore | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Tin.prefab |
| Pickable_Turnip | Turnip | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_Turnip.prefab |
| Pickable_VoltureEgg | Volture Egg | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Pickable_VoltureEgg.prefab |
| PickaxeAntler | Antler Pickaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/PickaxeAntler.prefab |
| PickaxeBlackMetal | Black Metal Pickaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/PickaxeBlackMetal.prefab |
| PickaxeBronze | Bronze Pickaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/PickaxeBronze.prefab |
| PickaxeIron | Iron Pickaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/PickaxeIron.prefab |
| PickaxeStone | Stone Pickaxe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/PickaxeStone.prefab |
| piece_ArcheryTarget | Archery Target | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_ArcheryTarget.prefab |
| piece_artisanstation | Artisan Table | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_artisanstation.prefab |
| piece_asksvinskeleton | Asksvin Skeleton | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_asksvinskeleton.prefab |
| piece_banner01 | Black Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner01.prefab |
| piece_banner02 | Blue Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner02.prefab |
| piece_banner03 | White and Red Striped Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner03.prefab |
| piece_banner04 | Red Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner04.prefab |
| piece_banner05 | Green Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner05.prefab |
| piece_banner06 | Blue, Red and White Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner06.prefab |
| piece_banner07 | White and Blue Striped Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner07.prefab |
| piece_banner08 | Yellow Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner08.prefab |
| piece_banner09 | Purple Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner09.prefab |
| piece_banner10 | Orange Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner10.prefab |
| piece_banner11 | White Banner | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_banner11.prefab |
| piece_barber | Barber Station | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_barber.prefab |
| piece_bathtub | Hot Tub | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_bathtub.prefab |
| piece_bed02 | Dragon Bed | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_bed02.prefab |
| piece_beehive | Beehive | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_beehive.prefab |
| piece_bench01 | Wood Bench | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_bench01.prefab |
| piece_bench_runed | Carved Bench | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_bench_runed.prefab |
| piece_birdnest | Birds&#x27; Nest | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_birdnest.prefab |
| piece_blackmarble_bench | Black Marble Bench | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_blackmarble_bench.prefab |
| piece_blackmarble_table | Black Marble Table | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_blackmarble_table.prefab |
| piece_blackmarble_throne | Black Marble Throne | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_blackmarble_throne.prefab |
| piece_blackwood_bench | Wood Bench | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_blackwood_bench.prefab |
| piece_blackwood_bench01 | Ashwood Bench | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_blackwood_bench01.prefab |
| piece_bone_throne | Bone Throne | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_bone_throne.prefab |
| piece_brazierceiling01 | Hanging Brazier; Fire | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_brazierceiling01.prefab |
| piece_brazierfloor01 | Fire; Standing Brazier | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_brazierfloor01.prefab |
| piece_brazierfloor02 | Fire; Blue Standing Brazier | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_brazierfloor02.prefab |
| piece_cartographytable | Cartography Table | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_cartographytable.prefab |
| piece_cauldron | Cauldron | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_cauldron.prefab |
| piece_CelebrationGarland | Flower Garland | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_CelebrationGarland.prefab |
| piece_chair | Stool | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chair.prefab |
| piece_chair02 | Wood Chair | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chair02.prefab |
| piece_chair03 | Darkwood Chair; Wood Chair | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chair03.prefab |
| piece_chair_runed | Carved Chair | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chair_runed.prefab |
| piece_Charred_Balista | Skugg | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Charred_Balista/piece_Charred_Balista.prefab |
| piece_chest | Reinforced Chest | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest.prefab |
| piece_chest_barrel | Barrel | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest_barrel.prefab |
| piece_chest_blackmetal | Black Metal Chest | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest_blackmetal.prefab |
| piece_chest_grausten | Grausten Chest | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest_grausten.prefab |
| piece_chest_private | Personal Chest | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest_private.prefab |
| piece_chest_treasure | Treasure Chest | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest_treasure.prefab |
| piece_chest_warderobe | Wardrobe | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest_warderobe.prefab |
| piece_chest_wood | Chest | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_chest_wood.prefab |
| piece_cloth_hanging_door | Red Jute Curtain | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_cloth_hanging_door.prefab |
| piece_cloth_hanging_door_blue | Blue Jute Drapes | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_cloth_hanging_door_blue.prefab |
| piece_cloth_hanging_door_blue2 | Blue Jute Curtain | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_cloth_hanging_door_blue2.prefab |
| piece_cookingstation | Cooking Station | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_cookingstation.prefab |
| piece_cookingstation_iron | Iron Cooking Station | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_cookingstation_iron.prefab |
| piece_drawbridge | Timberwood Drawbridge; Drawbridge | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_drawbridge.prefab |
| piece_drawbridge_log | Rustic Drawbridge; Drawbridge | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_drawbridge_log.prefab |
| piece_dvergr_lantern | Dvergr Wall Lantern | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_lantern.prefab |
| piece_dvergr_lantern_pole | Dvergr Pole Lantern | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_lantern_pole.prefab |
| piece_dvergr_metal_wall_2x2 | Dvergr Metal Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_metal_wall_2x2.prefab |
| piece_dvergr_pole | Dvergr Pole | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_pole.prefab |
| piece_dvergr_sharpstakes | Dvergr Sharp Stakes | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_sharpstakes.prefab |
| piece_dvergr_spiralstair | Dvergr Spiral Staircase Left | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_spiralstair.prefab |
| piece_dvergr_spiralstair_right | Dvergr Spiral Staircase Right | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_spiralstair_right.prefab |
| piece_dvergr_stake_wall | Dvergr Stakewall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_stake_wall.prefab |
| piece_dvergr_wood_door | Dvergr Door | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_wood_door.prefab |
| piece_dvergr_wood_wall | Dvergr Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_dvergr_wood_wall.prefab |
| piece_EternalPyre | Eternal Pyre | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_EternalPyre.prefab |
| piece_FaderEmbers | Eternal Pyre | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_FaderEmbers.prefab |
| piece_FairylightGarland | Fey Lights | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_FairylightGarland.prefab |
| Piece_flametal_beam | Flametal Beam | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_flametal_beam.prefab |
| Piece_flametal_pillar | Flametal Pillar | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_flametal_pillar.prefab |
| piece_FrostFoundry | Frost Foundry | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_FrostFoundry.prefab |
| piece_FrostKiln | Frigid Kiln | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_FrostKiln.prefab |
| piece_gift1 | Yuleklapp | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_gift1.prefab |
| piece_gift2 | Yuleklapp | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_gift2.prefab |
| piece_gift3 | Yuleklapp | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_gift3.prefab |
| Piece_grausten_floor_1x1 | Grausten Floor 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_floor_1x1.prefab |
| Piece_grausten_floor_2x2 | Grausten Floor 2x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_floor_2x2.prefab |
| Piece_grausten_floor_4x4 | Grausten Floor 4x4 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_floor_4x4.prefab |
| Piece_grausten_pillar_arch | Grausten Medium Arch | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillar_arch.prefab |
| Piece_grausten_pillar_arch_small | Grausten Small Arch | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillar_arch_small.prefab |
| Piece_grausten_pillarbase_medium | Grausten Medium Pillar | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillarbase_medium.prefab |
| Piece_grausten_pillarbase_small | Grausten Small Pillar | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillarbase_small.prefab |
| Piece_grausten_pillarbase_tapered | Grausten Tapered Pillar | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillarbase_tapered.prefab |
| Piece_grausten_pillarbase_tapered_inverted | Grausten Tapered Pillar (Inverted) | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillarbase_tapered_inverted.prefab |
| Piece_grausten_pillarbeam_medium | Grausten Medium Beam | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillarbeam_medium.prefab |
| Piece_grausten_pillarbeam_small | Grausten Small Beam | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_pillarbeam_small.prefab |
| piece_grausten_roof_45 | Grausten Roof | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_grausten_roof_45.prefab |
| piece_grausten_roof_45_arch | Grausten Arched Roof | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_grausten_roof_45_arch.prefab |
| piece_grausten_roof_45_arch_corner | Grausten Arched Roof Corner | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_grausten_roof_45_arch_corner.prefab |
| piece_grausten_roof_45_arch_corner2 | Grausten Arched Roof Corner | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_grausten_roof_45_arch_corner2.prefab |
| piece_grausten_roof_45_corner | Grausten Roof Corner | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_grausten_roof_45_corner.prefab |
| piece_grausten_roof_45_corner2 | Grausten Roof Corner | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_grausten_roof_45_corner2.prefab |
| Piece_grausten_stone_ladder | Grausten Steep Stairs | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_stone_ladder.prefab |
| piece_grausten_stonestair | Grausten Stairs | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_grausten_stonestair.prefab |
| Piece_grausten_wall_1x2 | Grausten Wall 1x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_wall_1x2.prefab |
| Piece_grausten_wall_2x2 | Grausten Wall 2x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_wall_2x2.prefab |
| Piece_grausten_wall_4x2 | Grausten Wall 4x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_wall_4x2.prefab |
| Piece_grausten_wall_arch | Grausten Wall Arch | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_wall_arch.prefab |
| Piece_grausten_wall_arch_inverted | Grausten Wall Arch (Inverted) | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_wall_arch_inverted.prefab |
| Piece_grausten_window_2x2 | Grausten Window 2x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_window_2x2.prefab |
| Piece_grausten_window_4x2 | Grausten Window 4x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/Piece_grausten_window_4x2.prefab |
| piece_groundtorch | Standing Iron Torch | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_groundtorch.prefab |
| piece_groundtorch_blue | Standing Blue-burning Iron Torch | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_groundtorch_blue.prefab |
| piece_groundtorch_green | Standing Green-burning Iron Torch | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_groundtorch_green.prefab |
| piece_groundtorch_mist | Wisp Torch | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_groundtorch_mist.prefab |
| piece_groundtorch_wood | Standing Wood Torch | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_groundtorch_wood.prefab |
| piece_hexagonal_door | Hexagonal Gate | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_hexagonal_door.prefab |
| piece_hoodedlantern | Hooded Lantern | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_hoodedlantern.prefab |
| piece_icecube | Ice Block | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_icecube.prefab |
| piece_icon | — | UI/prefabs | 7 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/piece_icon.prefab |
| piece_jackoturnip | Jack-o-turnip | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_jackoturnip.prefab |
| piece_Lavalantern | Lava Lantern | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_Lavalantern.prefab |
| piece_logbench01 | Sitting Log | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_logbench01.prefab |
| piece_magetable | Galdr Table | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_magetable.prefab |
| piece_magetable_ext | Rune Table | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_magetable_ext.prefab |
| piece_magetable_ext2 | Unfading Candles | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_magetable_ext2.prefab |
| piece_magetable_ext3 | Feathery Wreath | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_magetable_ext3.prefab |
| piece_magetable_ext4 | Standing Loom | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_magetable_ext4.prefab |
| piece_maypole | Maypole | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_maypole.prefab |
| piece_MeadCauldron | Mead Ketill | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/MeadCauldron/piece_MeadCauldron.prefab |
| piece_mistletoe | Mistletoe | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_mistletoe.prefab |
| piece_moose_throne | Antler Throne | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_moose_throne.prefab |
| piece_oven | Stone Oven | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_oven.prefab |
| piece_pot1 | Medium Green Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot1.prefab |
| piece_pot1_cracked | Medium Green Pot; Medium Clay Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot1_cracked.prefab |
| piece_pot1_red | Medium Red Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot1_red.prefab |
| piece_pot2 | Large Green Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot2.prefab |
| piece_pot2_cracked | Large Green Pot; Large Clay Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot2_cracked.prefab |
| piece_pot2_red | Large Red Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot2_red.prefab |
| piece_pot3 | Small Green Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot3.prefab |
| piece_pot3_cracked | Small Green Pot; Small Clay Pot | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot3_cracked.prefab |
| piece_pot3_red | Small Red Pot | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_pot3_red.prefab |
| piece_preptable | Food Preparation Table | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_preptable.prefab |
| piece_remove_feaster | Remove | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_remove_feaster.prefab |
| piece_repair | Repair | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_repair.prefab |
| piece_sapcollector | Sap Extractor | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_sapcollector.prefab |
| piece_sharpstakes | Sharp Stakes | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_sharpstakes.prefab |
| piece_shieldgenerator | Shield Generator | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_shieldgenerator.prefab |
| piece_snowlantern | Snow Lantern | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_snowlantern.prefab |
| piece_spinningwheel | Spinning Wheel | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_spinningwheel.prefab |
| piece_stakewall_blackwood | Ashwood Stakewall | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_stakewall_blackwood.prefab |
| piece_stonecutter | Stonecutter | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_stonecutter.prefab |
| piece_table | Table | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_table.prefab |
| piece_table_oak | Long Heavy Table | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_table_oak.prefab |
| piece_table_round | Round Table | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_table_round.prefab |
| piece_table_runed | Long Carved Table | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_table_runed.prefab |
| piece_table_runed_small | Square Carved Table | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_table_runed_small.prefab |
| piece_throne01 | Raven Throne | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_throne01.prefab |
| piece_throne02 | Stone Throne | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_throne02.prefab |
| piece_TrainingDummy | T.W.I.G. | GameElements/Pieces | 10 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_TrainingDummy.prefab |
| piece_trap_troll | Trap | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_trap_troll.prefab |
| piece_turret | Ballista | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_turret.prefab |
| piece_walltorch | Sconce | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_walltorch.prefab |
| piece_wisplure | Wisp Fountain | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_wisplure.prefab |
| piece_workbench | Workbench | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_workbench.prefab |
| piece_workbench_ext1 | Chopping Block | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_workbench_ext1.prefab |
| piece_workbench_ext2 | Tanning Rack | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_workbench_ext2.prefab |
| piece_workbench_ext3 | Adze | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_workbench_ext3.prefab |
| piece_workbench_ext4 | Tool Shelf | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_workbench_ext4.prefab |
| piece_xmascrown | Yule Wreath | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_xmascrown.prefab |
| piece_xmasgarland | Yule Garland | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_xmasgarland.prefab |
| piece_xmastree | Yule Tree | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/piece_xmastree.prefab |
| PineCone | Pine Cone | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/PineCone.prefab |
| PineTree | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/PineTree.prefab |
| Pinetree_01 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/PineTree/Pinetree_01.prefab |
| Pinetree_01_Stub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/PineTree/Pinetree_01_Stub.prefab |
| PineTree_log | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/PineTree/logs/PineTree_log.prefab |
| PineTree_log_half | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/PineTree/logs/PineTree_log_half.prefab |
| PineTree_log_halfOLD | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/logs/PineTree_log_halfOLD.prefab |
| PineTree_logOLD | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/logs/PineTree_logOLD.prefab |
| PineTree_Sapling | Pine Sapling | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/PineTree/PineTree_Sapling.prefab |
| Pinetree_Snow | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/PineTree/Pinetree_Snow.prefab |
| Pinetree_Snow_dead | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/PineTree/Pinetree_Snow_dead.prefab |
| PineTree_Snow_log | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/PineTree/logs/PineTree_Snow_log.prefab |
| PineTree_Snow_log_half | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/PineTree/logs/PineTree_Snow_log_half.prefab |
| PineTree_Snow_log_half_frost_troll | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/PineTree/logs/PineTree_Snow_log_half_frost_troll.prefab |
| PineTree_Snow_log_XL | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/PineTree/logs/PineTree_Snow_log_XL.prefab |
| PineTree_Snow_log_XL_half | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/PineTree/logs/PineTree_Snow_log_XL_half.prefab |
| Pinetree_Snow_Stub | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/PineTree/Pinetree_Snow_Stub.prefab |
| PineTree_snowfall | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/PineTree/fx/PineTree_snowfall.prefab |
| PiquantPie | Piquant Pie | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/PiquantPie.prefab |
| PiquantPieUncooked | Uncooked Piquant Pie | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/PiquantPieUncooked.prefab |
| placeable_bigrock_01 | Ornamental Boulder | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/placeable_bigrock_01.prefab |
| placeable_bigrock_02 | Decorative Boulder | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/placeable_bigrock_02.prefab |
| Placeable_HardRock | Mysterious Rock | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Placeable_HardRock.prefab |
| Placeable_Stone | Stone | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/Placeable_Stone.prefab |
| PlaceMarker | — | Characters/Player | 1 components; active: yes | c4210710 / Assets/Characters/Player/fx/PlaceMarker.prefab |
| PlaceofMystery1 | — | world/Locations | 2 components; active: yes | ceeec7a8 / Assets/world/Locations/Ashlands/PlaceofMystery1.prefab |
| PlaceofMystery2 | — | world/Locations | 2 components; active: yes | 7176ff77 / Assets/world/Locations/Ashlands/PlaceofMystery2.prefab |
| Player | Human | Characters/Player | 12 components; active: yes | c4210710 / Assets/Characters/Player/Player.prefab |
| Player_ragdoll | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/fx/Player_ragdoll.prefab |
| Player_ragdoll_old | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/fx/Player_ragdoll_old.prefab |
| Player_tombstone | Grave | Characters/Player | 9 components; active: yes | c4210710 / Assets/Characters/Player/Player_tombstone.prefab |
| PlayerUnarmed | Unarmed | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/PlayerUnarmed.prefab |
| portal | Portal | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/portal.prefab |
| portal_stone | Portal – Stone | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/portal_stone.prefab |
| portal_wood | Portal | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/portal_wood.prefab |
| Pot_Shard_Green | Pot Shard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Pot_Shard_Green.prefab |
| Pot_Shard_Red | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Pot_Shard_Red.prefab |
| Poteitr | Poteitr | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Poteitr.prefab |
| PoteitrSeeds | Seed Poteitr | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/PoteitrSeeds.prefab |
| PowderedDragonEgg | Powdered Dragon Eggshells | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/PowderedDragonEgg.prefab |
| projectile_ashlandmeteor | — | Characters/Meteor | 4 components; active: yes | c4210710 / Assets/Characters/Meteor/projectile_ashlandmeteor.prefab |
| projectile_ashlandmeteor2 | — | Characters/Meteor | 4 components; active: yes | c4210710 / Assets/Characters/Meteor/projectile_ashlandmeteor2.prefab |
| projectile_beam | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/projectile_beam.prefab |
| projectile_chitinharpoon | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/ChitinHarpoon/projectile_chitinharpoon.prefab |
| projectile_FimbulvinterMeteor | — | Characters/Meteor | 4 components; active: yes | c4210710 / Assets/Characters/Meteor/projectile_FimbulvinterMeteor.prefab |
| Projectile_GrapplingHook | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/GrapplingHook/Projectile_GrapplingHook.prefab |
| Projectile_GrapplingHook_secondary | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/GrapplingHook/Projectile_GrapplingHook_secondary.prefab |
| projectile_lavaRock | — | Characters/LavaRock | 4 components; active: yes | c4210710 / Assets/Characters/LavaRock/projectile_lavaRock.prefab |
| projectile_meteor | — | Characters/GoblinKing | 5 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/projectile_meteor.prefab |
| projectile_meteor_fader | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/projectile_meteor_fader.prefab |
| projectile_spikes_frozenking | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/projectile_spikes_frozenking.prefab |
| projectile_splitner | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Splitner/projectile_splitner.prefab |
| projectile_splitner_blood | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Splitner/projectile_splitner_blood.prefab |
| projectile_splitner_lightning | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Splitner/projectile_splitner_lightning.prefab |
| projectile_splitner_nature | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Splitner/projectile_splitner_nature.prefab |
| projectile_wolffang | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/wolffang/projectile_wolffang.prefab |
| prop_ashwood_bed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_ashwood_bed.prefab |
| prop_bed02 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_bed02.prefab |
| prop_bonfire | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_bonfire.prefab |
| prop_cauldron_ext1_spice | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_cauldron_ext1_spice.prefab |
| prop_cauldron_ext3_butchertable | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_cauldron_ext3_butchertable.prefab |
| prop_cauldron_ext5_mortarandpestle | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_cauldron_ext5_mortarandpestle.prefab |
| prop_cauldron_ext6_rollingpins | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_cauldron_ext6_rollingpins.prefab |
| prop_chest_warderobe | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_chest_warderobe.prefab |
| prop_FeastAshlands | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_FeastAshlands.prefab |
| prop_FeastMeadows | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_FeastMeadows.prefab |
| prop_forge_ext2 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_forge_ext2.prefab |
| prop_forge_ext5 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_forge_ext5.prefab |
| prop_hearth | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_hearth.prefab |
| prop_itemstand | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_itemstand.prefab |
| prop_itemstand_TrophyDraugrElite | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_itemstand_TrophyDraugrElite.prefab |
| prop_itemstand_TrophyGoblinBrute | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_itemstand_TrophyGoblinBrute.prefab |
| prop_itemstand_TrophyGoblinShaman | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_itemstand_TrophyGoblinShaman.prefab |
| prop_itemstand_TrophyGreydwarf | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_itemstand_TrophyGreydwarf.prefab |
| prop_itemstand_TrophyGreydwarfBrute | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_itemstand_TrophyGreydwarfBrute.prefab |
| prop_itemstand_TrophySeekerBrute | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_itemstand_TrophySeekerBrute.prefab |
| prop_piece_bench_runed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_bench_runed.prefab |
| prop_piece_brazierfloor01 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_brazierfloor01.prefab |
| prop_piece_cauldron | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_cauldron.prefab |
| prop_piece_chair03 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_chair03.prefab |
| prop_piece_cookingstation | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_cookingstation.prefab |
| prop_piece_MeadCauldron | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_MeadCauldron.prefab |
| prop_piece_workbench_ext1 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_workbench_ext1.prefab |
| prop_piece_workbench_ext2 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_workbench_ext2.prefab |
| prop_piece_workbench_ext3 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_workbench_ext3.prefab |
| prop_piece_workbench_ext4 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_piece_workbench_ext4.prefab |
| prop_preptable | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_preptable.prefab |
| prop_Tankard | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_Tankard.prefab |
| prop_TrophyDraugrElite | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_TrophyDraugrElite.prefab |
| prop_TrophyGoblinBrute | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_TrophyGoblinBrute.prefab |
| prop_TrophyGoblinShaman | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_TrophyGoblinShaman.prefab |
| prop_TrophyGreydwarf | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_TrophyGreydwarf.prefab |
| prop_TrophyGreydwarfBrute | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_TrophyGreydwarfBrute.prefab |
| prop_TrophySeekerBrute | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_TrophySeekerBrute.prefab |
| prop_wood_stack | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/prop_wood_stack.prefab |
| PropFeastDeepNorth | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/DeepNorth_TimberHall/PropFeastDeepNorth.prefab |
| ProustitePowder | Proustite Powder | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/ProustitePowder.prefab |
| PSGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/PSGamepadMap.prefab |
| Pukeberries | Bukeperries | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Pukeberries.prefab |
| PulledBear | Pulled Bear | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/PulledBear.prefab |
| PungentPebbles | Pungent Pebbles | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/PungentPebbles.prefab |
| QueenBee | Queen Bee | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/QueenBee.prefab |
| QueenDrop | Majestic Carapace | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/QueenDrop.prefab |
| QueensJam | Queen&#x27;s Jam | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/QueensJam.prefab |
| RadialTab | — | UI/prefabs | 6 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/RadialTab.prefab |
| radiation | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/eitr/radiation.prefab |
| Raft | Raft | GameElements/Ships | 10 components; active: yes | c4210710 / Assets/GameElements/Ships/Raft.prefab |
| Ragdoll_Asksvin | — | Characters/Asksvin | 3 components; active: yes | c4210710 / Assets/Characters/Asksvin/fx/Ragdoll_Asksvin.prefab |
| Ragdoll_Asksvin_Hatchling | — | Characters/Asksvin | 3 components; active: yes | c4210710 / Assets/Characters/Asksvin/fx/Ragdoll_Asksvin_Hatchling.prefab |
| raise | Raise Ground | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/raise.prefab |
| raise_v2 | Raise Ground | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/raise_v2.prefab |
| RandomAmbientBase | — | Audio/Ambients | 4 components; active: yes | 61c598bb / Assets/Audio/Ambients/RandomAmbientBase.prefab |
| Raspberry | Raspberries | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Raspberry.prefab |
| RaspberryBush | Raspberries | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Bush01/RaspberryBush.prefab |
| Ravens | — | Characters/Raven | 1 components; active: yes | c4210710 / Assets/Characters/Raven/Ravens.prefab |
| RawMeat | Boar Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/RawMeat.prefab |
| replant | Grass | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/replant.prefab |
| replant_v2 | Grass | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/replant_v2.prefab |
| ReportUser | — | UI/prefabs | 7 components; active: yes | c4210710 / Assets/UI/prefabs/ReportUser.prefab |
| Resin | Resin | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Resin.prefab |
| RoastedCrustPie | Roasted Crust Pie | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/RoastedCrustPie.prefab |
| RoastedCrustPieUncooked | Uncooked Roasted Crust Pie | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/RoastedCrustPieUncooked.prefab |
| rock1_mistlands | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock1_mistlands.prefab |
| rock1_mountain | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock1_mountain.prefab |
| rock1_mountain_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock1_mountain_frac.prefab |
| rock2_heath | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock2_heath.prefab |
| rock2_heath_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock2_heath_frac.prefab |
| rock2_mountain | — | world/Props | 3 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/rock2_mountain.prefab |
| rock2_mountain | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock2_mountain.prefab |
| rock2_mountain_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock2_mountain_frac.prefab |
| rock3_ice | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_ice.prefab |
| rock3_ice_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_ice_frac.prefab |
| rock3_mountain | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_mountain.prefab |
| rock3_mountain_1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_mountain_1.prefab |
| rock3_mountain_1_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_mountain_1_frac.prefab |
| rock3_mountain_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_mountain_frac.prefab |
| rock3_silver | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_silver.prefab |
| rock3_silver_frac | Silver Deposit | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock3_silver_frac.prefab |
| rock4_ashlands_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_ashlands_frac.prefab |
| rock4_bigrock_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_bigrock_frac.prefab |
| rock4_coast | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_coast.prefab |
| rock4_coast_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_coast_frac.prefab |
| rock4_copper | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_copper.prefab |
| rock4_copper_frac | Copper Deposit | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_copper_frac.prefab |
| rock4_forest | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_forest.prefab |
| rock4_forest_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_forest_frac.prefab |
| rock4_heath | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_heath.prefab |
| rock4_heath_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/rock4_heath_frac.prefab |
| Rock_3 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rock_3.prefab |
| Rock_3_deepnorth | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rock_3_deepnorth.prefab |
| Rock_3_deepnorth_frac | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rock_3_deepnorth_frac.prefab |
| Rock_3_frac | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rock_3_frac.prefab |
| Rock_3_static | — | world/Props | 3 components; active: yes | 1e488b5 / Assets/world/Props/Rock_3_static.prefab |
| Rock_4 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rock_4.prefab |
| Rock_4_deepnorth | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rock_4_deepnorth.prefab |
| Rock_4_plains | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rock_4_plains.prefab |
| Rock_7 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rock_7.prefab |
| Rock_7_deepnorth | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rock_7_deepnorth.prefab |
| Rock_7_meadows | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rock_7_meadows.prefab |
| rock_a | — | world/Props | 6 components; active: yes | d59cfac / Assets/world/Props/rock_a/rock_a.prefab |
| Rock_destructible | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Rock_destructible.prefab |
| Rock_destructible_test | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/MineRock/Rock_destructible_test.prefab |
| rock_mistlands1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/rock_mistlands1.prefab |
| rock_mistlands1_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/rock_mistlands1_frac.prefab |
| rock_mistlands2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/rock_mistlands2.prefab |
| RockDolmen_1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/RockDolmen_1.prefab |
| RockDolmen_2 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/RockDolmen_2.prefab |
| RockDolmen_3 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/RockDolmen_3.prefab |
| RockFinger | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/YagluthLocation/RockFinger.prefab |
| RockFinger_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/YagluthLocation/RockFinger_frac.prefab |
| RockFingerBroken | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/YagluthLocation/RockFingerBroken.prefab |
| RockFingerBroken_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/YagluthLocation/RockFingerBroken_frac.prefab |
| rockformation1 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/rockformation1/rockformation1.prefab |
| RockThumb | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/YagluthLocation/RockThumb.prefab |
| RockThumb_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/YagluthLocation/RockThumb_frac.prefab |
| Root | Root | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Root.prefab |
| root07 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CryptKit/root07.prefab |
| root08 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CryptKit/root08.prefab |
| root11 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CryptKit/root11.prefab |
| root12 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CryptKit/root12.prefab |
| RottenMeat | Rotten Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/RottenMeat.prefab |
| RoundLog | Corewood | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/RoundLog.prefab |
| RoyalJelly | Royal Jelly | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/RoyalJelly.prefab |
| Ruby | Ruby | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/Ruby.prefab |
| rug_asksvin | Asksvin Rug | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_asksvin.prefab |
| rug_Bjorn | Bearskin Rug | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_Bjorn.prefab |
| rug_bogwitch_deer | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/BogWitchHut/rug_bogwitch_deer.prefab |
| rug_bogwitch_fur | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/BogWitchHut/rug_bogwitch_fur.prefab |
| rug_bogwitch_wolf | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/BogWitchHut/rug_bogwitch_wolf.prefab |
| rug_deer | Deer Rug | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_deer.prefab |
| rug_fur | Lox Rug | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_fur.prefab |
| rug_hare | Hare Rug | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_hare.prefab |
| rug_moose | Moose Hide Carpet | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_moose.prefab |
| rug_seal | Sealskin Rug | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_seal.prefab |
| rug_straw | Straw | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_straw.prefab |
| rug_wolf | Wolf Rug | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/rug_wolf.prefab |
| Runestone_Ashlands | — | world/Locations | 2 components; active: yes | 2dd816d / Assets/world/Locations/Ashlands/Runestone_Ashlands.prefab |
| RuneStone_Ashlands | Runestone | world/Props | 5 components; active: yes | 2dd816d / Assets/world/Props/RuneStones/RuneStone_Ashlands.prefab |
| Runestone_BlackForest | — | world/Locations | 2 components; active: yes | 96faf98f / Assets/world/Locations/BlackForest/Runestone_BlackForest.prefab |
| RuneStone_BlackForest | Runestone | world/Props | 5 components; active: yes | 96faf98f / Assets/world/Props/RuneStones/RuneStone_BlackForest.prefab |
| Runestone_Boars | — | world/Locations | 2 components; active: yes | 21380151 / Assets/world/Locations/Meadows/Runestone_Boars.prefab |
| RuneStone_Boars | Runestone | world/Props | 5 components; active: yes | 21380151 / Assets/world/Props/RuneStones/RuneStone_Boars.prefab |
| RuneStone_Bonemass | Runestone | world/Props | 4 components; active: yes | cd230c7f / Assets/world/Props/RuneStones/RuneStone_Bonemass.prefab |
| RuneStone_CaveMan | Runestone | world/Props | 5 components; active: yes | b6bd492f / Assets/world/Props/RuneStones/RuneStone_CaveMan.prefab |
| RuneStone_Cavepainting1 | — | world/Props | 3 components; active: yes | 5403a2f0 / Assets/world/Props/RuneStones/RuneStone_Cavepainting1.prefab |
| RuneStone_Cavepainting2 | — | world/Props | 3 components; active: yes | b4cb088a / Assets/world/Props/RuneStones/RuneStone_Cavepainting2.prefab |
| RuneStone_Cavepainting3 | — | world/Props | 3 components; active: yes | 69b96195 / Assets/world/Props/RuneStones/RuneStone_Cavepainting3.prefab |
| RuneStone_Cavepainting4 | — | world/Props | 3 components; active: yes | cf123e5b / Assets/world/Props/RuneStones/RuneStone_Cavepainting4.prefab |
| Runestone_DeepNorth | — | world/Locations | 2 components; active: yes | ab4fa3dd / Assets/world/Locations/Ashlands/Runestone_DeepNorth.prefab |
| RuneStone_DeepNorth | Runestone | world/Props | 5 components; active: yes | ab4fa3dd / Assets/world/Props/RuneStones/RuneStone_DeepNorth.prefab |
| RuneStone_DragonQueen | Runestone | world/Props | 4 components; active: yes | fac4ecb7 / Assets/world/Props/RuneStones/RuneStone_DragonQueen.prefab |
| RuneStone_Drake | Runestone | world/Props | 4 components; active: yes | d9afdb37 / Assets/world/Props/RuneStones/RuneStone_Drake.prefab |
| Runestone_Draugr | — | world/Locations | 2 components; active: yes | 4a83d2b7 / Assets/world/Locations/Swamp/Runestone_Draugr.prefab |
| RuneStone_Draugr | Runestone | world/Props | 5 components; active: yes | 4a83d2b7 / Assets/world/Props/RuneStones/RuneStone_Draugr.prefab |
| RuneStone_GDKing | Runestone | world/Props | 4 components; active: yes | 5f09202f / Assets/world/Props/RuneStones/RuneStone_GDKing.prefab |
| Runestone_Greydwarfs | — | world/Locations | 2 components; active: yes | efbc8659 / Assets/world/Locations/BlackForest/Runestone_Greydwarfs.prefab |
| RuneStone_Greydwarfs | Runestone | world/Props | 5 components; active: yes | efbc8659 / Assets/world/Props/RuneStones/RuneStone_Greydwarfs.prefab |
| Runestone_Meadows | — | world/Locations | 2 components; active: yes | f3aa55b4 / Assets/world/Locations/Meadows/Runestone_Meadows.prefab |
| RuneStone_Meadows | Runestone | world/Props | 5 components; active: yes | f3aa55b4 / Assets/world/Props/RuneStones/RuneStone_Meadows.prefab |
| RuneStone_Memorial1 | Runestone | world/Props | 5 components; active: yes | 25830207 / Assets/world/Props/RuneStones/RuneStone_Memorial1.prefab |
| Runestone_Mistlands | — | world/Locations | 2 components; active: yes | c356035e / Assets/world/Locations/Mistlands/Runestone_Mistlands.prefab |
| RuneStone_Mistlands | Runestone | world/Props | 5 components; active: yes | c356035e / Assets/world/Props/RuneStones/RuneStone_Mistlands.prefab |
| RuneStone_Mistlands_bosshint | A mysterious text | world/Props | 5 components; active: yes | ba621cac / Assets/world/Props/RuneStones/RuneStone_Mistlands_bosshint.prefab |
| Runestone_Mountains | — | world/Locations | 2 components; active: yes | ec2725ad / Assets/world/Locations/Mountains/Runestone_Mountains.prefab |
| RuneStone_Mountains | Runestone | world/Props | 5 components; active: yes | ec2725ad / Assets/world/Props/RuneStones/RuneStone_Mountains.prefab |
| Runestone_Plains | — | world/Locations | 2 components; active: yes | e13071d / Assets/world/Locations/Heath/Runestone_Plains.prefab |
| RuneStone_Plains | Runestone | world/Props | 5 components; active: yes | e13071d / Assets/world/Props/RuneStones/RuneStone_Plains.prefab |
| Runestone_Swamps | — | world/Locations | 2 components; active: yes | c71dfca4 / Assets/world/Locations/Swamp/Runestone_Swamps.prefab |
| RuneStone_Swamps | Runestone | world/Props | 5 components; active: yes | c71dfca4 / Assets/world/Props/RuneStones/RuneStone_Swamps.prefab |
| RuneStone_UpgradeStation | Runestone | world/Props | 5 components; active: yes | c58d692a / Assets/world/Props/RuneStones/RuneStone_UpgradeStation.prefab |
| RuneStone_Windingtunnels | Runestone | world/Props | 5 components; active: yes | 7d165429 / Assets/world/Props/RuneStones/RuneStone_Windingtunnels.prefab |
| RuneTablet_Eikthyr | Runestone | world/Props | 4 components; active: yes | b3a2b0f3 / Assets/world/Props/RuneStones/RuneTablet_Eikthyr.prefab |
| RuneTablet_Fader | Runestone | world/Props | 4 components; active: yes | 1080ee37 / Assets/world/Props/RuneStones/RuneTablet_Fader.prefab |
| RuneTablet_FrozenKing | Runestone | world/Props | 4 components; active: yes | e06fccc7 / Assets/world/Props/RuneStones/RuneTablet_FrozenKing.prefab |
| RuneTablet_GoblinKing | Runestone | world/Props | 4 components; active: yes | 32fd94e5 / Assets/world/Props/RuneStones/RuneTablet_GoblinKing.prefab |
| SacredPillar | — | world/Props | 2 components; active: yes | 4d5957b8 / Assets/world/Props/SacredPillar/model/SacredPillar.prefab |
| SaddleAsksvin | Asksvin Saddle | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/tools/SaddleAsksvin.prefab |
| SaddleLox | Lox Saddle | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/tools/SaddleLox.prefab |
| SaddleMoose | Moose Saddle | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/tools/SaddleMoose.prefab |
| Salad | Salad | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Salad.prefab |
| Sap | Sap | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Sap.prefab |
| sapling_barley | Barley | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_barley.prefab |
| sapling_carrot | Carrot | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_carrot.prefab |
| sapling_flax | Flax | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_flax.prefab |
| sapling_jotunpuffs | Jotun Puffs Primordia; Jotun Puffs | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_jotunpuffs.prefab |
| sapling_Kale | Kale | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_Kale.prefab |
| sapling_magecap | Magecap Primordia; Magecap | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_magecap.prefab |
| sapling_oat | Oat Straw | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_oat.prefab |
| sapling_onion | Onion | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_onion.prefab |
| sapling_poteitr | Poteitr | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_poteitr.prefab |
| sapling_seedcarrot | Seed-carrot | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_seedcarrot.prefab |
| sapling_seedkale | Seed Kale | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_seedkale.prefab |
| sapling_seedonion | Seed-onion | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_seedonion.prefab |
| sapling_seedturnip | Seed-turnip | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_seedturnip.prefab |
| sapling_turnip | Turnip | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/sapling_turnip.prefab |
| Sausages | Sausages | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Sausages.prefab |
| scale_halfwall_1x2 | Scalewood Half Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_halfwall_1x2.prefab |
| scale_quarterwall_1x1 | Scalewood Quarter Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_quarterwall_1x1.prefab |
| scale_wall_2x2 | Scalewood Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_2x2.prefab |
| scale_wall_roof_26 | Scalewood Wall 26° Left | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_26.prefab |
| scale_wall_roof_26_flipped | Scalewood Wall 26° Right | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_26_flipped.prefab |
| scale_wall_roof_26_upsidedown | Scalewood Wall 26° Right (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_26_upsidedown.prefab |
| scale_wall_roof_26_upsidedown_flipped | Scalewood Wall 26° Left (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_26_upsidedown_flipped.prefab |
| scale_wall_roof_45 | Scalewood Wall 45° Left | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_45.prefab |
| scale_wall_roof_45_flipped | Scalewood Wall 45° Right | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_45_flipped.prefab |
| scale_wall_roof_45_upsidedown | Scalewood Wall 45° Right (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_45_upsidedown.prefab |
| scale_wall_roof_45_upsidedown_flipped | Scalewood Wall 45° Left (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_45_upsidedown_flipped.prefab |
| scale_wall_roof_67 | Scalewood Wall 67° Left | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_67.prefab |
| scale_wall_roof_67_flipped | Scalewood Wall 67° Right | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_67_flipped.prefab |
| scale_wall_roof_67_upsidedown | Scalewood Wall 67° Right (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_67_upsidedown.prefab |
| scale_wall_roof_67_upsidedown_flipped | Scalewood Wall 67° Left (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/scale_wall_roof_67_upsidedown_flipped.prefab |
| Scaled 3D Viewport | — | Systems | 4 components; active: yes | c4210710 / Assets/Systems/Scaled 3D Viewport.prefab |
| ScaleHide | Scale Hide | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/ScaleHide.prefab |
| ScorchingMedley | Scorching Medley | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ScorchingMedley.prefab |
| Scythe | Scythe | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/tools/Scythe.prefab |
| ScytheHandle | Scythe Handle | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/ScytheHandle.prefab |
| Seagal | — | Characters/animals | 9 components; active: yes | c4210710 / Assets/Characters/animals/birds/Seagal.prefab |
| Seal | Seal | Characters/seal | 10 components; active: yes | c4210710 / Assets/Characters/seal/Seal.prefab |
| Seal_Pup | Baby Seal | Characters/seal | 10 components; active: yes | c4210710 / Assets/Characters/seal/Seal_Pup.prefab |
| seal_pup_ragdoll | — | Characters/seal | 4 components; active: yes | c4210710 / Assets/Characters/seal/seal_pup_ragdoll.prefab |
| seal_ragdoll | — | Characters/seal | 5 components; active: yes | c4210710 / Assets/Characters/seal/seal_ragdoll.prefab |
| SealBlubber | Seal Blubber | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SealBlubber.prefab |
| SealHide | Seal Pelt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SealHide.prefab |
| SealSoup | Seal Meat Soup | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SealSoup.prefab |
| Seeker | Seeker | Characters/Seeker | 10 components; active: yes | c4210710 / Assets/Characters/Seeker/Seeker.prefab |
| seeker_claw_left | Dragon claw left | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/seeker_claw_left.prefab |
| seeker_claw_right | Dragon claw left | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/seeker_claw_right.prefab |
| seeker_groundslam | Dragon claw left | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/seeker_groundslam.prefab |
| seeker_groundslam_flying | Dragon claw left | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/seeker_groundslam_flying.prefab |
| seeker_land | land | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/seeker_land.prefab |
| seeker_pincers | Dragon claw left | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/seeker_pincers.prefab |
| seeker_takeoff | takeoff | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/attacks/seeker_takeoff.prefab |
| SeekerAspic | Seeker Aspic | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SeekerAspic.prefab |
| SeekerBrood | Seeker Brood | Characters/Seeker | 10 components; active: yes | c4210710 / Assets/Characters/Seeker/SeekerBrood.prefab |
| SeekerBrute | Seeker Soldier | Characters/SeekerBrute | 10 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/SeekerBrute.prefab |
| SeekerBrute_bite | Dragon claw left | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/attacks/SeekerBrute_bite.prefab |
| SeekerBrute_groundslam | slap | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/attacks/SeekerBrute_groundslam.prefab |
| SeekerBrute_ram | Dragon claw left | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/attacks/SeekerBrute_ram.prefab |
| SeekerBrute_Taunt | Brute taunt | Characters/SeekerBrute | 7 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/attacks/SeekerBrute_Taunt.prefab |
| SeekerEgg | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Dvergr/SeekerEgg/SeekerEgg.prefab |
| SeekerEgg_alwayshatch | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Dvergr/SeekerEgg/SeekerEgg_alwayshatch.prefab |
| SeekerQueen | The Queen | Characters/SeekerQueen | 11 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/SeekerQueen.prefab |
| SeekerQueen_Bite | slap | Characters/SeekerQueen | 3 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_Bite.prefab |
| SeekerQueen_Call | Brute taunt | Characters/SeekerQueen | 7 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_Call.prefab |
| SeekerQueen_PierceAOE | slap | Characters/SeekerQueen | 3 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_PierceAOE.prefab |
| SeekerQueen_projectile_spit | — | Characters/SeekerQueen | 4 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_projectile_spit.prefab |
| SeekerQueen_projectile_teleport | — | Characters/SeekerQueen | 3 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_projectile_teleport.prefab |
| SeekerQueen_Rush | slap | Characters/SeekerQueen | 3 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_Rush.prefab |
| SeekerQueen_Slap | slap | Characters/SeekerQueen | 3 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_Slap.prefab |
| SeekerQueen_Spit | dragon breath | Characters/SeekerQueen | 3 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_Spit.prefab |
| SeekerQueen_spithit | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_spithit.prefab |
| SeekerQueen_SpitSpawnAbility | — | Characters/SeekerQueen | 2 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_SpitSpawnAbility.prefab |
| SeekerQueen_Teleport | Brute taunt | Characters/SeekerQueen | 7 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_Teleport.prefab |
| SeekerQueen_triggerspawn_ability | — | Characters/SeekerQueen | 2 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/attacks/SeekerQueen_triggerspawn_ability.prefab |
| Serpent | Serpent | Characters/Serpent | 10 components; active: yes | c4210710 / Assets/Characters/Serpent/Serpent.prefab |
| Serpent_attack | Serpent bite | Characters/Serpent | 3 components; active: yes | c4210710 / Assets/Characters/Serpent/misc/Serpent_attack.prefab |
| Serpent_taunt | Serpent Taunt | Characters/Serpent | 3 components; active: yes | c4210710 / Assets/Characters/Serpent/misc/Serpent_taunt.prefab |
| SerpentMeat | Serpent Meat | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SerpentMeat.prefab |
| SerpentMeatCooked | Cooked Serpent Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SerpentMeatCooked.prefab |
| SerpentScale | Serpent Scale | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SerpentScale.prefab |
| SerpentStew | Serpent Stew | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SerpentStew.prefab |
| SessionPlayerList | — | UI/prefabs | 6 components; active: yes | c4210710 / Assets/UI/prefabs/SessionPlayerList.prefab |
| SessionPlayerListEntry | — | UI/prefabs | 3 components; active: yes | c4210710 / Assets/UI/prefabs/SessionPlayerListEntry.prefab |
| Settings | — | UI/prefabs | 8 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/Settings.prefab |
| SettingsTooltip | — | UI/prefabs | 1 components; active: yes | c4210710 / Assets/UI/prefabs/Settings/SettingsTooltip.prefab |
| sfx_Abomination_alerted | — | Characters/Abomination | 4 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_Abomination_alerted.prefab |
| sfx_abomination_arise_end | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/wav/Arise/sfx_abomination_arise_end.prefab |
| sfx_Abomination_attack | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_Abomination_attack.prefab |
| sfx_Abomination_Attack2_slam_whoosh | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_Abomination_Attack2_slam_whoosh.prefab |
| sfx_Abomination_idle | — | Characters/Abomination | 4 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_Abomination_idle.prefab |
| sfx_Abomination_move | — | Characters/Abomination | 4 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_Abomination_move.prefab |
| sfx_Abomination_swing | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_Abomination_swing.prefab |
| sfx_achievement_unlocked | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/sfx_achievement_unlocked.prefab |
| sfx_arbalest_fire | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/fx/sfx_arbalest_fire.prefab |
| sfx_archery_target_hit | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_archery_target_hit.prefab |
| sfx_arrow_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/fx/sfx_arrow_hit.prefab |
| sfx_asksvin_alert | — | Characters/Asksvin | 5 components; active: yes | c4210710 / Assets/Characters/Asksvin/sfx/Alert/sfx_asksvin_alert.prefab |
| sfx_asksvin_bite | — | Characters/Asksvin | 5 components; active: yes | c4210710 / Assets/Characters/Asksvin/sfx/Bite/sfx_asksvin_bite.prefab |
| sfx_asksvin_death | — | Characters/Asksvin | 5 components; active: yes | c4210710 / Assets/Characters/Asksvin/sfx/Death/sfx_asksvin_death.prefab |
| sfx_asksvin_footstep | — | Characters/Asksvin | 5 components; active: yes | c4210710 / Assets/Characters/Asksvin/sfx/Footsteps/sfx_asksvin_footstep.prefab |
| sfx_asksvin_idle | — | Characters/Asksvin | 5 components; active: yes | c4210710 / Assets/Characters/Asksvin/sfx/Idle/sfx_asksvin_idle.prefab |
| sfx_asksvin_pounce | — | Characters/Asksvin | 5 components; active: yes | c4210710 / Assets/Characters/Asksvin/sfx/Pounce/sfx_asksvin_pounce.prefab |
| sfx_atgeir_attack | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/atgier/fx/sfx_atgeir_attack.prefab |
| sfx_atgeir_attack_secondary | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/atgier/fx/sfx_atgeir_attack_secondary.prefab |
| sfx_axe_flint_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/axe/sfx_axe_flint_hit.prefab |
| sfx_axe_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/axe/sfx_axe_hit.prefab |
| sfx_axe_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/axe/sfx_axe_swing.prefab |
| sfx_baby_seeker_alerted | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_baby_seeker_alerted.prefab |
| sfx_baby_seeker_attack_start | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_baby_seeker_attack_start.prefab |
| sfx_baby_seeker_idle | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_baby_seeker_idle.prefab |
| sfx_babyseal_idle | — | Characters/seal | 5 components; active: yes | c4210710 / Assets/Characters/seal/fx/Audio/BabySeal/sfx_babyseal_idle.prefab |
| sfx_barley_hit | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/barley/fx/sfx_barley_hit.prefab |
| sfx_barnacle_destroyed | — | Characters/Leviathan | 5 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/sfx_barnacle_destroyed.prefab |
| sfx_bat_alerted | — | Characters/Bat | 5 components; active: yes | c4210710 / Assets/Characters/Bat/fx/sfx_bat_alerted.prefab |
| sfx_bat_attack | — | Characters/Bat | 5 components; active: yes | c4210710 / Assets/Characters/Bat/fx/sfx_bat_attack.prefab |
| sfx_bat_idle | — | Characters/Bat | 5 components; active: yes | c4210710 / Assets/Characters/Bat/fx/sfx_bat_idle.prefab |
| sfx_battering_ram_anticipation | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/BatteringRam/sfx/Piston Anticipation/sfx_battering_ram_anticipation.prefab |
| sfx_battering_ram_engine | — | GameElements/Cart | 3 components; active: yes | c4210710 / Assets/GameElements/Cart/BatteringRam/sfx/sfx_battering_ram_engine.prefab |
| sfx_battering_ram_impact | — | GameElements/Cart | 3 components; active: yes | c4210710 / Assets/GameElements/Cart/BatteringRam/sfx/Impact/sfx_battering_ram_impact.prefab |
| sfx_battleaxe_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/battleaxe/sfx_battleaxe_hit.prefab |
| sfx_battleaxe_swing_start | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/battleaxe/sfx_battleaxe_swing_start.prefab |
| sfx_battleaxe_swing_wosh | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/battleaxe/sfx_battleaxe_swing_wosh.prefab |
| sfx_bear_bite_attack | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Melee/sfx_bear_bite_attack.prefab |
| sfx_bear_bite_attack_impact | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Melee/sfx_bear_bite_attack_impact.prefab |
| sfx_bear_claw_attack | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Melee/sfx_bear_claw_attack.prefab |
| sfx_bear_claw_attack slash | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Melee/sfx_bear_claw_attack slash.prefab |
| sfx_bear_death | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Death/sfx_bear_death.prefab |
| sfx_bear_footstep | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Footsteps/sfx_bear_footstep.prefab |
| sfx_bear_hurt | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Hurt/sfx_bear_hurt.prefab |
| sfx_bear_idle | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Idle/sfx_bear_idle.prefab |
| sfx_beehive_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/BeeHive/fx/sfx_beehive_destroyed.prefab |
| sfx_beehive_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/BeeHive/fx/sfx_beehive_hit.prefab |
| sfx_blob_alerted | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blob_alerted.prefab |
| sfx_blob_attack | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blob_attack.prefab |
| sfx_blob_death | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blob_death.prefab |
| sfx_blob_hit | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blob_hit.prefab |
| sfx_blob_idle | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blob_idle.prefab |
| sfx_blob_jump | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blob_jump.prefab |
| sfx_blob_land | — | Characters/Blob | 4 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blob_land.prefab |
| sfx_bloblava_alert | — | Characters/Blob | 6 components; active: yes | c4210710 / Assets/Characters/Blob/sfx/Alert/sfx_bloblava_alert.prefab |
| sfx_bloblava_crawl | — | Characters/Blob | 4 components; active: yes | c4210710 / Assets/Characters/Blob/sfx/Crawl/sfx_bloblava_crawl.prefab |
| sfx_bloblava_death | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/sfx/Death/sfx_bloblava_death.prefab |
| sfx_blobLava_explosion | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blobLava_explosion.prefab |
| sfx_bloblava_grow | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/sfx/Grow/sfx_bloblava_grow.prefab |
| sfx_bloblava_idle | — | Characters/Blob | 6 components; active: yes | c4210710 / Assets/Characters/Blob/sfx/Idle/sfx_bloblava_idle.prefab |
| sfx_bloblava_jump | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/sfx/Jump Land/sfx_bloblava_jump.prefab |
| sfx_bloblava_land | — | Characters/Blob | 4 components; active: yes | c4210710 / Assets/Characters/Blob/sfx/Jump Land/sfx_bloblava_land.prefab |
| sfx_blobtar_attack_spit | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blobtar_attack_spit.prefab |
| sfx_blobtar_idle | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/sfx_blobtar_idle.prefab |
| sfx_boar_alerted | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/sfx_boar_alerted.prefab |
| sfx_boar_attack | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/sfx_boar_attack.prefab |
| sfx_boar_birth | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/sfx_boar_birth.prefab |
| sfx_boar_death | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/sfx_boar_death.prefab |
| sfx_boar_hit | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/sfx_boar_hit.prefab |
| sfx_boar_idle | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/sfx_boar_idle.prefab |
| sfx_boar_love | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/sfx_boar_love.prefab |
| sfx_bogwitch_creak | — | Characters/BogWitch | 5 components; active: yes | c4210710 / Assets/Characters/BogWitch/fx/sfx_bogwitch_creak.prefab |
| sfx_bogwitch_greet | — | Characters/BogWitch | 5 components; active: yes | c4210710 / Assets/Characters/BogWitch/fx/sfx_bogwitch_greet.prefab |
| sfx_bogwitch_random | — | Characters/BogWitch | 5 components; active: yes | c4210710 / Assets/Characters/BogWitch/fx/sfx_bogwitch_random.prefab |
| sfx_bogwitch_trade | — | Characters/BogWitch | 5 components; active: yes | c4210710 / Assets/Characters/BogWitch/fx/sfx_bogwitch_trade.prefab |
| sfx_BogwitchKvastur_attack_hit | — | Characters/Kvastur | 4 components; active: yes | c4210710 / Assets/Characters/Kvastur/fx/sfx_BogwitchKvastur_attack_hit.prefab |
| sfx_BogwitchKvastur_idle | — | Characters/Kvastur | 4 components; active: yes | c4210710 / Assets/Characters/Kvastur/fx/sfx_BogwitchKvastur_idle.prefab |
| sfx_bomb_throw | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/sfx_bomb_throw.prefab |
| sfx_bombdynamite_drop | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombDynamite/sfx/sfx_bombdynamite_drop.prefab |
| sfx_bombdynamite_explosion | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombDynamite/sfx/sfx_bombdynamite_explosion.prefab |
| sfx_bombdynamite_fuse | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombDynamite/sfx/sfx_bombdynamite_fuse.prefab |
| sfx_bomblava_crumble | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombLava/sfx/Crumble/sfx_bomblava_crumble.prefab |
| sfx_bomblava_fail | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombLava/sfx/Fail/sfx_bomblava_fail.prefab |
| sfx_bomblava_rocks | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombLava/sfx/Rocks/sfx_bomblava_rocks.prefab |
| sfx_bombsiege_explosion | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSiege/sfx/sfx_bombsiege_explosion.prefab |
| sfx_Bonemass_alert | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_alert.prefab |
| sfx_Bonemass_death | — | Characters/Bonemass | 6 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_death.prefab |
| sfx_Bonemass_Hit | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_Hit.prefab |
| sfx_Bonemass_idle | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_idle.prefab |
| sfx_Bonemass_punch_start | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_punch_start.prefab |
| sfx_Bonemass_spawn_draugr_start | — | Characters/Bonemass | 4 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_spawn_draugr_start.prefab |
| sfx_Bonemass_throw_start | — | Characters/Bonemass | 4 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_throw_start.prefab |
| sfx_Bonemass_throw_trigger | — | Characters/Bonemass | 4 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_Bonemass_throw_trigger.prefab |
| sfx_bonemaw_serpent_alert | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/sfx/Alert/sfx_bonemaw_serpent_alert.prefab |
| sfx_bonemaw_serpent_bite | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/sfx/Bite/sfx_bonemaw_serpent_bite.prefab |
| sfx_bonemaw_serpent_death | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/sfx/Death/sfx_bonemaw_serpent_death.prefab |
| sfx_bonemaw_serpent_spit | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/sfx/Spit/sfx_bonemaw_serpent_spit.prefab |
| sfx_bonemaw_serpent_spit_hit | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/sfx/Spit/sfx_bonemaw_serpent_spit_hit.prefab |
| sfx_bonepile_destroyed | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_bonepile_destroyed.prefab |
| sfx_bones_pick | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/fx/sfx_bones_pick.prefab |
| sfx_bossstone_attach_done | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/StartTemple/fx/sfx_bossstone_attach_done.prefab |
| sfx_bow_draw | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/fx/sfx_bow_draw.prefab |
| sfx_bow_fire | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/fx/sfx_bow_fire.prefab |
| sfx_bow_fire_silent | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/fx/sfx_bow_fire_silent.prefab |
| sfx_bowl_AddItem | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/bowl/fx/sfx_bowl_AddItem.prefab |
| sfx_branch_break | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/TheHole/Branch/sfx/sfx_branch_break.prefab |
| sfx_branch_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/TheHole/Branch/sfx/sfx_branch_hit.prefab |
| sfx_build_cultivator | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_cultivator.prefab |
| sfx_build_hammer_crystal | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_hammer_crystal.prefab |
| sfx_build_hammer_default | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_hammer_default.prefab |
| sfx_build_hammer_ice | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_hammer_ice.prefab |
| sfx_build_hammer_metal | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_hammer_metal.prefab |
| sfx_build_hammer_stone | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_hammer_stone.prefab |
| sfx_build_hammer_wood | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_hammer_wood.prefab |
| sfx_build_hoe | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_build_hoe.prefab |
| sfx_bush_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Bush01/fx/sfx_bush_hit.prefab |
| sfx_carrion_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/sfx_carrion_destroyed.prefab |
| sfx_cart_hit | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/fx/sfx_cart_hit.prefab |
| sfx_catapult_ammo_load | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/sfx/Load Ammo/sfx_catapult_ammo_load.prefab |
| sfx_catapult_charge | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/sfx/sfx_catapult_charge.prefab |
| sfx_catapult_legs_down | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/sfx/Legs/sfx_catapult_legs_down.prefab |
| sfx_catapult_legs_up | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/sfx/Legs/sfx_catapult_legs_up.prefab |
| sfx_catapult_place_item | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/vfx/sfx_catapult_place_item.prefab |
| sfx_catapult_shoot | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/sfx/sfx_catapult_shoot.prefab |
| sfx_charred_alert | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Melee/Alert/sfx_charred_alert.prefab |
| sfx_charred_archer_bow_draw | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Archer/sfx_charred_archer_bow_draw.prefab |
| sfx_charred_archer_bow_release | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Archer/sfx_charred_archer_bow_release.prefab |
| sfx_charred_archer_volley_draw | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Archer/sfx_charred_archer_volley_draw.prefab |
| sfx_charred_archer_volley_release | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Archer/sfx_charred_archer_volley_release.prefab |
| sfx_charred_death | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Melee/Death/sfx_charred_death.prefab |
| sfx_charred_footstep | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Footsteps/sfx_charred_footstep.prefab |
| sfx_charred_hurt | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Hurt/sfx_charred_hurt.prefab |
| sfx_charred_idle | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Melee/Idle/sfx_charred_idle.prefab |
| sfx_charred_mage_alert | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Mage/Alert/sfx_charred_mage_alert.prefab |
| sfx_charred_mage_attack_charge | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Mage/Attack/sfx_charred_mage_attack_charge.prefab |
| sfx_charred_mage_attack_impact | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Mage/Attack/sfx_charred_mage_attack_impact.prefab |
| sfx_charred_mage_attack_shoot | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Mage/Attack/sfx_charred_mage_attack_shoot.prefab |
| sfx_charred_mage_spawn_ground | — | Characters/TheCharred | 4 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Mage/Spawn/sfx_charred_mage_spawn_ground.prefab |
| sfx_charred_mage_spawn_staff | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Mage/Spawn/sfx_charred_mage_spawn_staff.prefab |
| sfx_charred_melee_attack_lift | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Melee/Attack/sfx_charred_melee_attack_lift.prefab |
| sfx_charred_melee_attack_stab | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Melee/Attack/sfx_charred_melee_attack_stab.prefab |
| sfx_charred_melee_attack_swing | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Melee/Attack/sfx_charred_melee_attack_swing.prefab |
| sfx_charred_spawner_destroy | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Charred Spawner/sfx_charred_spawner_destroy.prefab |
| sfx_charred_spawner_loop | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Charred Spawner/sfx_charred_spawner_loop.prefab |
| sfx_charred_twitcher_alert | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Alert/sfx_charred_twitcher_alert.prefab |
| sfx_charred_twitcher_attack | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Attack/sfx_charred_twitcher_attack.prefab |
| sfx_charred_twitcher_death | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Death/sfx_charred_twitcher_death.prefab |
| sfx_charred_twitcher_hurt | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Hurt/sfx_charred_twitcher_hurt.prefab |
| sfx_charred_twitcher_idle | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Idle/sfx_charred_twitcher_idle.prefab |
| sfx_charred_twitcher_summoned_alert | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Alert/sfx_charred_twitcher_summoned_alert.prefab |
| sfx_charred_twitcher_throw | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Throw/sfx_charred_twitcher_throw.prefab |
| sfx_charred_twitcher_throw_impact | — | Characters/TheCharred | 5 components; active: yes | c4210710 / Assets/Characters/TheCharred/sfx/Twitcher/Throw/sfx_charred_twitcher_throw_impact.prefab |
| sfx_chest_close | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Chests/fx/sfx_chest_close.prefab |
| sfx_chest_open | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Chests/fx/sfx_chest_open.prefab |
| sfx_chick_hurt | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_chick_hurt.prefab |
| sfx_chicken_death | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_chicken_death.prefab |
| sfx_chicken_eat | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_chicken_eat.prefab |
| sfx_chicken_footstep | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_chicken_footstep.prefab |
| sfx_chicken_hurt | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_chicken_hurt.prefab |
| sfx_chicken_idle_vocal | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_chicken_idle_vocal.prefab |
| sfx_chicken_idle_wingflap | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_chicken_idle_wingflap.prefab |
| sfx_cinder_rain_hit | — | Audio/Ambients | 5 components; active: yes | c4210710 / Assets/Audio/Ambients/Ashlands/Cinder Rain/sfx_cinder_rain_hit.prefab |
| sfx_claw_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sword/sfx_claw_swing.prefab |
| sfx_clay_pot_break | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/objects/clay_pots/sfx_clay_pot_break.prefab |
| sfx_club_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/club/sfx_club_hit.prefab |
| sfx_club_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/club/sfx_club_swing.prefab |
| sfx_coins_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_coins_destroyed.prefab |
| sfx_coins_pile_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_coins_pile_destroyed.prefab |
| sfx_coins_pile_placed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_coins_pile_placed.prefab |
| sfx_coins_placed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_coins_placed.prefab |
| sfx_cooking_station_burnt | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Grill/fx/sfx_cooking_station_burnt.prefab |
| sfx_cooking_station_done | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Grill/fx/sfx_cooking_station_done.prefab |
| sfx_cooking_station_take | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Grill/fx/sfx_cooking_station_take.prefab |
| sfx_creature_consume | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/sfx_creature_consume.prefab |
| sfx_crow_death | — | Characters/animals | 5 components; active: yes | c4210710 / Assets/Characters/animals/birds/crow/fx/sfx_crow_death.prefab |
| sfx_crow_idle | — | Characters/animals | 4 components; active: yes | c4210710 / Assets/Characters/animals/birds/crow/fx/sfx_crow_idle.prefab |
| sfx_darkwood_door_close | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_darkwood_door_close.prefab |
| sfx_darkwood_door_open | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_darkwood_door_open.prefab |
| sfx_death_vibration_only | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_death_vibration_only.prefab |
| sfx_deathsquito_attack | — | Characters/Deathsquito | 5 components; active: yes | c4210710 / Assets/Characters/Deathsquito/fx/sfx_deathsquito_attack.prefab |
| sfx_deepnorth_gate_activate | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/sfx/sfx_deepnorth_gate_activate.prefab |
| sfx_deepnorth_gate_close_loop | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/sfx/sfx_deepnorth_gate_close_loop.prefab |
| sfx_deepnorth_gate_open_loop | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/sfx/sfx_deepnorth_gate_open_loop.prefab |
| sfx_deer_alerted | — | Characters/Deer | 5 components; active: yes | c4210710 / Assets/Characters/Deer/audio/sfx_deer_alerted.prefab |
| sfx_deer_death | — | Characters/Deer | 5 components; active: yes | c4210710 / Assets/Characters/Deer/audio/sfx_deer_death.prefab |
| sfx_deer_idle | — | Characters/Deer | 5 components; active: yes | c4210710 / Assets/Characters/Deer/audio/sfx_deer_idle.prefab |
| sfx_demister_start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/demister/sfx/sfx_demister_start.prefab |
| sfx_dodge | — | Characters/Player | 6 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_dodge.prefab |
| sfx_door_close | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_door_close.prefab |
| sfx_door_open | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_door_open.prefab |
| sfx_dragon_alerted | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_alerted.prefab |
| sfx_dragon_coldball_explode | — | Characters/Dragon | 6 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_coldball_explode.prefab |
| sfx_dragon_coldball_launch | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_coldball_launch.prefab |
| sfx_dragon_coldball_start | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_coldball_start.prefab |
| sfx_dragon_coldbreath_start | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_coldbreath_start.prefab |
| sfx_dragon_coldbreath_trailon | — | Characters/Dragon | 6 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_coldbreath_trailon.prefab |
| sfx_dragon_death | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_death.prefab |
| sfx_dragon_flap | — | Characters/Dragon | 4 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_flap.prefab |
| sfx_dragon_footstep | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_footstep.prefab |
| sfx_dragon_hurt | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_hurt.prefab |
| sfx_dragon_idle | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_idle.prefab |
| sfx_dragon_melee_hit | — | Characters/Dragon | 6 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_melee_hit.prefab |
| sfx_dragon_melee_start | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_melee_start.prefab |
| sfx_dragon_scream | — | Characters/Dragon | 6 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/sfx_dragon_scream.prefab |
| sfx_dragonegg_destroy | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/dragon/sfx_dragonegg_destroy.prefab |
| sfx_draugr_alerted | — | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/sfx_draugr_alerted.prefab |
| sfx_draugr_death | — | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/sfx_draugr_death.prefab |
| sfx_draugr_hit | — | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/sfx_draugr_hit.prefab |
| sfx_draugr_idle | — | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/sfx_draugr_idle.prefab |
| sfx_draugrpile_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DraugrPileSpawner/fx/sfx_draugrpile_destroyed.prefab |
| sfx_draugrpile_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DraugrPileSpawner/fx/sfx_draugrpile_hit.prefab |
| sfx_DraugrSpawn | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_DraugrSpawn.prefab |
| sfx_drink | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_drink.prefab |
| sfx_drop | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_drop.prefab |
| sfx_dverger_ball_start | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_ball_start.prefab |
| sfx_dverger_fireball_rain_shot | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_fireball_rain_shot.prefab |
| sfx_dverger_fireball_rain_start | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_fireball_rain_start.prefab |
| sfx_dverger_footsteps | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_footsteps.prefab |
| sfx_dverger_heal_finish | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_heal_finish.prefab |
| sfx_dverger_heal_start | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_heal_start.prefab |
| sfx_dverger_heavyattack_launch | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_heavyattack_launch.prefab |
| sfx_dverger_ice_aoe_start | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_ice_aoe_start.prefab |
| sfx_dverger_ice_projectile_start | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_ice_projectile_start.prefab |
| sfx_dverger_staff_baseattack_foley | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_staff_baseattack_foley.prefab |
| sfx_dverger_staff_kolvattack_foley | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_staff_kolvattack_foley.prefab |
| sfx_dverger_staff_poke_foley | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/Attacks/sfx_dverger_staff_poke_foley.prefab |
| sfx_dverger_vo_alerted | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/VO/sfx_dverger_vo_alerted.prefab |
| sfx_dverger_vo_attack | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/VO/sfx_dverger_vo_attack.prefab |
| sfx_dverger_vo_death | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/VO/sfx_dverger_vo_death.prefab |
| sfx_dverger_vo_hurt | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/VO/sfx_dverger_vo_hurt.prefab |
| sfx_dverger_vo_idle | — | Characters/Dverger | 5 components; active: yes | c4210710 / Assets/Characters/Dverger/sfx/VO/sfx_dverger_vo_idle.prefab |
| sfx_eat | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_eat.prefab |
| sfx_eikthyr_alert | — | Characters/Eikthyr | 5 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/sfx_eikthyr_alert.prefab |
| sfx_eikthyr_attack | — | Characters/Eikthyr | 5 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/sfx_eikthyr_attack.prefab |
| sfx_eikthyr_death | — | Characters/Eikthyr | 5 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/sfx_eikthyr_death.prefab |
| sfx_eikthyr_footstep | — | Characters/Eikthyr | 5 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/sfx_eikthyr_footstep.prefab |
| sfx_eikthyr_hit | — | Characters/Eikthyr | 5 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/sfx_eikthyr_hit.prefab |
| sfx_eikthyr_idle | — | Characters/Eikthyr | 5 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/sfx_eikthyr_idle.prefab |
| sfx_eikthyr_spawn | — | Characters/Eikthyr | 4 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/sfx_eikthyr_spawn.prefab |
| sfx_elaking_alerted | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_alerted.prefab |
| sfx_elaking_alerted_old | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_alerted_old.prefab |
| sfx_elaking_attack_claw | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_attack_claw.prefab |
| sfx_elaking_attack_claw_impact | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_attack_claw_impact.prefab |
| sfx_elaking_attack_jump | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_attack_jump.prefab |
| sfx_elaking_attack_jump_impact | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_attack_jump_impact.prefab |
| sfx_elaking_death | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_death.prefab |
| sfx_elaking_death_old | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_death_old.prefab |
| sfx_elaking_hit | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_hit.prefab |
| sfx_elaking_hit_old | — | Characters/Elaking | 3 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_hit_old.prefab |
| sfx_elaking_idle | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_idle.prefab |
| sfx_elaking_idle_old | — | Characters/Elaking | 5 components; active: yes | c4210710 / Assets/Characters/Elaking/fx/sfx_elaking_idle_old.prefab |
| sfx_elaking_spawner_idle_loop | — | Characters/Elaking | 4 components; active: yes | c4210710 / Assets/Characters/Elaking/sfx/sfx_elaking_spawner_idle_loop.prefab |
| sfx_equip | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_equip.prefab |
| sfx_equip_start | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_equip_start.prefab |
| sfx_equip_vibration_only | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_equip_vibration_only.prefab |
| sfx_EternalPyre_Drone_Loop | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/EternalPyre/sfx/sfx_EternalPyre_Drone_Loop.prefab |
| sfx_EternalPyre_Embers_Loop | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/EternalPyre/sfx/sfx_EternalPyre_Embers_Loop.prefab |
| sfx_EternalPyre_Fire_Loop | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/EternalPyre/sfx/sfx_EternalPyre_Fire_Loop.prefab |
| sfx_fader_bell | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/sfx/sfx_fader_bell.prefab |
| sfx_fader_bite_pre | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Bite/sfx_fader_bite_pre.prefab |
| sfx_fader_bite_snarl | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Bite/sfx_fader_bite_snarl.prefab |
| sfx_fader_charredsummon_impact | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/CharredSummon/sfx_fader_charredsummon_impact.prefab |
| sfx_fader_charredsummon_projectile | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/CharredSummon/sfx_fader_charredsummon_projectile.prefab |
| sfx_fader_charredsummon_roar | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/CharredSummon/sfx_fader_charredsummon_roar.prefab |
| sfx_fader_claw_pre | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/ClawSwipe/sfx_fader_claw_pre.prefab |
| sfx_fader_claw_swipe | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/ClawSwipe/sfx_fader_claw_swipe.prefab |
| sfx_fader_death_explosion | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Death/sfx_fader_death_explosion.prefab |
| sfx_fader_death_start | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Death/sfx_fader_death_start.prefab |
| sfx_fader_firebreath_in | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/FireBreath/sfx_fader_firebreath_in.prefab |
| sfx_fader_firebreath_out | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/FireBreath/sfx_fader_firebreath_out.prefab |
| sfx_fader_firewall_fireburst | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/FireWall/sfx_fader_firewall_fireburst.prefab |
| sfx_fader_firewall_start | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/FireWall/sfx_fader_firewall_start.prefab |
| sfx_fader_fissure | — | Characters/Fader | 6 components; active: yes | c4210710 / Assets/Characters/Fader/fx/sfx_fader_fissure.prefab |
| sfx_fader_fissure_fire | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Fissure/sfx_fader_fissure_fire.prefab |
| sfx_fader_fissure_footimpact | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Fissure/sfx_fader_fissure_footimpact.prefab |
| sfx_fader_fissure_footslide | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Fissure/sfx_fader_fissure_footslide.prefab |
| sfx_fader_fissure_pillar | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Fissure/sfx_fader_fissure_pillar.prefab |
| sfx_fader_footstep | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Footsteps/sfx_fader_footstep.prefab |
| sfx_fader_idle | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Idle/sfx_fader_idle.prefab |
| sfx_fader_meteor_impact | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/MeteorCall/sfx_fader_meteor_impact.prefab |
| sfx_fader_meteor_start | — | Characters/Fader | 4 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/MeteorCall/sfx_fader_meteor_start.prefab |
| sfx_fader_spawn_meteor_ambience | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Spawn/sfx_fader_spawn_meteor_ambience.prefab |
| sfx_fader_spawn_meteor_arrival | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Spawn/sfx_fader_spawn_meteor_arrival.prefab |
| sfx_fader_spawn_meteor_impact | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/Spawn/sfx_fader_spawn_meteor_impact.prefab |
| sfx_fader_spin | — | Characters/Fader | 5 components; active: yes | c4210710 / Assets/Characters/Fader/sfx/SpinAttack/sfx_fader_spin.prefab |
| sfx_fader_taunt | — | Characters/Fader | 6 components; active: yes | c4210710 / Assets/Characters/Fader/fx/sfx_fader_taunt.prefab |
| sfx_fallenvalkyrie_alert | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Alert/sfx_fallenvalkyrie_alert.prefab |
| sfx_fallenvalkyrie_attack | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/fx/sfx_fallenvalkyrie_attack.prefab |
| sfx_fallenvalkyrie_attack_claw | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Claw/sfx_fallenvalkyrie_attack_claw.prefab |
| sfx_fallenvalkyrie_attack_spin_charge | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/WingSpin/sfx_fallenvalkyrie_attack_spin_charge.prefab |
| sfx_fallenvalkyrie_attack_spin_release | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/WingSpin/sfx_fallenvalkyrie_attack_spin_release.prefab |
| sfx_fallenvalkyrie_attack_spit_charge | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Spit/sfx_fallenvalkyrie_attack_spit_charge.prefab |
| sfx_fallenvalkyrie_attack_spit_projectile | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Spit/sfx_fallenvalkyrie_attack_spit_projectile.prefab |
| sfx_fallenvalkyrie_attack_spit_projectile_impact | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Spit/sfx_fallenvalkyrie_attack_spit_projectile_impact.prefab |
| sfx_fallenvalkyrie_attack_spit_vocal | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Spit/sfx_fallenvalkyrie_attack_spit_vocal.prefab |
| sfx_fallenvalkyrie_death | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Death/sfx_fallenvalkyrie_death.prefab |
| sfx_fallenvalkyrie_idle | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/Idle/sfx_fallenvalkyrie_idle.prefab |
| sfx_fallenvalkyrie_screech | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/fx/sfx_fallenvalkyrie_screech.prefab |
| sfx_fallenvalkyrie_taunt | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/fx/sfx_fallenvalkyrie_taunt.prefab |
| sfx_fallenvalkyrie_wingflap | — | Characters/FallenValkyrie | 5 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/sfx/WingFlap/sfx_fallenvalkyrie_wingflap.prefab |
| sfx_fallenwarrior_attack | — | Characters/FallenWarrior | 5 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/Audio/Attack/sfx_fallenwarrior_attack.prefab |
| sfx_fallenwarrior_attack_impact | — | Characters/FallenWarrior | 5 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/Audio/Attack/sfx_fallenwarrior_attack_impact.prefab |
| sfx_fallenwarrior_death | — | Characters/FallenWarrior | 5 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/Audio/Death/sfx_fallenwarrior_death.prefab |
| sfx_fallenwarrior_hurt | — | Characters/FallenWarrior | 5 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/Audio/Hurt/sfx_fallenwarrior_hurt.prefab |
| sfx_fallenwarrior_idle | — | Characters/FallenWarrior | 5 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/Audio/Idle/sfx_fallenwarrior_idle.prefab |
| sfx_feast_destroyed | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Feasts/Fx/sfx_feast_destroyed.prefab |
| sfx_fenring_alerted | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_alerted.prefab |
| sfx_fenring_claw_hit | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_claw_hit.prefab |
| sfx_fenring_claw_start | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_claw_start.prefab |
| sfx_fenring_claw_trailstart | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_claw_trailstart.prefab |
| sfx_fenring_death | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_death.prefab |
| sfx_fenring_fireclaw | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_fireclaw.prefab |
| sfx_fenring_howl | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_howl.prefab |
| sfx_fenring_idle | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_idle.prefab |
| sfx_fenring_jump_start | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_jump_start.prefab |
| sfx_fenring_jump_trailstart | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_jump_trailstart.prefab |
| sfx_fenring_jump_trigger | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/sfx_fenring_jump_trigger.prefab |
| sfx_fermenter_add | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/fermenter/fx/sfx_fermenter_add.prefab |
| sfx_fermenter_tap | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/fermenter/fx/sfx_fermenter_tap.prefab |
| sfx_fire_loop | — | Audio/Ambients | 4 components; active: yes | c4210710 / Assets/Audio/Ambients/Ashlands/sfx_fire_loop.prefab |
| sfx_FireAddFuel | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/firepit/sfx_FireAddFuel.prefab |
| sfx_firestaff_launch | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/sfx_firestaff_launch.prefab |
| sfx_firework_explode | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/sfx_firework_explode.prefab |
| sfx_fishingrod_linebreak | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/tools/_res/FishingRod/fx/sfx_fishingrod_linebreak.prefab |
| sfx_fishingrod_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/tools/_res/FishingRod/fx/sfx_fishingrod_swing.prefab |
| sfx_fist_metal_blocked | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_fist_metal_blocked.prefab |
| sfx_flametalgate_door_close | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_flametalgate_door_close.prefab |
| sfx_flametalgate_door_open | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_flametalgate_door_open.prefab |
| sfx_footstep | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep.prefab |
| sfx_footstep_climb | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep_climb.prefab |
| sfx_footstep_ice_run | — | Characters/Player | 3 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep_ice_run.prefab |
| sfx_footstep_ice_walk | — | Characters/Player | 3 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep_ice_walk.prefab |
| sfx_footstep_run | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep_run.prefab |
| sfx_footstep_sneak | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_footstep_sneak.prefab |
| sfx_footstep_snow_run | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep_snow_run.prefab |
| sfx_footstep_snow_walk | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep_snow_walk.prefab |
| sfx_footstep_swim | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_footstep_swim.prefab |
| sfx_footstep_water | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_footstep_water.prefab |
| sfx_forgeofpotential_fail | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/ForgeOfPotential/sfx_forgeofpotential_fail.prefab |
| sfx_forgeofpotential_success | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/ForgeOfPotential/sfx_forgeofpotential_success.prefab |
| sfx_Frost_Start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Frost_Start.prefab |
| sfx_frostcore_idle_loop | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/_res/FrostCore/sfx/sfx_frostcore_idle_loop.prefab |
| sfx_frostfoundry_activate | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostFoundry/sfx/sfx_frostfoundry_activate.prefab |
| sfx_frostfoundry_deactivate | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostFoundry/sfx/sfx_frostfoundry_deactivate.prefab |
| sfx_frostfoundry_loop | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostFoundry/sfx/sfx_frostfoundry_loop.prefab |
| sfx_frostkiln_loop | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostKiln/sfx/sfx_frostkiln_loop.prefab |
| sfx_frozenking_attackmelee_double_chain | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Double/sfx_frozenking_attackmelee_double_chain.prefab |
| sfx_frozenking_attackmelee_double_impact | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Double/sfx_frozenking_attackmelee_double_impact.prefab |
| sfx_frozenking_attackmelee_double_whoosh_follow | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Double/sfx_frozenking_attackmelee_double_whoosh_follow.prefab |
| sfx_frozenking_attackmelee_double_whoosh_lead | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Double/sfx_frozenking_attackmelee_double_whoosh_lead.prefab |
| sfx_frozenking_attackmelee_single_chainback | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Single/sfx_frozenking_attackmelee_single_chainback.prefab |
| sfx_frozenking_attackmelee_single_charge | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Single/sfx_frozenking_attackmelee_single_charge.prefab |
| sfx_frozenking_attackmelee_single_impact | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Single/sfx_frozenking_attackmelee_single_impact.prefab |
| sfx_frozenking_attackmelee_single_whsh | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/AttackMelee/Single/sfx_frozenking_attackmelee_single_whsh.prefab |
| sfx_frozenking_chainflurry_chain | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Chain Flurry/sfx_frozenking_chainflurry_chain.prefab |
| sfx_frozenking_chainflurry_coldvortex | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Chain Flurry/sfx_frozenking_chainflurry_coldvortex.prefab |
| sfx_frozenking_chainflurry_fly | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Chain Flurry/sfx_frozenking_chainflurry_fly.prefab |
| sfx_frozenking_chainflurry_start | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Chain Flurry/sfx_frozenking_chainflurry_start.prefab |
| sfx_frozenking_charge_chainback | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Charge/sfx_frozenking_charge_chainback.prefab |
| sfx_frozenking_charge_doublehookup | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Charge/sfx_frozenking_charge_doublehookup.prefab |
| sfx_frozenking_charge_start | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Charge/sfx_frozenking_charge_start.prefab |
| sfx_frozenking_charge_whoosh | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Charge/sfx_frozenking_charge_whoosh.prefab |
| sfx_frozenking_death_crystal_break | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Death p1/sfx_frozenking_death_crystal_break.prefab |
| sfx_frozenking_death_crystal_loop | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Death p1/sfx_frozenking_death_crystal_loop.prefab |
| sfx_frozenking_death_crystal_sequence | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Death p1/sfx_frozenking_death_crystal_sequence.prefab |
| sfx_frozenking_death_p3_sequence | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/sfx_frozenking_death_p3_sequence.prefab |
| sfx_frozenking_doubleslam_explosion | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpikeRain/sfx_frozenking_doubleslam_explosion.prefab |
| sfx_frozenking_fly_loop | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/sfx_frozenking_fly_loop.prefab |
| sfx_frozenking_frozenspark_whip | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/FrozenSparks/sfx_frozenking_frozenspark_whip.prefab |
| sfx_frozenking_frozentwirl_charge | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/FrozenTwirl/sfx_frozenking_frozentwirl_charge.prefab |
| sfx_frozenking_frozentwirl_coldvortex | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/FrozenTwirl/sfx_frozenking_frozentwirl_coldvortex.prefab |
| sfx_frozenking_frozentwirl_tornado | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/FrozenTwirl/sfx_frozenking_frozentwirl_tornado.prefab |
| sfx_frozenking_frozentwirl_wind | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/FrozenTwirl/sfx_frozenking_frozentwirl_wind.prefab |
| sfx_frozenking_idle_breath | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Voice/sfx_frozenking_idle_breath.prefab |
| sfx_frozenking_idle_chained | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Voice/sfx_frozenking_idle_chained.prefab |
| sfx_frozenking_idle_chained_loop | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/sfx_frozenking_idle_chained_loop.prefab |
| sfx_frozenking_idle_phase3_loop | — | Characters/FrozenKing | 4 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/sfx_frozenking_idle_phase3_loop.prefab |
| sfx_frozenking_intro_chainpressure | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Intro/sfx_frozenking_intro_chainpressure.prefab |
| sfx_frozenking_intro_icepillar_left_break | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Intro/sfx_frozenking_intro_icepillar_left_break.prefab |
| sfx_frozenking_intro_icepillar_right_break | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Intro/sfx_frozenking_intro_icepillar_right_break.prefab |
| sfx_frozenking_intro_rise | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Intro/sfx_frozenking_intro_rise.prefab |
| sfx_frozenking_punchaoe_chain_end | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_chain_end.prefab |
| sfx_frozenking_punchaoe_chain_start | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_chain_start.prefab |
| sfx_frozenking_punchaoe_debris | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_debris.prefab |
| sfx_frozenking_punchaoe_punch_first | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_punch_first.prefab |
| sfx_frozenking_punchaoe_punch_second | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_punch_second.prefab |
| sfx_frozenking_punchaoe_punch_third | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_punch_third.prefab |
| sfx_frozenking_punchaoe_whoosh_punch | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_whoosh_punch.prefab |
| sfx_frozenking_punchaoe_whoosh_start | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/PunchAOE/sfx_frozenking_punchaoe_whoosh_start.prefab |
| sfx_frozenking_spikerain_chain | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpikeRain/sfx_frozenking_spikerain_chain.prefab |
| sfx_frozenking_spikerain_explosion | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpikeRain/sfx_frozenking_spikerain_explosion.prefab |
| sfx_frozenking_spikerain_flyby | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpikeRain/sfx_frozenking_spikerain_flyby.prefab |
| sfx_frozenking_spikerain_iceceiling | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpikeRain/sfx_frozenking_spikerain_iceceiling.prefab |
| sfx_frozenking_spikerain_shards | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpikeRain/sfx_frozenking_spikerain_shards.prefab |
| sfx_frozenking_spirit_death | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpiritSummon/sfx_frozenking_spirit_death.prefab |
| sfx_frozenking_spirit_summon | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/SpiritSummon/sfx_frozenking_spirit_summon.prefab |
| sfx_frozenking_tendril_attack | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Tendril/sfx_frozenking_tendril_attack.prefab |
| sfx_frozenking_tendril_death | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Tendril/sfx_frozenking_tendril_death.prefab |
| sfx_frozenking_tendril_grow | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Tendril/sfx_frozenking_tendril_grow.prefab |
| sfx_frozenking_tendril_summon | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Tendril/sfx_frozenking_tendril_summon.prefab |
| sfx_frozenking_turn | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Movement/sfx_frozenking_turn.prefab |
| sfx_frozenking_voice_attack | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Voice/sfx_frozenking_voice_attack.prefab |
| sfx_frozenking_voice_scream | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/sfx/Voice/sfx_frozenking_voice_scream.prefab |
| sfx_gameltroll_death | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Death/sfx_gameltroll_death.prefab |
| sfx_gameltroll_footstep | — | Characters/FrostTroll | 4 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Footsteps/sfx_gameltroll_footstep.prefab |
| sfx_gameltroll_hurt | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Hurt/sfx_gameltroll_hurt.prefab |
| sfx_gameltroll_idle | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Idle/sfx_gameltroll_idle.prefab |
| sfx_gameltroll_melee_attack | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Melee/sfx_gameltroll_melee_attack.prefab |
| sfx_gameltroll_melee_attack_Impact | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Melee/sfx_gameltroll_melee_attack_Impact.prefab |
| sfx_gameltroll_stomp_attack | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Melee/sfx_gameltroll_stomp_attack.prefab |
| sfx_gameltroll_stomp_attack_impact | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Melee/sfx_gameltroll_stomp_attack_impact.prefab |
| sfx_gameltroll_stoneturn_death | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Death/sfx_gameltroll_stoneturn_death.prefab |
| sfx_gameltroll_throw_attack | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Ranged/sfx_gameltroll_throw_attack.prefab |
| sfx_gameltroll_throw_attack_impact | — | Characters/FrostTroll | 5 components; active: yes | c4210710 / Assets/Characters/FrostTroll/sfx/Ranged/sfx_gameltroll_throw_attack_impact.prefab |
| sfx_gdking_alert | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_alert.prefab |
| sfx_gdking_death | — | Characters/Greydwarf_king | 6 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_death.prefab |
| sfx_gdking_footstep | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_footstep.prefab |
| sfx_gdking_idle | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_idle.prefab |
| sfx_gdking_projectile_hit | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_projectile_hit.prefab |
| sfx_gdking_punch | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_punch.prefab |
| sfx_gdking_rock_destroyed | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_rock_destroyed.prefab |
| sfx_gdking_scream | — | Characters/Greydwarf_king | 6 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_scream.prefab |
| sfx_gdking_shoot_start | — | Characters/Greydwarf_king | 6 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_shoot_start.prefab |
| sfx_gdking_shoot_trigger | — | Characters/Greydwarf_king | 6 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_shoot_trigger.prefab |
| sfx_gdking_spawn | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_spawn.prefab |
| sfx_gdking_stomp | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_gdking_stomp.prefab |
| sfx_ghost_alert | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/sfx_ghost_alert.prefab |
| sfx_ghost_attack | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/sfx_ghost_attack.prefab |
| sfx_ghost_attack_hit | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/sfx_ghost_attack_hit.prefab |
| sfx_ghost_death | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/sfx_ghost_death.prefab |
| sfx_ghost_hurt | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/sfx_ghost_hurt.prefab |
| sfx_ghost_idle | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/sfx_ghost_idle.prefab |
| sfx_ghosts_death | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/sfx/Death/sfx_ghosts_death.prefab |
| sfx_ghosts_footstep | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/sfx/Footsteps/sfx_ghosts_footstep.prefab |
| sfx_ghosts_hurt | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/sfx/Hurt/sfx_ghosts_hurt.prefab |
| sfx_ghosts_idle | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/sfx/Idle/sfx_ghosts_idle.prefab |
| sfx_ghosts_melee_attack | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/sfx/Melee/sfx_ghosts_melee_attack.prefab |
| sfx_ghosts_melee_attack_impact | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/sfx/Melee/sfx_ghosts_melee_attack_impact.prefab |
| sfx_gjall_alerted | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_alerted.prefab |
| sfx_gjall_attack_shake | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_attack_shake.prefab |
| sfx_gjall_attack_tick_drop | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_attack_tick_drop.prefab |
| sfx_gjall_death | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_death.prefab |
| sfx_gjall_idle_blowout | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_idle_blowout.prefab |
| sfx_gjall_idle_shiver | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_idle_shiver.prefab |
| sfx_gjall_idle_vocals | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_idle_vocals.prefab |
| sfx_gjall_spit | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_spit.prefab |
| sfx_gjall_spit_fx | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_spit_fx.prefab |
| sfx_gjall_spit_impact | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_spit_impact.prefab |
| sfx_gjall_tick_drop | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/sfx/sfx_gjall_tick_drop.prefab |
| sfx_glowworm_idle_loop | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/TheHole/GlowWorm/sfx/sfx_glowworm_idle_loop.prefab |
| sfx_glowworm_pickup | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/TheHole/GlowWorm/sfx/sfx_glowworm_pickup.prefab |
| sfx_goblin_alerted | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/sfx_goblin_alerted.prefab |
| sfx_goblin_death | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/sfx_goblin_death.prefab |
| sfx_goblin_hit | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/sfx_goblin_hit.prefab |
| sfx_goblin_idle | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/sfx_goblin_idle.prefab |
| sfx_goblinbrute_alerted | — | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_alerted.prefab |
| sfx_goblinbrute_clubhit | — | Characters/GoblinBrute | 6 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_clubhit.prefab |
| sfx_goblinbrute_clubswing | — | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_clubswing.prefab |
| sfx_goblinbrute_death | — | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_death.prefab |
| sfx_goblinbrute_hit | — | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_hit.prefab |
| sfx_goblinbrute_idle | — | Characters/GoblinBrute | 4 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_idle.prefab |
| sfx_goblinbrute_shout | — | Characters/GoblinBrute | 4 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_shout.prefab |
| sfx_goblinbrute_taunt | — | Characters/GoblinBrute | 4 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/sfx_goblinbrute_taunt.prefab |
| sfx_goblinking_beam | — | Characters/GoblinKing | 6 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/sfx_goblinking_beam.prefab |
| sfx_goblinking_taunt | — | Characters/GoblinKing | 6 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/sfx_goblinking_taunt.prefab |
| sfx_GoblinShaman_alerted | — | Characters/GoblinShaman | 5 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/sfx_GoblinShaman_alerted.prefab |
| sfx_GoblinShaman_death | — | Characters/GoblinShaman | 5 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/sfx_GoblinShaman_death.prefab |
| sfx_GoblinShaman_fireball_launch | — | Characters/GoblinShaman | 5 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/sfx_GoblinShaman_fireball_launch.prefab |
| sfx_GoblinShaman_hurt | — | Characters/GoblinShaman | 5 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/sfx_GoblinShaman_hurt.prefab |
| sfx_GoblinShaman_idle | — | Characters/GoblinShaman | 5 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/fx/sfx_GoblinShaman_idle.prefab |
| sfx_grapplinghook_detach | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/grapplinghook/sfx_grapplinghook_detach.prefab |
| sfx_grapplinghook_fire | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/grapplinghook/sfx_grapplinghook_fire.prefab |
| sfx_grapplinghook_hit | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/grapplinghook/sfx_grapplinghook_hit.prefab |
| sfx_grapplinghook_pull | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/grapplinghook/sfx_grapplinghook_pull.prefab |
| sfx_grapplinghook_reload | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/grapplinghook/sfx_grapplinghook_reload.prefab |
| sfx_grapplinghook_repel | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/grapplinghook/sfx_grapplinghook_repel.prefab |
| sfx_greydwarf_alerted | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_alerted.prefab |
| sfx_greydwarf_attack | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_attack.prefab |
| sfx_greydwarf_attack_hit | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_attack_hit.prefab |
| sfx_greydwarf_death | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_death.prefab |
| sfx_greydwarf_deepnorth_death | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_deepnorth_death.prefab |
| sfx_greydwarf_deepnorth_verse_attack | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_deepnorth_verse_attack.prefab |
| sfx_greydwarf_elite_alerted | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_elite_alerted.prefab |
| sfx_greydwarf_elite_attack | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_elite_attack.prefab |
| sfx_greydwarf_elite_death | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_elite_death.prefab |
| sfx_greydwarf_elite_idle | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_elite_idle.prefab |
| sfx_greydwarf_hit | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_hit.prefab |
| sfx_greydwarf_idle | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_idle.prefab |
| sfx_greydwarf_shaman_attack | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_shaman_attack.prefab |
| sfx_greydwarf_shaman_heal | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_shaman_heal.prefab |
| sfx_greydwarf_stone_hit | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/sfx_greydwarf_stone_hit.prefab |
| sfx_greydwarf_throw | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greydwarf_throw.prefab |
| sfx_greydwarfnest_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GreyDwarfSpawner/fx/sfx_greydwarfnest_destroyed.prefab |
| sfx_greydwarfnest_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GreyDwarfSpawner/fx/sfx_greydwarfnest_hit.prefab |
| sfx_greyling_alerted | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greyling_alerted.prefab |
| sfx_greyling_attack | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greyling_attack.prefab |
| sfx_greyling_death | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greyling_death.prefab |
| sfx_greyling_hit | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greyling_hit.prefab |
| sfx_greyling_idle | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/audio/sfx_greyling_idle.prefab |
| sfx_GuckSackDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GuckSack/fx/sfx_GuckSackDestroyed.prefab |
| sfx_GuckSackHit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GuckSack/fx/sfx_GuckSackHit.prefab |
| sfx_gui_biomefound | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/inventory_gui/sfx_gui_biomefound.prefab |
| sfx_gui_button | — | Audio/sfx | 4 components; active: yes | 8d5dbad8 / Assets/Audio/sfx/inventory_gui/sfx_gui_button.prefab |
| sfx_gui_button_vibrateonly_dull | — | Audio/sfx | 4 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_button_vibrateonly_dull.prefab |
| sfx_gui_button_vibrateonly_heavy | — | Audio/sfx | 4 components; active: yes | b8689a71 / Assets/Audio/sfx/inventory_gui/sfx_gui_button_vibrateonly_heavy.prefab |
| sfx_gui_button_vibrateonly_light | — | Audio/sfx | 4 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_button_vibrateonly_light.prefab |
| sfx_gui_button_vibrateonly_medium | — | Audio/sfx | 4 components; active: yes | 8d5dbad8 / Assets/Audio/sfx/inventory_gui/sfx_gui_button_vibrateonly_medium.prefab |
| sfx_gui_button_vibrateonly_ultralight_tap | — | Audio/sfx | 4 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_button_vibrateonly_ultralight_tap.prefab |
| sfx_gui_craftitem | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem.prefab |
| sfx_gui_craftitem_cauldron | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem_cauldron.prefab |
| sfx_gui_craftitem_cauldron_end | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem_cauldron_end.prefab |
| sfx_gui_craftitem_end | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem_end.prefab |
| sfx_gui_craftitem_forge | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem_forge.prefab |
| sfx_gui_craftitem_forge_end | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem_forge_end.prefab |
| sfx_gui_craftitem_workbench | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem_workbench.prefab |
| sfx_gui_craftitem_workbench_end | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_craftitem_workbench_end.prefab |
| sfx_gui_inventory_close | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/inventory_gui/sfx_gui_inventory_close.prefab |
| sfx_gui_inventory_open | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/inventory_gui/sfx_gui_inventory_open.prefab |
| sfx_gui_inventory_select | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/inventory_gui/sfx_gui_inventory_select.prefab |
| sfx_gui_moveitem | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/inventory_gui/sfx_gui_moveitem.prefab |
| sfx_gui_moveitem_vibrateonly | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/inventory_gui/sfx_gui_moveitem_vibrateonly.prefab |
| sfx_gui_repairitem_forge | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_repairitem_forge.prefab |
| sfx_gui_repairitem_workbench | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_repairitem_workbench.prefab |
| sfx_gui_select | — | Audio/sfx | 4 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_gui_select.prefab |
| sfx_gui_sell | — | Audio/sfx | 4 components; active: yes | d59cfac / Assets/Audio/sfx/inventory_gui/sfx_gui_sell.prefab |
| sfx_haldor_greet | — | Characters/TraderHaldor | 5 components; active: yes | c4210710 / Assets/Characters/TraderHaldor/fx/sfx_haldor_greet.prefab |
| sfx_haldor_laugh | — | Characters/TraderHaldor | 5 components; active: yes | c4210710 / Assets/Characters/TraderHaldor/fx/sfx_haldor_laugh.prefab |
| sfx_haldor_yea | — | Characters/TraderHaldor | 5 components; active: yes | c4210710 / Assets/Characters/TraderHaldor/fx/sfx_haldor_yea.prefab |
| sfx_hare_alerted | — | Characters/Hare | 5 components; active: yes | c4210710 / Assets/Characters/Hare/sfx/sfx_hare_alerted.prefab |
| sfx_hare_death_vocal | — | Characters/Hare | 5 components; active: yes | c4210710 / Assets/Characters/Hare/sfx/sfx_hare_death_vocal.prefab |
| sfx_hare_footstep_run | — | Characters/Hare | 4 components; active: yes | c4210710 / Assets/Characters/Hare/sfx/sfx_hare_footstep_run.prefab |
| sfx_hare_idle | — | Characters/Hare | 5 components; active: yes | c4210710 / Assets/Characters/Hare/sfx/sfx_hare_idle.prefab |
| sfx_hare_idle_eating | — | Characters/Hare | 5 components; active: yes | c4210710 / Assets/Characters/Hare/sfx/sfx_hare_idle_eating.prefab |
| sfx_hatchling_alerted | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatchling_alerted.prefab |
| sfx_hatchling_coldball_explode | — | Characters/Hatchling | 6 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatchling_coldball_explode.prefab |
| sfx_hatchling_coldball_launch | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatchling_coldball_launch.prefab |
| sfx_hatchling_coldball_start | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatchling_coldball_start.prefab |
| sfx_hatchling_death | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatchling_death.prefab |
| sfx_hatchling_flap | — | Characters/Hatchling | 4 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatchling_flap.prefab |
| sfx_hatchling_idle | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatchling_idle.prefab |
| sfx_hatcling_hurt | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/sfx_hatcling_hurt.prefab |
| sfx_hildir_bye | — | Characters/Hildir | 4 components; active: yes | c4210710 / Assets/Characters/Hildir/fx/sfx_hildir_bye.prefab |
| sfx_hildir_hello | — | Characters/Hildir | 4 components; active: yes | c4210710 / Assets/Characters/Hildir/fx/sfx_hildir_hello.prefab |
| sfx_hildir_talk | — | Characters/Hildir | 4 components; active: yes | c4210710 / Assets/Characters/Hildir/fx/sfx_hildir_talk.prefab |
| sfx_hildir_trade | — | Characters/Hildir | 4 components; active: yes | c4210710 / Assets/Characters/Hildir/fx/sfx_hildir_trade.prefab |
| sfx_hit | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_hit.prefab |
| sfx_hit_vibration_only | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_hit_vibration_only.prefab |
| sfx_HiveQueen_acitspit | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_acitspit.prefab |
| sfx_HiveQueen_alerted | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_alerted.prefab |
| sfx_HiveQueen_backslam | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_backslam.prefab |
| sfx_HiveQueen_bite | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_bite.prefab |
| sfx_HiveQueen_burrow | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_burrow.prefab |
| sfx_HiveQueen_callout | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_callout.prefab |
| sfx_HiveQueen_doubleslash | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_doubleslash.prefab |
| sfx_HiveQueen_idle | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_idle.prefab |
| sfx_HiveQueen_move | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_move.prefab |
| sfx_HiveQueen_pierce | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_pierce.prefab |
| sfx_HiveQueen_rush | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_rush.prefab |
| sfx_HiveQueen_slash | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_slash.prefab |
| sfx_HiveQueen_slashcombo | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_slashcombo.prefab |
| sfx_HiveQueen_spitimpact | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_spitimpact.prefab |
| sfx_HiveQueen_turn | — | Characters/SeekerQueen | 5 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/sfx/sfx_HiveQueen_turn.prefab |
| sfx_hugin_kaw | — | Characters/Raven | 4 components; active: yes | c4210710 / Assets/Characters/Raven/fx/sfx_hugin_kaw.prefab |
| sfx_ice_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/fx/sfx_ice_destroyed.prefab |
| sfx_ice_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/fx/sfx_ice_hit.prefab |
| sfx_icestaff_start | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/sfx_icestaff_start.prefab |
| sfx_imp_alerted | — | Characters/Surtling | 5 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/sfx_imp_alerted.prefab |
| sfx_imp_death | — | Characters/Surtling | 6 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/sfx_imp_death.prefab |
| sfx_imp_fireball_explode | — | Characters/Surtling | 6 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/sfx_imp_fireball_explode.prefab |
| sfx_imp_fireball_launch | — | Characters/Surtling | 5 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/sfx_imp_fireball_launch.prefab |
| sfx_imp_hit | — | Characters/Surtling | 5 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/sfx_imp_hit.prefab |
| sfx_jotunwarrior_attack1 | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Audio/Melee/sfx_jotunwarrior_attack1.prefab |
| sfx_jotunwarrior_attack2 | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Audio/Melee/sfx_jotunwarrior_attack2.prefab |
| sfx_jotunwarrior_death | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Audio/Death/sfx_jotunwarrior_death.prefab |
| sfx_jotunwarrior_hurt | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Audio/Hurt/sfx_jotunwarrior_hurt.prefab |
| sfx_jotunwarrior_Idle | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Audio/Idle/sfx_jotunwarrior_Idle.prefab |
| sfx_jotunwarrior_impact_flesh | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Audio/Melee/sfx_jotunwarrior_impact_flesh.prefab |
| sfx_jotunwarrior_impact_ground | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Audio/Melee/sfx_jotunwarrior_impact_ground.prefab |
| sfx_jotunwitch_attackball | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Melee/sfx_jotunwitch_attackball.prefab |
| sfx_jotunwitch_attackball_impact | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Melee/sfx_jotunwitch_attackball_impact.prefab |
| sfx_jotunwitch_attackblast | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Melee/sfx_jotunwitch_attackblast.prefab |
| sfx_jotunwitch_attackbuildup | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Melee/sfx_jotunwitch_attackbuildup.prefab |
| sfx_jotunwitch_death | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Death/sfx_jotunwitch_death.prefab |
| sfx_jotunwitch_dodge | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Dodge/sfx_jotunwitch_dodge.prefab |
| sfx_jotunwitch_flight | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Dodge/sfx_jotunwitch_flight.prefab |
| sfx_jotunwitch_hurt | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Hurt/sfx_jotunwitch_hurt.prefab |
| sfx_jotunwitch_Idle | — | Characters/Jotnar | 5 components; active: yes | c4210710 / Assets/Characters/Jotnar/fx/Jotun Witch Audio/Idle/sfx_jotunwitch_Idle.prefab |
| sfx_jump | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_jump.prefab |
| sfx_jump_vibration_only | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_jump_vibration_only.prefab |
| sfx_kiln_addore | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/charcoalkiln/fx/sfx_kiln_addore.prefab |
| sfx_kiln_produce | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/charcoalkiln/fx/sfx_kiln_produce.prefab |
| sfx_knife_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sword/sfx_knife_swing.prefab |
| sfx_kromsword_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Krom/sfx/sfx_kromsword_swing.prefab |
| sfx_kvastur_death | — | Characters/Surtling | 6 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/sfx_kvastur_death.prefab |
| sfx_land | — | Characters/Player | 6 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_land.prefab |
| sfx_land_water | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/audio/old/sfx_land_water.prefab |
| sfx_leech_alerted | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/sfx_leech_alerted.prefab |
| sfx_leech_attack | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/sfx_leech_attack.prefab |
| sfx_leech_attack_hit | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/sfx_leech_attack_hit.prefab |
| sfx_leech_death | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/sfx_leech_death.prefab |
| sfx_leech_hit | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/sfx_leech_hit.prefab |
| sfx_leech_idle | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/sfx_leech_idle.prefab |
| sfx_levelup | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_levelup.prefab |
| sfx_leviathanlava_sink | — | Characters/Leviathan | 4 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/sfx/Leviathan Lava/sfx_leviathanlava_sink.prefab |
| sfx_leviathanlava_taunt | — | Characters/Leviathan | 4 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/sfx/Leviathan Lava/sfx_leviathanlava_taunt.prefab |
| sfx_lootspawn | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/fx/sfx_lootspawn.prefab |
| sfx_lox_alerted | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/sfx_lox_alerted.prefab |
| sfx_lox_attack_bite | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/sfx_lox_attack_bite.prefab |
| sfx_lox_attack_stomp | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/sfx_lox_attack_stomp.prefab |
| sfx_lox_breath | — | Characters/Lox | 4 components; active: yes | c4210710 / Assets/Characters/Lox/fx/sfx_lox_breath.prefab |
| sfx_lox_chew1 | — | Characters/Lox | 4 components; active: yes | c32ede71 / Assets/Characters/Lox/fx/sfx_lox_chew1.prefab |
| sfx_lox_chew2 | — | Characters/Lox | 4 components; active: yes | c32ede71 / Assets/Characters/Lox/fx/sfx_lox_chew2.prefab |
| sfx_lox_shout | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/sfx_lox_shout.prefab |
| sfx_loxcalf_alerted | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/sfx_loxcalf_alerted.prefab |
| sfx_magma_loop | — | Audio/Ambients | 4 components; active: yes | 61c598bb / Assets/Audio/Ambients/Ashlands/sfx_magma_loop.prefab |
| sfx_malicious_ice_break | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_malicious_ice_break.prefab |
| sfx_malicious_ice_loop | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_malicious_ice_loop.prefab |
| sfx_MeadBurp | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/mead/fx/sfx_MeadBurp.prefab |
| sfx_metal_blocked | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_metal_blocked.prefab |
| sfx_metal_blocked_overlay | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_metal_blocked_overlay.prefab |
| sfx_metal_shield_blocked | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_metal_shield_blocked.prefab |
| sfx_metal_shield_blocked_overlay | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_metal_shield_blocked_overlay.prefab |
| sfx_metalbars_break | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_metalbars_break.prefab |
| sfx_metalbars_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_metalbars_hit.prefab |
| sfx_metaldoor_sliding_open | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/Sliding_door/sfx_metaldoor_sliding_open.prefab |
| sfx_metalgate_close | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_metalgate_close.prefab |
| sfx_metalgate_open | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/door/fx/sfx_metalgate_open.prefab |
| sfx_mill_add | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/windmill/fx/sfx_mill_add.prefab |
| sfx_mill_produce | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/windmill/fx/sfx_mill_produce.prefab |
| sfx_mistlands_thunder | — | Audio/sfx | 5 components; active: yes | d59cfac / Assets/Audio/sfx/thunder/sfx_mistlands_thunder.prefab |
| sfx_moleman_alert | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Alert/sfx_moleman_alert.prefab |
| sfx_moleman_attack | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Melee Attack/sfx_moleman_attack.prefab |
| sfx_moleman_death | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Death/sfx_moleman_death.prefab |
| sfx_moleman_footsteps | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Footsteps/sfx_moleman_footsteps.prefab |
| sfx_moleman_hurt | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Hurt/sfx_moleman_hurt.prefab |
| sfx_moleman_idle | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Idle/sfx_moleman_idle.prefab |
| sfx_moleman_spawn | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Spawn/sfx_moleman_spawn.prefab |
| sfx_moleman_stonedust | — | Characters/ElakingMole | 5 components; active: yes | c4210710 / Assets/Characters/ElakingMole/sfx/Stonedust/sfx_moleman_stonedust.prefab |
| sfx_moose_alert | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Alert/sfx_moose_alert.prefab |
| sfx_moose_attack_melee | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Attack/sfx_moose_attack_melee.prefab |
| sfx_moose_attack_melee_hit | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Attack/sfx_moose_attack_melee_hit.prefab |
| sfx_moose_attack_melee_movement | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Attack/sfx_moose_attack_melee_movement.prefab |
| sfx_moose_attack_melee_whoosh | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Attack/sfx_moose_attack_melee_whoosh.prefab |
| sfx_moose_calf_verse | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Moose Calf/sfx_moose_calf_verse.prefab |
| sfx_moose_death | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Death/sfx_moose_death.prefab |
| sfx_moose_death_explode | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Death/sfx_moose_death_explode.prefab |
| sfx_moose_hurt | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Hurt/sfx_moose_hurt.prefab |
| sfx_moose_idle | — | Characters/moose | 5 components; active: yes | c4210710 / Assets/Characters/moose/fx/Audio/Idle/sfx_moose_idle.prefab |
| sfx_morgen_alert | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Alert/sfx_morgen_alert.prefab |
| sfx_morgen_attack | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Attack/sfx_morgen_attack.prefab |
| sfx_morgen_death | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Death/sfx_morgen_death.prefab |
| sfx_morgen_footstep | — | Characters/Morgen | 4 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Footsteps/sfx_morgen_footstep.prefab |
| sfx_morgen_idle | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Idle/sfx_morgen_idle.prefab |
| sfx_morgen_roll_jump | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Roll/sfx_morgen_roll_jump.prefab |
| sfx_morgen_roll_land | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Roll/sfx_morgen_roll_land.prefab |
| sfx_morgen_slap | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Slap/sfx_morgen_slap.prefab |
| sfx_morgen_slap_delayed | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Slap/sfx_morgen_slap_delayed.prefab |
| sfx_morgen_spawn | — | Characters/Morgen | 5 components; active: yes | c4210710 / Assets/Characters/Morgen/sfx/Spawn/sfx_morgen_spawn.prefab |
| sfx_morkhalla_gate_open_end | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_morkhalla_gate_open_end.prefab |
| sfx_morkhalla_gate_open_start | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_morkhalla_gate_open_start.prefab |
| sfx_morkhalla_gate_slide | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_morkhalla_gate_slide.prefab |
| sfx_morkhalla_torch_loop | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/sfx/sfx_morkhalla_torch_loop.prefab |
| sfx_MudDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MudPile/fx/sfx_MudDestroyed.prefab |
| sfx_MudHit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MudPile/fx/sfx_MudHit.prefab |
| sfx_neck_alerted | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/sfx_neck_alerted.prefab |
| sfx_neck_attack | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/sfx_neck_attack.prefab |
| sfx_neck_attack_hit | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/sfx_neck_attack_hit.prefab |
| sfx_neck_death | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/sfx_neck_death.prefab |
| sfx_neck_hit | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/sfx_neck_hit.prefab |
| sfx_neck_idle | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/sfx_neck_idle.prefab |
| sfx_obliterator_close | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_obliterator_close.prefab |
| sfx_obliterator_open | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/inventory_gui/sfx_obliterator_open.prefab |
| sfx_offering | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_offering.prefab |
| sfx_oozebomb_explode | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/sfx_oozebomb_explode.prefab |
| sfx_OpenPortal | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/firepit/sfx_OpenPortal.prefab |
| sfx_oven_burnt | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/sfx_oven_burnt.prefab |
| sfx_oven_close | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/sfx_oven_close.prefab |
| sfx_oven_done | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/sfx_oven_done.prefab |
| sfx_oven_open | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/sfx_oven_open.prefab |
| sfx_oven_take | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/oven/fx/sfx_oven_take.prefab |
| sfx_perfect_dodge | — | Characters/Player | 6 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_perfect_dodge.prefab |
| sfx_perfectblock | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_perfectblock.prefab |
| sfx_pickable_pick | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/fx/sfx_pickable_pick.prefab |
| sfx_pickaxe_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/pickaxe/sfx_pickaxe_hit.prefab |
| sfx_pickaxe_hit_vibration_only | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/pickaxe/sfx_pickaxe_hit_vibration_only.prefab |
| sfx_pickaxe_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/pickaxe/sfx_pickaxe_swing.prefab |
| sfx_pickup | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/sfx_pickup.prefab |
| sfx_Poison_Start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Poison_Start.prefab |
| sfx_Potion_eitr_minor | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_eitr_minor.prefab |
| sfx_Potion_fireresist_Start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_fireresist_Start.prefab |
| sfx_Potion_frostresist_Start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_frostresist_Start.prefab |
| sfx_Potion_health_large | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_health_large.prefab |
| sfx_Potion_health_medium | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_health_medium.prefab |
| sfx_Potion_health_minor | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_health_minor.prefab |
| sfx_Potion_health_Start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_health_Start.prefab |
| sfx_Potion_stamina_Start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_stamina_Start.prefab |
| sfx_Potion_stamina_Start_lingering | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_stamina_Start_lingering.prefab |
| sfx_Potion_stamina_Start_medium | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Potion_stamina_Start_medium.prefab |
| sfx_prespawn | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_prespawn.prefab |
| sfx_prespawn_fader | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_prespawn_fader.prefab |
| sfx_prespawn_fader_vibration_only | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_prespawn_fader_vibration_only.prefab |
| sfx_prespawn_vibration_only | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_prespawn_vibration_only.prefab |
| sfx_prespawnLastBossGate | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_prespawnLastBossGate.prefab |
| sfx_ProjectileHit | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/sfx_ProjectileHit.prefab |
| sfx_Puke_female | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Puke_female.prefab |
| sfx_Puke_male | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_Puke_male.prefab |
| sfx_queendoor_open | — | world/dungeon | 4 components; active: yes | c4210710 / Assets/world/dungeon/doors/QueenDoor/sfx_queendoor_open.prefab |
| sfx_queendoor_sequence | — | world/dungeon | 4 components; active: yes | c4210710 / Assets/world/dungeon/doors/QueenDoor/sfx_queendoor_sequence.prefab |
| sfx_raven_flap | — | Characters/Raven | 4 components; active: yes | c4210710 / Assets/Characters/Raven/fx/sfx_raven_flap.prefab |
| sfx_raven_kaw | — | Characters/Raven | 4 components; active: yes | c4210710 / Assets/Characters/Raven/fx/sfx_raven_kaw.prefab |
| sfx_reload_done | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/fx/sfx_reload_done.prefab |
| sfx_reload_dverger_done | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/fx/sfx_reload_dverger_done.prefab |
| sfx_reload_dverger_start | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/fx/sfx_reload_dverger_start.prefab |
| sfx_reload_start | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/fx/sfx_reload_start.prefab |
| sfx_rock_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/sfx_rock_destroyed.prefab |
| sfx_rock_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/sfx_rock_hit.prefab |
| sfx_rock_wall_crumble | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/sfx/sfx_rock_wall_crumble.prefab |
| sfx_rooster_idle | — | Characters/Chicken | 5 components; active: yes | c4210710 / Assets/Characters/Chicken/sfx/sfx_rooster_idle.prefab |
| sfx_runestone_activate | — | world/Props | 4 components; active: yes | d59cfac / Assets/world/Props/Waystone/sfx_runestone_activate.prefab |
| sfx_runestone_interact | — | world/Props | 4 components; active: yes | 843e7fe6 / Assets/world/Props/RuneStones/sfx/sfx_runestone_interact.prefab |
| sfx_seagull_idle | — | Characters/animals | 4 components; active: yes | c4210710 / Assets/Characters/animals/birds/crow/fx/sfx_seagull_idle.prefab |
| sfx_seal_alert | — | Characters/seal | 5 components; active: yes | c4210710 / Assets/Characters/seal/fx/Audio/Alert/sfx_seal_alert.prefab |
| sfx_seal_crawl | — | Characters/seal | 4 components; active: yes | c4210710 / Assets/Characters/seal/fx/Audio/Movement/sfx_seal_crawl.prefab |
| sfx_seal_death | — | Characters/seal | 5 components; active: yes | c4210710 / Assets/Characters/seal/fx/Audio/Death/sfx_seal_death.prefab |
| sfx_seal_idle | — | Characters/seal | 5 components; active: yes | c4210710 / Assets/Characters/seal/fx/Audio/Idle/sfx_seal_idle.prefab |
| sfx_secretfound | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_secretfound.prefab |
| sfx_seeker_alerted | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_alerted.prefab |
| sfx_seeker_attack_claws | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_attack_claws.prefab |
| sfx_seeker_attack_claws_flying | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_attack_claws_flying.prefab |
| sfx_seeker_attack_pierce | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_attack_pierce.prefab |
| sfx_seeker_attack_start | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_attack_start.prefab |
| sfx_seeker_brute_alerted | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_alerted.prefab |
| sfx_seeker_brute_attack_bite | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_attack_bite.prefab |
| sfx_seeker_brute_attack_ram_hit | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_attack_ram_hit.prefab |
| sfx_seeker_brute_attack_ram_start | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_attack_ram_start.prefab |
| sfx_seeker_brute_footstep | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_footstep.prefab |
| sfx_seeker_brute_groundslam_impact | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_groundslam_impact.prefab |
| sfx_seeker_brute_groundslam_Start | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_groundslam_Start.prefab |
| sfx_seeker_brute_idle | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_idle.prefab |
| sfx_seeker_brute_mandible | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_mandible.prefab |
| sfx_seeker_brute_taunt | — | Characters/SeekerBrute | 4 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/sfx/sfx_seeker_brute_taunt.prefab |
| sfx_seeker_flying | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_flying.prefab |
| sfx_seeker_hurt | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_hurt.prefab |
| sfx_seeker_idle | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_idle.prefab |
| sfx_seeker_land | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_land.prefab |
| sfx_seeker_overlay | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_overlay.prefab |
| sfx_seeker_takeoff | — | Characters/Seeker | 4 components; active: yes | c4210710 / Assets/Characters/Seeker/fx/sfx_seeker_takeoff.prefab |
| sfx_serpent_alerted | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_alerted.prefab |
| sfx_serpent_attack | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_attack.prefab |
| sfx_serpent_attack_hit | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_attack_hit.prefab |
| sfx_serpent_attack_trigger | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_attack_trigger.prefab |
| sfx_serpent_death | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_death.prefab |
| sfx_serpent_hurt | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_hurt.prefab |
| sfx_serpent_idle | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_idle.prefab |
| sfx_serpent_taunt | — | Characters/Serpent | 6 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/sfx_serpent_taunt.prefab |
| sfx_shieldgenerator_hit | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/sfx/Shield Hit/sfx_shieldgenerator_hit.prefab |
| sfx_shieldgenerator_lowfuel_loop | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/sfx/sfx_shieldgenerator_lowfuel_loop.prefab |
| sfx_shieldgenerator_powered_loop | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/sfx/sfx_shieldgenerator_powered_loop.prefab |
| sfx_shieldgenerator_refuel | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/sfx/sfx_shieldgenerator_refuel.prefab |
| sfx_shieldgenerator_shutdown | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/sfx/sfx_shieldgenerator_shutdown.prefab |
| sfx_shieldgenerator_startup | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/sfx/sfx_shieldgenerator_startup.prefab |
| sfx_shieldgenerator_wall_loop | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/sfx/sfx_shieldgenerator_wall_loop.prefab |
| sfx_ship_destroyed | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/sfx_ship_destroyed.prefab |
| sfx_ship_impact | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/sfx_ship_impact.prefab |
| sfx_ship_sailposition_change_vibration_only | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/sfx_ship_sailposition_change_vibration_only.prefab |
| sfx_ship_waterimpact | — | GameElements/Ships | 4 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/sfx_ship_waterimpact.prefab |
| sfx_silvermace_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/SilverWarhammer/fx/sfx_silvermace_hit.prefab |
| sfx_skeleton_alerted | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_alerted.prefab |
| sfx_skeleton_attack | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_attack.prefab |
| sfx_skeleton_basic_attack_melee | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Basic/sfx_skeleton_basic_attack_melee.prefab |
| sfx_skeleton_basic_death | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Basic/sfx_skeleton_basic_death.prefab |
| sfx_skeleton_basic_verse_attack | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Basic/sfx_skeleton_basic_verse_attack.prefab |
| sfx_skeleton_basic_verse_idle | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Basic/sfx_skeleton_basic_verse_idle.prefab |
| sfx_skeleton_big_alerted | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_big_alerted.prefab |
| sfx_skeleton_big_death | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_big_death.prefab |
| sfx_skeleton_death | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_death.prefab |
| sfx_skeleton_frozen_attack_melee | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/DeepNorth/sfx_skeleton_frozen_attack_melee.prefab |
| sfx_skeleton_frozen_death | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/DeepNorth/sfx_skeleton_frozen_death.prefab |
| sfx_skeleton_frozen_verse_attack | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/DeepNorth/sfx_skeleton_frozen_verse_attack.prefab |
| sfx_skeleton_frozen_verse_idle | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/DeepNorth/sfx_skeleton_frozen_verse_idle.prefab |
| sfx_skeleton_hildir_attack_melee | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Hildir/sfx_skeleton_hildir_attack_melee.prefab |
| sfx_skeleton_hildir_attack_skill | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Hildir/sfx_skeleton_hildir_attack_skill.prefab |
| sfx_skeleton_hildir_death | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Hildir/sfx_skeleton_hildir_death.prefab |
| sfx_skeleton_hildir_torch_loop | — | Characters/Skeleton | 4 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Hildir/sfx_skeleton_hildir_torch_loop.prefab |
| sfx_skeleton_hildir_verse_attack | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Hildir/sfx_skeleton_hildir_verse_attack.prefab |
| sfx_skeleton_hildir_verse_idle | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Hildir/sfx_skeleton_hildir_verse_idle.prefab |
| sfx_skeleton_hit | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_hit.prefab |
| sfx_skeleton_idle | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_idle.prefab |
| sfx_skeleton_mace_hit | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_mace_hit.prefab |
| sfx_skeleton_poison_attack_melee | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Poison/sfx_skeleton_poison_attack_melee.prefab |
| sfx_skeleton_poison_death | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Poison/sfx_skeleton_poison_death.prefab |
| sfx_skeleton_poison_verse_attack | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Poison/sfx_skeleton_poison_verse_attack.prefab |
| sfx_skeleton_poison_verse_idle | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Poison/sfx_skeleton_poison_verse_idle.prefab |
| sfx_skeleton_rise | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/sfx_skeleton_rise.prefab |
| sfx_skeleton_swamp_attack_melee | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Swamp/sfx_skeleton_swamp_attack_melee.prefab |
| sfx_skeleton_swamp_death | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Swamp/sfx_skeleton_swamp_death.prefab |
| sfx_skeleton_swamp_verse_attack | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Swamp/sfx_skeleton_swamp_verse_attack.prefab |
| sfx_skeleton_swamp_verse_idle | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/New sfx/Swamp/sfx_skeleton_swamp_verse_idle.prefab |
| sfx_skull_summon_skeleton | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/sfx_skull_summon_skeleton.prefab |
| sfx_sledge_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sledge/sfx_sledge_hit.prefab |
| sfx_sledge_iron_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/IronSledge/fx/sfx_sledge_iron_hit.prefab |
| sfx_sledge_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sledge/sfx_sledge_swing.prefab |
| sfx_slide | — | Characters/Player | 4 components; active: yes | b8689a71 / Assets/Characters/Player/audio/old/sfx_slide.prefab |
| sfx_smelter_add | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/smelter/fx/sfx_smelter_add.prefab |
| sfx_smelter_produce | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/smelter/fx/sfx_smelter_produce.prefab |
| sfx_snow_hit_debris | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/SnowAudio/sfx_snow_hit_debris.prefab |
| sfx_snow_hit_transient | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/SnowAudio/sfx_snow_hit_transient.prefab |
| sfx_spawn | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_spawn.prefab |
| sfx_spawn_vibration_only | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/sfx_spawn_vibration_only.prefab |
| sfx_spear_flint_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/spear/sfx_spear_flint_hit.prefab |
| sfx_spear_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/spear/sfx_spear_hit.prefab |
| sfx_spear_poke | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/spear/sfx_spear_poke.prefab |
| sfx_spear_throw | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/spear/sfx_spear_throw.prefab |
| sfx_staff_elder_burst | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Elder Staff/Burst/sfx_staff_elder_burst.prefab |
| sfx_staff_elder_cast | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Elder Staff/Cast/sfx_staff_elder_cast.prefab |
| sfx_staff_elder_grow | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Elder Staff/Grow/sfx_staff_elder_grow.prefab |
| sfx_staff_elder_root_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Elder Staff/Root Hit/sfx_staff_elder_root_hit.prefab |
| sfx_staff_elder_root_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Elder Staff/Root Swing/sfx_staff_elder_root_swing.prefab |
| sfx_staff_grenade_cast | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Grenade Staff/sfx_staff_grenade_cast.prefab |
| sfx_staff_grenade_impact_big | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Grenade Staff/sfx_staff_grenade_impact_big.prefab |
| sfx_staff_grenade_impact_small | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Grenade Staff/sfx_staff_grenade_impact_small.prefab |
| sfx_staff_lightning_charge | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Lightning Staff/sfx_staff_lightning_charge.prefab |
| sfx_staff_lightning_fire | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Lightning Staff/sfx_staff_lightning_fire.prefab |
| sfx_staff_trollstav_cast | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Trollstav/sfx_staff_trollstav_cast.prefab |
| sfx_staff_trollstav_meteorite | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Trollstav/sfx_staff_trollstav_meteorite.prefab |
| sfx_staff_trollstav_troll_impact | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx/Trollstav/sfx_staff_trollstav_troll_impact.prefab |
| sfx_stafffrostorbs_cast | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffFrostOrbs/sfx/sfx_stafffrostorbs_cast.prefab |
| sfx_stafffrostorbs_shield_bounce | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffFrostOrbs/sfx/sfx_stafffrostorbs_shield_bounce.prefab |
| sfx_stafffrostorbs_shield_loop | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffFrostOrbs/sfx/sfx_stafffrostorbs_shield_loop.prefab |
| sfx_stafffrostorbs_shield_spawn | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffFrostOrbs/sfx/sfx_stafffrostorbs_shield_spawn.prefab |
| sfx_StaffLightning_charge | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx_StaffLightning_charge.prefab |
| sfx_StaffLightning_fire | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsStaffs/sfx_StaffLightning_fire.prefab |
| sfx_stafforbofahri_cast | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffOrbofAhri/sfx/sfx_stafforbofahri_cast.prefab |
| sfx_stafforbofahri_explosion | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffOrbofAhri/sfx/sfx_stafforbofahri_explosion.prefab |
| sfx_stafforbofahri_projectile_loop | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffOrbofAhri/sfx/sfx_stafforbofahri_projectile_loop.prefab |
| sfx_staffspiritcaller_cast | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffSpiritCaller/sfx/sfx_staffspiritcaller_cast.prefab |
| sfx_staffspiritcaller_summon | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffSpiritCaller/sfx/sfx_staffspiritcaller_summon.prefab |
| sfx_staffthunderblood_cast | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffThunderBlood/sfx/sfx_staffthunderblood_cast.prefab |
| sfx_staffthunderblood_thunder | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Molds/model/StaffThunderBlood/sfx/sfx_staffthunderblood_thunder.prefab |
| sfx_stonedoor_sliding_open | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Dvergr/Sliding_door/sfx_stonedoor_sliding_open.prefab |
| sfx_stonegolem_alerted | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_alerted.prefab |
| sfx_stonegolem_attack_hit | — | Characters/StoneGolem | 6 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_attack_hit.prefab |
| sfx_stonegolem_attack_wosh | — | Characters/StoneGolem | 6 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_attack_wosh.prefab |
| sfx_stonegolem_death | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_death.prefab |
| sfx_stonegolem_footstep | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_footstep.prefab |
| sfx_stonegolem_hurt | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_hurt.prefab |
| sfx_stonegolem_idle | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_idle.prefab |
| sfx_stonegolem_primary_start | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_primary_start.prefab |
| sfx_stonegolem_second_start | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_second_start.prefab |
| sfx_stonegolem_spikeattack_trailon | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_spikeattack_trailon.prefab |
| sfx_stonegolem_wakeup | — | Characters/StoneGolem | 6 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/sfx_stonegolem_wakeup.prefab |
| sfx_sword_hit | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sword/sfx_sword_hit.prefab |
| sfx_sword_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sword/sfx_sword_swing.prefab |
| sfx_tentaroot_attack | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/sfx_tentaroot_attack.prefab |
| sfx_thunder | — | Audio/sfx | 5 components; active: yes | d59cfac / Assets/Audio/sfx/thunder/sfx_thunder.prefab |
| sfx_tick_alerted | — | Characters/Tick | 5 components; active: yes | c4210710 / Assets/Characters/Tick/SFX/sfx_tick_alerted.prefab |
| sfx_tick_attack_drain | — | Characters/Tick | 5 components; active: yes | c4210710 / Assets/Characters/Tick/SFX/sfx_tick_attack_drain.prefab |
| sfx_tick_attack_jump | — | Characters/Tick | 5 components; active: yes | c4210710 / Assets/Characters/Tick/SFX/sfx_tick_attack_jump.prefab |
| sfx_tick_attack_land | — | Characters/Tick | 4 components; active: yes | c4210710 / Assets/Characters/Tick/SFX/sfx_tick_attack_land.prefab |
| sfx_tick_hurt | — | Characters/Tick | 5 components; active: yes | c4210710 / Assets/Characters/Tick/SFX/sfx_tick_hurt.prefab |
| sfx_tick_idle | — | Characters/Tick | 5 components; active: yes | c4210710 / Assets/Characters/Tick/SFX/sfx_tick_idle.prefab |
| sfx_torch_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/torch/sfx_torch_swing.prefab |
| sfx_trainingdummy_alert | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Alert/sfx_trainingdummy_alert.prefab |
| sfx_trainingdummy_heavy_attack | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Melee/sfx_trainingdummy_heavy_attack.prefab |
| sfx_trainingdummy_heavy_attack impact | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Melee/sfx_trainingdummy_heavy_attack impact.prefab |
| sfx_trainingdummy_idle | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Idle/sfx_trainingdummy_idle.prefab |
| sfx_trainingdummy_light_attack | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Melee/sfx_trainingdummy_light_attack.prefab |
| sfx_trainingdummy_light_attack impact | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Melee/sfx_trainingdummy_light_attack impact.prefab |
| sfx_trainingdummy_stagger | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Stagger/sfx_trainingdummy_stagger.prefab |
| sfx_trainingdummy_throw | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Throw/sfx_trainingdummy_throw.prefab |
| sfx_trainingdummy_throw_impact | — | Characters/TrainingDummy | 5 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/sfx/Throw/sfx_trainingdummy_throw_impact.prefab |
| sfx_treasurechest_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_treasurechest_destroyed.prefab |
| sfx_tree_fall | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/sfx_tree_fall.prefab |
| sfx_tree_fall_abomination | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_tree_fall_abomination.prefab |
| sfx_tree_fall_hit | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/sfx_tree_fall_hit.prefab |
| sfx_tree_firedamage_tick | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/sfx_tree_firedamage_tick.prefab |
| sfx_tree_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/sfx_tree_hit.prefab |
| sfx_tree_hit_abomination | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/sfx_tree_hit_abomination.prefab |
| sfx_troll_alerted | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_alerted.prefab |
| sfx_troll_attack_hit | — | Characters/Troll | 6 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_attack_hit.prefab |
| sfx_troll_attacking | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_attacking.prefab |
| sfx_troll_death | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_death.prefab |
| sfx_troll_footstep | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_footstep.prefab |
| sfx_troll_footstep_water | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_footstep_water.prefab |
| sfx_troll_hit | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_hit.prefab |
| sfx_troll_idle | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_idle.prefab |
| sfx_troll_rock_destroyed | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/sfx_troll_rock_destroyed.prefab |
| sfx_trollfire_attack_club_impact | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Club/sfx_trollfire_attack_club_impact.prefab |
| sfx_trollfire_attack_club_swing_down | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Club/sfx_trollfire_attack_club_swing_down.prefab |
| sfx_trollfire_attack_club_swing_up | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Club/sfx_trollfire_attack_club_swing_up.prefab |
| sfx_trollfire_attack_slam_impact | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Slam/sfx_trollfire_attack_slam_impact.prefab |
| sfx_trollfire_attack_slam_start | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Slam/sfx_trollfire_attack_slam_start.prefab |
| sfx_trollfire_attack_slap_impact | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Slap/sfx_trollfire_attack_slap_impact.prefab |
| sfx_trollfire_attack_slap_start | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Slap/sfx_trollfire_attack_slap_start.prefab |
| sfx_trollfire_attack_slap_swing | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Slap/sfx_trollfire_attack_slap_swing.prefab |
| sfx_trollfire_attack_throw | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Attack Throw/sfx_trollfire_attack_throw.prefab |
| sfx_trollfire_death | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Death/sfx_trollfire_death.prefab |
| sfx_trollfire_fire_loop | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Idle/sfx_trollfire_fire_loop.prefab |
| sfx_trollfire_footstep | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Footsteps/sfx_trollfire_footstep.prefab |
| sfx_trollfire_idle | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Idle/sfx_trollfire_idle.prefab |
| sfx_trollfire_roar | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/sfx/Roar/sfx_trollfire_roar.prefab |
| sfx_ui_player_damage_tick_vibration_only | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/vibration/sfx_ui_player_damage_tick_vibration_only.prefab |
| sfx_ui_player_firedamage_ignite | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/FireDamage/sfx_ui_player_firedamage_ignite.prefab |
| sfx_ui_player_firedamage_loop | — | Characters/Player | 3 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/FireDamage/sfx_ui_player_firedamage_loop.prefab |
| sfx_ui_player_firedamage_tick | — | Characters/Player | 4 components; active: yes | c4210710 / Assets/Characters/Player/audio/wav/FireDamage/sfx_ui_player_firedamage_tick.prefab |
| sfx_ulv_death | — | Characters/Ulv | 5 components; active: yes | c4210710 / Assets/Characters/Ulv/Fx/sfx_ulv_death.prefab |
| sfx_unarmed_blocked | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_unarmed_blocked.prefab |
| sfx_unarmed_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sfx_unarmed_hit.prefab |
| sfx_unarmed_swing | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sfx_unarmed_swing.prefab |
| sfx_unbjorn_bite_attack | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Melee/sfx_unbjorn_bite_attack.prefab |
| sfx_unbjorn_bite_attack_impact | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Melee/sfx_unbjorn_bite_attack_impact.prefab |
| sfx_unbjorn_claw_attack | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Melee/sfx_unbjorn_claw_attack.prefab |
| sfx_unbjorn_claw_attack_slash | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Melee/sfx_unbjorn_claw_attack_slash.prefab |
| sfx_unbjorn_death | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Death/sfx_unbjorn_death.prefab |
| sfx_unbjorn_footstep | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Footsteps/sfx_unbjorn_footstep.prefab |
| sfx_unbjorn_hurt | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Hurt/sfx_unbjorn_hurt.prefab |
| sfx_unbjorn_idle | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Unbjorn/sfx/Idle/sfx_unbjorn_idle.prefab |
| sfx_UndeadBurn_Start | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_UndeadBurn_Start.prefab |
| sfx_unstablerock_explosion | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Flametal/model/sfx/sfx_unstablerock_explosion.prefab |
| sfx_valkyrie_flapwing | — | Characters/Valkyrie | 4 components; active: yes | c4210710 / Assets/Characters/Valkyrie/fx/sfx_valkyrie_flapwing.prefab |
| sfx_vulture_alert | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Alert/sfx_vulture_alert.prefab |
| sfx_vulture_attack_claw | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Attack Claw/sfx_vulture_attack_claw.prefab |
| sfx_vulture_death | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Death/sfx_vulture_death.prefab |
| sfx_vulture_eat_bite | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Eat/sfx_vulture_eat_bite.prefab |
| sfx_vulture_eat_break | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Eat/sfx_vulture_eat_break.prefab |
| sfx_vulture_eat_swallow | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Eat/sfx_vulture_eat_swallow.prefab |
| sfx_vulture_footstep | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Footsteps/sfx_vulture_footstep.prefab |
| sfx_vulture_idle | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Idle/sfx_vulture_idle.prefab |
| sfx_vulture_wing_flap | — | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/sfx/Wing Flap/sfx_vulture_wing_flap.prefab |
| sfx_weapons_blood_enable | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Blood/Enable/sfx_weapons_blood_enable.prefab |
| sfx_weapons_blood_impact | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Blood/Impact/sfx_weapons_blood_impact.prefab |
| sfx_weapons_lightning_chain | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Lightning/Chain/sfx_weapons_lightning_chain.prefab |
| sfx_weapons_lightning_enable | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Lightning/Enable/sfx_weapons_lightning_enable.prefab |
| sfx_weapons_lightning_impact | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Lightning/Impact/sfx_weapons_lightning_impact.prefab |
| sfx_weapons_nature_enable | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Nature/Enable/sfx_weapons_nature_enable.prefab |
| sfx_weapons_nature_impact | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Nature/Impact/sfx_weapons_nature_impact.prefab |
| sfx_weapons_nature_root | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Enchantments/Nature/Root/sfx_weapons_nature_root.prefab |
| sfx_window_open | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/window/fx/sfx_window_open.prefab |
| sfx_windows_close | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/window/fx/sfx_windows_close.prefab |
| sfx_WishbonePing_closer | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_WishbonePing_closer.prefab |
| sfx_WishbonePing_far | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_WishbonePing_far.prefab |
| sfx_WishbonePing_further | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_WishbonePing_further.prefab |
| sfx_WishbonePing_med | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_WishbonePing_med.prefab |
| sfx_WishbonePing_near | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/sfx_WishbonePing_near.prefab |
| sfx_wolf_alerted | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_alerted.prefab |
| sfx_wolf_attack | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_attack.prefab |
| sfx_wolf_attack_hit | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_attack_hit.prefab |
| sfx_wolf_birth | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_birth.prefab |
| sfx_wolf_death | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_death.prefab |
| sfx_wolf_haul | — | Characters/Wolf | 4 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_haul.prefab |
| sfx_wolf_hit | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_hit.prefab |
| sfx_wolf_love | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/sfx_wolf_love.prefab |
| sfx_wood_blocked | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_wood_blocked.prefab |
| sfx_wood_blocked_overlay | — | Audio/sfx | 5 components; active: yes | c4210710 / Assets/Audio/sfx/sfx_wood_blocked_overlay.prefab |
| sfx_wood_break | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/sfx_wood_break.prefab |
| sfx_wood_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_wood_destroyed.prefab |
| sfx_wood_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/sfx_wood_hit.prefab |
| sfx_woosh_scythe | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/sfx_woosh_scythe.prefab |
| sfx_wraith_alerted | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/sfx_wraith_alerted.prefab |
| sfx_wraith_attack | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/sfx_wraith_attack.prefab |
| sfx_wraith_attack_hit | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/sfx_wraith_attack_hit.prefab |
| sfx_wraith_death | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/sfx_wraith_death.prefab |
| sfx_wraith_hit | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/sfx_wraith_hit.prefab |
| sfx_wraith_idle | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/sfx_wraith_idle.prefab |
| sfx_writhan_bite | — | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/sfx/Attack Bite/sfx_writhan_bite.prefab |
| sfx_writhan_bite_attack | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Melee/sfx_writhan_bite_attack.prefab |
| sfx_writhan_bite_attack_impact | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Melee/sfx_writhan_bite_attack_impact.prefab |
| sfx_writhan_death_charge | — | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/sfx/Death/sfx_writhan_death_charge.prefab |
| sfx_writhan_death_explosion | — | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/sfx/Death/sfx_writhan_death_explosion.prefab |
| sfx_writhan_fizz | — | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/sfx/Melee/sfx_writhan_fizz.prefab |
| sfx_writhan_idle | — | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/sfx/sfx_writhan_idle.prefab |
| sfx_writhan_step | — | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/sfx/Footstep/sfx_writhan_step.prefab |
| sfx_writhan_verse_attack | — | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/sfx/Attack Bite/sfx_writhan_verse_attack.prefab |
| sfx_writhan_verse_death | — | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/sfx/Death/sfx_writhan_verse_death.prefab |
| ShadowPerson | Shadow; Haldor | Characters/FallenWarrior | 12 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/ShadowPerson.prefab |
| shaman_attack_aoe | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/shaman_attack_aoe.prefab |
| shaman_attack_aoe_frozen | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/shaman_attack_aoe_frozen.prefab |
| shaman_heal_aoe | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/shaman_heal_aoe.prefab |
| shaman_heal_aoe_frozen | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/misc/shaman_heal_aoe_frozen.prefab |
| SharpeningStone | Sharpening Stone | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SharpeningStone.prefab |
| ShieldBanded | Banded Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldBanded.prefab |
| ShieldBlackmetal | Black Metal Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldBlackmetal.prefab |
| ShieldBlackmetalTower | Black Metal Tower Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldBlackmetalTower.prefab |
| ShieldBoneTower | Bone Tower Shield | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldBoneTower.prefab |
| ShieldBronzeBuckler | Bronze Buckler | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldBronzeBuckler.prefab |
| ShieldBucklerGoldUncooked | Cast: Nord Buckler | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ShieldBucklerGoldUncooked.prefab |
| ShieldCarapace | Carapace Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldCarapace.prefab |
| ShieldCarapaceBuckler | Carapace Buckler | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldCarapaceBuckler.prefab |
| ShieldCore | Shield Core | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ShieldCore.prefab |
| ShieldFlametal | Flametal Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldFlametal.prefab |
| ShieldFlametalTower | Flametal Tower Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldFlametalTower.prefab |
| shieldgenerator_attack | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/shieldgenerator_attack.prefab |
| ShieldGold | Nord Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldGold.prefab |
| ShieldGoldBuckler | Nord Buckler | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldGoldBuckler.prefab |
| ShieldGoldTower | Nord Greatshield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldGoldTower.prefab |
| ShieldIronBuckler | Iron Buckler | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldIronBuckler.prefab |
| ShieldIronSquare | Iron Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldIronSquare.prefab |
| ShieldIronTower | Iron Tower Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldIronTower.prefab |
| ShieldKnight | Knight shield UNUSED | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldKnight.prefab |
| ShieldRoots | Shield of Roots | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldRoots.prefab |
| ShieldRoundGoldUncooked | Cast: Nord Shield | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ShieldRoundGoldUncooked.prefab |
| ShieldSerpentscale | Serpent Scale Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldSerpentscale.prefab |
| ShieldSilver | Silver Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldSilver.prefab |
| ShieldTowerGoldUncooked | Cast: Nord Greatshield | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ShieldTowerGoldUncooked.prefab |
| ShieldWood | Wood Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldWood.prefab |
| ShieldWoodTower | Wood Tower Shield | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/shields/ShieldWoodTower.prefab |
| ShimmeringSand_rock | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/ShimmeringSand_rock.prefab |
| ShimmeringSand_rock_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/ShimmeringSand_rock_frac.prefab |
| ship_construction | Ship construction | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/ship_construction.prefab |
| shipwreck_karve_bottomboards | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckKarve/shipwreck_karve_bottomboards.prefab |
| shipwreck_karve_bow | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckKarve/shipwreck_karve_bow.prefab |
| shipwreck_karve_chest | Chest | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/ShipwreckKarve/shipwreck_karve_chest.prefab |
| shipwreck_karve_dragonhead | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckKarve/shipwreck_karve_dragonhead.prefab |
| shipwreck_karve_stern | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckKarve/shipwreck_karve_stern.prefab |
| shipwreck_karve_sternpost | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckKarve/shipwreck_karve_sternpost.prefab |
| shipwreck_vikingship_chest | Chest | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/ShipwreckVikingship/shipwreck_vikingship_chest.prefab |
| shipwreck_vikingship_front | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckVikingship/shipwreck_vikingship_front.prefab |
| shipwreck_vikingship_frontpiece | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckVikingship/shipwreck_vikingship_frontpiece.prefab |
| shipwreck_vikingship_mast1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/ShipwreckVikingship/shipwreck_vikingship_mast1.prefab |
| shipwreck_vikingship_rear | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/ShipwreckVikingship/shipwreck_vikingship_rear.prefab |
| ShocklateSmoothie | Muckshake | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/ShocklateSmoothie.prefab |
| ShootStump | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Shoots/ShootStump.prefab |
| Shovel | Snow Shovel | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/tools/Shovel.prefab |
| shrub_2 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Shrub02/shrub_2.prefab |
| shrub_2_heath | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Shrub02/shrub_2_heath.prefab |
| siege_wall_1x1 | Temp Siege Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/siege_wall_1x1.prefab |
| siegebomb_explosion | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSiege/siegebomb_explosion.prefab |
| siegebomb_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSiege/siegebomb_projectile.prefab |
| sign | Sign | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/sign.prefab |
| sign_notext | Sign | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/sign_notext.prefab |
| Silver | Silver | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Silver.prefab |
| SilverNecklace | Silver Necklace | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/valuables/SilverNecklace.prefab |
| SilverOre | Silver Ore | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SilverOre.prefab |
| silvervein | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/silvervein.prefab |
| silvervein_frac | Silver Vein | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/silvervein_frac.prefab |
| SizzlingBerryBroth | Sizzling Berry Broth | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SizzlingBerryBroth.prefab |
| Skeleton | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton.prefab |
| Skeleton_aspect | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_aspect.prefab |
| skeleton_bow | Bow | Characters/Skeleton | 7 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_bow.prefab |
| skeleton_bow2 | Bow | Characters/Skeleton | 7 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_bow2.prefab |
| skeleton_bow_meadows | Bow | Characters/Skeleton | 7 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_bow_meadows.prefab |
| skeleton_bow_mountains | Bow | Characters/Skeleton | 7 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_bow_mountains.prefab |
| skeleton_bow_swamps | Bow | Characters/Skeleton | 7 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_bow_swamps.prefab |
| Skeleton_DeepNorth | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_DeepNorth.prefab |
| skeleton_firenova_aoe | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_firenova_aoe.prefab |
| Skeleton_Friendly | Skelett | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Friendly.prefab |
| Skeleton_Hildir | &lt;color=orange&gt;Brenna&lt;/color&gt; | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Hildir.prefab |
| skeleton_hildir_firenova | Fire Skeleton Sword | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_hildir_firenova.prefab |
| Skeleton_Hildir_nochest | &lt;color=orange&gt;Brenna&lt;/color&gt; | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Hildir_nochest.prefab |
| skeleton_mace | Dragur axe | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_mace.prefab |
| skeleton_mace_DeepNorth | Dragur axe | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_mace_DeepNorth.prefab |
| Skeleton_Meadows | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Meadows.prefab |
| Skeleton_Meadows_noarcher | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Meadows_noarcher.prefab |
| Skeleton_Mountains | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Mountains.prefab |
| Skeleton_Mountains_noarcher | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Mountains_noarcher.prefab |
| Skeleton_NoArcher | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_NoArcher.prefab |
| Skeleton_Poison | Rancid Remains | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Poison.prefab |
| Skeleton_Swamps | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Swamps.prefab |
| Skeleton_Swamps_noarcher | Skeleton | Characters/Skeleton | 11 components; active: yes | c4210710 / Assets/Characters/Skeleton/Skeleton_Swamps_noarcher.prefab |
| skeleton_sword | Dragur axe | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_sword.prefab |
| skeleton_sword2 | Dragur axe | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_sword2.prefab |
| skeleton_sword_hildir | Fire Skeleton Sword | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_sword_hildir.prefab |
| skeleton_sword_meadows | Dragur axe | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_sword_meadows.prefab |
| skeleton_sword_mountains | Dragur axe | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_sword_mountains.prefab |
| skeleton_sword_swamps | Dragur axe | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/weapons/skeleton_sword_swamps.prefab |
| SkillListTooltip | — | UI/prefabs | 1 components; active: yes | c4210710 / Assets/UI/prefabs/IngameGui/SkillListTooltip.prefab |
| Skull1 | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/Bones/Skull1.prefab |
| Skull2 | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/Bones/Skull2.prefab |
| skull_pile | Pile of Skulls | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/skull_pile.prefab |
| Sled | — | GameElements/Cart | 12 components; active: yes | c4210710 / Assets/GameElements/Cart/Sled.prefab |
| sledge_aoe | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sledge/sledge_aoe.prefab |
| SledgeCheat | Cheat sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeCheat.prefab |
| SledgeDemolisher | Demolisher | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeDemolisher.prefab |
| SledgeGold | Nord Sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeGold.prefab |
| SledgeGold_BloodLightning | Thunderblood Sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeGold_BloodLightning.prefab |
| SledgeGold_FrostFire | Frostfire Sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeGold_FrostFire.prefab |
| SledgeGoldUncooked | Cast: Nord Sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeGoldUncooked.prefab |
| SledgeIron | Iron Sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeIron.prefab |
| SledgeStagbreaker | Stagbreaker | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeStagbreaker.prefab |
| SledgeWood | Wooden Sledge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SledgeWood.prefab |
| small_rock1 | — | world/Props | 1 components; active: yes | b8689a71 / Assets/world/Props/ground_clutter/old/small_rock1.prefab |
| small_rock2 | — | world/Props | 1 components; active: yes | c4210710 / Assets/world/Props/ground_clutter/old/small_rock2.prefab |
| SmallPartsGoldUncooked | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SmallPartsGoldUncooked.prefab |
| smelter | Smelter | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/smelter.prefab |
| smoke_area | — | Effects | 3 components; active: yes | 68ab52e3 / Assets/Effects/smoke_area.prefab |
| SmokeBall | — | world/SmokeFire | 4 components; active: yes | c4210710 / Assets/world/SmokeFire/SmokeBall.prefab |
| SmokeBallBomb | — | world/SmokeFire | 7 components; active: yes | c4210710 / Assets/world/SmokeFire/SmokeBallBomb.prefab |
| SmokeBallTurbulent | — | world/SmokeFire | 7 components; active: yes | c4210710 / Assets/world/SmokeFire/SmokeBallTurbulent.prefab |
| smokebomb_explosion | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSmoke/smokebomb_explosion.prefab |
| smokebomb_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSmoke/smokebomb_projectile.prefab |
| SmokedFish | Smoked Fish | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SmokedFish.prefab |
| SmokedMooseMeat | Smoked Moose Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SmokedMooseMeat.prefab |
| SmokeParticleSystem | — | world/SmokeFire | 3 components; active: yes | d59cfac / Assets/world/SmokeFire/SmokeParticleSystem.prefab |
| snow_decrease | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_decrease.prefab |
| snow_decrease_firepit_placed_large | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_decrease_firepit_placed_large.prefab |
| snow_decrease_firepit_placed_small | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_decrease_firepit_placed_small.prefab |
| snow_fire | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_fire.prefab |
| snow_fire_big | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_fire_big.prefab |
| snow_increase | Snow Increase | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_increase.prefab |
| snow_increase_roller | Snow Increase | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_increase_roller.prefab |
| snow_increase_tree | Snow Increase | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_increase_tree.prefab |
| snow_increase_treesmall | Snow Increase | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_increase_treesmall.prefab |
| snow_shovel | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_shovel.prefab |
| snow_shovel_big | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_shovel_big.prefab |
| snow_tree | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_tree.prefab |
| snow_walk | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_walk.prefab |
| snow_walk_big | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_walk_big.prefab |
| snow_walk_huge | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_walk_huge.prefab |
| snow_walk_medium | Snow Decrease | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/snow_walk_medium.prefab |
| Snowball | Snowball | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Snowball.prefab |
| snowball_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Snowball/snowball_projectile.prefab |
| SnowballBig | Big Snowball | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SnowballBig.prefab |
| snowballbig_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Snowball/snowballbig_projectile.prefab |
| SnowFirTree | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/SnowFirTree.prefab |
| SnowFirTree 2 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/SnowFirTree 2.prefab |
| SnowFirTree2_snowfall | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/fx/SnowFirTree2_snowfall.prefab |
| SnowFirTree_small | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/SnowFirTree_small.prefab |
| SnowFirTree_snowfall | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/fx/SnowFirTree_snowfall.prefab |
| SnowFirTreeSmall_snowfall | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Trees/fx/SnowFirTreeSmall_snowfall.prefab |
| SnowRoller | — | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/misc/SnowRoller.prefab |
| SnowStorm | — | Effects/weather | 1 components; active: yes | d59cfac / Assets/Effects/weather/SnowStorm.prefab |
| Softtissue | Soft Tissue | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Softtissue.prefab |
| SP_ArmorBronzeChest | Bronze Plate Tunic | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorBronzeChest.prefab |
| SP_ArmorBronzeLegs | Bronze Plate Leggings | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorBronzeLegs.prefab |
| SP_ArmorDress1 | Plain Brown Dress | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/SP_ArmorDress1.prefab |
| SP_ArmorFenringChest | Fenris Coat | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorFenringChest.prefab |
| SP_ArmorFenringLegs | Fenris Leggings | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorFenringLegs.prefab |
| SP_ArmorLeatherLegs | Leather Trousers | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/SP_ArmorLeatherLegs.prefab |
| SP_ArmorMageChest | Eitr-weave Robe | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorMageChest.prefab |
| SP_ArmorMageChest_Ashlands | Robes of Embla | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorMageChest_Ashlands.prefab |
| SP_ArmorMageLegs | Eitr-weave Trousers | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorMageLegs.prefab |
| SP_ArmorMageLegs_Ashlands | Trousers of Embla | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorMageLegs_Ashlands.prefab |
| SP_ArmorPaddedCuirass | Padded Cuirass | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorPaddedCuirass.prefab |
| SP_ArmorPaddedGreaves | Padded Greaves | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorPaddedGreaves.prefab |
| SP_ArmorTrollLeatherChest | Troll Leather Tunic | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorTrollLeatherChest.prefab |
| SP_ArmorTrollLeatherLegs | Troll Leather Trousers | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ArmorTrollLeatherLegs.prefab |
| SP_ArmorTunic5 | Red Tunic with Cape | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/armor/SP_ArmorTunic5.prefab |
| SP_AxeBronze | Bronze Axe | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_AxeBronze.prefab |
| SP_BattleaxeCrystal | Crystal Battleaxe | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_BattleaxeCrystal.prefab |
| SP_BowDraugrFang | Draugr Fang | Characters/FallenWarrior | 9 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_BowDraugrFang.prefab |
| SP_CapeLinen | Linen Cape | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_CapeLinen.prefab |
| SP_CapeTrollHide | Troll Hide Cape | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_CapeTrollHide.prefab |
| SP_CapeWolf | Wolf Fur Cape | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_CapeWolf.prefab |
| SP_HelmetBronze | Bronze Helmet | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_HelmetBronze.prefab |
| SP_KnifeSilver | Silver Knife | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_KnifeSilver.prefab |
| SP_KnifeSkollAndHati | Skoll and Hati | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_KnifeSkollAndHati.prefab |
| SP_ShieldBlackmetalTower | Black Metal Tower Shield | Characters/FallenWarrior | 8 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_ShieldBlackmetalTower.prefab |
| SP_StaffFireball | Staff of Embers | Characters/FallenWarrior | 8 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_StaffFireball.prefab |
| SP_StaffLightning | Dundr | Characters/FallenWarrior | 8 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_StaffLightning.prefab |
| SP_SwordBlackmetal | Black Metal Sword | Characters/FallenWarrior | 7 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/Equipment/ShadowPerson/SP_SwordBlackmetal.prefab |
| Sparkler | Sparkler | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Sparkler.prefab |
| SparklingShroomshake | Sparkling Shroomshake | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SparklingShroomshake.prefab |
| spawn_fader_meteors | — | Characters/Fader | 2 components; active: yes | c4210710 / Assets/Characters/Fader/attacks/spawn_fader_meteors.prefab |
| spawn_frozenking_spikerain | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/spawn_frozenking_spikerain.prefab |
| spawn_meteors | — | Characters/GoblinKing | 2 components; active: yes | c4210710 / Assets/Characters/GoblinKing/attacks/spawn_meteors.prefab |
| spawn_roots | — | Characters/Greydwarf_king | 2 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/spawn_roots.prefab |
| spawn_tendril | — | Characters/FrozenKing | 2 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/spawn_tendril.prefab |
| Spawner_Bat | — | Characters/Wraith | 3 components; active: yes | c4210710 / Assets/Characters/Wraith/Spawner_Bat.prefab |
| Spawner_Bjorn_sleeping | — | Characters/Bjorn | 3 components; active: yes | c4210710 / Assets/Characters/Bjorn/Spawner_Bjorn_sleeping.prefab |
| Spawner_Blob | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/Spawner_Blob.prefab |
| Spawner_BlobElite | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/Spawner_BlobElite.prefab |
| Spawner_BlobTar | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/Spawner_BlobTar.prefab |
| Spawner_BlobTar_respawn_30 | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/Spawner_BlobTar_respawn_30.prefab |
| Spawner_Boar | — | Characters/Boar | 3 components; active: yes | c4210710 / Assets/Characters/Boar/Spawner_Boar.prefab |
| Spawner_BogWitchKvastur_respawn_30 | — | Characters/Kvastur | 3 components; active: yes | c4210710 / Assets/Characters/Kvastur/Spawner_BogWitchKvastur_respawn_30.prefab |
| Spawner_Charred | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_Charred.prefab |
| Spawner_Charred_Archer | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_Charred_Archer.prefab |
| Spawner_Charred_balista | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_Charred_balista.prefab |
| Spawner_Charred_Dyrnwyn | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_Charred_Dyrnwyn.prefab |
| Spawner_Charred_Mage | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_Charred_Mage.prefab |
| Spawner_CharredCross | — | Characters/TheCharred | 6 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_CharredCross.prefab |
| Spawner_CharredStone | — | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_CharredStone.prefab |
| Spawner_CharredStone_Elite | — | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_CharredStone_Elite.prefab |
| Spawner_CharredStone_event | — | Characters/TheCharred | 7 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_CharredStone_event.prefab |
| Spawner_Chicken | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/Spawner_Chicken.prefab |
| Spawner_Cultist | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/Spawner_Cultist.prefab |
| Spawner_Cultist_Hildir | — | Characters/Fenring | 4 components; active: yes | c4210710 / Assets/Characters/Fenring/Spawner_Cultist_Hildir.prefab |
| Spawner_Cultist_Hildir_bossroom | — | Characters/Fenring | 4 components; active: yes | c4210710 / Assets/Characters/Fenring/Spawner_Cultist_Hildir_bossroom.prefab |
| Spawner_Draugr | — | Characters/Draugr | 3 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_Draugr.prefab |
| Spawner_Draugr_Elite | — | Characters/Draugr | 3 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_Draugr_Elite.prefab |
| Spawner_Draugr_Noise | — | Characters/Draugr | 3 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_Draugr_Noise.prefab |
| Spawner_Draugr_Ranged | — | Characters/Draugr | 3 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_Draugr_Ranged.prefab |
| Spawner_Draugr_Ranged_Noise | — | Characters/Draugr | 3 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_Draugr_Ranged_Noise.prefab |
| Spawner_Draugr_respawn_30 | — | Characters/Draugr | 3 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_Draugr_respawn_30.prefab |
| Spawner_DraugrPile | — | Characters/Draugr | 7 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_DraugrPile.prefab |
| Spawner_DvergerArbalest | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Spawner_DvergerArbalest.prefab |
| Spawner_DvergerAshlands | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Spawner_DvergerAshlands.prefab |
| Spawner_DvergerDeepNorth | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Spawner_DvergerDeepNorth.prefab |
| Spawner_DvergerMage | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Spawner_DvergerMage.prefab |
| Spawner_DvergerRandom | — | Characters/Dverger | 3 components; active: yes | c4210710 / Assets/Characters/Dverger/Spawner_DvergerRandom.prefab |
| Spawner_ElakingMole_Wakeup | — | Characters/ElakingMole | 3 components; active: yes | c4210710 / Assets/Characters/ElakingMole/Spawner_ElakingMole_Wakeup.prefab |
| Spawner_FallenValkyrie | — | Characters/FallenValkyrie | 3 components; active: yes | c4210710 / Assets/Characters/FallenValkyrie/Spawner_FallenValkyrie.prefab |
| Spawner_Fenring | — | Characters/Fenring | 3 components; active: yes | c4210710 / Assets/Characters/Fenring/Spawner_Fenring.prefab |
| Spawner_Fish4 | — | Characters/animals | 3 components; active: yes | c4210710 / Assets/Characters/animals/fishes/Spawner_Fish4.prefab |
| Spawner_Frysling | — | Characters/Frysling | 3 components; active: yes | c4210710 / Assets/Characters/Frysling/Spawner_Frysling.prefab |
| Spawner_Frysling_respawn_30 | — | Characters/Frysling | 3 components; active: yes | c4210710 / Assets/Characters/Frysling/Spawner_Frysling_respawn_30.prefab |
| Spawner_Ghost | — | Characters/Ghost | 3 components; active: yes | c4210710 / Assets/Characters/Ghost/Spawner_Ghost.prefab |
| Spawner_Ghost_sleeping | — | Characters/Ghost | 3 components; active: yes | c4210710 / Assets/Characters/Ghost/Spawner_Ghost_sleeping.prefab |
| Spawner_Ghost_Void | — | Characters/Ghost | 3 components; active: yes | c4210710 / Assets/Characters/Ghost/Spawner_Ghost_Void.prefab |
| Spawner_Goblin | — | Characters/Goblin | 3 components; active: yes | c4210710 / Assets/Characters/Goblin/Spawner_Goblin.prefab |
| Spawner_GoblinArcher | — | Characters/Goblin | 3 components; active: yes | c4210710 / Assets/Characters/Goblin/Spawner_GoblinArcher.prefab |
| Spawner_GoblinBrute | — | Characters/GoblinBrute | 3 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/Spawner_GoblinBrute.prefab |
| Spawner_GoblinBrute_Hildir | — | Characters/GoblinBrute | 3 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/Spawner_GoblinBrute_Hildir.prefab |
| Spawner_GoblinDeepNorth | — | Characters/Goblin | 3 components; active: yes | c4210710 / Assets/Characters/Goblin/Spawner_GoblinDeepNorth.prefab |
| Spawner_GoblinShaman | — | Characters/GoblinShaman | 3 components; active: yes | c4210710 / Assets/Characters/GoblinShaman/Spawner_GoblinShaman.prefab |
| Spawner_Greydwarf | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Spawner_Greydwarf.prefab |
| Spawner_Greydwarf_Elite | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Spawner_Greydwarf_Elite.prefab |
| Spawner_Greydwarf_Shaman | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Spawner_Greydwarf_Shaman.prefab |
| Spawner_Greydwarf_Surprise | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Spawner_Greydwarf_Surprise.prefab |
| Spawner_GreydwarfNest | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/GreyDwarfSpawner/Spawner_GreydwarfNest.prefab |
| Spawner_Hatchling | — | Characters/Hatchling | 3 components; active: yes | c4210710 / Assets/Characters/Hatchling/Spawner_Hatchling.prefab |
| Spawner_Hen | — | Characters/Chicken | 3 components; active: yes | c4210710 / Assets/Characters/Chicken/Spawner_Hen.prefab |
| Spawner_Hole | — | Characters/Elaking | 7 components; active: yes | c4210710 / Assets/Characters/Elaking/Spawner_Hole.prefab |
| Spawner_Hole_double | — | Characters/Elaking | 6 components; active: yes | c4210710 / Assets/Characters/Elaking/Spawner_Hole_double.prefab |
| Spawner_imp | — | Characters/Surtling | 3 components; active: yes | c4210710 / Assets/Characters/Surtling/Spawner_imp.prefab |
| Spawner_imp_respawn | — | Characters/Surtling | 3 components; active: yes | c4210710 / Assets/Characters/Surtling/Spawner_imp_respawn.prefab |
| Spawner_JotunDualWield | — | Characters/Jotnar | 3 components; active: yes | c4210710 / Assets/Characters/Jotnar/Spawner_JotunDualWield.prefab |
| Spawner_JotunWarrior | — | Characters/Jotnar | 3 components; active: yes | c4210710 / Assets/Characters/Jotnar/Spawner_JotunWarrior.prefab |
| Spawner_JotunWitch | — | Characters/Jotnar | 3 components; active: yes | c4210710 / Assets/Characters/Jotnar/Spawner_JotunWitch.prefab |
| Spawner_Kvastur | — | Characters/Draugr | 3 components; active: yes | c4210710 / Assets/Characters/Draugr/Spawner_Kvastur.prefab |
| Spawner_Leech_cave | — | Characters/Leech | 3 components; active: yes | c4210710 / Assets/Characters/Leech/Spawner_Leech_cave.prefab |
| Spawner_Location_Elite | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Spawner_Location_Elite.prefab |
| Spawner_Location_Greydwarf | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Spawner_Location_Greydwarf.prefab |
| Spawner_Location_Shaman | — | Characters/GreyDwarf | 3 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/Spawner_Location_Shaman.prefab |
| Spawner_Morgen | — | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/Spawner_Morgen.prefab |
| Spawner_Morgen_wakeup | — | Characters/Morgen | 3 components; active: yes | c4210710 / Assets/Characters/Morgen/Spawner_Morgen_wakeup.prefab |
| Spawner_Seeker | — | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/Spawner_Seeker.prefab |
| Spawner_Seeker_respawn_240 | — | Characters/Seeker | 3 components; active: yes | c4210710 / Assets/Characters/Seeker/Spawner_Seeker_respawn_240.prefab |
| Spawner_SeekerBrute | — | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/Spawner_SeekerBrute.prefab |
| Spawner_SeekerBrute_respawn_240 | — | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/Spawner_SeekerBrute_respawn_240.prefab |
| Spawner_ShadowPerson | — | Characters/Goblin | 3 components; active: yes | c4210710 / Assets/Characters/Goblin/Spawner_ShadowPerson.prefab |
| Spawner_Skeleton | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton.prefab |
| Spawner_Skeleton_hildir | — | Characters/Skeleton | 4 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_hildir.prefab |
| Spawner_Skeleton_hildir_bossroom | — | Characters/Skeleton | 4 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_hildir_bossroom.prefab |
| Spawner_Skeleton_Meadows | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_Meadows.prefab |
| Spawner_Skeleton_Meadows_night_noarcher | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_Meadows_night_noarcher.prefab |
| Spawner_Skeleton_Mountains | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_Mountains.prefab |
| Spawner_Skeleton_Mountains_night_noarcher | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_Mountains_night_noarcher.prefab |
| Spawner_Skeleton_night_noarcher | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_night_noarcher.prefab |
| Spawner_Skeleton_poison | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_poison.prefab |
| Spawner_Skeleton_respawn_30 | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_respawn_30.prefab |
| Spawner_Skeleton_rise | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_rise.prefab |
| Spawner_Skeleton_Swamp | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_Swamp.prefab |
| Spawner_Skeleton_Swamp_night_noarcher | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/Spawner_Skeleton_Swamp_night_noarcher.prefab |
| Spawner_StoneGolem | — | Characters/StoneGolem | 3 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Spawner_StoneGolem.prefab |
| Spawner_Tick | — | Characters/Tick | 3 components; active: yes | c4210710 / Assets/Characters/Tick/Spawner_Tick.prefab |
| Spawner_Tick_stared | — | Characters/Tick | 3 components; active: yes | c4210710 / Assets/Characters/Tick/Spawner_Tick_stared.prefab |
| Spawner_Tick_stared_respawn_240 | — | Characters/Tick | 3 components; active: yes | c4210710 / Assets/Characters/Tick/Spawner_Tick_stared_respawn_240.prefab |
| Spawner_Troll | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/Spawner_Troll.prefab |
| Spawner_TrollFrost | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/Spawner_TrollFrost.prefab |
| Spawner_Twitcher | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/Spawner_Twitcher.prefab |
| Spawner_Ulv | — | Characters/Ulv | 3 components; active: yes | c4210710 / Assets/Characters/Ulv/Spawner_Ulv.prefab |
| Spawner_Volture | — | Characters/Volture | 3 components; active: yes | c4210710 / Assets/Characters/Volture/Spawner_Volture.prefab |
| Spawner_Wraith | — | Characters/Wraith | 3 components; active: yes | c4210710 / Assets/Characters/Wraith/Spawner_Wraith.prefab |
| Spawner_Writhan | — | Characters/Writhan | 3 components; active: yes | c4210710 / Assets/Characters/Writhan/Spawner_Writhan.prefab |
| SpawnPlatform | — | world/Props | 4 components; active: yes | d59cfac / Assets/world/Props/SpawnPlatform.prefab |
| SpearBronze | Bronze Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearBronze.prefab |
| SpearCarapace | Carapace Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearCarapace.prefab |
| SpearChitin | Abyssal Harpoon | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearChitin.prefab |
| SpearElderbark | Ancient Bark Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearElderbark.prefab |
| SpearFlint | Flint Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearFlint.prefab |
| SpearGold | Nord Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearGold.prefab |
| SpearGold_BloodLightning | Thunderblood Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearGold_BloodLightning.prefab |
| SpearGold_FrostFire | Frostfire Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearGold_FrostFire.prefab |
| SpearGoldUncooked | Cast: Nord Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearGoldUncooked.prefab |
| SpearSplitner | Splitnir | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearSplitner.prefab |
| SpearSplitner_Blood | Splitnir the Bleeding | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearSplitner_Blood.prefab |
| SpearSplitner_Lightning | Splitnir the Storming | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearSplitner_Lightning.prefab |
| SpearSplitner_Nature | Splitnir the Primal | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearSplitner_Nature.prefab |
| SpearWolfFang | Fang Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearWolfFang.prefab |
| SpearWood | Wooden Spear | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SpearWood.prefab |
| SpiceAshlands | Fiery Spice Powder | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SpiceAshlands.prefab |
| SpiceDeepNorth | Seasoning of the Gourd | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SpiceDeepNorth.prefab |
| SpiceForests | Woodland Herb Blend | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SpiceForests.prefab |
| SpiceMistlands | Herbs of the Hidden Hills | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SpiceMistlands.prefab |
| SpiceMountains | Mountain Peak Pepper Powder | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SpiceMountains.prefab |
| SpiceOceans | Seafarer&#x27;s Herbs | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SpiceOceans.prefab |
| SpicePlains | Grasslands Herbalist Harvest | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SpicePlains.prefab |
| SpicyMarmalade | Spicy Marmalade | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/SpicyMarmalade.prefab |
| spiritbjorn_bite | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/spiritbjorn_bite.prefab |
| spiritbjorn_claws | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/spiritbjorn_claws.prefab |
| spiritbjorn_slam | slap | Characters/Bjorn | 3 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/spiritbjorn_slam.prefab |
| spiritbjorn_swipe_combo | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/spiritbjorn_swipe_combo.prefab |
| spiritbjorn_swipe_l | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/spiritbjorn_swipe_l.prefab |
| spiritbjorn_swipe_r | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/spiritbjorn_swipe_r.prefab |
| spiritboar_base_attack | boar attack1 | Characters/Boar | 3 components; active: yes | c4210710 / Assets/Characters/Boar/attacks/spiritboar_base_attack.prefab |
| spiritmoose_hooves | moose horns | Characters/moose | 2 components; active: yes | c4210710 / Assets/Characters/moose/attacks/spiritmoose_hooves.prefab |
| spiritmoose_horns | moose horns | Characters/moose | 2 components; active: yes | c4210710 / Assets/Characters/moose/attacks/spiritmoose_horns.prefab |
| spiritmoose_horns_sweep | moose horns | Characters/moose | 2 components; active: yes | c4210710 / Assets/Characters/moose/attacks/spiritmoose_horns_sweep.prefab |
| SpiritWolf_Attack1 | WolfAttack1 | Characters/Wolf | 3 components; active: yes | c4210710 / Assets/Characters/Wolf/misc/SpiritWolf_Attack1.prefab |
| SpiritWolf_Attack2 | WolfAttack2 | Characters/Wolf | 3 components; active: yes | c4210710 / Assets/Characters/Wolf/misc/SpiritWolf_Attack2.prefab |
| SpiritWolf_Attack3 | WolfAttack3 | Characters/Wolf | 3 components; active: yes | c4210710 / Assets/Characters/Wolf/misc/SpiritWolf_Attack3.prefab |
| SplitDialog | — | UI/prefabs | 4 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/SplitDialog.prefab |
| staff_clusterbombstaff_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_clusterbombstaff_projectile.prefab |
| staff_clusterbombstaff_splinter_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_clusterbombstaff_splinter_projectile.prefab |
| staff_fireball_projectile | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_fireball_projectile.prefab |
| staff_FrostOrbs_aoe | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_FrostOrbs_aoe.prefab |
| staff_FrostOrbs_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_FrostOrbs_projectile.prefab |
| staff_greenroots_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_greenroots_projectile.prefab |
| staff_greenroots_spawn | — | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_greenroots_spawn.prefab |
| staff_greenroots_tentaroot | Summoned Root | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_greenroots_tentaroot.prefab |
| staff_greenroots_tentaroot_attack | Dragur axe | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_greenroots_tentaroot_attack.prefab |
| staff_iceshard_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_iceshard_projectile.prefab |
| staff_lightning_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_lightning_projectile.prefab |
| staff_OrbofAhri_aoe | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_OrbofAhri_aoe.prefab |
| staff_OrbofAhri_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_OrbofAhri_projectile.prefab |
| staff_OrbofAhri_projectile_return | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_OrbofAhri_projectile_return.prefab |
| staff_redtroll_aoe | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_redtroll_aoe.prefab |
| staff_redtroll_spawn | — | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_redtroll_spawn.prefab |
| staff_shield_aoe | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_shield_aoe.prefab |
| staff_skeleton_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_skeleton_projectile.prefab |
| staff_skeleton_spawn | — | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_skeleton_spawn.prefab |
| staff_SpiritCaller_spawn | — | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_SpiritCaller_spawn.prefab |
| staff_thunderblood_aoe | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_thunderblood_aoe.prefab |
| staff_thunderblood_projectile | — | GameElements/Items | 4 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/staff_thunderblood_projectile.prefab |
| StaffClusterbomb | Staff of Fracturing | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffClusterbomb.prefab |
| StaffFireball | Staff of Embers | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffFireball.prefab |
| StaffFrostOrbs | Northern Vengeance | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffFrostOrbs.prefab |
| StaffFrostOrbsUncooked | Cast: Northern Vengeance | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffFrostOrbsUncooked.prefab |
| StaffGreenRoots | Staff of the Wild | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffGreenRoots.prefab |
| StaffIceShards | Staff of Frost | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffIceShards.prefab |
| StaffLightning | Dundr | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffLightning.prefab |
| StaffOrbofAhri | Echo Spike | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffOrbofAhri.prefab |
| StaffOrbofAhriUncooked | Cast: Echo Spike | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffOrbofAhriUncooked.prefab |
| StaffRedTroll | Trollstav | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffRedTroll.prefab |
| StaffShield | Staff of Protection | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffShield.prefab |
| StaffSkeleton | Dead Raiser | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffSkeleton.prefab |
| StaffSpiritCaller | Spirit Caller | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffSpiritCaller.prefab |
| StaffSpiritCallerUncooked | Cast: Spirit Caller | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffSpiritCallerUncooked.prefab |
| StaffThunderBlood | Lightning Strike | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffThunderBlood.prefab |
| StaffThunderbloodUncooked | Cast: Lightning Strike | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/StaffThunderbloodUncooked.prefab |
| stake_wall | Stakewall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stake_wall.prefab |
| StaminaUpgrade_Greydwarf | Stamina Greydwarf | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/StaminaUpgrade_Greydwarf.prefab |
| StaminaUpgrade_Troll | Stamina Troll | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/StaminaUpgrade_Troll.prefab |
| StaminaUpgrade_Wraith | Stamina Wraith | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/StaminaUpgrade_Wraith.prefab |
| StartGui | — | UI/prefabs | Not decoded (root properties unavailable) | b8689a71 / Assets/UI/prefabs/StartGui/StartGui.prefab |
| StartGui_AddServer | — | UI/prefabs | 3 components; active: no | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_AddServer.prefab |
| StartGui_BoardgameButton | — | UI/prefabs | 1 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_BoardgameButton.prefab |
| StartGui_BottomLeftButtons | — | UI/prefabs | 3 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_BottomLeftButtons.prefab |
| StartGui_CharacterSelection | — | UI/prefabs | 1 components; active: no | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_CharacterSelection.prefab |
| StartGui_ConnectionFailed | — | UI/prefabs | 3 components; active: no | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_ConnectionFailed.prefab |
| StartGui_Credits | — | UI/prefabs | 1 components; active: yes | c4210710 / Assets/UI/prefabs/StartGui/StartGui_Credits.prefab |
| StartGui_EULA | — | UI/prefabs | 7 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui_EULA.prefab |
| StartGui_ManageSavesMenu | — | UI/prefabs | 4 components; active: no | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_ManageSavesMenu.prefab |
| StartGui_Menu | — | UI/prefabs | 3 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_Menu.prefab |
| StartGui_MenuCinematics | — | UI/prefabs | 3 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_MenuCinematics.prefab |
| StartGui_MerchButton | — | UI/prefabs | 1 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_MerchButton.prefab |
| StartGui_ServerOptions | — | UI/prefabs | Not decoded (root properties unavailable) | c4210710 / Assets/UI/prefabs/StartGui/StartGui_ServerOptions.prefab |
| StartGui_StartGame | — | UI/prefabs | 2 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui/StartGui_StartGame.prefab |
| StartPlatform | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/StartTemple/StartPlatform.prefab |
| StartTemple | — | world/Locations | 2 components; active: yes | 1e488b5 / Assets/world/Locations/Meadows/StartTemple.prefab |
| StatueCorgi | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Statues/StatueCorgi.prefab |
| StatueDeer | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Statues/StatueDeer.prefab |
| StatueEvil | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/Statues/StatueEvil.prefab |
| StatueFreya | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Statues_Thor_Freya/StatueFreya.prefab |
| StatueFreya_broken_left | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Statues_Thor_Freya/StatueFreya_broken_left.prefab |
| StatueFreya_broken_right | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Statues_Thor_Freya/StatueFreya_broken_right.prefab |
| StatueHare | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Statues/StatueHare.prefab |
| StatueSeed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Statues/StatueSeed.prefab |
| StatueThor | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Statues_Thor_Freya/StatueThor.prefab |
| StatueThor_broken_bottom | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Statues_Thor_Freya/StatueThor_broken_bottom.prefab |
| StatueThor_broken_top | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Statues_Thor_Freya/StatueThor_broken_top.prefab |
| stave_beam_26 | Timber Beam 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_beam_26.prefab |
| stave_beam_2m | Timber Beam 2m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_beam_2m.prefab |
| stave_beam_45 | Timber Beam 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_beam_45.prefab |
| stave_beam_4m | Timber Beam 4m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_beam_4m.prefab |
| stave_beam_67 | Timber Beam 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_beam_67.prefab |
| stave_deco_beam_26 | Decorated Timber Beam 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_deco_beam_26.prefab |
| stave_deco_beam_2m | Decorated Timber Beam 2m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_deco_beam_2m.prefab |
| stave_deco_beam_45 | Decorated Timber Beam 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_deco_beam_45.prefab |
| stave_deco_beam_67 | Decorated Timber Beam 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_deco_beam_67.prefab |
| stave_deco_pole_2m | Decorated Timber Pole 2m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_deco_pole_2m.prefab |
| stave_deco_wall_2x2 | Lathed Timber Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_deco_wall_2x2.prefab |
| stave_gate | Timberwood Gate | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_gate.prefab |
| stave_pole_2m | Timber Pole 2m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_pole_2m.prefab |
| stave_pole_4m | Timber Pole 4m | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_pole_4m.prefab |
| stave_wall_2x2 | Timber Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_wall_2x2.prefab |
| stave_wall_cross_26 | Timber Roof Cross 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_wall_cross_26.prefab |
| stave_wall_cross_45 | Timber Roof Cross 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_wall_cross_45.prefab |
| stave_wall_cross_67 | Timber Roof Cross 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stave_wall_cross_67.prefab |
| SteamDeckPSGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/SteamDeckPSGamepadMap.prefab |
| SteamDeckXboxGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/SteamDeckXboxGamepadMap.prefab |
| Stone | Stone | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Stone.prefab |
| Stone1_huge | — | world/Props | 5 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/Stone1_huge.prefab |
| Stone1_huge | — | world/Props | 5 components; active: yes | 6b7bb025 / Assets/world/Props/stone/Stone1_huge.prefab |
| Stone1_interior | — | world/Props | 6 components; active: yes | c8b1e6fc / Assets/world/Props/stone/Stone1_interior.prefab |
| stone_arch | Stone Arch | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_arch.prefab |
| stone_fence | Stone Fence | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_fence.prefab |
| stone_floor | Stone Floor 4x4 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_floor.prefab |
| stone_floor_2x2 | Stone Floor 2x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_floor_2x2.prefab |
| stone_pile | Stone Pile | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_pile.prefab |
| stone_pillar | Stone Pillar | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_pillar.prefab |
| stone_stair | Stone Stair | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_stair.prefab |
| stone_wall_1x1 | Stone Wall 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_wall_1x1.prefab |
| stone_wall_1x1_ruin | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/stone_wall_1x1_ruin.prefab |
| stone_wall_2x1 | Stone Wall 2x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_wall_2x1.prefab |
| stone_wall_2x1_ruin | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/stone_wall_2x1_ruin.prefab |
| stone_wall_4x2 | Stone Wall 4x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/stone_wall_4x2.prefab |
| stone_wall_ruin | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/stone_wall_ruin.prefab |
| stone_wall_ruin_2 | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/stone_wall_ruin_2.prefab |
| Stoneblock | — | world/Props | 5 components; active: yes | 5f09202f / Assets/world/Props/stonepillar/Stoneblock.prefab |
| stoneblock_fracture | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/stonepillar/stoneblock_fracture.prefab |
| StoneblockSmall | — | world/Props | 5 components; active: yes | 5f09202f / Assets/world/Props/stonepillar/StoneblockSmall.prefab |
| stonechest | Stone box | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Chests/stonechest.prefab |
| StoneGolem | Stone Golem | Characters/StoneGolem | 11 components; active: yes | c4210710 / Assets/Characters/StoneGolem/StoneGolem.prefab |
| stonegolem_attack1_spike | Spike attack | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/stonegolem_attack1_spike.prefab |
| stonegolem_attack2_left_groundslam | One hand ground slam | Characters/StoneGolem | 3 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/stonegolem_attack2_left_groundslam.prefab |
| stonegolem_attack3_spikesweep | Spike sweep | Characters/StoneGolem | 3 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/stonegolem_attack3_spikesweep.prefab |
| stonegolem_attack_doublesmash | slap | Characters/StoneGolem | 3 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/stonegolem_attack_doublesmash.prefab |
| stonegolem_attack_sonicboom_NOTUSED | slap | Characters/StoneGolem | 3 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/stonegolem_attack_sonicboom_NOTUSED.prefab |
| StoneGolem_clubs | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/StoneGolem_clubs.prefab |
| StoneGolem_hat | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/StoneGolem_hat.prefab |
| Stonegolem_ragdoll | — | Characters/StoneGolem | 3 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/Stonegolem_ragdoll.prefab |
| StoneGolem_spikes | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/Misc/StoneGolem_spikes.prefab |
| StoneKit_ext_wall_2x2 | — | world/Props | 2 components; active: yes | 4a83d2b7 / Assets/world/Props/CastleBuildingKit/StoneKit_ext_wall_2x2.prefab |
| StoneKit_int_floor_2x2 | — | world/Props | 4 components; active: yes | 2d83afb1 / Assets/world/Props/CastleBuildingKit/StoneKit_int_floor_2x2.prefab |
| StonePillar | — | world/Props | 2 components; active: yes | 55ed7e7d / Assets/world/Props/stonepillar/StonePillar.prefab |
| StonePillar_mountain | — | world/Props | 1 components; active: yes | c57803a9 / Assets/world/Props/stonepillar/StonePillar_mountain.prefab |
| StonePillarTall | — | world/Props | 1 components; active: yes | 5f09202f / Assets/world/Props/stonepillar/StonePillarTall.prefab |
| StonePillarTall_mountain | — | world/Props | 1 components; active: yes | cea59785 / Assets/world/Props/stonepillar/StonePillarTall_mountain.prefab |
| StoneRock | Rock | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/StoneRock.prefab |
| StoneSlab | — | world/Props | 2 components; active: yes | c27cce3a / Assets/world/Props/stoneslab/StoneSlab.prefab |
| stonewall | — | world/Props | 3 components; active: yes | f41e610c / Assets/world/Props/stonewall/stonewall.prefab |
| stonewall_1 | — | world/Props | 3 components; active: yes | 577352c9 / Assets/world/Props/stonewall/stonewall_1.prefab |
| stonewall_2 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/stonewall/stonewall_2.prefab |
| stonewall_3 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/stonewall/stonewall_3.prefab |
| stubbe | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/stubbe/stubbe.prefab |
| stubbe_deepnorth | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/stubbe/stubbe_deepnorth.prefab |
| stubbe_spawner | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/stubbe/stubbe_spawner.prefab |
| StumpHole | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StumpHut/StumpHole.prefab |
| StumpHole_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StumpHut/StumpHole_destroyed.prefab |
| StumpHut | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/StumpHut/StumpHut.prefab |
| StumpHut_frac | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/StumpHut/StumpHut_frac.prefab |
| StumpLog | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/StumpHut/StumpLog.prefab |
| SulfurStone | Sulfur | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SulfurStone.prefab |
| sunken_crypt_gate | Iron Gate | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/Crypt/sunken_crypt_gate.prefab |
| SunkenKit_int_arch | — | world/Props | 2 components; active: yes | bdf7ccd3 / Assets/world/Props/CastleBuildingKit/SunkenKit_int_arch.prefab |
| SunkenKit_int_floor_2x2 | — | world/Props | 3 components; active: yes | ebdd9f85 / Assets/world/Props/CastleBuildingKit/SunkenKit_int_floor_2x2.prefab |
| SunkenKit_int_floor_4x4 | — | world/Props | 2 components; active: yes | 78af1e60 / Assets/world/Props/CastleBuildingKit/SunkenKit_int_floor_4x4.prefab |
| SunkenKit_int_stair | — | world/Props | 1 components; active: yes | 507d6273 / Assets/world/Props/CastleBuildingKit/SunkenKit_int_stair.prefab |
| SunkenKit_int_towerwall_LOD | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/CastleBuildingKit/SunkenKit_int_towerwall_LOD.prefab |
| SunkenKit_int_wall_1x2 | — | world/Props | 2 components; active: yes | 9e5274ca / Assets/world/Props/CastleBuildingKit/SunkenKit_int_wall_1x2.prefab |
| SunkenKit_int_wall_1x4 | — | world/Props | 2 components; active: yes | 5b5d26ec / Assets/world/Props/CastleBuildingKit/SunkenKit_int_wall_1x4.prefab |
| SunkenKit_int_wall_2x4 | — | world/Props | 2 components; active: yes | a353f557 / Assets/world/Props/CastleBuildingKit/SunkenKit_int_wall_2x4.prefab |
| SunkenKit_int_wall_4x4 | — | world/Props | 2 components; active: yes | 67966a64 / Assets/world/Props/CastleBuildingKit/SunkenKit_int_wall_4x4.prefab |
| SunkenKit_slope1x2 | — | world/Props | 1 components; active: yes | 5b5d26ec / Assets/world/Props/CastleBuildingKit/SunkenKit_slope1x2.prefab |
| SunkenKit_stair_corner_left | — | world/Props | 2 components; active: yes | 5b5d26ec / Assets/world/Props/CastleBuildingKit/SunkenKit_stair_corner_left.prefab |
| Surtling | Surtling | Characters/Surtling | 9 components; active: yes | c4210710 / Assets/Characters/Surtling/Surtling.prefab |
| SurtlingCore | Surtling Core | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/SurtlingCore.prefab |
| SwampTree1 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/SwampTree/SwampTree1.prefab |
| SwampTree1_log | — | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/SwampTree/logs/SwampTree1_log.prefab |
| SwampTree1_Stub | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/SwampTree/SwampTree1_Stub.prefab |
| SwampTree2 | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/SwampTree/SwampTree2.prefab |
| SwampTree2_darkland | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/SwampTree/SwampTree2_darkland.prefab |
| SwampTree2_log | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/SwampTree/SwampTree2_log.prefab |
| SwitchCursor | — | UI/prefabs | 5 components; active: yes | c4210710 / Assets/UI/prefabs/SwitchCursor.prefab |
| SwitchJoyCon2MouseGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/SwitchJoyCon2MouseGamepadMap.prefab |
| SwitchJoyconGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/SwitchJoyconGamepadMap.prefab |
| SwitchProGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/SwitchProGamepadMap.prefab |
| Sword2h_JotunWarrior | Club | Characters/Jotnar | 8 components; active: yes | c4210710 / Assets/Characters/Jotnar/model/weapons/Sword2h_JotunWarrior.prefab |
| SwordBlackmetal | Black Metal Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordBlackmetal.prefab |
| SwordBronze | Bronze Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordBronze.prefab |
| SwordCheat | Cheat sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordCheat.prefab |
| SwordDyrnwyn | Dyrnwyn | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordDyrnwyn.prefab |
| SwordGold | Nord Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordGold.prefab |
| SwordGold_BloodLightning | Thunderblood Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordGold_BloodLightning.prefab |
| SwordGold_FrostFire | Frostfire Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordGold_FrostFire.prefab |
| SwordGoldUncooked | Cast: Nord Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordGoldUncooked.prefab |
| SwordIron | Iron Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordIron.prefab |
| SwordIronFire | Dyrnwyn | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordIronFire.prefab |
| SwordMistwalker | Mistwalker | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordMistwalker.prefab |
| SwordNiedhogg | Nidhögg | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordNiedhogg.prefab |
| SwordNiedhoggBlood | Nidhögg the Bleeding | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordNiedhoggBlood.prefab |
| SwordNiedhoggLightning | Nidhögg the Thundering | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordNiedhoggLightning.prefab |
| SwordNiedhoggNature | Nidhögg the Primal | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordNiedhoggNature.prefab |
| SwordSilver | Silver Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordSilver.prefab |
| SwordWood | Wooden Sword | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/SwordWood.prefab |
| Tankard | Tankard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/Tankard.prefab |
| Tankard_dvergr | Dvergr Tankard | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/Tankard_dvergr.prefab |
| TankardAnniversary | Horn of Celebration | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/TankardAnniversary.prefab |
| TankardOdin | Mead Horn of Oden | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/TankardOdin.prefab |
| Tar | Tar | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Tar.prefab |
| TarLiquid | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Tar/TarLiquid.prefab |
| tarlump1 | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/tarlump1.prefab |
| tarlump1_frac | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/tarlump1_frac.prefab |
| Tendril | Tendril | Characters/FrozenKing | 9 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/Tendril.prefab |
| tendril_attack | Dragur axe | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/attacks/tendril_attack.prefab |
| Tendril_back | Root | Characters/FrozenKing | 9 components; active: yes | c4210710 / Assets/Characters/FrozenKing/Tendril_back.prefab |
| TentaRoot | Root | Characters/Greydwarf_king | 9 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/TentaRoot.prefab |
| tentaroot_attack | Dragur axe | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/misc/tentaroot_attack.prefab |
| TentaRoot_wild | Root | Characters/Greydwarf_king | 9 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/TentaRoots/TentaRoot_wild.prefab |
| TERRAIN_TEST | — | Misc | 1 components; active: yes | d59cfac / Assets/Misc/TERRAIN_TEST.prefab |
| TheHive | — | Characters/TheHive | 9 components; active: yes | c4210710 / Assets/Characters/TheHive/TheHive.prefab |
| Thistle | Thistle | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Thistle.prefab |
| Thor | — | Effects/thunder | 2 components; active: yes | d59cfac / Assets/Effects/thunder/Thor.prefab |
| ThrowItem | — | UI/prefabs | 4 components; active: yes | c4210710 / Assets/UI/prefabs/Radial/elements/ThrowItem.prefab |
| THSwordGold | Nord Greatsword | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordGold.prefab |
| THSwordGold_BloodLightning | Thunderblood Greatsword | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordGold_BloodLightning.prefab |
| THSwordGold_FrostFire | Frostfire Greatsword | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordGold_FrostFire.prefab |
| THSwordGoldUncooked | Cast: Nord Greatsword | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordGoldUncooked.prefab |
| THSwordKrom | Krom | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordKrom.prefab |
| THSwordSlayer | Slayer | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordSlayer.prefab |
| THSwordSlayerBlood | Brutal Slayer | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordSlayerBlood.prefab |
| THSwordSlayerLightning | Scourging Slayer | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordSlayerLightning.prefab |
| THSwordSlayerNature | Primal Slayer | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordSlayerNature.prefab |
| THSwordWood | Wooden Greatsword | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/THSwordWood.prefab |
| Thunderstone | Thunder Stone | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Thunderstone.prefab |
| Tick | Tick | Characters/Tick | 10 components; active: yes | c4210710 / Assets/Characters/Tick/Tick.prefab |
| tick_attack | boar attack1 | Characters/Tick | 3 components; active: yes | c4210710 / Assets/Characters/Tick/attacks/tick_attack.prefab |
| tick_attack_attach | boar attack1 | Characters/Tick | 3 components; active: yes | c4210710 / Assets/Characters/Tick/attacks/tick_attack_attach.prefab |
| Tin | Tin | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Tin.prefab |
| TinOre | Tin Ore | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/TinOre.prefab |
| tolroko_flyer | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/small_flyer/tolroko_flyer.prefab |
| Tooltip | — | UI/prefabs | 3 components; active: yes | c4210710 / Assets/UI/prefabs/Tooltip.prefab |
| TooltipWorldModifiers | — | UI/prefabs | 3 components; active: yes | b8689a71 / Assets/UI/prefabs/StartGui/TooltipWorldModifiers.prefab |
| TopLeftMessage | — | UI/prefabs | 4 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/TopLeftMessage.prefab |
| Torch | Torch | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/Torch.prefab |
| TorchMist | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/TorchMist.prefab |
| trader_wagon | — | world/Props | 1 components; active: yes | 84b014f6 / Assets/world/Props/vagon/trader_wagon.prefab |
| trader_wagon_destructable | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/vagon/trader_wagon_destructable.prefab |
| TraderChest_static | — | world/Props | 2 components; active: yes | 17a773de / Assets/world/Props/TraderChest/TraderChest_static.prefab |
| TraderLamp | — | world/Props | 1 components; active: yes | 17a773de / Assets/world/Props/TraderTent/TraderLamp.prefab |
| TraderRune | — | world/Props | 2 components; active: yes | c32ede71 / Assets/world/Props/TraderRune/TraderRune.prefab |
| TraderTent | — | world/Props | 1 components; active: yes | 17a773de / Assets/world/Props/TraderTent/TraderTent.prefab |
| Trailership | Longship | GameElements/Ships | 10 components; active: yes | c4210710 / Assets/GameElements/Ships/Trailership.prefab |
| TrainingDummy | TrainingDummy | Characters/TrainingDummy | 11 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/TrainingDummy.prefab |
| TrainingDummy_attack | dummy attack | Characters/TrainingDummy | 3 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/Attacks/TrainingDummy_attack.prefab |
| TrainingDummy_attack2 | dummy attack | Characters/TrainingDummy | 3 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/Attacks/TrainingDummy_attack2.prefab |
| TrainingDummy_attack3 | dummy attack | Characters/TrainingDummy | 3 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/Attacks/TrainingDummy_attack3.prefab |
| TrainingDummy_throw | dummy throw stone | Characters/TrainingDummy | 3 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/Attacks/TrainingDummy_throw.prefab |
| TrainingDummy_throw_projectile | — | Characters/TrainingDummy | 4 components; active: yes | c4210710 / Assets/Characters/TrainingDummy/Attacks/TrainingDummy_throw_projectile.prefab |
| treasure_pile | Coin Pile | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/treasure_pile.prefab |
| treasure_stack | Coin Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/treasure_stack.prefab |
| TreasureChest_ashland_stone | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_ashland_stone.prefab |
| TreasureChest_blackforest | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_blackforest.prefab |
| TreasureChest_charredfortress | Charred Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_charredfortress.prefab |
| TreasureChest_deepnorth_village | Chest | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_deepnorth_village.prefab |
| TreasureChest_dvergr_loose_stone | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_dvergr_loose_stone.prefab |
| TreasureChest_dvergrtower | Dvergr Treasure Chest; Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_dvergrtower.prefab |
| TreasureChest_dvergrtown | Dvergr Treasure Chest; Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_dvergrtown.prefab |
| TreasureChest_fCrypt | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_fCrypt.prefab |
| TreasureChest_forestcrypt | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_forestcrypt.prefab |
| TreasureChest_forestcrypt_hildir | Dvergr Treasure Chest; Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_forestcrypt_hildir.prefab |
| TreasureChest_heath | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_heath.prefab |
| TreasureChest_heath_hildir | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_heath_hildir.prefab |
| TreasureChest_meadows | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_meadows.prefab |
| TreasureChest_meadows_01 | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_meadows_01.prefab |
| TreasureChest_meadows_02 | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_meadows_02.prefab |
| TreasureChest_meadows_buried | Chest | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_meadows_buried.prefab |
| TreasureChest_meadows_combat | Chest | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_meadows_combat.prefab |
| TreasureChest_memorial_buried | Chest | GameElements/Items | 6 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_memorial_buried.prefab |
| TreasureChest_morkhalla | Jotun&#x27;s Chest; Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_morkhalla.prefab |
| TreasureChest_mountaincave | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_mountaincave.prefab |
| TreasureChest_mountaincave_hildir | Dvergr Treasure Chest; Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_mountaincave_hildir.prefab |
| TreasureChest_mountains | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_mountains.prefab |
| TreasureChest_plains_stone | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_plains_stone.prefab |
| TreasureChest_plainsfortress_hildir | Dvergr Treasure Chest; Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_plainsfortress_hildir.prefab |
| TreasureChest_sunkencrypt | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_sunkencrypt.prefab |
| TreasureChest_swamp | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_swamp.prefab |
| TreasureChest_trollcave | Chest | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/TreasureChest_trollcave.prefab |
| TriggerSpawner_Brood | — | Characters/SeekerQueen | 4 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/spawnhole/TriggerSpawner_Brood.prefab |
| TriggerSpawner_Seeker | — | Characters/SeekerQueen | 4 components; active: yes | c4210710 / Assets/Characters/SeekerQueen/spawnhole/TriggerSpawner_Seeker.prefab |
| TrinketBlackDamageHealth | Bracelets of the Brave | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketBlackDamageHealth.prefab |
| TrinketBlackStamina | Evasion Mantle | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketBlackStamina.prefab |
| TrinketBloodGoldHealth | Neckstabber | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketBloodGoldHealth.prefab |
| TrinketBloodGoldStamina | Witch Crown | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketBloodGoldStamina.prefab |
| TrinketBronzeHealth | Heart of the Forest | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketBronzeHealth.prefab |
| TrinketBronzeStamina | Bronze Pendant | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketBronzeStamina.prefab |
| TrinketCarapaceEitr | Pulsating Earrings | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketCarapaceEitr.prefab |
| TrinketChitinSwim | Fins of Destiny | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketChitinSwim.prefab |
| TrinketFlametalEitr | Jörmundling | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketFlametalEitr.prefab |
| TrinketFlametalStaminaHealth | Brimstone | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketFlametalStaminaHealth.prefab |
| TrinketIronHealth | Iron Brooch | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketIronHealth.prefab |
| TrinketIronStamina | Nimble Anklet | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketIronStamina.prefab |
| TrinketScaleStaminaDamage | Resounding Shackle | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketScaleStaminaDamage.prefab |
| TrinketSilverDamage | Wolf Sight | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketSilverDamage.prefab |
| TrinketSilverResist | Crystal Heart | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/Trinkets/TrinketSilverResist.prefab |
| Troll | Troll | Characters/Troll | 11 components; active: yes | c4210710 / Assets/Characters/Troll/Troll.prefab |
| troll_groundslam | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_groundslam.prefab |
| troll_groundslam_aoe | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_groundslam_aoe.prefab |
| troll_log_swing_h | LOG | Characters/Troll | 7 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_log_swing_h.prefab |
| troll_log_swing_v | LOG | Characters/Troll | 7 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_log_swing_v.prefab |
| troll_punch | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_punch.prefab |
| Troll_ragdoll | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/fx/Troll_ragdoll.prefab |
| Troll_sleeping | Troll | Characters/Troll | 11 components; active: yes | c4210710 / Assets/Characters/Troll/Troll_sleeping.prefab |
| Troll_Summoned | Summoned Troll | Characters/Troll | 12 components; active: yes | c4210710 / Assets/Characters/Troll/Troll_Summoned.prefab |
| troll_summoned_groundslam | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_summoned_groundslam.prefab |
| troll_summoned_groundslam_aoe | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_summoned_groundslam_aoe.prefab |
| troll_summoned_log_swing_h | LOG | Characters/Troll | 7 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_summoned_log_swing_h.prefab |
| troll_summoned_log_swing_v | LOG | Characters/Troll | 7 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_summoned_log_swing_v.prefab |
| troll_summoned_punch | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_summoned_punch.prefab |
| Troll_summoned_ragdoll | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/fx/Troll_summoned_ragdoll.prefab |
| troll_summoned_throw | fireballattack | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_summoned_throw.prefab |
| troll_summoned_throw_projectile | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_summoned_throw_projectile.prefab |
| troll_throw | fireballattack | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_throw.prefab |
| troll_throw_projectile | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/misc/troll_throw_projectile.prefab |
| TrollFrost | Gammeltroll | Characters/Troll | 11 components; active: yes | c4210710 / Assets/Characters/Troll/TrollFrost.prefab |
| TrollFrost_Dead | — | Characters/Troll | 6 components; active: yes | c4210710 / Assets/Characters/Troll/TrollFrost_Dead.prefab |
| TrollFrost_Frac | Petrified Gammeltroll | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/TrollFrost_Frac.prefab |
| TrollFrost_Frac_arm | Petrified Gammeltroll | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/TrollFrost_Frac_arm.prefab |
| TrollFrost_Frac_legs | Petrified Gammeltroll | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Rocks/TrollFrost_Frac_legs.prefab |
| TrollHide | Troll Hide | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/TrollHide.prefab |
| trollsnow_groundslam | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/trollsnow_groundslam.prefab |
| trollsnow_groundslam_aoe | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/trollsnow_groundslam_aoe.prefab |
| trollsnow_groundslam_r | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/trollsnow_groundslam_r.prefab |
| trollsnow_punch | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/trollsnow_punch.prefab |
| trollsnow_punch_r | slap | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/trollsnow_punch_r.prefab |
| Trollsnow_ragdoll | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/fx/Trollsnow_ragdoll.prefab |
| trollsnow_throw | fireballattack | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/misc/trollsnow_throw.prefab |
| trollsnow_throw_projectile | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/misc/trollsnow_throw_projectile.prefab |
| TrophyAbomination | Abomination Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyAbomination.prefab |
| TrophyAsksvin | Asksvin Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyAsksvin.prefab |
| TrophyBarka | Barka Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBarka.prefab |
| TrophyBjorn | Bear Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBjorn.prefab |
| TrophyBjornUndead | Vile Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBjornUndead.prefab |
| TrophyBlob | Blob Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBlob.prefab |
| TrophyBlob_Frost | Frost Blob Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBlob_Frost.prefab |
| TrophyBlob_Lava | Lava Blob Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBlob_Lava.prefab |
| TrophyBlob_Morkhalla | Pulp Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBlob_Morkhalla.prefab |
| TrophyBoar | Boar Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBoar.prefab |
| TrophyBonemass | Bonemass Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBonemass.prefab |
| TrophyBonemawSerpent | Bonemaw Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyBonemawSerpent.prefab |
| TrophyCharredArcher | Marksman Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyCharredArcher.prefab |
| TrophyCharredMage | Warlock Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyCharredMage.prefab |
| TrophyCharredMelee | Warrior Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyCharredMelee.prefab |
| TrophyCultist | Cultist Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyCultist.prefab |
| TrophyCultist_Hildir | Geirrhafa Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyCultist_Hildir.prefab |
| TrophyDeathsquito | Deathsquito Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDeathsquito.prefab |
| TrophyDeer | Deer Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDeer.prefab |
| TrophyDeerWhite | — | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDeerWhite.prefab |
| TrophyDragonQueen | Moder Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDragonQueen.prefab |
| TrophyDraugr | Draugr Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDraugr.prefab |
| TrophyDraugrElite | Draugr Elite Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDraugrElite.prefab |
| TrophyDraugrFem | Draugr Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDraugrFem.prefab |
| TrophyDvergr | Dvergr Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyDvergr.prefab |
| TrophyEikthyr | Eikthyr Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyEikthyr.prefab |
| TrophyElaking | Elaking Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyElaking.prefab |
| TrophyFader | Fader Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyFader.prefab |
| TrophyFallenValkyrie | Fallen Valkyrie Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyFallenValkyrie.prefab |
| TrophyFenring | Fenring Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyFenring.prefab |
| TrophyForestTroll | Troll Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyForestTroll.prefab |
| TrophyFrostTroll | Troll Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyFrostTroll.prefab |
| TrophyGhost | Ghost Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGhost.prefab |
| TrophyGjall | Gjall Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGjall.prefab |
| TrophyGoblin | Fuling Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGoblin.prefab |
| TrophyGoblinBrute | Fuling Berserker Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGoblinBrute.prefab |
| TrophyGoblinBruteBrosBrute | Thungr Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGoblinBruteBrosBrute.prefab |
| TrophyGoblinBruteBrosShaman | Zil Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGoblinBruteBrosShaman.prefab |
| TrophyGoblinKing | Yagluth Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGoblinKing.prefab |
| TrophyGoblinShaman | Fuling Shaman Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGoblinShaman.prefab |
| TrophyGreydwarf | Greydwarf Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGreydwarf.prefab |
| TrophyGreydwarfBrute | Greydwarf Brute Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGreydwarfBrute.prefab |
| TrophyGreydwarfShaman | Greydwarf Shaman Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGreydwarfShaman.prefab |
| TrophyGrowth | Growth Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyGrowth.prefab |
| TrophyHare | Hare Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyHare.prefab |
| TrophyHatchling | Drake Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyHatchling.prefab |
| TrophyJotunWarrior | Krigen Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyJotunWarrior.prefab |
| TrophyJotunWitch | Hexen Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyJotunWitch.prefab |
| TrophyKvastur | Kvastur | Characters/Kvastur | 8 components; active: yes | c4210710 / Assets/Characters/Kvastur/TrophyKvastur.prefab |
| TrophyLeech | Leech Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyLeech.prefab |
| TrophyLox | Lox Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyLox.prefab |
| TrophyMole | Eyeless One Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyMole.prefab |
| TrophyMoose | Moose Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyMoose.prefab |
| TrophyMorgen | Morgen Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyMorgen.prefab |
| TrophyNeck | Neck Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyNeck.prefab |
| TrophySeal | Seal Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySeal.prefab |
| TrophySeeker | Seeker Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySeeker.prefab |
| TrophySeekerBrute | Seeker Soldier Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySeekerBrute.prefab |
| TrophySeekerQueen | The Queen Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySeekerQueen.prefab |
| TrophySerpent | Serpent Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySerpent.prefab |
| TrophySGolem | Stone Golem Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySGolem.prefab |
| TrophySkeleton | Skeleton Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySkeleton.prefab |
| TrophySkeletonHildir | Brenna Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySkeletonHildir.prefab |
| TrophySkeletonPoison | Rancid Remains Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySkeletonPoison.prefab |
| TrophySurtling | Surtling Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophySurtling.prefab |
| TrophyTheElder | The Elder Trophy | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyTheElder.prefab |
| TrophyTick | Tick Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyTick.prefab |
| TrophyUlv | Ulv Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyUlv.prefab |
| TrophyVolture | Volture Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyVolture.prefab |
| TrophyWolf | Wolf Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyWolf.prefab |
| TrophyWraith | Wraith Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyWraith.prefab |
| TrophyWrithan | Writhan Trophy | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/trophies/TrophyWrithan.prefab |
| tunnel_web | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/webs/tunnel_web.prefab |
| turf_roof | Wood roof | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/turf_roof.prefab |
| turf_roof_top | Wood roof ridge | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/turf_roof_top.prefab |
| turf_roof_wall | Wood wall roof | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/old_roof/turf_roof_wall.prefab |
| Turnip | Turnip | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Turnip.prefab |
| TurnipSeeds | Turnip Seeds | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/TurnipSeeds.prefab |
| TurnipStew | Turnip Stew | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/TurnipStew.prefab |
| Turret_projectile | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/Turret_projectile.prefab |
| Turret_projectile_bloodgold | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/Turret_projectile_bloodgold.prefab |
| Turret_projectilebone | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Turret/Turret_projectilebone.prefab |
| TurretBolt | Black Metal Missile | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/TurretBolt.prefab |
| TurretBoltBloodgold | Bloodgold Missile | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/TurretBoltBloodgold.prefab |
| TurretBoltBone | — | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/TurretBoltBone.prefab |
| TurretBoltFlametal | Flametal Missile | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/TurretBoltFlametal.prefab |
| TurretBoltWood | Wooden Missile | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/TurretBoltWood.prefab |
| Tutorial | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/Tutorial.prefab |
| Ulv | Ulv | Characters/Ulv | 10 components; active: yes | c4210710 / Assets/Characters/Ulv/Ulv.prefab |
| Ulv_attack1_bite | Bite Attack | Characters/Ulv | 5 components; active: yes | c4210710 / Assets/Characters/Ulv/Attacks/Ulv_attack1_bite.prefab |
| Ulv_attack2_slash | Slash Attack | Characters/Ulv | 5 components; active: yes | c4210710 / Assets/Characters/Ulv/Attacks/Ulv_attack2_slash.prefab |
| Ulv_Ragdoll | — | Characters/Ulv | 3 components; active: yes | c4210710 / Assets/Characters/Ulv/Fx/Ulv_Ragdoll.prefab |
| Unbjorn | Vile | Characters/Bjorn | 11 components; active: yes | c4210710 / Assets/Characters/Bjorn/Unbjorn.prefab |
| unbjorn_bite | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/unbjorn_bite.prefab |
| unbjorn_claws | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/unbjorn_claws.prefab |
| Unbjorn_ragdoll | — | Characters/Bjorn | 4 components; active: yes | c4210710 / Assets/Characters/Bjorn/Unbjorn_ragdoll.prefab |
| unbjorn_slam | slap | Characters/Bjorn | 3 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/unbjorn_slam.prefab |
| unbjorn_swipe_combo | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/unbjorn_swipe_combo.prefab |
| unbjorn_swipe_l | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/unbjorn_swipe_l.prefab |
| unbjorn_swipe_r | bjorn bite | Characters/Bjorn | 5 components; active: yes | c4210710 / Assets/Characters/Bjorn/attacks/unbjorn_swipe_r.prefab |
| UndeadBjornRibcage | Vile Ribcage | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/UndeadBjornRibcage.prefab |
| UnifiedPopup | — | UI/prefabs | 6 components; active: yes | 8d5dbad8 / Assets/UI/prefabs/UnifiedPopup.prefab |
| UnlockAchievementPopup | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/UnlockAchievementPopup.prefab |
| UnlockMessageBase | — | UI/prefabs | 4 components; active: yes | d59cfac / Assets/UI/prefabs/IngameGui/UnlockMessageBase.prefab |
| UnstableLavaRock | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Rocks/model/UnstableLavaRock.prefab |
| UnstableLavaRock_explosion | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/BombSiege/UnstableLavaRock_explosion.prefab |
| Upgrader0Armor | Wooden Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader0Armor.prefab |
| Upgrader0Weapon | Wooden Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader0Weapon.prefab |
| Upgrader1Armor | Bronze Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader1Armor.prefab |
| Upgrader1Weapon | Bronze Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader1Weapon.prefab |
| Upgrader2Armor | Iron Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader2Armor.prefab |
| Upgrader2Weapon | Iron Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader2Weapon.prefab |
| Upgrader3Armor | Silver Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader3Armor.prefab |
| Upgrader3Weapon | Silver Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader3Weapon.prefab |
| Upgrader4Armor | Black Metal Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader4Armor.prefab |
| Upgrader4Weapon | Black Metal Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader4Weapon.prefab |
| Upgrader5Armor | Black Marble Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader5Armor.prefab |
| Upgrader5Weapon | Black Marble Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader5Weapon.prefab |
| Upgrader6Armor | Flametal Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader6Armor.prefab |
| Upgrader6Weapon | Flametal Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader6Weapon.prefab |
| Upgrader7Armor | Bloodgold Protection Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader7Armor.prefab |
| Upgrader7Weapon | Bloodgold Battle Idol | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/Upgrades/Upgrader7Weapon.prefab |
| UpgraderGlow | — | GameElements/Items | 2 components; active: yes | c4210710 / Assets/GameElements/Items/materials/_res/Upgrader/UpgraderGlow.prefab |
| UpgradeStation | Forge of Potential | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/UpgradeStation.prefab |
| ValheimRadial | — | UI/prefabs | 5 components; active: yes | d59cfac / Assets/UI/prefabs/Radial/ValheimRadial.prefab |
| Valkyrie | — | Characters/Valkyrie | 5 components; active: yes | c4210710 / Assets/Characters/Valkyrie/Valkyrie.prefab |
| Valkyrie_End | — | Characters/Valkyrie | 6 components; active: yes | c4210710 / Assets/Characters/Valkyrie/Valkyrie_End.prefab |
| veg_skull_Ashlands | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/veg_skull_Ashlands.prefab |
| Vegvisir_Bonemass | Vegvisir | world/Props | 4 components; active: yes | 4a26d414 / Assets/world/Props/RuneStones/Vegvisir_Bonemass.prefab |
| Vegvisir_DNBoss | Vegvisir | world/Props | 5 components; active: yes | cf482a9b / Assets/world/Props/RuneStones/Vegvisir_DNBoss.prefab |
| Vegvisir_DragonQueen | Vegvisir | world/Props | 4 components; active: yes | 1251bd53 / Assets/world/Props/RuneStones/Vegvisir_DragonQueen.prefab |
| Vegvisir_Eikthyr | Vegvisir | world/Props | 4 components; active: yes | 1e488b5 / Assets/world/Props/RuneStones/Vegvisir_Eikthyr.prefab |
| Vegvisir_Fader | Vegvisir | world/Props | 5 components; active: yes | 5e82feae / Assets/world/Props/RuneStones/Vegvisir_Fader.prefab |
| Vegvisir_GDKing | Vegvisir | world/Props | 4 components; active: yes | baf02216 / Assets/world/Props/RuneStones/Vegvisir_GDKing.prefab |
| Vegvisir_GoblinKing | Vegvisir | world/Props | 4 components; active: yes | 13b68f4c / Assets/world/Props/RuneStones/Vegvisir_GoblinKing.prefab |
| Vegvisir_placeofmystery | Vegvisir | world/Props | 5 components; active: yes | 1cee1f85 / Assets/world/Props/RuneStones/Vegvisir_placeofmystery.prefab |
| Vegvisir_placeofmystery_2 | Vegvisir | world/Props | 5 components; active: yes | ceeec7a8 / Assets/world/Props/RuneStones/Vegvisir_placeofmystery_2.prefab |
| Vegvisir_placeofmystery_3 | Vegvisir | world/Props | 5 components; active: yes | 7176ff77 / Assets/world/Props/RuneStones/Vegvisir_placeofmystery_3.prefab |
| Vegvisir_SeekerQueen | Vegvisir | world/Props | 4 components; active: yes | 48120de7 / Assets/world/Props/RuneStones/Vegvisir_SeekerQueen.prefab |
| VegvisirShard_Bonemass | Yagluth thing | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/misc/VegvisirShard_Bonemass.prefab |
| Vendor_BlackForest | — | world/Locations | 2 components; active: yes | 17a773de / Assets/world/Locations/BlackForest/Vendor_BlackForest.prefab |
| vertical_web | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/webs/vertical_web.prefab |
| vfx_ carrion_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vfx_ carrion_destroyed.prefab |
| vfx_arbalest_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/Arbalest/fx/vfx_arbalest_fire.prefab |
| vfx_archerytarget_bullseye | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ArcheryTarget/vfx/vfx_archerytarget_bullseye.prefab |
| vfx_archerytarget_bullseye_double | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ArcheryTarget/vfx/vfx_archerytarget_bullseye_double.prefab |
| vfx_archerytarget_bullseye_quint | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ArcheryTarget/vfx/vfx_archerytarget_bullseye_quint.prefab |
| vfx_ArcheryTarget_hit | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ArcheryTarget/vfx/vfx_ArcheryTarget_hit.prefab |
| vfx_arrowhit | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/vfx_arrowhit.prefab |
| vfx_Ash_Arch2_Broken1_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ash_Arch2_Broken1_destroyed.prefab |
| vfx_Ash_Arch2_Broken2_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ash_Arch2_Broken2_destroyed.prefab |
| vfx_ashland_gate_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vfx_ashland_gate_destruction.prefab |
| vfx_ashland_ruin_wall_windows_broken_4x6_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vfx_ashland_ruin_wall_windows_broken_4x6_destruction.prefab |
| vfx_ashland_wall_2x2_corner_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vfx_ashland_wall_2x2_corner_destruction.prefab |
| vfx_ashland_wall_2x2_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vfx_ashland_wall_2x2_destruction.prefab |
| vfx_Ashlands_HeatDistortion | — | Effects/weather | 4 components; active: yes | d59cfac / Assets/Effects/weather/ashlands/vfx_Ashlands_HeatDistortion.prefab |
| vfx_ashlandsbow_blood_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshFang/fx/vfx_ashlandsbow_blood_fire.prefab |
| vfx_ashlandsbow_lightning_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshFang/fx/vfx_ashlandsbow_lightning_fire.prefab |
| vfx_ashlandsbow_nature_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshFang/fx/vfx_ashlandsbow_nature_fire.prefab |
| vfx_ashlandslogdestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/fx/vfx_ashlandslogdestroyed.prefab |
| vfx_ashlandslogdestroyed_half | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/fx/vfx_ashlandslogdestroyed_half.prefab |
| vfx_ashlandstreecut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Trees/fx/vfx_ashlandstreecut.prefab |
| vfx_Ashpiece_roof_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashpiece_roof_destroyed.prefab |
| vfx_AshPieceDestroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_AshPieceDestroyed.prefab |
| vfx_Ashruin_steepstair_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_steepstair_destroyed.prefab |
| vfx_Ashruin_wall3_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_wall3_destroyed.prefab |
| vfx_Ashruin_wall4_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_wall4_destroyed.prefab |
| vfx_Ashruin_wall5_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_wall5_destroyed.prefab |
| vfx_Ashruin_window2_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_window2_destroyed.prefab |
| vfx_Ashruin_window3_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_window3_destroyed.prefab |
| vfx_Ashruin_window4_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_window4_destroyed.prefab |
| vfx_Ashruin_window5_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_window5_destroyed.prefab |
| vfx_Ashruin_window6_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Ashruin_window6_destroyed.prefab |
| vfx_aspect_summoned_prespawn | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/vfx_aspect_summoned_prespawn.prefab |
| vfx_auto_pickup | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_auto_pickup.prefab |
| vfx_bar_ancientmetal_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_ancientmetal_stack_destroyed.prefab |
| vfx_bar_blackmetal_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_blackmetal_stack_destroyed.prefab |
| vfx_bar_bronze_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_bronze_stack_destroyed.prefab |
| vfx_bar_copper_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_copper_stack_destroyed.prefab |
| vfx_bar_flametal_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_flametal_stack_destroyed.prefab |
| vfx_bar_gold_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_gold_stack_destroyed.prefab |
| vfx_bar_iron_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_iron_stack_destroyed.prefab |
| vfx_bar_silver_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_silver_stack_destroyed.prefab |
| vfx_bar_tin_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bar_tin_stack_destroyed.prefab |
| vfx_barley_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/barley/fx/vfx_barley_destroyed.prefab |
| vfx_barnacle_destroyed | — | Characters/Leviathan | 5 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/vfx_barnacle_destroyed.prefab |
| vfx_barnacle_hit | — | Characters/Leviathan | 3 components; active: yes | c4210710 / Assets/Characters/Leviathan/fx/vfx_barnacle_hit.prefab |
| vfx_barrle_destroyed | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/barrell/vfx_barrle_destroyed.prefab |
| vfx_beech_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Beech/fx/vfx_beech_cut.prefab |
| vfx_beech_small1_destroy | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Beech/fx/vfx_beech_small1_destroy.prefab |
| vfx_beech_small2_destroy | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Beech/fx/vfx_beech_small2_destroy.prefab |
| vfx_beechlog_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Beech/fx/vfx_beechlog_destroyed.prefab |
| vfx_beechlog_half_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Beech/fx/vfx_beechlog_half_destroyed.prefab |
| vfx_beehive_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/BeeHive/fx/vfx_beehive_destroyed.prefab |
| vfx_beehive_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/BeeHive/fx/vfx_beehive_hit.prefab |
| vfx_BigBlob_destroyed | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/vfx_BigBlob_destroyed.prefab |
| vfx_birch1_aut_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Birch/fx/vfx_birch1_aut_cut.prefab |
| vfx_birch1_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Birch/fx/vfx_birch1_cut.prefab |
| vfx_birch2_aut_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Birch/fx/vfx_birch2_aut_cut.prefab |
| vfx_birch2_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Birch/fx/vfx_birch2_cut.prefab |
| vfx_bjorn_groundslam | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/vfx_bjorn_groundslam.prefab |
| vfx_blackice_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/BlackIce/vfx_blackice_destroyed.prefab |
| vfx_blastfurance_addfuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/BlastFurnace/fx/vfx_blastfurance_addfuel.prefab |
| vfx_blastfurnace_addore | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/BlastFurnace/fx/vfx_blastfurnace_addore.prefab |
| vfx_blastfurnace_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/BlastFurnace/fx/vfx_blastfurnace_produce.prefab |
| vfx_blob_attack | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blob_attack.prefab |
| vfx_blob_death | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blob_death.prefab |
| vfx_blob_frost_attack | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blob_frost_attack.prefab |
| vfx_blob_frost_death | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blob_frost_death.prefab |
| vfx_blob_frost_hit | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blob_frost_hit.prefab |
| vfx_blob_hit | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blob_hit.prefab |
| vfx_blobelite_attack | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blobelite_attack.prefab |
| vfx_blobmork_attack | — | Characters/Blob | 3 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blobmork_attack.prefab |
| vfx_blobmork_death | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blobmork_death.prefab |
| vfx_blobmork_hit | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blobmork_hit.prefab |
| vfx_blobtar_death | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blobtar_death.prefab |
| vfx_blobtar_hit | — | Characters/Blob | 5 components; active: yes | c4210710 / Assets/Characters/Blob/fx/vfx_blobtar_hit.prefab |
| vfx_blocked | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_blocked.prefab |
| vfx_BloodDeath | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_BloodDeath.prefab |
| vfx_BloodHit | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_BloodHit.prefab |
| vfx_boar_birth | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/vfx_boar_birth.prefab |
| vfx_boar_death | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/vfx_boar_death.prefab |
| vfx_boar_hit | — | Characters/Boar | 5 components; active: yes | c4210710 / Assets/Characters/Boar/fx/vfx_boar_hit.prefab |
| vfx_boar_love | — | Characters/Boar | 3 components; active: yes | c4210710 / Assets/Characters/Boar/fx/vfx_boar_love.prefab |
| vfx_BombBlob_explode_frost | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/vfx_BombBlob_explode_frost.prefab |
| vfx_BombBlob_explode_lava | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/vfx_BombBlob_explode_lava.prefab |
| vfx_BombBlob_explode_morkhalla | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/vfx_BombBlob_explode_morkhalla.prefab |
| vfx_BombBlob_explode_poison | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/vfx_BombBlob_explode_poison.prefab |
| vfx_BombBlob_explode_poisonelite | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/vfx_BombBlob_explode_poisonelite.prefab |
| vfx_BombBlob_explode_tar | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bombooze/fx/vfx_BombBlob_explode_tar.prefab |
| vfx_bone_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_bone_stack_destroyed.prefab |
| vfx_BonemassDeath | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/vfx_BonemassDeath.prefab |
| vfx_BonemassHit | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/vfx_BonemassHit.prefab |
| vfx_bonemawserpent_death | — | Characters/BonemawSerpent | 5 components; active: yes | c4210710 / Assets/Characters/BonemawSerpent/fx/vfx_bonemawserpent_death.prefab |
| vfx_bonepile_destroyed | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_bonepile_destroyed.prefab |
| vfx_bones_pick | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/fx/vfx_bones_pick.prefab |
| vfx_bonfire_AddFuel | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Bonfire/vfx_bonfire_AddFuel.prefab |
| vfx_bonfire_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Bonfire/vfx_bonfire_destroyed.prefab |
| vfx_bow_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/fx/vfx_bow_fire.prefab |
| vfx_bowl_AddItem | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/bowl/fx/vfx_bowl_AddItem.prefab |
| vfx_BugRepellent | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_BugRepellent.prefab |
| vfx_Burning | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Burning.prefab |
| vfx_Burning_blue | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Burning_blue.prefab |
| vfx_Burning_green | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Burning_green.prefab |
| vfx_bush2_e_hit | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Bush01/fx/vfx_bush2_e_hit.prefab |
| vfx_bush2_en_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Bush01/fx/vfx_bush2_en_destroyed.prefab |
| vfx_bush_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Bush01/fx/vfx_bush_destroyed.prefab |
| vfx_bush_destroyed_heath | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Bush01/fx/vfx_bush_destroyed_heath.prefab |
| vfx_bush_leaf_puff | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Bush01/fx/vfx_bush_leaf_puff.prefab |
| vfx_bush_leaf_puff_heath | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Bush01/fx/vfx_bush_leaf_puff_heath.prefab |
| vfx_cartograpertable_write | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/CartographerTable/fx/vfx_cartograpertable_write.prefab |
| vfx_catapult_legdown | — | GameElements/Cart | 3 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/vfx/vfx_catapult_legdown.prefab |
| vfx_catapult_load | — | GameElements/Cart | 3 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/vfx/vfx_catapult_load.prefab |
| vfx_catapult_release | — | GameElements/Cart | 3 components; active: yes | c4210710 / Assets/GameElements/Cart/Catapult/vfx/vfx_catapult_release.prefab |
| vfx_changedcharacter | — | world/Menu | 4 components; active: yes | b8689a71 / Assets/world/Menu/vfx_changedcharacter.prefab |
| vfx_CharredBanner1_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CharredBanners/vfx_CharredBanner1_destroyed.prefab |
| vfx_CharredBanner2_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CharredBanners/vfx_CharredBanner2_destroyed.prefab |
| vfx_CharredBanner3_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/CharredBanners/vfx_CharredBanner3_destroyed.prefab |
| vfx_charredbanner_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/CharredBanners/vfx_charredbanner_destroyed.prefab |
| vfx_charredcross_spawner_destroyed | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/vfx_charredcross_spawner_destroyed.prefab |
| vfx_cloth_hanging_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_cloth_hanging_destroyed.prefab |
| vfx_clubhit | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/vfx_clubhit.prefab |
| vfx_CoalDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_CoalDestroyed.prefab |
| vfx_CoalHit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_CoalHit.prefab |
| vfx_coin_pile_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_coin_pile_destroyed.prefab |
| vfx_coin_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_coin_stack_destroyed.prefab |
| vfx_Cold | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Cold.prefab |
| vfx_ColdBall_Hit | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/vfx_ColdBall_Hit.prefab |
| vfx_ColdBall_launch | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/vfx_ColdBall_launch.prefab |
| vfx_cooking_station_transform | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Grill/fx/vfx_cooking_station_transform.prefab |
| vfx_corpse_destruction_large | — | Effects | 6 components; active: yes | c4210710 / Assets/Effects/vfx_corpse_destruction_large.prefab |
| vfx_corpse_destruction_medium | — | Effects | 6 components; active: yes | c4210710 / Assets/Effects/vfx_corpse_destruction_medium.prefab |
| vfx_corpse_destruction_small | — | Effects | 6 components; active: yes | c4210710 / Assets/Effects/vfx_corpse_destruction_small.prefab |
| vfx_crate_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_crate_destroyed.prefab |
| vfx_creature_soothed | — | Characters/character_effects | 3 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_creature_soothed.prefab |
| vfx_creep_hangingdetroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_creep_hangingdetroyed.prefab |
| vfx_crossbow_blood_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsCrossbow/fx/vfx_crossbow_blood_fire.prefab |
| vfx_crossbow_lightning_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsCrossbow/fx/vfx_crossbow_lightning_fire.prefab |
| vfx_crossbow_nature_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/AshlandsCrossbow/fx/vfx_crossbow_nature_fire.prefab |
| vfx_crow_death | — | Characters/animals | 3 components; active: yes | c4210710 / Assets/Characters/animals/birds/crow/fx/vfx_crow_death.prefab |
| vfx_crypt_skeleton_chest_destroyed | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_crypt_skeleton_chest_destroyed.prefab |
| vfx_damaged_cart | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/fx/vfx_damaged_cart.prefab |
| vfx_Damaged_Karve | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Damaged_Karve.prefab |
| vfx_Damaged_Raft | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Damaged_Raft.prefab |
| vfx_Damaged_VikingShip | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Damaged_VikingShip.prefab |
| vfx_darkland_groundfog | — | Effects | 2 components; active: yes | c4210710 / Assets/Effects/vfx_darkland_groundfog.prefab |
| vfx_deer_death | — | Characters/Deer | 5 components; active: yes | c4210710 / Assets/Characters/Deer/fx/vfx_deer_death.prefab |
| vfx_deer_hit | — | Characters/Deer | 5 components; active: yes | c4210710 / Assets/Characters/Deer/fx/vfx_deer_hit.prefab |
| vfx_Destroyed_AshlandsShip | — | GameElements/Ships | 3 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Destroyed_AshlandsShip.prefab |
| vfx_Destroyed_Karve | — | GameElements/Ships | 3 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Destroyed_Karve.prefab |
| vfx_Destroyed_Raft | — | GameElements/Ships | 3 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Destroyed_Raft.prefab |
| vfx_Destroyed_VikingShip | — | GameElements/Ships | 3 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Destroyed_VikingShip.prefab |
| vfx_Destroyed_VikingShip_frozen | — | GameElements/Ships | 3 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Destroyed_VikingShip_frozen.prefab |
| vfx_dragon_coldbreath | — | Characters/Dragon | 4 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/vfx_dragon_coldbreath.prefab |
| vfx_dragon_death | — | Characters/Dragon | 3 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/vfx_dragon_death.prefab |
| vfx_dragon_footstep | — | Characters/Dragon | 4 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/vfx_dragon_footstep.prefab |
| vfx_dragon_footstep_snow | — | Characters/Dragon | 4 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/vfx_dragon_footstep_snow.prefab |
| vfx_dragon_hurt | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/vfx_dragon_hurt.prefab |
| vfx_dragon_ice_hit | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/vfx_dragon_ice_hit.prefab |
| vfx_dragonegg_destroy | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/dragon/vfx_dragonegg_destroy.prefab |
| vfx_draugr_death | — | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/vfx_draugr_death.prefab |
| vfx_draugr_hit | — | Characters/Draugr | 5 components; active: yes | c4210710 / Assets/Characters/Draugr/fx/vfx_draugr_hit.prefab |
| vfx_draugrpile_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DraugrPileSpawner/fx/vfx_draugrpile_destroyed.prefab |
| vfx_draugrpile_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DraugrPileSpawner/fx/vfx_draugrpile_hit.prefab |
| vfx_DraugrSpawn | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/vfx_DraugrSpawn.prefab |
| vfx_dvergpost_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergpost_destroyed.prefab |
| vfx_dvergr_beam_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_beam_destroyed.prefab |
| vfx_dvergr_curtain_banner_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_curtain_banner_destroyed.prefab |
| vfx_dvergr_curtain_banner_destroyed_horisontal | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_curtain_banner_destroyed_horisontal.prefab |
| vfx_dvergr_pole_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_pole_destroyed.prefab |
| vfx_dvergr_stake_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_stake_destroyed.prefab |
| vfx_dvergr_stakewall_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_stakewall_destroyed.prefab |
| vfx_dvergr_wood_wall02_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_wood_wall02_destroyed.prefab |
| vfx_dvergr_wood_wall03_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_wood_wall03_destroyed.prefab |
| vfx_dvergr_wood_wall04_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergr_wood_wall04_destroyed.prefab |
| vfx_dvergrchair_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrchair_destroyed.prefab |
| vfx_dvergrcomponentcrate_destruction | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/vfx_dvergrcomponentcrate_destruction.prefab |
| vfx_dvergrcreep_beam_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrcreep_beam_destroyed.prefab |
| vfx_dvergrcreep_pole_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrcreep_pole_destroyed.prefab |
| vfx_dvergrcreep_support_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrcreep_support_destroyed.prefab |
| vfx_dvergrcreep_wood_wall02_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrcreep_wood_wall02_destroyed.prefab |
| vfx_dvergrcreep_wood_wall03_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrcreep_wood_wall03_destroyed.prefab |
| vfx_dvergrstool_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrstool_destroyed.prefab |
| vfx_dvergrtable_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Dvergr/fx/vfx_dvergrtable_destroyed.prefab |
| vfx_edge_clouds | — | Effects | 2 components; active: yes | c4210710 / Assets/Effects/vfx_edge_clouds.prefab |
| vfx_eikthyr_death | — | Characters/Eikthyr | 5 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/vfx_eikthyr_death.prefab |
| vfx_eikthyr_footstep | — | Characters/Eikthyr | 2 components; active: yes | c4210710 / Assets/Characters/Eikthyr/fx/vfx_eikthyr_footstep.prefab |
| vfx_ExtensionConnection | — | Effects | 1 components; active: yes | c4210710 / Assets/Effects/vfx_ExtensionConnection.prefab |
| vfx_ExtensionConnection_mage | — | Effects | 2 components; active: yes | c4210710 / Assets/Effects/vfx_ExtensionConnection_mage.prefab |
| vfx_FallenWarrior_death | — | Characters/FallenWarrior | 3 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/vfx_FallenWarrior_death.prefab |
| vfx_FallenWarrior_hit | — | Characters/FallenWarrior | 3 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/vfx_FallenWarrior_hit.prefab |
| vfx_fenring_cultist_death | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/vfx_fenring_cultist_death.prefab |
| vfx_fenring_cultist_hildir_death | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/vfx_fenring_cultist_hildir_death.prefab |
| vfx_fenring_death | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/vfx_fenring_death.prefab |
| vfx_fenring_hurt | — | Characters/Fenring | 5 components; active: yes | c4210710 / Assets/Characters/Fenring/fx/vfx_fenring_hurt.prefab |
| vfx_fenrirhide_hanging_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_fenrirhide_hanging_destroyed.prefab |
| vfx_fermenter_add | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/fermenter/fx/vfx_fermenter_add.prefab |
| vfx_fermenter_tap | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/fermenter/fx/vfx_fermenter_tap.prefab |
| vfx_FernAshlands_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Vegetation/vfx_FernAshlands_destroyed.prefab |
| vfx_FernAshlands_puff | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ashlands/Vegetation/vfx_FernAshlands_puff.prefab |
| vfx_fir_oldlog | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_fir_oldlog.prefab |
| vfx_FireAddFuel | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/firepit/vfx_FireAddFuel.prefab |
| vfx_FireballHit | — | Characters/Surtling | 5 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/vfx_FireballHit.prefab |
| vfx_firetree_regrow | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetree_regrow.prefab |
| vfx_firetreecut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetreecut.prefab |
| vfx_firetreecut_dead | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetreecut_dead.prefab |
| vfx_firetreecut_dead_abomination | — | Characters/Abomination | 4 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/vfx_firetreecut_dead_abomination.prefab |
| vfx_firetreecut_dead_snow | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetreecut_dead_snow.prefab |
| vfx_firetreecut_snow | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetreecut_snow.prefab |
| vfx_firetreecut_snow_FrostTrollDeath | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetreecut_snow_FrostTrollDeath.prefab |
| vfx_firetreecut_snow_FrostTrollThrow | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetreecut_snow_FrostTrollThrow.prefab |
| vfx_firetreecut_snow_small | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firetreecut_snow_small.prefab |
| vfx_FireWork_BlackCore | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/firepit/vfx_FireWork_BlackCore.prefab |
| vfx_Firework_Rocket | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Rocket.prefab |
| vfx_Firework_Rocket_Blue | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Rocket_Blue.prefab |
| vfx_Firework_Rocket_Cyan | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Rocket_Cyan.prefab |
| vfx_Firework_Rocket_Green | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Rocket_Green.prefab |
| vfx_Firework_Rocket_Purple | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Rocket_Purple.prefab |
| vfx_Firework_Rocket_Red | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Rocket_Red.prefab |
| vfx_Firework_Rocket_Yellow | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Rocket_Yellow.prefab |
| vfx_Firework_Sparkler | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/Fireworks/vfx_Firework_Sparkler.prefab |
| vfx_FireWork_SurtlingCore | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/firepit/vfx_FireWork_SurtlingCore.prefab |
| vfx_FireWork_ThunderStone | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/firepit/vfx_FireWork_ThunderStone.prefab |
| vfx_firlogdestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firlogdestroyed.prefab |
| vfx_firlogdestroyed_half | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_firlogdestroyed_half.prefab |
| vfx_FlameBall_launch | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/vfx_FlameBall_launch.prefab |
| vfx_flintpile_destroyed | — | Characters/Skeleton | 4 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_flintpile_destroyed.prefab |
| vfx_foresttroll_hit | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_foresttroll_hit.prefab |
| vfx_ForgeAddFuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/forge/vfx_ForgeAddFuel.prefab |
| vfx_Freezing | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Freezing.prefab |
| vfx_Frost | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Frost.prefab |
| vfx_frostarrow_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/fx/vfx_frostarrow_hit.prefab |
| vfx_frostcore_pick | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/fx/vfx_frostcore_pick.prefab |
| vfx_frostfoundry_transform | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostFoundry/vfx/vfx_frostfoundry_transform.prefab |
| vfx_frostkiln_addore | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostKiln/vfx/vfx_frostkiln_addore.prefab |
| vfx_frostkiln_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/FrostKiln/vfx/vfx_frostkiln_produce.prefab |
| vfx_FrostOrbs | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/shield/vfx_FrostOrbs.prefab |
| vfx_frosttroll_hit | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_frosttroll_hit.prefab |
| vfx_frozengd_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorthEnv/Frozen/fx/vfx_frozengd_destroyed.prefab |
| vfx_frozenking_blackice_destroyed | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/vfx_frozenking_blackice_destroyed.prefab |
| vfx_frozenking_death | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/vfx_frozenking_death.prefab |
| vfx_frozenking_final_death | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/vfx_frozenking_final_death.prefab |
| vfx_frozenking_final_death_ground | — | Characters/FrozenKing | 5 components; active: yes | c4210710 / Assets/Characters/FrozenKing/fx/vfx_frozenking_final_death_ground.prefab |
| vfx_gdking_projectile_hit | — | Characters/Greydwarf_king | 5 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/vfx_gdking_projectile_hit.prefab |
| vfx_gdking_stomp | — | Characters/Greydwarf_king | 6 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/vfx_gdking_stomp.prefab |
| vfx_ghost_death | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/vfx_ghost_death.prefab |
| vfx_ghost_hit | — | Characters/Ghost | 5 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/vfx_ghost_hit.prefab |
| vfx_ghost_spawn | — | Characters/Ghost | 3 components; active: yes | c4210710 / Assets/Characters/Ghost/fx/vfx_ghost_spawn.prefab |
| vfx_GiantMetal_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/vfx_GiantMetal_destroyed.prefab |
| vfx_gjall_spit | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/fx/vfx_gjall_spit.prefab |
| vfx_goblin_death | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/vfx_goblin_death.prefab |
| vfx_goblin_dn_death | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/vfx_goblin_dn_death.prefab |
| vfx_goblin_dn_hit | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/vfx_goblin_dn_hit.prefab |
| vfx_goblin_hit | — | Characters/Goblin | 5 components; active: yes | c4210710 / Assets/Characters/Goblin/fx/vfx_goblin_hit.prefab |
| vfx_goblin_woodwall_destroyed | — | world/dungeon | 5 components; active: yes | c4210710 / Assets/world/dungeon/goblicamp/GoblinVillage/effects/vfx_goblin_woodwall_destroyed.prefab |
| vfx_goblinbrute_death | — | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/vfx_goblinbrute_death.prefab |
| vfx_goblinbrute_hildir_death | — | Characters/GoblinBruteBros | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBruteBros/fx/vfx_goblinbrute_hildir_death.prefab |
| vfx_goblinbrute_hit | — | Characters/GoblinBrute | 5 components; active: yes | c4210710 / Assets/Characters/GoblinBrute/fx/vfx_goblinbrute_hit.prefab |
| vfx_goblinking_beam_OLD | — | Characters/GoblinKing | 4 components; active: yes | c4210710 / Assets/Characters/GoblinKing/fx/vfx_goblinking_beam_OLD.prefab |
| vfx_GoblinShield | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_GoblinShield.prefab |
| vfx_GodExplosion | — | Characters/Deer | 5 components; active: yes | c4210710 / Assets/Characters/Deer/fx/vfx_GodExplosion.prefab |
| vfx_grausten_stair_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_grausten_stair_destroyed.prefab |
| vfx_GraustenDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_GraustenDestroyed.prefab |
| vfx_GraustenDestroyed_large | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_GraustenDestroyed_large.prefab |
| vfx_greydwarf_death | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/vfx_greydwarf_death.prefab |
| vfx_greydwarf_elite_death | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/vfx_greydwarf_elite_death.prefab |
| vfx_greydwarf_hit | — | Characters/GreyDwarf | 5 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/vfx_greydwarf_hit.prefab |
| vfx_greydwarf_root_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GreyDwarfSpawner/fx/vfx_greydwarf_root_destroyed.prefab |
| vfx_greydwarf_shaman_pray | — | Characters/GreyDwarf | 6 components; active: yes | c4210710 / Assets/Characters/GreyDwarf/fx/vfx_greydwarf_shaman_pray.prefab |
| vfx_greydwarfnest_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GreyDwarfSpawner/fx/vfx_greydwarfnest_destroyed.prefab |
| vfx_greydwarfnest_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GreyDwarfSpawner/fx/vfx_greydwarfnest_hit.prefab |
| vfx_ground_fog | — | Effects | 3 components; active: yes | 90f7c60f / Assets/Effects/vfx_ground_fog.prefab |
| vfx_groundtorch_addFuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/walltorch/vfx_groundtorch_addFuel.prefab |
| vfx_guardstone_connection | — | GameElements/Pieces | 1 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/guardstone/vfx_guardstone_connection.prefab |
| vfx_GuckSackDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GuckSack/fx/vfx_GuckSackDestroyed.prefab |
| vfx_GuckSackHit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GuckSack/fx/vfx_GuckSackHit.prefab |
| vfx_GuckSackSmall_Destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/GuckSack/fx/vfx_GuckSackSmall_Destroyed.prefab |
| vfx_Harpooned | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Harpooned.prefab |
| vfx_hatchling_death | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/vfx_hatchling_death.prefab |
| vfx_hatchling_hurt | — | Characters/Hatchling | 5 components; active: yes | c4210710 / Assets/Characters/Hatchling/fx/vfx_hatchling_hurt.prefab |
| vfx_HealthUpgrade | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/healthupgrade/vfx_HealthUpgrade.prefab |
| vfx_HearthAddFuel | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/hearth/vfx_HearthAddFuel.prefab |
| vfx_HitSparks | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/vfx_HitSparks.prefab |
| vfx_hjall_spit_hit | — | Characters/Gjall | 5 components; active: yes | c4210710 / Assets/Characters/Gjall/fx/vfx_hjall_spit_hit.prefab |
| vfx_HoleSpawner_destruction | — | Characters/Elaking | 4 components; active: yes | c4210710 / Assets/Characters/Elaking/vfx_HoleSpawner_destruction.prefab |
| vfx_HoleSpawner_double_destruction | — | Characters/Elaking | 4 components; active: yes | c4210710 / Assets/Characters/Elaking/vfx_HoleSpawner_double_destruction.prefab |
| vfx_ice_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/fx/vfx_ice_destroyed.prefab |
| vfx_ice_destroyed_shelf | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/fx/vfx_ice_destroyed_shelf.prefab |
| vfx_ice_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/fx/vfx_ice_hit.prefab |
| vfx_iceblocker_destroyed | — | Characters/Dragon | 5 components; active: yes | c4210710 / Assets/Characters/Dragon/fx/vfx_iceblocker_destroyed.prefab |
| vfx_icecube_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Ice/fx/vfx_icecube_destroyed.prefab |
| vfx_ImpDeath | — | Characters/Surtling | 3 components; active: yes | c4210710 / Assets/Characters/Surtling/fx/vfx_ImpDeath.prefab |
| vfx_kiln_addore | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/charcoalkiln/fx/vfx_kiln_addore.prefab |
| vfx_kiln_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/charcoalkiln/fx/vfx_kiln_produce.prefab |
| vfx_LastBossGate_destroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/DeepNorth/LastBossGate/vfx_LastBossGate_destroyed.prefab |
| vfx_leech_death | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/vfx_leech_death.prefab |
| vfx_leech_hit | — | Characters/Leech | 5 components; active: yes | c4210710 / Assets/Characters/Leech/fx/vfx_leech_hit.prefab |
| vfx_lever | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/incinerator/fx/vfx_lever.prefab |
| vfx_LightFoot | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_LightFoot.prefab |
| vfx_lightningstaff_fire | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/staffs/fx/vfx_lightningstaff_fire.prefab |
| vfx_lootspawn | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/loot/fx/vfx_lootspawn.prefab |
| vfx_lox_groundslam | — | Characters/Lox | 5 components; active: yes | c4210710 / Assets/Characters/Lox/fx/vfx_lox_groundslam.prefab |
| vfx_lox_love | — | Characters/Lox | 3 components; active: yes | c4210710 / Assets/Characters/Lox/fx/vfx_lox_love.prefab |
| vfx_lox_soothed | — | Characters/Lox | 3 components; active: yes | c4210710 / Assets/Characters/Lox/fx/vfx_lox_soothed.prefab |
| vfx_MarbleDestroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_MarbleDestroyed.prefab |
| vfx_MarbleHit | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_MarbleHit.prefab |
| vfx_MeadBzerker | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_MeadBzerker.prefab |
| vfx_MeadHasty | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_MeadHasty.prefab |
| vfx_MeadSplash | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/_res/mead/fx/vfx_MeadSplash.prefab |
| vfx_MeadStrength | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_MeadStrength.prefab |
| vfx_MeadSwimmer | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_MeadSwimmer.prefab |
| vfx_MeadTamer | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_MeadTamer.prefab |
| vfx_mill_add | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/windmill/fx/vfx_mill_add.prefab |
| vfx_mill_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/windmill/fx/vfx_mill_produce.prefab |
| vfx_mistlands_mist | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/vfx_mistlands_mist.prefab |
| vfx_morgenhole_pile_destroyed | — | Characters/TheCharred | 3 components; active: yes | c4210710 / Assets/Characters/TheCharred/vfx_morgenhole_pile_destroyed.prefab |
| vfx_morkhalla_bench_destroyed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_bench_destroyed.prefab |
| vfx_morkhalla_firepit_destroyed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_firepit_destroyed.prefab |
| vfx_morkhalla_gatedoor02_destroyed | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_gatedoor02_destroyed.prefab |
| vfx_morkhalla_gatedoor03_destroyed | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_gatedoor03_destroyed.prefab |
| vfx_morkhalla_gatedoor_destroyed | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_gatedoor_destroyed.prefab |
| vfx_morkhalla_stool_destroyed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_stool_destroyed.prefab |
| vfx_morkhalla_table_destroyed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_table_destroyed.prefab |
| vfx_morkhalla_trainingdummy1_destroyed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_trainingdummy1_destroyed.prefab |
| vfx_morkhalla_trainingdummy2_destroyed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_trainingdummy2_destroyed.prefab |
| vfx_morkhalla_weaponstand_destroyed | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_weaponstand_destroyed.prefab |
| vfx_morkhalla_web_destroyed | — | world/Props | 2 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_morkhalla_web_destroyed.prefab |
| vfx_MorkhallaStatueDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Morkhalla/vfx_MorkhallaStatueDestroyed.prefab |
| vfx_mountainkit_chair_destroyed | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_mountainkit_chair_destroyed.prefab |
| vfx_mountainkit_table_destroyed | — | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_mountainkit_table_destroyed.prefab |
| vfx_MudDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MudPile/fx/vfx_MudDestroyed.prefab |
| vfx_MudHit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MudPile/fx/vfx_MudHit.prefab |
| vfx_neck_death | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/vfx_neck_death.prefab |
| vfx_neck_hit | — | Characters/Neck | 5 components; active: yes | c4210710 / Assets/Characters/Neck/fx/vfx_neck_hit.prefab |
| vfx_oak_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/oak/fx/vfx_oak_cut.prefab |
| vfx_oaklogdestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/oak/fx/vfx_oaklogdestroyed.prefab |
| vfx_oaklogdestroyed_half | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/oak/fx/vfx_oaklogdestroyed_half.prefab |
| vfx_obsidian_destroyed | — | Characters/Skeleton | 4 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_obsidian_destroyed.prefab |
| vfx_ocean_clouds | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/vfx_ocean_clouds.prefab |
| vfx_odin_despawn | — | Characters/Odin | 5 components; active: yes | c4210710 / Assets/Characters/Odin/vfx_odin_despawn.prefab |
| vfx_offering | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/vfx_offering.prefab |
| vfx_perfectblock | — | Characters/character_effects | 5 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_perfectblock.prefab |
| vfx_pick_wisp | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/WispLure/vfx_pick_wisp.prefab |
| vfx_pickable_pick | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/pickables/fx/vfx_pickable_pick.prefab |
| vfx_pinelogdestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/fx/vfx_pinelogdestroyed.prefab |
| vfx_pinelogdestroyed_half | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/fx/vfx_pinelogdestroyed_half.prefab |
| vfx_pinetree_regrow | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/fx/vfx_pinetree_regrow.prefab |
| vfx_pinetreecut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/fx/vfx_pinetreecut.prefab |
| vfx_pinetreecut_dead | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/fx/vfx_pinetreecut_dead.prefab |
| vfx_pinetreecut_snow | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/PineTreeOLD/fx/vfx_pinetreecut_snow.prefab |
| vfx_Place_bed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_bed.prefab |
| vfx_Place_beehive | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_beehive.prefab |
| vfx_Place_brazierceiling01 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_brazierceiling01.prefab |
| vfx_Place_cart | — | GameElements/Cart | 5 components; active: yes | c4210710 / Assets/GameElements/Cart/fx/vfx_Place_cart.prefab |
| vfx_Place_cauldron | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_cauldron.prefab |
| vfx_Place_charcoalkiln | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_charcoalkiln.prefab |
| vfx_Place_chest | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_chest.prefab |
| vfx_Place_cookingstation_iron | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_cookingstation_iron.prefab |
| vfx_Place_darkwood_gate | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_darkwood_gate.prefab |
| vfx_Place_digg | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_digg.prefab |
| vfx_Place_forge | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_forge.prefab |
| vfx_Place_HildirClothesRack | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/Effects/vfx_Place_HildirClothesRack.prefab |
| vfx_Place_HildirFabricRoll | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/Effects/vfx_Place_HildirFabricRoll.prefab |
| vfx_Place_HildirTableClothes | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/HildirWagon/Effects/vfx_Place_HildirTableClothes.prefab |
| vfx_Place_Karve | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Place_Karve.prefab |
| vfx_Place_mud_road | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_mud_road.prefab |
| vfx_Place_oven | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_oven.prefab |
| vfx_Place_portal | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_portal.prefab |
| vfx_Place_Raft | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Place_Raft.prefab |
| vfx_Place_raise | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_raise.prefab |
| vfx_Place_refinery | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_refinery.prefab |
| vfx_Place_replant | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_replant.prefab |
| vfx_Place_smallitem | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_smallitem.prefab |
| vfx_Place_smelter | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_smelter.prefab |
| vfx_Place_spinningwheel | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_spinningwheel.prefab |
| vfx_Place_stone_floor | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_stone_floor.prefab |
| vfx_Place_stone_floor_2x2 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_stone_floor_2x2.prefab |
| vfx_Place_stone_wall_2x1 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_stone_wall_2x1.prefab |
| vfx_Place_stone_wall_4x2 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_stone_wall_4x2.prefab |
| vfx_Place_throne02 | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_throne02.prefab |
| vfx_Place_turret | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_turret.prefab |
| vfx_Place_VikingShip | — | GameElements/Ships | 5 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_Place_VikingShip.prefab |
| vfx_Place_windmill | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_windmill.prefab |
| vfx_Place_wood_beam | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_beam.prefab |
| vfx_Place_wood_floor | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_floor.prefab |
| vfx_Place_wood_pole | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_pole.prefab |
| vfx_Place_wood_roof | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_roof.prefab |
| vfx_Place_wood_stair | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_stair.prefab |
| vfx_Place_wood_wall | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_wall.prefab |
| vfx_Place_wood_wall_half | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_wall_half.prefab |
| vfx_Place_wood_wall_roof | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_wood_wall_roof.prefab |
| vfx_Place_workbench | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_Place_workbench.prefab |
| vfx_player_death | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/fx/vfx_player_death.prefab |
| vfx_player_hit | — | Characters/Player | 5 components; active: yes | c4210710 / Assets/Characters/Player/fx/vfx_player_hit.prefab |
| vfx_Poison | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Poison.prefab |
| vfx_poisonarrow_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/bow/fx/vfx_poisonarrow_hit.prefab |
| vfx_Potion_eitr_minor | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Potion_eitr_minor.prefab |
| vfx_Potion_health_medium | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Potion_health_medium.prefab |
| vfx_Potion_stamina_medium | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Potion_stamina_medium.prefab |
| vfx_prespawn | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/vfx_prespawn.prefab |
| vfx_prespawn_fader | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/vfx_prespawn_fader.prefab |
| vfx_ProjectileHit | — | Characters/Bonemass | 5 components; active: yes | c4210710 / Assets/Characters/Bonemass/fx/vfx_ProjectileHit.prefab |
| vfx_raven_feathers | — | Characters/Raven | 4 components; active: yes | c4210710 / Assets/Characters/Raven/fx/vfx_raven_feathers.prefab |
| vfx_raven_land | — | Characters/Raven | 4 components; active: yes | c4210710 / Assets/Characters/Raven/fx/vfx_raven_land.prefab |
| vfx_RockDestroyed | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_RockDestroyed.prefab |
| vfx_RockDestroyed_large | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_RockDestroyed_large.prefab |
| vfx_RockDestroyed_marble | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_RockDestroyed_marble.prefab |
| vfx_RockDestroyed_Obsidian | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_RockDestroyed_Obsidian.prefab |
| vfx_RockHit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_RockHit.prefab |
| vfx_RockHit_Marble | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_RockHit_Marble.prefab |
| vfx_RockHit_Obsidian | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/MineRock/fx/vfx_RockHit_Obsidian.prefab |
| vfx_SawDust | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/vfx_SawDust.prefab |
| vfx_SawDust_abomination | — | Characters/Abomination | 5 components; active: yes | c4210710 / Assets/Characters/Abomination/fx/vfx_SawDust_abomination.prefab |
| vfx_SawDust_Ashlands | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/vfx_SawDust_Ashlands.prefab |
| vfx_seagull_death | — | Characters/animals | 3 components; active: yes | c4210710 / Assets/Characters/animals/birds/crow/fx/vfx_seagull_death.prefab |
| vfx_seal_hit | — | Characters/seal | 5 components; active: yes | c4210710 / Assets/Characters/seal/fx/vfx_seal_hit.prefab |
| vfx_seekerbrute_groundslam | — | Characters/SeekerBrute | 3 components; active: yes | c4210710 / Assets/Characters/SeekerBrute/fx/vfx_seekerbrute_groundslam.prefab |
| vfx_serpent_attack_trigger | — | Characters/Serpent | 3 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/vfx_serpent_attack_trigger.prefab |
| vfx_serpent_death | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/vfx_serpent_death.prefab |
| vfx_serpent_hurt | — | Characters/Serpent | 5 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/vfx_serpent_hurt.prefab |
| vfx_serpent_watersurface | — | Characters/Serpent | 2 components; active: yes | c4210710 / Assets/Characters/Serpent/fx/vfx_serpent_watersurface.prefab |
| vfx_ShadowPerson_death | — | Characters/FallenWarrior | 3 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/vfx_ShadowPerson_death.prefab |
| vfx_ShadowPerson_hit | — | Characters/FallenWarrior | 3 components; active: yes | c4210710 / Assets/Characters/FallenWarrior/fx/vfx_ShadowPerson_hit.prefab |
| vfx_shieldgenerator_refuel | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/vfx_shieldgenerator_refuel.prefab |
| vfx_shieldgenerator_startup | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/ShieldGenerator/vfx_shieldgenerator_startup.prefab |
| vfx_shrub_2_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Shrub02/fx/vfx_shrub_2_destroyed.prefab |
| vfx_shrub_2_heath_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Shrub02/fx/vfx_shrub_2_heath_destroyed.prefab |
| vfx_shrub_2_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Shrub02/fx/vfx_shrub_2_hit.prefab |
| vfx_shrub_heath_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Shrub02/fx/vfx_shrub_heath_hit.prefab |
| vfx_silvermace_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/SilverWarhammer/fx/vfx_silvermace_hit.prefab |
| vfx_skeleton_big_death | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_skeleton_big_death.prefab |
| vfx_skeleton_death | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_skeleton_death.prefab |
| vfx_skeleton_fire_death | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_skeleton_fire_death.prefab |
| vfx_skeleton_hit | — | Characters/Skeleton | 5 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_skeleton_hit.prefab |
| vfx_skeleton_mace_hit | — | Characters/Skeleton | 3 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_skeleton_mace_hit.prefab |
| vfx_skilllevelup | — | Characters/Player | 2 components; active: yes | c4210710 / Assets/Characters/Player/fx/vfx_skilllevelup.prefab |
| vfx_skullpile_destroyed | — | Characters/Skeleton | 4 components; active: yes | c4210710 / Assets/Characters/Skeleton/fx/vfx_skullpile_destroyed.prefab |
| vfx_sledge_hit | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/sledge/vfx_sledge_hit.prefab |
| vfx_sledge_iron_hit | — | GameElements/Items | 3 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/IronSledge/fx/vfx_sledge_iron_hit.prefab |
| vfx_Slimed | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Slimed.prefab |
| vfx_smelter_addfuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/smelter/fx/vfx_smelter_addfuel.prefab |
| vfx_smelter_addore | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/smelter/fx/vfx_smelter_addore.prefab |
| vfx_smelter_produce | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/smelter/fx/vfx_smelter_produce.prefab |
| vfx_Smoked | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Smoked.prefab |
| vfx_spawn | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/vfx_spawn.prefab |
| vfx_spawn_large | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/offeraltar/fx/vfx_spawn_large.prefab |
| vfx_spawn_small | — | Effects | 5 components; active: yes | c4210710 / Assets/Effects/vfx_spawn_small.prefab |
| vfx_spikey_beam_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vfx_spikey_beam_destruction.prefab |
| vfx_StaffShield | — | GameElements/StatusEffects | 4 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/shield/vfx_StaffShield.prefab |
| vfx_StaminaUpgrade | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/healthupgrade/vfx_StaminaUpgrade.prefab |
| vfx_standing_brazier_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_standing_brazier_destroyed.prefab |
| vfx_stone_floor_2x2_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_stone_floor_2x2_destroyed.prefab |
| vfx_stone_floor_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_stone_floor_destroyed.prefab |
| vfx_stone_stair_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_stone_stair_destroyed.prefab |
| vfx_stone_wall_4x2_destroyed | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_stone_wall_4x2_destroyed.prefab |
| vfx_stone_wall_ruin_2_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/vfx_stone_wall_ruin_2_destroyed.prefab |
| vfx_stone_wall_ruin_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/vfx_stone_wall_ruin_destroyed.prefab |
| vfx_stonegolem_attack_hit | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/vfx_stonegolem_attack_hit.prefab |
| vfx_stonegolem_death | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/vfx_stonegolem_death.prefab |
| vfx_stonegolem_footstep | — | Characters/StoneGolem | 4 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/vfx_stonegolem_footstep.prefab |
| vfx_stonegolem_footstep_snow | — | Characters/StoneGolem | 4 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/vfx_stonegolem_footstep_snow.prefab |
| vfx_stonegolem_hurt | — | Characters/StoneGolem | 5 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/vfx_stonegolem_hurt.prefab |
| vfx_stonegolem_wakeup | — | Characters/StoneGolem | 3 components; active: yes | c4210710 / Assets/Characters/StoneGolem/fx/vfx_stonegolem_wakeup.prefab |
| vfx_stubbe | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/stubbe/fx/vfx_stubbe.prefab |
| vfx_swamp_mist | — | Effects | 4 components; active: yes | c4210710 / Assets/Effects/vfx_swamp_mist.prefab |
| vfx_swamptree_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/SwampTree/fx/vfx_swamptree_cut.prefab |
| vfx_tar_surface | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_tar_surface.prefab |
| vfx_Tared | — | GameElements/StatusEffects | 6 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Tared.prefab |
| vfx_tentaroot_hit | — | Characters/Greydwarf_king | 3 components; active: yes | c4210710 / Assets/Characters/Greydwarf_king/fx/vfx_tentaroot_hit.prefab |
| vfx_torch_hit | — | GameElements/Items | 5 components; active: yes | c4210710 / Assets/GameElements/Items/weapons/_res/torch/vfx_torch_hit.prefab |
| vfx_TrainingDummy_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/TrainingDummy/vfx/vfx_TrainingDummy_destruction.prefab |
| vfx_TrainingDummy_hit | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/TrainingDummy/vfx/vfx_TrainingDummy_hit.prefab |
| vfx_tree_fall_hit | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/FirTree/fx/vfx_tree_fall_hit.prefab |
| vfx_troll_attack_hit | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_attack_hit.prefab |
| vfx_troll_death | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_death.prefab |
| vfx_troll_footstep | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_footstep.prefab |
| vfx_troll_footstep_water | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_footstep_water.prefab |
| vfx_troll_groundslam | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_groundslam.prefab |
| vfx_troll_log_hitground | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_log_hitground.prefab |
| vfx_troll_rock_destroyed | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_rock_destroyed.prefab |
| vfx_troll_summoned_death | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_troll_summoned_death.prefab |
| vfx_troll_summoned_prespawn | — | Characters/TrollSkeleton | 5 components; active: yes | c4210710 / Assets/Characters/TrollSkeleton/vfx/vfx_troll_summoned_prespawn.prefab |
| vfx_TrollFrost_Death | — | Characters/Troll | 3 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_TrollFrost_Death.prefab |
| vfx_TrollPheromones | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_TrollPheromones.prefab |
| vfx_trollsnow_attack_hit | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_trollsnow_attack_hit.prefab |
| vfx_trollsnow_footstep | — | Characters/Troll | 4 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_trollsnow_footstep.prefab |
| vfx_trollsnow_groundslam | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_trollsnow_groundslam.prefab |
| vfx_trollsnow_log_destroyed | — | Characters/Troll | 5 components; active: yes | c4210710 / Assets/Characters/Troll/fx/vfx_trollsnow_log_destroyed.prefab |
| vfx_turnip_grow | — | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/turnip/fx/vfx_turnip_grow.prefab |
| vfx_ulv_death | — | Characters/Ulv | 5 components; active: yes | c4210710 / Assets/Characters/Ulv/Fx/vfx_ulv_death.prefab |
| vfx_UndeadBurn | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_UndeadBurn.prefab |
| vfx_vines_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Vines/fx/vfx_vines_destroyed.prefab |
| vfx_wagon_destroyed | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/vagon/vfx_wagon_destroyed.prefab |
| vfx_walltorch_addFuel | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/walltorch/vfx_walltorch_addFuel.prefab |
| vfx_water_surface | — | Characters/character_effects | 4 components; active: yes | c4210710 / Assets/Characters/character_effects/vfx_water_surface.prefab |
| vfx_water_surface_fish | — | Characters/animals | 4 components; active: yes | c4210710 / Assets/Characters/animals/fishes/misc/vfx_water_surface_fish.prefab |
| vfx_WaterImpact_Karve | — | GameElements/Ships | 6 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_WaterImpact_Karve.prefab |
| vfx_WaterImpact_Raft | — | GameElements/Ships | 6 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_WaterImpact_Raft.prefab |
| vfx_WaterImpact_VikingShip | — | GameElements/Ships | 6 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_WaterImpact_VikingShip.prefab |
| vfx_watersplash_bathtub | — | GameElements/Pieces | 2 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_watersplash_bathtub.prefab |
| vfx_watersplash_karve | — | GameElements/Ships | 2 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_watersplash_karve.prefab |
| vfx_watersplash_longship | — | GameElements/Ships | 3 components; active: yes | c4210710 / Assets/GameElements/Ships/_res/fx/vfx_watersplash_longship.prefab |
| vfx_Wet | — | GameElements/StatusEffects | 3 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_Wet.prefab |
| vfx_WishbonePing | — | GameElements/StatusEffects | 5 components; active: yes | c4210710 / Assets/GameElements/StatusEffects/effects/vfx_WishbonePing.prefab |
| vfx_wolf_death | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/vfx_wolf_death.prefab |
| vfx_wolf_hit | — | Characters/Wolf | 5 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/vfx_wolf_hit.prefab |
| vfx_wood_black_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_wood_black_stack_destroyed.prefab |
| vfx_wood_core_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_wood_core_stack_destroyed.prefab |
| vfx_wood_fine_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_wood_fine_stack_destroyed.prefab |
| vfx_wood_frost_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_wood_frost_stack_destroyed.prefab |
| vfx_wood_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_wood_stack_destroyed.prefab |
| vfx_wood_yggdrasil_stack_destroyed | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/effects/vfx_wood_yggdrasil_stack_destroyed.prefab |
| vfx_wooden_path_destroyed | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/vfx_wooden_path_destroyed.prefab |
| vfx_wraith_death | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/vfx_wraith_death.prefab |
| vfx_wraith_hit | — | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/fx/vfx_wraith_hit.prefab |
| vfx_yggashoot_cut | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Shoots/fx/vfx_yggashoot_cut.prefab |
| vfx_yggashoot_small1_destroy | — | world/Props | 3 components; active: yes | c4210710 / Assets/world/Props/Shoots/fx/vfx_yggashoot_small1_destroy.prefab |
| VikingCupcake | Frosted Sweetbread | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/VikingCupcake.prefab |
| VikingCupcakeUncooked | Unbaked Sweetbread | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/VikingCupcakeUncooked.prefab |
| VikingShip | Longship | GameElements/Ships | 10 components; active: yes | c4210710 / Assets/GameElements/Ships/VikingShip.prefab |
| VikingShip_Ashlands | Drakkar | GameElements/Ships | 10 components; active: yes | c4210710 / Assets/GameElements/Ships/VikingShip_Ashlands.prefab |
| VineAsh | Vineberry Cluster | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Vines_Ashlands/VineAsh.prefab |
| VineAsh_sapling | Ashvine | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Vines_Ashlands/VineAsh_sapling.prefab |
| Vineberry | Vineberry Cluster | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/Vineberry.prefab |
| VineberrySeeds | Vineberry Seeds | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/Vines_Ashlands/VineberrySeeds.prefab |
| VineGreen | Vineberry Cluster | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Vines_Green/VineGreen.prefab |
| VineGreen_sapling | Ivy | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Vines_Green/VineGreen_sapling.prefab |
| VineGreenSeeds | Ivy Seeds | world/Props | 9 components; active: yes | c4210710 / Assets/world/Props/Vines_Green/VineGreenSeeds.prefab |
| vines | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/Vines/vines.prefab |
| Voidplasm | Ectoplasm | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Voidplasm.prefab |
| Volture | Volture | Characters/Volture | 9 components; active: yes | c4210710 / Assets/Characters/Volture/Volture.prefab |
| Volture_ragdoll | — | Characters/Volture | 3 components; active: yes | c4210710 / Assets/Characters/Volture/fx/Volture_ragdoll.prefab |
| volture_strawpile | — | Characters/Volture | 4 components; active: yes | c4210710 / Assets/Characters/Volture/volture_strawpile.prefab |
| volture_talons | Volture Talons | Characters/Volture | 5 components; active: yes | c4210710 / Assets/Characters/Volture/attacks/volture_talons.prefab |
| VoltureEgg | Volture Egg | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/VoltureEgg.prefab |
| VoltureMeat | Volture Meat | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/VoltureMeat.prefab |
| vx_ashland_pot1_green_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vx_ashland_pot1_green_destruction.prefab |
| vx_ashland_pot1_red_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vx_ashland_pot1_red_destruction.prefab |
| vx_ashland_pot2_green_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vx_ashland_pot2_green_destruction.prefab |
| vx_ashland_pot2_red_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vx_ashland_pot2_red_destruction.prefab |
| vx_ashland_pot3_green_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vx_ashland_pot3_green_destruction.prefab |
| vx_ashland_pot3_red_destruction | — | GameElements/Pieces | 3 components; active: yes | c4210710 / Assets/GameElements/Pieces/_res/Ashlands_Build/prefabs/vx_ashland_pot3_red_destruction.prefab |
| WallSnow1 | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/WallSnow1.prefab |
| WallSnow2 | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/WallSnow2.prefab |
| WallSnow3 | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/WallSnow3.prefab |
| WallSnow4 | — | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/WallSnow4.prefab |
| WaterCube_cave | — | world/dungeon | 1 components; active: yes | 944ddcad / Assets/world/dungeon/WaterCube_cave.prefab |
| WaterCube_sunkencrypt | — | world/dungeon | 1 components; active: yes | 147b47a2 / Assets/world/dungeon/WaterCube_sunkencrypt.prefab |
| waterflow | — | world/Props | 2 components; active: yes | e6b86a17 / Assets/world/Props/CryptKit/waterflow.prefab |
| WaterLiquid | — | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Tar/WaterLiquid.prefab |
| Waystone | — | world/Props | 3 components; active: yes | d59cfac / Assets/world/Props/Waystone/Waystone.prefab |
| widestone | — | world/Props | 3 components; active: yes | 98c14cfe / Assets/world/Props/DeepNorth/HotSpring/widestone.prefab |
| widestone | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/widestone.prefab |
| widestone_2 | — | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/widestone_2.prefab |
| widestone_2_frac | Rock | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/widestone_2_frac.prefab |
| widestone_frac | Rock | world/Props | 6 components; active: yes | c4210710 / Assets/world/Props/Rocks/widestone_frac.prefab |
| windmill | Windmill | GameElements/Pieces | 8 components; active: yes | c4210710 / Assets/GameElements/Pieces/windmill.prefab |
| Wishbone | Wishbone | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/utility/Wishbone.prefab |
| Wisp | Wisp | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Wisp.prefab |
| WitheredBone | Withered Bone | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/WitheredBone.prefab |
| Wolf | Wolf | Characters/Wolf | 12 components; active: yes | c4210710 / Assets/Characters/Wolf/Wolf.prefab |
| Wolf_Attack1 | WolfAttack1 | Characters/Wolf | 3 components; active: yes | c4210710 / Assets/Characters/Wolf/misc/Wolf_Attack1.prefab |
| Wolf_Attack2 | WolfAttack2 | Characters/Wolf | 3 components; active: yes | c4210710 / Assets/Characters/Wolf/misc/Wolf_Attack2.prefab |
| Wolf_Attack3 | WolfAttack3 | Characters/Wolf | 3 components; active: yes | c4210710 / Assets/Characters/Wolf/misc/Wolf_Attack3.prefab |
| Wolf_cub | Wolf Cub | Characters/Wolf | 10 components; active: yes | c4210710 / Assets/Characters/Wolf/Wolf_cub.prefab |
| Wolf_Ragdoll | — | Characters/Wolf | 4 components; active: yes | c4210710 / Assets/Characters/Wolf/fx/Wolf_Ragdoll.prefab |
| Wolf_spiritcaller | — | Characters/Wolf | 11 components; active: yes | c4210710 / Assets/Characters/Wolf/Wolf_spiritcaller.prefab |
| WolfClaw | Fenris Claw | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/WolfClaw.prefab |
| WolfFang | Wolf Fang | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/WolfFang.prefab |
| WolfHairBundle | Fenris Hair | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/WolfHairBundle.prefab |
| WolfJerky | Wolf Jerky | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/WolfJerky.prefab |
| WolfMeat | Wolf Meat | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/WolfMeat.prefab |
| WolfMeatSkewer | Wolf Skewer | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/WolfMeatSkewer.prefab |
| WolfPelt | Wolf Pelt | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/WolfPelt.prefab |
| WolfStatue | — | world/Props | 2 components; active: yes | d29ca153 / Assets/world/Props/WolfStatue/model/WolfStatue.prefab |
| Wood | Wood | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/Wood.prefab |
| wood_beam | Wood Beam 2 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_beam.prefab |
| wood_beam_1 | Wood Beam 1 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_beam_1.prefab |
| wood_beam_26 | Wood Beam 26° | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_beam_26.prefab |
| wood_beam_45 | Wood Beam 45° | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_beam_45.prefab |
| wood_beam_67 | Wood Beam 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_beam_67.prefab |
| wood_core_stack | Corewood Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_core_stack.prefab |
| wood_door | Wood Door | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_door.prefab |
| wood_dragon1 | Wood Dragon Adornment | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_dragon1.prefab |
| wood_fence | Roundpole Fence | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_fence.prefab |
| wood_fence_gate | Roundpole Gate | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_fence_gate.prefab |
| wood_fine_stack | Finewood Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_fine_stack.prefab |
| wood_floor | Wood Floor 2x2 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_floor.prefab |
| wood_floor_1x1 | Wood Floor 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_floor_1x1.prefab |
| wood_frost_stack | Timberwood Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_frost_stack.prefab |
| wood_gate | Wood Gate | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_gate.prefab |
| wood_ledge | Wood Ledge | GameElements/Pieces | 6 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_ledge.prefab |
| wood_log_26 | Log Beam 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_log_26.prefab |
| wood_log_45 | Log Beam 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_log_45.prefab |
| wood_log_67 | Log Beam 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_log_67.prefab |
| wood_pole | Wood Pole 1 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_pole.prefab |
| wood_pole2 | Wood Pole 2 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_pole2.prefab |
| wood_pole_log | Log Pole 2 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_pole_log.prefab |
| wood_pole_log_4 | Log Pole 4 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_pole_log_4.prefab |
| wood_pole_log_4_worn | Log Pole 4 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_pole_log_4_worn.prefab |
| wood_roof | Thatch Roof 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof.prefab |
| wood_roof_45 | Thatch Roof 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_45.prefab |
| wood_roof_67 | Thatch Roof 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_67.prefab |
| wood_roof_icorner | Thatch Roof Inner Corner 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_icorner.prefab |
| wood_roof_icorner_45 | Thatch Roof Inner Corner 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_icorner_45.prefab |
| wood_roof_icorner_67 | Thatch Roof Inner Corner 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_icorner_67.prefab |
| wood_roof_ocorner | Thatch Roof Outer Corner 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_ocorner.prefab |
| wood_roof_ocorner_45 | Thatch Roof Outer Corner 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_ocorner_45.prefab |
| wood_roof_ocorner_67 | Thatch Roof Outer Corner 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_ocorner_67.prefab |
| wood_roof_top | Thatch Roof Ridge 26° | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_top.prefab |
| wood_roof_top_45 | Thatch Roof Ridge 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_top_45.prefab |
| wood_roof_top_67 | Thatch Roof Ridge 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_roof_top_67.prefab |
| wood_stack | Wood Stack | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_stack.prefab |
| wood_stair | Wood Stairs | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_stair.prefab |
| wood_stepladder | Wood Ladder | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_stepladder.prefab |
| wood_wall_half | Wood Wall Half | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_half.prefab |
| wood_wall_log | Log Beam 2 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_log.prefab |
| wood_wall_log_4x0.5 | Log Beam 4 m | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_log_4x0.5.prefab |
| wood_wall_quarter | Wood Wall 1x1 | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_quarter.prefab |
| wood_wall_roof | Wood Wall 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof.prefab |
| wood_wall_roof_45 | Wood Wall 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_45.prefab |
| wood_wall_roof_45_upsidedown | Wood Wall 45° (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_45_upsidedown.prefab |
| wood_wall_roof_67_a | Wood Wall 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_67_a.prefab |
| wood_wall_roof_67_upsidedown | Wood Wall 67° (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_67_upsidedown.prefab |
| wood_wall_roof_a | Wood Wall 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_a.prefab |
| wood_wall_roof_top | Wood Roof Cross 26° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_top.prefab |
| wood_wall_roof_top_45 | Wood Roof Cross 45° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_top_45.prefab |
| wood_wall_roof_top_67 | Wood Roof Cross 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_top_67.prefab |
| wood_wall_roof_upsidedown | Wood Wall 26° (Inverted) | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_wall_roof_upsidedown.prefab |
| wood_window | Wood Shutter | GameElements/Pieces | 7 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_window.prefab |
| wood_yggdrasil_stack | Yggdrasil Wood Stack | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/wood_yggdrasil_stack.prefab |
| wooden_path | — | world/Props | 4 components; active: yes | c4210710 / Assets/world/Props/wooden_path.prefab |
| woodiron_beam | Wood Iron Beam | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/woodiron_beam.prefab |
| woodiron_beam_26 | Wood Iron Beam 26° | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/woodiron_beam_26.prefab |
| woodiron_beam_45 | Wood Iron Beam 45° | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/woodiron_beam_45.prefab |
| woodiron_beam_67 | Wood Iron Beam 67° | GameElements/Pieces | 4 components; active: yes | c4210710 / Assets/GameElements/Pieces/woodiron_beam_67.prefab |
| woodiron_pole | Wood Iron Pole | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/woodiron_pole.prefab |
| woodwall | Wood Wall | GameElements/Pieces | 5 components; active: yes | c4210710 / Assets/GameElements/Pieces/woodwall.prefab |
| Wraith | Wraith | Characters/Wraith | 9 components; active: yes | c4210710 / Assets/Characters/Wraith/Wraith.prefab |
| wraith_melee | Wraith melee | Characters/Wraith | 5 components; active: yes | c4210710 / Assets/Characters/Wraith/misc/wraith_melee.prefab |
| Writhan | Writhan | Characters/Writhan | 11 components; active: yes | c4210710 / Assets/Characters/Writhan/Writhan.prefab |
| writhan_bite | writhan bite | Characters/Writhan | 5 components; active: yes | c4210710 / Assets/Characters/Writhan/attacks/writhan_bite.prefab |
| writhan_explode_aoe | — | Characters/Writhan | 3 components; active: yes | c4210710 / Assets/Characters/Writhan/attacks/writhan_explode_aoe.prefab |
| writhan_explosion | — | Characters/Writhan | 4 components; active: yes | c4210710 / Assets/Characters/Writhan/attacks/writhan_explosion.prefab |
| WrithanRoots | Writhan Roots | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/WrithanRoots.prefab |
| XboxGamepadMap | — | UI/Gamepad | 3 components; active: yes | c4210710 / Assets/UI/Gamepad/Prefabs/XboxGamepadMap.prefab |
| YagluthAltarBase | — | world/Props | 6 components; active: yes | 32fd94e5 / Assets/world/Props/YagluthLocation/YagluthAltarBase.prefab |
| YagluthDrop | Torn Spirit | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/misc/YagluthDrop.prefab |
| YggaShoot1 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Shoots/YggaShoot1.prefab |
| YggaShoot2 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Shoots/YggaShoot2.prefab |
| YggaShoot3 | — | world/Props | 7 components; active: yes | c4210710 / Assets/world/Props/Shoots/YggaShoot3.prefab |
| yggashoot_log | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Shoots/logs/yggashoot_log.prefab |
| yggashoot_log_half | — | world/Props | 10 components; active: yes | c4210710 / Assets/world/Props/Shoots/logs/yggashoot_log_half.prefab |
| YggaShoot_small1 | — | world/Props | 8 components; active: yes | c4210710 / Assets/world/Props/Shoots/YggaShoot_small1.prefab |
| YggdrasilPorridge | Yggdrasil Porridge | GameElements/Items | 7 components; active: yes | c4210710 / Assets/GameElements/Items/consumables/YggdrasilPorridge.prefab |
| YggdrasilRoot | Ancient Root | world/Props | 5 components; active: yes | c4210710 / Assets/world/Props/Mistlands/YggdrasilRoot.prefab |
| YggdrasilWood | Yggdrasil Wood | GameElements/Items | 9 components; active: yes | c4210710 / Assets/GameElements/Items/materials/YggdrasilWood.prefab |
| YmirRemains | Ymir Flesh | GameElements/Items | 8 components; active: yes | c4210710 / Assets/GameElements/Items/materials/YmirRemains.prefab |
