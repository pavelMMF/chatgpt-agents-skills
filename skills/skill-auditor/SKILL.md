---
name: skill-auditor
description: 'Audit and maintain local Codex skills for quality, drift, trigger overlap, metadata validity, context bloat, broken scripts, stale references, missing smoke tests, and unsafe instructions. Use when reviewing `$CODEX_HOME/skills`, project `.codex/skills`, new or edited SKILL.md files, skill registries, or when asked to clean up, deduplicate, validate, or improve personal skills.'
---

# Skill Auditor

Use this to keep the local skill library small, discoverable, and safe. The goal is not more skills; the goal is sharper routing, lower context cost, and fewer stale instructions.

## Audit Workflow

1. Inventory target skills:
   - list skill folders,
   - read names and descriptions first,
   - read full `SKILL.md` only for likely issues or requested skills.
2. Check metadata:
   - `name` matches folder and hyphen-case rules,
   - `description` says what the skill does and when to use it,
   - trigger terms are specific enough to avoid broad accidental activation.
3. Check progressive disclosure:
   - `SKILL.md` stays concise,
   - long details live in directly linked `references/`,
   - scripts are used for repeatable deterministic work,
   - no unused `README`, changelog, or filler docs.
4. Check behavior:
   - workflow has clear start, decision points, and output format,
   - validation or smoke test is named when possible,
   - security-sensitive tools and writes are scoped,
   - failure modes and escalation points are explicit.
5. Check overlap:
   - mark duplicates, conflicts, and skills that should be merged,
   - prefer one router plus narrow specialist skills over many generic skills.
6. Validate:
   - run the skill validator when dependencies are available,
   - if validator tooling is missing, report that and perform a manual frontmatter/path check.

## Finding Format

```markdown
Skill: skill-name
Severity: P1 | P2 | P3
Issue: ...
Evidence: path or snippet summary
Fix: ...
```

## Recommendations

- Keep edits surgical: metadata first, then workflow clarity, then references/scripts.
- Do not rewrite a skill's domain knowledge unless the source is stale or incorrect.
- Do not import outside skills during an audit without first using `skill-supply-chain-review`.
