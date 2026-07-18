---
name: level-design
description: Design, block out, review, and iterate game levels, encounters, traversal, spatial metrics, pacing, landmarks, navigation, tutorialization, checkpoints, difficulty, and environmental storytelling. Use for greyboxes, mission flow, combat arenas, puzzle spaces, open zones, multiplayer maps, or diagnosing player confusion and pacing.
---

# Level Design

Build spaces around player decisions, readable affordances, and testable pacing.

## Workflow

1. Define the level's purpose, player state on entry, desired decisions, exit state, mechanics taught/tested, and production constraints.
2. Establish metrics from the actual controller, camera, speed, jump, combat ranges, navigation agents, and target platform.
3. Draw the critical path, optional paths, loops, gates, sightlines, landmarks, encounter beats, resources, checkpoints, and recovery.
4. Create a greybox using primitive geometry and representative collision before final art.
5. Validate readability from player height and camera, including spawn orientation, occlusion, lighting, audio cues, and accessibility.
6. Test navigation, exploits, soft locks, backtracking, difficulty spikes, downtime, multiplayer fairness, and performance pressure.
7. Observe players without coaching. Separate intended route, actual behavior, confusion, delight, and workaround.
8. Iterate geometry and encounter logic before committing expensive art.

## Guardrails

- Do not use arbitrary dimensions detached from controller and camera metrics.
- Do not solve unclear navigation only with text or waypoint spam.
- Do not infer player understanding from designer familiarity.
- Preserve escape routes, accessibility, checkpoint safety, and recovery from failure.

## Output

Return the level intent, metric sheet, flow map, beat table, greybox plan, encounter contracts, readability checklist, playtest tasks, risks, and iteration priorities.

Read [references/sources.md](references/sources.md).
