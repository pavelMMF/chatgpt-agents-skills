---
name: bi-data-visualization
description: Design or review decision-ready BI dashboards, analytical charts, KPI scorecards, and data stories with correct metric semantics, visual encodings, uncertainty, accessibility, and source tie-out. Use when choosing charts, structuring dashboards, explaining trends, or auditing misleading visualizations.
---

# BI and Data Visualization

Start with the decision and metric contract. A polished chart cannot rescue ambiguous data.

## Workflow

1. Identify the audience, decision, cadence, and action each view should support.
2. Define each metric: owner, formula, grain, population, time zone, denominator, filters, target, and source.
3. Validate totals against an authoritative source before styling.
4. Match encoding to the question: position for comparison, lines for ordered time, bars for categories, distributions for spread, and tables for exact lookup.
5. Show baseline, target, denominator, uncertainty, missingness, annotations, and comparable periods.
6. Build a hierarchy from status to drivers to diagnostic detail. Keep filters and defaults visible.
7. Check contrast, redundant non-color cues, labels, keyboard behavior, mobile layout, loading, empty, error, and stale-data states.
8. Test representative questions and document caveats.

## Guardrails

- Do not truncate axes or use dual axes without a defensible reason.
- Do not imply precision beyond the source or hide small denominators.
- Use maps only when spatial position matters.
- Distinguish reporting delay from true change and correlation from causation.
- Never modify production dashboards or metric definitions without authorization.

## Output

Provide the audience and decision, metric contracts, information hierarchy, chart rationale, interaction states, accessibility checks, validation evidence, and limitations.

## Routing

- Use `data-analysis` for the underlying analysis.
- Use `design-system` or `ui-styling` for implementation-level visual design.

## References

See [references/sources.md](references/sources.md).
