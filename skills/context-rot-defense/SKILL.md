---
name: context-rot-defense
description: 'Prevent stale, noisy, or superseded context from polluting long Codex tasks by auditing `task_plan.md`, `findings.md`, `progress.md`, memory files, handoff notes, and compact summaries. Use before or after `/compact`, after long research/debugging phases, when resuming old tasks, when facts may be outdated, or when durable notes need confidence, source, date, validity, and supersession markers.'
---

# Context Rot Defense

Use this when context length or age is a quality risk. The goal is to preserve useful state while marking stale assumptions, dead ends, and superseded decisions.

## Workflow

1. Locate durable context:
   - project `task_plan.md`, `findings.md`, `progress.md`,
   - project `.codex/` notes,
   - relevant global memory files,
   - handoff or compact summaries.
2. Classify entries:
   - evidence,
   - decision,
   - assumption,
   - todo,
   - error/dead end,
   - stale or superseded note.
3. Add freshness metadata where useful:
   - `source`,
   - `date_checked`,
   - `confidence`: high, medium, low,
   - `still_valid`: yes, no, unknown,
   - `superseded_by`,
   - `decision_status`: proposed, accepted, rejected, obsolete.
4. Rewrite only the durable notes needed for the next phase.
5. Suggest `/compact` only after important state is written to files.

## Durable Finding Template

```markdown
### Finding: short title

- Source:
- Date checked:
- Confidence: high | medium | low
- Still valid: yes | no | unknown
- Superseded by:
- Impact:
- Next action:
```

## Rules

- Do not delete old notes silently. Mark stale or move to an archive section unless the user asks for cleanup.
- Keep verified facts separate from guesses and preferences.
- When external facts may have changed, re-check before relying on them.
- Do not preserve command dumps; summarize command, outcome, and important evidence.
