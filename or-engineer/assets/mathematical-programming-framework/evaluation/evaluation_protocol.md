# Evaluation Protocol

Before solving:

- verify objective sign, units, and scale,
- verify variable domains,
- verify constraint units and index coverage,
- define acceptable solver status and gap,
- define baseline or relaxation comparisons.

After solving:

- report solver status, objective, bound, gap, runtime, node or iteration count when available,
- validate hard constraints independently from solver status,
- check objective reconstruction from exported solution,
- inspect dual values, slacks, IIS, or infeasibility certificates when relevant,
- compare against each baseline, relaxation, incumbent policy, or ex-post benchmark separately,
- label time-limited, infeasible, unbounded, or numerically suspect results clearly.

Baseline reporting:

- list every baseline or bound separately with objective sense, feasibility assumptions, information timing, and solver/runtime status,
- report each comparator's objective, bound/gap when relevant, feasibility status, and runtime,
- do not use an aggregate comparator row when multiple comparator methods were evaluated,
- interpret which comparator performed better by pointing to the individual comparator rows.
