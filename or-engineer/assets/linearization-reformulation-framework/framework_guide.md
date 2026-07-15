# Linearization And Reformulation Framework Guide

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a general scaffold for turning difficult relationships into exact formulations, approximations, or relaxations. It is intentionally not runnable until task-specific expressions, bounds, variables, and validation logic are implemented.

## Industrial Implementation Contract

Do not use this asset to create arbitrary big-M constants, unvalidated PWL segments, or reformulations whose exactness is unclear. A serious deployment must derive or justify bounds, classify each transformation as exact, relaxation, inner approximation, outer approximation, or heuristic approximation, validate approximation error in original units, test sensitivity to bounds or segment counts, and evaluate final decisions against the original relationships when possible.

Use it for:

- big-M and indicator constraints,
- logical implications and disjunctions,
- bilinear and multilinear terms,
- McCormick envelopes,
- piecewise-linear inner or outer approximations,
- SOS2 or binary segment selection,
- perspective reformulations,
- complementarity and KKT-derived constraints,
- conic or convex reformulations,
- relaxation models for lower or upper bounds.

Adaptation flow:

1. Identify each nonlinear or logical relationship and its variable domains.
2. Derive safe bounds before choosing big-M, envelopes, or segment ranges.
3. Classify each reformulation as exact, relaxation, inner approximation, outer approximation, or heuristic approximation.
4. Implement reformulation blocks in `patterns/` or `approximations/`.
5. Validate approximation error and feasibility implications in `validation/`.
6. Pass the resulting model to a mathematical programming or constraint programming asset when solving.
7. Save reformulation assumptions, error reports, segment sensitivity, and solver outcomes under `run_records/`.

Minimum acceptance criteria:

- State whether each transformation is exact or approximate.
- Record all bound assumptions.
- Quantify approximation error on representative points or scenarios.
- Run segment-count or bound-sensitivity checks when approximation quality affects decisions.
