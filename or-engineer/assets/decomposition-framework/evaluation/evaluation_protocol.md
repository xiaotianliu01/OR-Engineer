# Evaluation Protocol

Track:

- lower bound,
- upper bound or incumbent objective,
- absolute and relative gap,
- master status,
- subproblem statuses,
- cut count, column count, or multiplier norm,
- primal recovery feasibility,
- per-partition infeasibility or poor convergence,
- runtime by master, subproblem, and coordination phase.

Validate:

- final incumbent against original constraints,
- bound direction and objective sense,
- cut validity or pricing reduced-cost sign,
- convergence stopping criterion,
- comparison to direct solve on small instances and other baselines when feasible.

Baseline reporting:

- report direct solve, heuristic, relaxation, and decomposition variants separately when used,
- include method definition, instance set, objective/bound/gap, feasibility, and runtime for each comparator,
- do not collapse comparator methods into an aggregate row,
- interpret which comparator performed better by pointing to the individual comparator rows.
