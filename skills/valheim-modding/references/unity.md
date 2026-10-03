# Unity Documentation for Valheim Mods

Use the official Unity 6.0 documentation when a mod touches Unity objects,
lifecycle methods, timing, physics, input, audio, animation, UI, scenes, assets,
cameras, or rendering.

## Documentation entry points

| Need | URL |
| --- | --- |
| Concepts, systems, lifecycle, workflows, and performance | [Unity 6.0 Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/index.html) |
| Types, members, signatures, parameters, and return values | [Unity 6.0 Scripting API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/index.html) |

## Search

Insert a URL-encoded query after `q=`:

```text
https://docs.unity3d.com/6000.0/Documentation/Manual/30_search.html?q=QUERY
https://docs.unity3d.com/6000.0/Documentation/ScriptReference/30_search.html?q=QUERY
```

Examples:

```text
https://docs.unity3d.com/6000.0/Documentation/Manual/30_search.html?q=execution%20order
https://docs.unity3d.com/6000.0/Documentation/ScriptReference/30_search.html?q=GameObject.AddComponent
```

Use the Manual search for behavior and concepts. Use the Scripting API search
for an exact namespace, type, property, event, or method. Search only for what
the current task needs; do not crawl or copy the complete documentation.
If the search page cannot be read, use a web search restricted to the relevant
official Unity version path, then open the matching documentation page.

## Verify against Valheim

The website documents the Unity 6.0 release line, while Valheim ships a specific
Unity patch and a selected set of modules. A result on the website does not prove
that the API exists in the installed game.

1. Find the relevant official documentation with the search URLs above.
2. Before using the API in code, follow [local assembly inspection](environment.md#inspect-the-actual-game)
   to confirm the type, member, overload, and Unity module.
3. Inspect `assembly_valheim.dll` when ownership, initialization, or call timing
   depends on Valheim code.
4. Do not use `UnityEditor` APIs. A BepInEx mod runs in the built player.
5. For code changes, follow [Validation](validation.md). A documentation-only
   answer does not require a build or a game session.
