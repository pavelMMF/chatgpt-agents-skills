---
name: gameplay-systems
description: Design, implement, or review modular gameplay mechanics, state, input, abilities, combat, interaction, AI behavior, inventory, quests, progression, saving, networking boundaries, and feedback. Use when translating game rules into engine-agnostic interfaces, debugging emergent interactions, or planning testable gameplay code.
---

# Gameplay Systems

Model rules and state explicitly; keep presentation, input, simulation, and persistence separated where that increases testability.

## Workflow

1. Define player intent, rules, state, invariants, timing, authority, failure states, and observable feedback.
2. Map the mechanic as inputs, decisions, state transitions, events, outputs, and persistence boundaries.
3. Choose modules and narrow interfaces. Separate deterministic simulation from engine adapters when replay, networking, or tests require it.
4. Specify data ownership, update frequency, ordering, cancellation, pause/time scale, save/load, and versioning.
5. Design composition and extension seams before inheritance hierarchies. Avoid global state unless the lifecycle truly is global.
6. Test nominal flow, boundary values, repeated input, interruption, missing dependencies, reload, low frame rate, and conflicting systems.
7. Validate game feel in a playable build; code correctness is not evidence that the mechanic feels good.

## Guardrails

- Do not invent networking authority, tick rate, scale, or determinism requirements.
- Do not couple core rules to UI, audio, particles, or one scene unless locality outweighs reuse.
- Preserve existing project conventions and engine lifecycle rules.
- Do not replace a working simple mechanic with a framework without measured leverage.

## Output

Return the rule contract, state model, modules/interfaces, event flow, persistence/network boundaries, failure modes, test matrix, and implementation sequence.

## Routing

- Use `game-engine-development` for Unity, Unreal, or Godot implementation details.
- Use `game-animation` for animation state and motion coupling.
- Use `game-performance` for measured runtime bottlenecks.

Read [references/sources.md](references/sources.md).
