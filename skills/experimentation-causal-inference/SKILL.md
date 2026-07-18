---
name: experimentation-causal-inference
description: Design, audit, analyze, or interpret controlled experiments and observational causal studies with explicit estimands, assumptions, diagnostics, uncertainty, and sensitivity analysis. Use for A/B tests, power, CUPED, sequential tests, quasi-experiments, matching, or causal claims.
---

# Experimentation and Causal Inference

Treat causal language as a claim that requires an identification strategy.

## Controlled Experiments

1. Define the decision, unit, population, treatment, outcome, estimand, assignment, and window.
2. Pre-specify primary and guardrail metrics, exclusions, minimum detectable effect, power assumptions, stopping rule, and multiplicity handling.
3. Check exposure logging, sample-ratio mismatch, balance, attrition, interference, novelty, and instrumentation changes.
4. Estimate absolute and relative effects with uncertainty intervals; report practical magnitude, not only a p-value.
5. Run planned robustness checks and label exploratory slicing.

## Observational Studies

1. Draw the assumed causal graph and state identification assumptions.
2. Distinguish confounders, mediators, colliders, instruments, and outcomes; prefer pre-treatment covariates.
3. Match the method to the process: adjustment, matching or weighting, regression discontinuity, difference-in-differences, synthetic control, or instruments.
4. Check overlap, balance, pre-trends, placebo outcomes, specification sensitivity, and unmeasured-confounding risk as applicable.
5. State the target population and what would invalidate the estimate.

## Guardrails

- Do not claim causality without a defensible identification strategy.
- Label outcome-driven analysis choices as exploratory.
- Do not install packages, alter configuration, or stop a live experiment without authorization.
- Statistical significance alone does not establish importance, validity, or replicability.
- Flag privacy, fairness, safety, and irreversible-exposure concerns before launch.

## Output

Return the estimand, design, assumptions, diagnostics, estimate with uncertainty, practical interpretation, threats to validity, and recommended decision or next test.

## References

See [references/sources.md](references/sources.md).
