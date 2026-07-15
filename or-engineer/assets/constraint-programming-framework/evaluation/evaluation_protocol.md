# Evaluation Protocol

Report:

- solver status,
- objective and best bound,
- relative gap when available,
- conflicts and branches,
- runtime,
- feasibility validation in original business rules,
- soft-constraint penalty breakdown,
- schedule or assignment quality metrics,
- comparison to MILP, heuristic, incumbent, or relaxed benchmarks when useful, reported separately for each comparator.

Baseline reporting:

- define every comparator by model/rule, constraints included, objective/penalty terms, time limit, and solver status,
- report each comparator's objective, penalty breakdown, feasibility status, and runtime,
- do not report only the best comparator when several were evaluated,
- do not add an aggregate baseline row; interpret metric results by pointing to individual rows.

For infeasibility:

- try constraint relaxation or assumption tracking when supported,
- report suspected conflicting rule groups,
- avoid deleting constraints silently.
