# Sources And Rationale

Use this reference only when explaining why the startup workflow exists or when maintaining the skill.

## Core Codex surfaces

- AGENTS.md is the right place for global startup behavior. Codex reads global AGENTS.md from CODEX_HOME before project instructions, then layers project files after it.
- Skills are the right place for reusable task workflows. Codex starts with skill names/descriptions and reads full SKILL.md only when a task matches the description.
- Custom subagents live under `~/.codex/agents/` for personal agents or `.codex/agents/` for project agents. Each TOML file needs `name`, `description`, and `developer_instructions`.

## Recommended external reading

- OpenAI Codex AGENTS.md documentation: https://developers.openai.com/codex/agent-configuration/agents-md
- OpenAI Codex subagents documentation: https://developers.openai.com/codex/agent-configuration/subagents
- OpenAI Codex build skills documentation: https://developers.openai.com/codex/build-skills
- OpenAI Multi-agent guide: https://developers.openai.com/api/docs/guides/responses-multi-agent
- Agent Skills standard: https://agentskills.io/
- OpenAI skills catalog: https://github.com/openai/skills
- Superpowers skills methodology: https://github.com/obra/superpowers
- Context rot report: https://www.trychroma.com/research/context-rot

## Found skill/plugin ideas

- Superpowers is the strongest external match for "skills that start every conversation" and "subagent-driven development". It includes skills such as `using-superpowers`, `brainstorming`, `writing-plans`, `dispatching-parallel-agents`, `subagent-driven-development`, `verification-before-completion`, and `writing-skills`.
- OpenAI's skills catalog is useful for examples, but its README says the repository is deprecated in favor of current plugin examples.
- Agent Skills is useful as the portable format reference.
