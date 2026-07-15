# Mathematical Programming Framework Guide

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a general scaffold for solver-based OR deployments. It is intentionally not runnable until task-specific sets, parameters, variables, constraints, objective, solver settings, and evaluation logic are implemented.

## Industrial Implementation Contract

Do not use this asset to create a toy optimization model that ignores confirmed data, omits core constraints, or reports a solution without solver status. A serious deployment must build the actual index sets and parameters, validate units and domains, handle infeasible/unbounded/time-limited statuses, report incumbent objective, bound, gap, runtime, and feasibility violations, and reconstruct the objective from the exported solution. When the full model is too large, provide a relaxation, decomposition, rolling-horizon, or benchmark plan rather than silently weakening the method.

Use it for:

- LP, MILP, MIQP, QP, SOCP, convex optimization, NLP, MINLP,
- deterministic equivalents,
- rolling-horizon MILP/MPC models,
- lower-bound or ex-post hindsight benchmarks,
- exact repair models for learned or heuristic policies.

Adaptation flow:

1. Define sets, indices, parameters, units, and time conventions.
2. Choose model family and solver candidate from `formulations/model_family_catalog.md`.
3. Implement data-to-index mapping in `data/`.
4. Implement variable, constraint, and objective construction in `models/`.
5. Implement solver adapter and status parsing in `solvers/`.
6. Implement solve loop and artifact writing in `runners/`.
7. Validate feasibility, objective terms, bounds, and benchmark gaps in `evaluation/`.
8. Save solver logs, model export, solution, and progress files under a run folder compatible with `run_records/`.

Minimum acceptance criteria:

- Report solver status, primal objective, best bound when available, absolute and relative gap, runtime, and feasibility violations.
- Export enough model and solution artifacts to reproduce or audit the run.
- Compare against a meaningful baseline or relaxation when the final solution is not proven optimal.
- Do not silently accept infeasible, unbounded, time-limited, or numerically suspect statuses as solved.
