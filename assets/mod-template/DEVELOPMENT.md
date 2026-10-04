# Development

Install the [.NET 10 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/10.0).
Set `VALHEIM_PATH` to the game root and `BEPINEX_PATH` to a development profile's
BepInEx folder. Use `ValheimManagedPath` to override a nonstandard Managed layout.

## Build and test

```bash
dotnet build -c Release
```

Builds do not deploy by default. To copy only this mod's DLL to the selected
development profile, explicitly enable deployment:

```bash
dotnet build -c Release -p:DeployOnBuild=true
```

Restart Valheim after deploying and test the feature. Review the BepInEx log.
Harmony Validator checks patch targets, not gameplay; this event-only starter
has no Harmony targets to validate.

## Package

Provide an original 256 × 256 `icon.png`. Update the manifest, player README,
changelog, and license before creating a release:

```bash
dotnet msbuild -restore -t:PackageMod -p:Configuration=Release -p:DeployOnBuild=false
```

Inspect `artifacts/ValheimMod.zip`, check metadata and README claims against the
code, and test it in a clean profile. This file is not included in that ZIP.
