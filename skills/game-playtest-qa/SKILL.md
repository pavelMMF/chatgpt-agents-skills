---
name: game-playtest-qa
description: Plan, execute, analyze, and report game playtests and QA across functionality, player comprehension, feel, balance, progression, visuals, audio, input, performance, compatibility, localization, accessibility, saves, and release risk. Use for test plans, bug reproduction, build acceptance, regression matrices, observation protocols, or verifying fixes.
---

# Game Playtest and QA

Separate player-research questions from defect verification, then connect both to reproducible evidence.

## Workflow

1. Define the build identifier, platform/device, test objective, risks, audience, environment, instrumentation, and decision this pass supports.
2. Choose the mode:
   - playtest: observe comprehension, behavior, emotion, strategy, and friction without coaching;
   - QA: verify expected behavior, boundaries, compatibility, and regressions against an explicit oracle.
3. Build a matrix covering critical path, state transitions, input devices, resolutions, saves, localization, accessibility, performance, online/offline transitions, and failure recovery as applicable.
4. Record exact steps, expected/actual result, frequency, severity, evidence, build/platform, logs, screenshots/video, and workaround.
5. For playtests, distinguish observation, participant quote, interpretation, and recommendation. Avoid leading questions.
6. Triage by player impact, reproducibility, reach, data-loss/safety risk, and release phase; do not let severity labels replace evidence.
7. Verify fixes on the original case plus adjacent regression cases. Report blocked and untested areas explicitly.

## Guardrails

- Never claim a test passed if the build, editor, device, or required service was unavailable.
- Do not expose tester personal data or record participants without consent.
- Do not infer broad player sentiment from a tiny convenience sample.
- Do not ship, publish, alter live services, or wipe saves without explicit authorization.

## Output

Return the scope, build matrix, test cases, observations/defects, evidence, severity rationale, blocked coverage, fix verification, residual risk, and release recommendation.

## Routing

- Use `game-performance` for profiling traces.
- Use `level-design` or `game-animation` for domain-specific iteration.
- Use `verification-loop` for repository-level automated proof.

Read [references/sources.md](references/sources.md).
