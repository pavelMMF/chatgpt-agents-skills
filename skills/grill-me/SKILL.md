---
name: grill-me
description: Stress-test a new idea, plan, product concept, architecture, or consequential decision through a one-question-at-a-time interview before execution. Use when the user introduces a new idea to explore or build, asks whether a plan makes sense, wants assumptions challenged, says "grill me", or has not yet resolved important product or design decisions. Do not trigger for simple questions, status checks, small fixes, or clearly specified execution requests unless the user asks for critique.
---

# Grill Me

Turn an under-specified idea into shared understanding before acting.

## Protocol

1. State briefly that the idea needs clarification and begin the interview.
2. Ask exactly one decision question per turn and wait for the answer.
3. Give a concrete recommended answer with each question and explain the main tradeoff in one or two sentences.
4. Resolve dependencies in order: desired outcome, user, problem/evidence, scope, constraints, success measure, risks, and execution shape.
5. Look up discoverable facts with available read-only tools instead of asking the user. Ask only for preferences, priorities, authority, or decisions that cannot be discovered.
6. Challenge assumptions and vague language. Ask for an example when an answer is abstract.
7. Keep a visible mental decision tree, but expose only the current branch so the interview remains easy to answer.
8. Periodically summarize confirmed decisions and unresolved points when the branch changes or after roughly five answers.
9. End when remaining uncertainty is low enough to act safely. Present a compact shared-understanding statement and ask for confirmation.
10. Do not implement, mutate external state, or expand scope until the user confirms. Read-only investigation is allowed.

## Adaptation Rules

- If the user asks for a quick answer, give the top concern and at most one question.
- If the idea is low-stakes and reversible, keep the interview short.
- If the user already supplied a complete specification, validate the few material assumptions and proceed.
- If a question becomes irrelevant because of a prior answer, drop that branch.

## Completion

Capture: goal, intended user, non-goals, constraints, success criteria, key decisions, open risks, and recommended next action. Hand off to planning or execution only after confirmation.
