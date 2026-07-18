---
name: agent-creator
description: 'Create, update, and validate custom Codex agent profiles in TOML for `$CODEX_HOME/agents` or project `.codex/agents`. Use when asked to create agents, subagents, reviewers, critics, workers, role profiles, multi-agent teams, or when auditing agent descriptions, developer instructions, sandbox mode, reasoning effort, overlap with existing agents, or safe delegation defaults.'
---

# Agent Creator

Use this to design custom Codex agents with narrow roles and safe defaults. Agents should make delegation clearer, not multiply vague opinions.

## Workflow

1. Understand the agent job:
   - concrete tasks it should handle,
   - tasks it must avoid,
   - whether it edits files or stays read-only,
   - expected output shape,
   - overlap with existing agents.
2. Choose location:
   - personal agents: `$CODEX_HOME/agents`,
   - project agents: `.codex/agents` for repo-specific behavior.
3. Design the profile:
   - `name`: snake_case role name,
   - filename: hyphen-case `.toml`,
   - `description`: short trigger/use case,
   - `model_reasoning_effort`: low, medium, high, or xhigh when supported,
   - `sandbox_mode`: prefer `read-only` unless editing is explicitly needed,
   - `developer_instructions`: specific role, priorities, forbidden scope, output format,
   - `nickname_candidates`: 2-3 user-facing names.
4. Validate:
   - no duplicate role with existing agents,
   - no broad authority like "handle everything",
   - no instruction to bypass system/developer/user constraints,
   - no secret, credential, or broad filesystem access unless explicitly justified.
5. If the agent came from outside, run `skill-supply-chain-review` before installing it.

## TOML Template

```toml
name = "role_name"
description = "One-sentence use case."
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Do one narrow job.
State priorities, forbidden scope, and output format.
Do not edit files unless explicitly assigned ownership.
"""
nickname_candidates = ["Name One", "Name Two", "Name Three"]
```

## Output

When creating or updating an agent, report:

- path written,
- intended trigger,
- sandbox/edit permissions,
- overlap check,
- how to invoke or delegate to it.
