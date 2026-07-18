---
name: blender-game-assets
description: Plan, create, normalize, export, and validate Blender assets for real-time game engines, including meshes, topology, UVs, normals, materials, textures, LODs, collisions, pivots, scale, naming, rigs, and glTF or FBX handoff. Use for Blender-to-Unity/Unreal/Godot pipelines, 3D asset briefs, import failures, or runtime asset budgets.
---

# Blender Game Assets

Treat the engine import as part of asset creation. A correct `.blend` file is not sufficient if the runtime artifact is wrong.

## Workflow

1. Record the target engine/version, platform, renderer, asset role, camera distance, units, axes, budget, material model, animation needs, and export format.
2. Establish naming, collections, origin/pivot, transforms, scale, handedness, and source/export folder contracts.
3. Model for silhouette and deformation first; keep topology intentional, remove hidden waste, and preserve source detail separately from runtime meshes.
4. Validate normals, tangents, smoothing, UV channels, texel density, material slots, texture color spaces, alpha, and packed maps.
5. Create required LODs, collisions, sockets/empties, lightmap UVs, and rig/skin data from measured project needs.
6. Freeze or apply only the transforms/modifiers required by the export contract; retain an editable source file.
7. Export a minimal test asset, import it into the target engine, and verify scale, orientation, shading, materials, collision, animation, bounds, and runtime cost.
8. Record provenance, license, generator/tool versions, and review status in the asset registry when available.

## Guardrails

- Do not overwrite the only editable source or destructively apply modifiers without authorization and a recoverable copy.
- Do not guess polygon, texture, bone, or draw-call budgets; derive them from platform and scene measurements.
- Do not export copyrighted or generated assets without verified usage rights.
- Do not claim visual correctness without an engine import or rendered review.

## Output

Return the asset contract, Blender preparation steps, export settings, engine import checks, budget evidence, naming/provenance, failures, and approval checklist.

## Routing

- Use `technical-art` for shaders, VFX, materials, and budget strategy.
- Use `game-animation` for rigs, clips, root motion, and state integration.
- Use `asset-librarian` for manifests and review queues.

Read [references/sources.md](references/sources.md).
