---
name: strategic-compact
description: Suggest manual Codex context compaction at meaningful task boundaries after durable state is saved. Use for long, multi-phase work, a completed milestone, a debugging dead end, a topic switch, or observed context pressure; avoid compaction during tightly coupled implementation.
---

# Strategic Compact

Compact at logical boundaries, not from an unverified universal token threshold.

## Workflow

1. Identify the current phase and whether the next phase needs the recent detailed context.
2. Save authoritative state before compaction:
   - `task_plan.md` for remaining phases and decisions;
   - `findings.md` for evidence and conclusions;
   - `progress.md` for changes, commands, errors, and next action;
   - `checkpoint` when unresolved hypotheses or a high-fidelity handoff would be costly to reconstruct.
3. Remove or label stale and superseded notes with `context-rot-defense`.
4. Suggest `/compact` with a short focus statement only when the boundary is useful.
5. After compaction, reread the durable files and verify the repository or external state before continuing.

## Decision Guide

| Boundary | Default | Reason |
|---|---|---|
| Research to plan | Compact after findings and decisions are saved | Raw research is bulky |
| Plan to implementation | Compact when the plan and file ownership are durable | Frees working space for code |
| Implementation to tests | Usually keep | Recent code paths often matter |
| Debugging dead end to new hypothesis | Compact after recording evidence and rejected hypotheses | Prevents stale reasoning from dominating |
| Milestone to unrelated task | Compact | Local details no longer help |
| Mid-edit or unresolved incident | Do not compact | Exact state and observations are still active |

## Guardrails

- Do not claim exact context use unless the platform exposes a measurement.
- Do not assume chat summaries preserve file contents, tool output, or nuanced user constraints.
- Do not delete planning files or memory as part of compaction.
- Do not use Claude-specific hooks, transcript paths, settings, or memory locations.
- Compaction is a suggestion; preserve the user's flow and do not repeatedly interrupt.

## Related Skills

- `context-budget` for measuring and reducing persistent context overhead.
- `context-rot-defense` for stale durable notes.
- `checkpoint` for high-fidelity phase snapshots.
- `planning-with-files` for durable task state.
