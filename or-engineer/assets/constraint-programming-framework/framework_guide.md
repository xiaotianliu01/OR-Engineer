# Constraint Programming Framework Guide

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a general scaffold for CP and CP-SAT deployments. It is intentionally not runnable until task-specific variables, domains, global constraints, objective, search settings, and validation logic are implemented.

## Industrial Implementation Contract

Do not use this asset to create a tiny scheduling or assignment toy that omits real domains, calendars, resource constraints, or soft penalties. A serious deployment must use the actual entities and domains, prefer global constraints where appropriate, validate extracted schedules or assignments against original rules, report solver status, objective, bound, gap when available, conflicts, branches, and runtime, and explain infeasibility through relaxation or conflict analysis when possible.

Use it for:

- scheduling with intervals,
- assignment and rostering,
- routing with combinatorial side constraints,
- cumulative resource constraints,
- no-overlap and disjunctive constraints,
- precedence and temporal logic,
- table, automaton, circuit, all-different, and element constraints,
- feasibility repair or exact combinatorial subproblems.

Adaptation flow:

1. Define entities, tasks, resources, time domains, and optional intervals.
2. Choose CP, CP-SAT, or hybrid CP/MILP route.
3. Implement variables and domains in `models/`.
4. Implement global constraints and task-specific logic in `constraints/`.
5. Implement schedule extraction or assignment extraction.
6. Configure solver limits, workers, search hints, and objective scaling.
7. Save search logs, solutions, feasibility checks, and progress under `run_records/`.

Minimum acceptance criteria:

- Report solver status, objective, bound, gap when available, conflicts, branches, runtime, and feasibility checks.
- Validate output schedules or assignments independently from solver status.
- Compare against MILP, heuristic, or relaxation baselines when appropriate.
- Treat unknown or time-limited status as limited evidence, not final proof.
