# Search Catalog

Simulation optimization methods:

- grid or factorial design for low-dimensional policy classes,
- random search as diagnostic baseline or simple search,
- local search and variable neighborhood search,
- simulated annealing,
- tabu search,
- genetic algorithms and evolutionary strategies,
- cross-entropy method,
- SPSA and stochastic approximation,
- Bayesian optimization,
- ranking and selection,
- optimal computing budget allocation,
- surrogate-assisted optimization,
- rollout or approximate policy iteration when a simulator supports sequential decisions.

Selection notes:

- Use common random numbers for fair candidate comparisons when possible.
- Use Bayesian optimization or surrogate assistance when evaluations are expensive and parameter dimension is moderate.
- Use SPSA when gradient-free stochastic approximation is appropriate.
- Use ranking and selection when choosing among a finite set of candidates.
- Treat random search as baseline unless the search space and quality target justify it.
