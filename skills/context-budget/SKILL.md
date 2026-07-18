---
name: context-budget
description: Audit and reduce Codex context overhead from instructions, skill metadata, tools, planning files, memory, and duplicated guidance while preserving task quality. Use when context feels crowded, routing overlaps, token use is high, or a repository needs a context-loading strategy.
---

# Context Budget

Treat context as a limited working set. Measure first, then move detail behind on-demand boundaries.

## Workflow

1. Inventory system and project instructions, skill metadata and bodies, agents, tool schemas, planning files, memory, logs, and history.
2. Separate always-visible routing metadata from content loaded only when triggered. Record byte or character counts where possible.
3. Estimate tokens only as a labeled heuristic, such as characters divided by four. Prefer real platform measurements when available.
4. Find duplication, stale instructions, broad triggers, embedded examples, unused tools, and detail that belongs in references.
5. Classify each item as keep always-on, load on demand, or archive/remove.
6. Make the smallest reversible change, then compare routing quality, missed constraints, latency, and size before and after.
7. Preserve safety, authorization, environment, and user-preference instructions even when they cost tokens.

## Guardrails

- Do not edit any context source when the user requested only an audit or recommendation.
- Do not claim exact costs for hidden platform context or tool schemas without measurement.
- Do not disable tools, delete memory, rewrite global instructions, or uninstall skills without explicit authorization.
- Do not optimize only for size; false routing and missing safety context are regressions.
- Avoid fixed universal thresholds. Compact at real phase boundaries and under observed pressure.

## Routing

- Use `strategic-compact` at meaningful phase transitions.
- Use `context-rot-defense` for stale durable context.
- Use `checkpoint` before a long pause or handoff.
- Use `skill-registry` to inspect routing overlap.

## Output

Return a before/after inventory with source, estimated or measured size, loading mode, value, risk, recommendation, expected savings, and verification step. Clearly label estimates.

## References

See [references/sources.md](references/sources.md).
