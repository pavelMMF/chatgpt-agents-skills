---
name: skill-registry
description: 'Build or refresh a lightweight machine-readable registry for local Codex skills and custom agents, including tags, triggers, scope, dependencies, conflicts, freshness, and routing notes. Use when asked to index skills, choose among many skills, reduce context cost, compare installed skills and agents, or create/update `skills_index.json` for personal or project-level skill routing.'
---

# Skill Registry

Use this to create a small routing index. The registry helps Codex choose the right skill without reading many full `SKILL.md` files.

## Default Locations

- Personal registry: `$CODEX_HOME/skills_index.json`
- Project registry: `.codex/skills_index.json` when the user wants repo-specific routing.
- Include custom agents from `$CODEX_HOME/agents` or project `.codex/agents` when relevant.

## Workflow

1. Inventory:
   - list skill folders and agent `.toml` files,
   - read frontmatter descriptions and agent descriptions,
   - avoid loading full skill bodies unless routing is ambiguous.
2. Classify each entry:
   - domain tags,
   - trigger phrases,
   - task complexity: simple, medium, complex,
   - scope: global, project, one-off,
   - dependencies: tools, network, browser, filesystem, MCP, plugins,
   - conflicts or overlaps,
   - related agents.
3. Score routing:
   - prefer exact domain match,
   - prefer narrower specialist over broad router,
   - prefer local project skill over global skill when both apply,
   - avoid loading multiple overlapping skills unless they serve distinct roles.
4. Write or update JSON only after preserving existing custom notes.

## Registry Shape

```json
{
  "version": 1,
  "updated_at": "YYYY-MM-DD",
  "skills": [
    {
      "name": "skill-name",
      "path": "absolute-or-project-relative-path",
      "tags": ["..."],
      "triggers": ["..."],
      "scope": "global|project",
      "complexity": ["simple","medium","complex"],
      "dependencies": ["..."],
      "conflicts_with": ["..."],
      "related_agents": ["..."],
      "notes": "short routing note"
    }
  ],
  "agents": [
    {
      "name": "agent_name",
      "path": "absolute-or-project-relative-path",
      "tags": ["..."],
      "use_for": ["..."],
      "avoid_for": ["..."]
    }
  ]
}
```

## Rules

- Keep registry summaries short; do not copy full `SKILL.md` bodies.
- Mark uncertainty instead of guessing hidden dependencies.
- Use `skill-auditor` if the inventory reveals duplicates, bad metadata, or stale skills.
- Use `skill-supply-chain-review` before adding external skills to the registry.
