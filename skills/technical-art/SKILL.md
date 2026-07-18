---
name: technical-art
description: Design, implement, debug, and review real-time shaders, materials, VFX, particles, lighting, post-processing, procedural content, rendering features, and art-pipeline tooling under measurable platform budgets. Use for Unity Shader Graph/HLSL, Unreal materials/Niagara, Godot shaders, visual defects, asset constraints, or artist-engineer workflow design.
---

# Technical Art

Translate visual intent into a measurable runtime contract and an artist-usable workflow.

## Workflow

1. Define the target look, camera, renderer, engine/version, platforms, quality tiers, frame budget, memory budget, and authoring constraints.
2. Reduce the effect to inputs, coordinate spaces, data flow, material passes, lighting interaction, transparency/overdraw, simulation, and output.
3. Build the cheapest representative version first. Preserve a visual reference and capture baseline profiling evidence.
4. Design exposed parameters, ranges, defaults, naming, preview states, validation, fallbacks, and batching/instancing behavior for artists.
5. Check precision, branching, texture sampling, variant count, overdraw, fill rate, particles, shadows, bandwidth, and platform feature support.
6. Validate in representative scenes and target builds, not only an isolated editor preview.
7. Document failure modes, quality scalars, debug views, asset rules, and ownership.

## Guardrails

- Profile before optimizing and remeasure after each material change.
- Do not assume a shader language, render pipeline, or hardware capability from the visual request alone.
- Avoid hidden global state, uncontrolled variants, unbounded particles, and artist parameters that can violate budgets silently.
- Do not change project render pipelines or global quality settings without authorization.

## Output

Return the visual contract, render path, parameters, budget, implementation plan, artist workflow, profiling evidence, platform fallbacks, debug plan, and validation checklist.

## Routing

- Use `blender-game-assets` for source mesh/texture/export problems.
- Use `game-performance` for frame-time diagnosis.
- Use `game-engine-development` for engine-specific project integration.

Read [references/sources.md](references/sources.md).
