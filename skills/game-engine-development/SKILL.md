---
name: game-engine-development
description: Inspect, implement, debug, or review game projects in Unity, Unreal Engine, or Godot while respecting engine version, project conventions, scene and asset formats, lifecycle, testing, packaging, and editor boundaries. Use for C# Unity, C++ or Blueprint Unreal, GDScript Godot, engine selection, migration, scene architecture, builds, or engine-specific code generation.
---

# Game Engine Development

Identify the project and engine version from repository evidence before applying engine-specific patterns.

## Workflow

1. Inspect manifests, project files, engine version, packages/plugins, target platforms, source layout, scenes/maps, build scripts, and existing conventions.
2. Route by engine:
   - Unity: assemblies, scenes/prefabs, components, ScriptableObjects, serialization, play mode, packages, and C# lifecycle.
   - Unreal: modules, UObjects/Actors/Components, Blueprints, reflection, assets/maps, build targets, cooking, and automation.
   - Godot: nodes/scenes/resources, GDScript or C#, signals, autoloads, imports, and export presets.
3. Verify current official documentation for the detected version; do not silently mix version-specific APIs.
4. Make the smallest project-native change. Keep engine adapters shallow and gameplay rules testable where practical.
5. Validate import/serialization, editor reload, runtime behavior, build/package, target platform, and version-control artifacts.
6. Report steps that require a live editor or unavailable SDK instead of claiming they ran.

## Guardrails

- Do not rewrite binary scenes/assets through guessed formats.
- Do not enable plugins, upgrade engine versions, regenerate project files, import packages, or change build targets without authorization.
- Do not hand-edit generated caches or commit engine-generated temporary folders.
- Back up or use version control before migrations and bulk serialization changes.

## Output

Return detected engine/version, project map, chosen engine-native pattern, changed or proposed interfaces, editor steps, tests, build verification, migration risk, and unresolved dependencies.

## Routing

- Use `gameplay-systems`, `level-design`, `technical-art`, `game-animation`, or `game-performance` for the specialized domain.

Read only the matching engine section in [references/engines.md](references/engines.md).
