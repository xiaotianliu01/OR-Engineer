# Decomposition Framework Guide

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a general scaffold for decomposition-based optimization. It is intentionally not runnable until task-specific master problems, subproblems, coupling constraints, cut or column generation, and convergence tests are implemented.

## Industrial Implementation Contract

Do not use this asset to create a superficial loop around independent subproblems without valid bounds or primal recovery. A serious deployment must identify the coupling structure, implement valid cuts, columns, multipliers, or consensus updates, track lower and upper bounds when available, validate recovered primal solutions in the original model, and report convergence, infeasibility, cut or column counts, and runtime by phase. If bounds are weak or primal recovery fails, label the method as inconclusive and redesign.

Use it for:

- Benders decomposition,
- L-shaped stochastic programming,
- Dantzig-Wolfe decomposition,
- column generation,
- branch-and-price,
- Lagrangian relaxation,
- ADMM or augmented Lagrangian coordination,
- progressive hedging,
- rolling horizon or temporal decomposition.

Adaptation flow:

1. Identify the complicating constraints, variables, scenarios, time blocks, or network partitions.
2. Choose a decomposition family from `methods/decomposition_catalog.md`.
3. Implement the master representation in `master/`.
4. Implement independent or parallelizable subproblems in `subproblems/`.
5. Implement cuts, columns, multipliers, penalties, or coordination rules in `coordination/`.
6. Implement primal recovery, incumbent tracking, and bound reporting.
7. Save iteration-level progress, bounds, gaps, cut/column counts, and status under `run_records/`.

Minimum acceptance criteria:

- Report lower and upper bounds when the method supports them.
- Track convergence gap, infeasibility, and incumbent quality.
- Validate primal recovered solutions in the original model.
- Compare against direct solve, relaxation, heuristic incumbent, or smaller-instance exact solves when feasible.
