# Global Constraint Catalog

Common CP constraints:

- all-different,
- table and allowed assignments,
- element,
- automaton,
- circuit and paths,
- no-overlap,
- cumulative,
- reservoir,
- optional interval,
- precedence,
- disjunctive resource constraints,
- at-most-one and exactly-one,
- sequence-dependent setup constraints,
- symmetry-breaking constraints,
- soft constraints with penalties.

Selection notes:

- Use interval variables for scheduling when start, duration, end, and optional presence interact.
- Use cumulative or no-overlap instead of pairwise disjunctions when the solver supports them.
- Use table or automaton constraints for compact logic representation.
- Add symmetry breaking when equivalent assignments slow search.
