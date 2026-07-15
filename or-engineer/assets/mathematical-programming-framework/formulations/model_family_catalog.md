# Model Family Catalog

Common model classes:

- LP: continuous linear variables, linear objective, linear constraints.
- MILP: discrete decisions, fixed charges, setups, logical choices, assignment, routing, capacity planning.
- QP/MIQP: quadratic cost or risk terms with continuous or mixed-integer domains.
- SOCP: conic norms, robust constraints, convex quadratic structures.
- SDP: matrix positive-semidefinite constraints when a convex relaxation is selected.
- NLP/MINLP: nonlinear objectives or constraints; require convexity or global/local-solver risk assessment.
- Rolling-horizon MILP/MPC: repeated finite-horizon solves with state carryover.
- Ex-post deterministic equivalent: perfect-information or hindsight benchmark for a realized trajectory.

Selection notes:

- Prefer LP/MILP when hard feasibility, explainability, and gap reporting matter.
- Prefer convex formulations when they preserve structure and avoid binary expansion.
- Prefer MIQP/SOCP when quadratic or conic terms improve model fidelity without destroying tractability.
- Treat MINLP as high-risk unless convexity, solver availability, and scaling are clear.
- Use relaxations and lower bounds to evaluate policies even when the full model is too large.
