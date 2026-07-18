---
name: agentic-startup-orchestrator
description: Use at the start of any Codex chat or task that involves coding, architecture, product ideas, UI/UX, long-running work, research, planning, multiple repositories, documentation, or non-trivial decisions. Coordinates automatic use of anti-slop prose, token/context economy, long-memory files, architecture design, UI/UX review, and multi-agent idea/architecture critique. Also use when the user asks for "auto skills", "start every chat", "agents", "subagents", "architecture debate", "long memory", "token saving", "anti slop", "UI UX", "brainstorming", or "relevance check".
---

# Agentic Startup Orchestrator

## Purpose

Use this as a startup router for serious work. It decides which persistent memory, architecture, UI/UX, writing, token-budget, and subagent patterns should be active before execution starts.

Do not turn every tiny answer into a ceremony. For simple facts, answer normally and apply only the anti-slop final pass.

## Startup Pass

Before substantive work on any non-trivial task:

1. Classify the task:
   - `simple`: direct answer or one small command.
   - `medium`: a few steps, one project, limited uncertainty.
   - `complex`: architecture, UI/UX, research, multi-repo, long-running implementation, or unclear idea quality.
2. Apply these defaults:
   - Always: anti-slop writing pass before final answer.
   - Medium/complex: persistent notes in project files when useful.
   - Complex: architecture vocabulary and explicit tradeoffs before edits.
   - UI-visible work: UI/UX design-system and accessibility pass.
   - Long or noisy work: token economy checkpoint and compact suggestion at phase boundaries.
   - Idea validation or architecture choices: spawn multiple independent agents only when the user asked for agent/subagent/debate work or when AGENTS.md explicitly authorizes it for complex decisions.
3. Keep the user loop tight:
   - Say which workflow is active in one short commentary line.
   - Save bulky findings to files instead of carrying them in context.
   - Do not spawn subagents for tiny tasks.

## Skill Routing

- Use `grill-me` when a new, consequential idea or plan is still under-specified. Interview one decision at a time before implementation; skip it for simple or already-specified execution.
- Use `checkpoint` at meaningful boundaries in complex work when open hypotheses, rejected approaches, or the immediate next action would be costly to reconstruct. Keep routine progress in the planning files.
- Use `anti-slop-writing` for final prose, README/docs, summaries, and any Russian/English text that should sound concrete.
- Use `planning-with-files` for work likely to take 5+ tool calls, multiple phases, research, or implementation.
- Use `strategic-compact` after research, after planning, after a debugging dead-end, or before switching topics.
- Use `codebase-design` for interfaces, seams, adapters, deep modules, testability, and architecture tradeoffs.
- Use `improve-codebase-architecture` when the user asks to scan a codebase for architecture problems.
- Use `ui-ux-pro-max`, `ui-styling`, `design-system`, and `better-icons` for any user-facing interface.
- Use `verification-loop`, `tdd`, or `eval-harness` when changes need proof.
- Use `skill-supply-chain-review` before importing external skills, agents, plugins, MCP configs, hooks, or instruction bundles.
- Use `skill-auditor` to maintain, deduplicate, validate, or clean up installed skills.
- Use `skill-registry` when a task needs an index of installed skills/agents or better routing metadata.
- Use `context-rot-defense` before/after compaction, after long research/debugging, or when durable notes may be stale.
- Use `parallel-delegation-protocol` before spawning multiple agents for one task.
- Use `agent-creator` when creating or updating custom Codex agent TOML profiles.
- Use `data-analysis`, `sql-databases`, `analytics-engineering`, or `bi-data-visualization` for analytical work based on the requested output.
- Use `data-engineering`, `data-architecture`, and `data-quality-governance` for pipelines, platform boundaries, contracts, lineage, and governance.
- Use `mle-workflow` for ML delivery and `ml-system-architecture` for architecture; add `experimentation-causal-inference` when causal claims or experiments are involved.
- Use `creator-audience-research` before choosing a creator niche, `creator-positioning-offers` to shape the promise, and `creator-monetization` to compare revenue paths without inventing demand.
- Use `short-form-video` for platform-native video packages, `ai-persona-studio` for disclosed and consent-based synthetic personas, `creator-growth-experiments` for measured distribution tests, and `creator-email-launch` for permission-based launch sequences.
- Use `game-design`, `gameplay-systems`, and `level-design` for player experience and rules; use `game-engine-development` for Unity, Unreal, or Godot implementation work.
- Use `blender-game-assets`, `technical-art`, and `game-animation` for the DCC-to-engine asset pipeline; finish with `game-performance` and `game-playtest-qa` when budgets, profiling, builds, or playtest evidence matter.
- Use `context-budget` for a measured context-overhead audit; do not add a duplicate token-advisor agent when `token_budgeter` already covers planning.

## Multi-Agent Pattern

Use subagents when work can split into independent, bounded streams:

- `explorer`: map code paths, dependencies, docs, and evidence. Read-only by default.
- `architecture_designer`: propose one architecture/interface from a distinct constraint.
- `idea_critic`: test relevance, value, risks, and failure modes.
- `ui_ux_reviewer`: critique interaction, accessibility, visual hierarchy, and product fit.
- `anti_slop_editor`: rewrite final docs/text.
- `token_budgeter`: suggest what to write to disk, what to compact, and what not to load.
- `worker`: implement a bounded patch with disjoint file ownership.

For architecture debate, spawn 3 agents with different briefs:

1. Minimal interface: 1-3 entry points, maximum leverage.
2. Flexible interface: extension and integration scenarios.
3. Common path: make the default caller trivial.

Compare outputs by depth, locality, seam placement, user value, cost, and implementation risk.

## Long Memory

Prefer project-local memory files:

- `task_plan.md`: phases, decisions, remaining work.
- `findings.md`: research and codebase discoveries.
- `progress.md`: what changed, commands run, errors, verification.

Use `$CODEX_HOME/memory/agentic-workflow.md` only for stable personal preferences that should apply across projects. Do not store secrets.

## Token Economy

- Read targeted files; avoid broad dumps.
- After every 2-3 expensive searches or reads, summarize durable findings to `findings.md`.
- Keep subagent briefs small and independent.
- Compact after research-to-plan or plan-to-implementation transitions when context is bulky.
- Do not load long references unless the current decision needs them.

## References

Read `references/sources.md` only when you need the external rationale or links behind this workflow.
