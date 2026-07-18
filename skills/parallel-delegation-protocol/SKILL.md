---
name: parallel-delegation-protocol
description: 'Plan and manage bounded multi-agent delegation for Codex tasks, including subagent briefs, role selection, forbidden scope, file ownership, evidence requirements, token budgets, merge criteria, and reconciliation. Use when a task should be split across multiple agents, when architecture or product ideas need independent perspectives, or when parallel workers could safely handle disjoint research, review, verification, or implementation streams.'
---

# Parallel Delegation Protocol

Use this before spawning multiple agents. Delegation is useful only when work can split into independent streams and the main agent has a clear local next step.

## Decision Gate

Delegate only when at least one is true:

- The user asked for agents, subagents, debate, or independent perspectives.
- The task has independent sidecar research/review/verification work.
- A high-impact architecture or product decision benefits from separate perspectives.
- Implementation can be split into disjoint file ownership.

Do not delegate when the task is small, tightly coupled, or immediately blocked on the delegated result.

## Delegation Plan

Before spawning agents, write a short plan:

```markdown
Local critical path:
- ...

Delegated streams:
- Agent:
  Role:
  Task:
  Inputs:
  Forbidden scope:
  File ownership:
  Evidence required:
  Token/time budget:
  Done when:
```

## Brief Rules

- Give each agent one concrete output.
- Avoid duplicated work across agents.
- State what the agent must not edit or assume.
- For code workers, define disjoint file/module ownership.
- For reviewers, request evidence and ranked findings, not generic advice.
- For idea/architecture critique, assign distinct perspectives: minimal interface, flexible interface, common-path UX/developer experience.

## Reconciliation

1. Wait only when the result blocks the next local action.
2. Read returned evidence before adopting conclusions.
3. Merge by file ownership and user value, not by majority vote.
4. Record accepted decisions and rejected alternatives in `findings.md` or `progress.md`.
5. Close completed agents when no longer needed.

## Output

Return:

- delegation plan,
- spawned roles or recommended roles,
- reconciliation summary,
- unresolved risks.
