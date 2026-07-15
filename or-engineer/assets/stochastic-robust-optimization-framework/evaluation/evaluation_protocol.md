# Evaluation Protocol

Report:

- in-sample objective,
- out-of-sample expected objective,
- service level or chance-constraint violation rate,
- risk metrics such as CVaR or worst-case cost,
- feasibility violation frequency and magnitude,
- sensitivity to scenario count, risk level, ambiguity radius, or uncertainty-set budget,
- comparison to deterministic, nominal, robust, stochastic, and heuristic baselines, reported one method at a time.

Baseline reporting:

- each deterministic, nominal, robust, stochastic, or heuristic comparator needs its own definition and result row,
- include scenario information, risk settings, feasibility status, and objective/risk metrics for each comparator,
- do not collapse all comparators into a single aggregate row,
- interpret which comparator performed better by pointing to the individual comparator rows.

Use:

- common random numbers for fair method comparison,
- held-out scenarios for final evaluation,
- confidence intervals when sampling noise affects conclusions,
- realized-trajectory benchmarks when possible.
