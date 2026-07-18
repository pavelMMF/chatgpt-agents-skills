---
name: game-design
description: Turn a game idea into a testable design contract covering player fantasy, audience, core loop, verbs, progression, constraints, prototype slice, failure criteria, scope, and evidence. Use for game concepts, GDD review, feature prioritization, vertical slices, pitch critique, scope reduction, or deciding what to prototype first.
---

# Game Design

Treat a design as a set of player-facing hypotheses, not a list of features.

## Workflow

1. Define the player fantasy, target audience, platform, session shape, constraints, and comparable experiences.
2. State the core loop as player verb, feedback, consequence, adaptation, and renewed choice.
3. Identify the differentiating hypothesis and what evidence would disprove it.
4. Map mechanics, resources, progression, failure/recovery, difficulty, accessibility, and content burden.
5. Compare three scopes: minimum playable truth, flexible extension seams, and the clearest common-path player experience.
6. Select a prototype slice that tests the riskiest assumption with placeholder content. Define what to fake and what must be real.
7. Specify playtest questions, observable behaviors, success/failure criteria, and the decision after each outcome.
8. Record cuts, dependencies, production risks, and assumptions separately from confirmed facts.

## Guardrails

- Do not infer fun, market demand, retention, or accessibility without player evidence.
- Do not turn every idea into a live service, multiplayer game, open world, or content treadmill.
- Avoid dark patterns, manipulative monetization, inaccessible defaults, and unbounded procedural content claims.
- Do not implement before the prototype question and scope are explicit.

## Output

Return the design pillars, player loop, hypothesis map, system/content dependencies, prototype slice, test plan, scope cuts, risks, and next decision.

## Routing

- Use `gameplay-systems` for mechanic architecture.
- Use `level-design` for spaces and encounters.
- Use `game-playtest-qa` after a playable artifact exists.

Read [references/sources.md](references/sources.md).
