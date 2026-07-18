---
name: game-animation
description: Design, implement, export, and review responsive game animation systems, including rigs, skinning, clips, root motion, state machines, blend trees, animation layers, IK, retargeting, events, procedural motion, transitions, and gameplay synchronization. Use for Blender-to-engine animation, locomotion, combat animation, animation bugs, or feel improvements.
---

# Game Animation

Make animation serve control readability and gameplay state; visual smoothness alone is not the objective.

## Workflow

1. Define player intent, gameplay authority, camera, responsiveness target, rig, engine/version, source format, and target platforms.
2. Map gameplay states, transitions, interrupts, priorities, timing windows, motion ownership, and animation events.
3. Define skeleton hierarchy, naming, scale, orientation, bind pose, deformation constraints, sockets, IK targets, and retargeting assumptions.
4. Decide where motion comes from: code/physics, root motion, authored curves, procedural systems, or a deliberate hybrid.
5. Build locomotion and high-frequency transitions before rare polish. Test starts, stops, reversals, slopes, turns, hit reactions, cancellation, and low frame rate.
6. Export and import representative clips; verify transforms, looping, compression, curves, events, masks/layers, and root displacement.
7. Evaluate latency, pose readability, foot sliding, popping, clipping, camera interaction, networking, and runtime cost in a playable build.

## Guardrails

- Do not let animation events become the sole authoritative source for critical game state unless the project deliberately requires it.
- Do not apply root motion or retargeting globally without testing controller, navigation, networking, and collision behavior.
- Preserve editable rigs and source clips before destructive baking.
- Do not claim improved feel without observation or playtest evidence.

## Output

Return the state/transition map, motion authority, rig/export contract, clip list, integration steps, edge-case tests, performance concerns, and feel-validation plan.

Read [references/sources.md](references/sources.md).
