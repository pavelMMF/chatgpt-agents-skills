---
name: checkpoint
description: Save, list, or restore high-fidelity task state for complex or long-running Codex work. Use when the user says checkpoint/save state/restore/resume, before context compaction or a long pause, when switching away from an unfinished complex task, or after a major phase whose hypotheses and rejected approaches would be costly to reconstruct. Do not create checkpoints for simple chats or duplicate ordinary progress logging.
---

# Checkpoint

Preserve perishable task understanding beyond ordinary summaries. Complement `task_plan.md`, `findings.md`, and `progress.md`; do not replace them.

## Storage

Store named snapshots under `<project-root>/.codex/checkpoints/<name>/`. If no project root exists, use the current workspace. Never store secrets, credentials, full environment dumps, or unrelated personal data.

Each checkpoint contains only:

- `meta.json`: name, timestamp, project path, git branch/SHA when available, and touched-file paths.
- `open-threads.md`: immediate next action, active hypotheses with evidence/tests, unnoticed leads, unresolved questions, uncertainties, and what to reread first.
- `knowledge-graph.md`: important entities, typed relationships, constraints, and a short file map.
- `decisions.md`: decided items with rationale, rejected alternatives, failed attempts with lessons, and still-open choices.
- `evidence/`: at most 3–7 compact raw outputs that would be expensive to rediscover; omit when unnecessary.
- `reload.md`: a compact orientation ordered as open threads, knowledge graph, decisions, evidence pointers, then git delta instructions.

## Save

1. Require or derive a short safe name; ask only if ambiguity could overwrite the wrong checkpoint.
2. Detect the project root and inspect existing planning files before extracting state.
3. If the checkpoint already exists, obtain confirmation before overwriting it.
4. Record reasoning that can be articulated: hypotheses, confidence, evidence, rejected paths, and the exact next action. Never claim to preserve hidden model state.
5. Keep evidence relevant and trimmed; point to large existing files instead of copying them.
6. Write atomically where practical and report created paths and any missing context.

## Load

1. Locate the named checkpoint within the current project. If absent, list available names and stop.
2. Read `meta.json`, `open-threads.md`, `knowledge-graph.md`, and `decisions.md`; read evidence only when needed.
3. Compare recorded SHA/files with current git state using read-only commands. Mark stale claims instead of silently trusting them.
4. Reconcile the checkpoint with current `task_plan.md`, `findings.md`, and `progress.md`; newer verified state wins.
5. Orient the user with where work stopped, changed files, stale assumptions, and the recommended next action. Do not mutate the project merely because a checkpoint was loaded.

## List

List checkpoint name, timestamp, branch/SHA, and immediate next action. Do not load full evidence.

## Automatic Use

For complex work, create or refresh a checkpoint only at a meaningful boundary: before compaction, before a requested pause/handoff, or when moving between major phases with unresolved reasoning. Mention the action in commentary. Avoid interrupting active work solely to checkpoint.
