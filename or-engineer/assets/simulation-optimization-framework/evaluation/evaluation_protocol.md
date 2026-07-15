# Evaluation Protocol

Report:

- mean objective and standard error,
- confidence interval,
- feasibility violation frequency and magnitude,
- best candidate and incumbent history,
- baseline comparison under common random numbers with one row per baseline policy,
- out-of-sample evaluation with fresh seeds,
- runtime per simulation and total simulation budget,
- sensitivity to replication count or policy parameterization.

For baseline reporting:

- define each baseline policy separately, including policy logic, parameter settings, seed/scenario usage, and feasibility handling,
- report every baseline's mean objective, uncertainty, feasibility, and runtime status,
- do not report an aggregate baseline value among several policies,
- interpret which policy performed better by pointing to the individual baseline rows.

Selection rules:

- Do not choose a candidate from noisy estimates without enough replications.
- Use paired tests or confidence intervals when differences are small.
- If the best candidate only beats weak diagnostic baselines, redesign the policy class or search before final deployment.
