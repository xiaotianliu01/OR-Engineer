# Decomposition Catalog

Method families:

- Benders decomposition: separate complicating first-stage or linking variables from second-stage recourse or subproblem feasibility.
- L-shaped method: Benders-style decomposition for two-stage stochastic linear programs.
- Dantzig-Wolfe decomposition: reformulate into convex combinations of subproblem extreme points.
- Column generation: generate variables or routes only when they have favorable reduced cost.
- Branch-and-price: integrate column generation with integer branching.
- Lagrangian relaxation: dualize complicating constraints and solve separable subproblems.
- Subgradient or bundle methods: update Lagrangian multipliers.
- ADMM or augmented Lagrangian: coordinate separable blocks with consensus variables.
- Progressive hedging: scenario decomposition for stochastic programs.
- Rolling horizon or temporal decomposition: solve moving windows with state carryover.

Selection notes:

- Use Benders when few linking variables drive many independent subproblems.
- Use column generation when the natural variable set is huge but pricing is tractable.
- Use Lagrangian relaxation when relaxing a few hard constraints creates easy subproblems and useful bounds.
- Use progressive hedging for scenario separability when nonanticipativity constraints couple scenarios.
- Use rolling horizon when exact global optimization is too large but state transitions are local.
