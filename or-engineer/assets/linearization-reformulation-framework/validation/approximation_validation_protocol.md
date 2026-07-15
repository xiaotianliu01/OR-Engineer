# Approximation Validation Protocol

For each transformed expression, report:

- original expression and domain,
- transformed formulation,
- exactness class: exact, relaxation, inner approximation, outer approximation, or heuristic approximation,
- required bounds and how they were derived,
- maximum, mean, and percentile approximation error on validation points,
- feasibility direction: conservative, permissive, or neither,
- sensitivity to segment count, domain range, and big-M values,
- numerical scaling risks.

When the transformed model is used for decisions:

- evaluate decisions in the original nonlinear expression when possible,
- report violation or error in original units,
- compare several segment counts or bound choices when the approximation can change the decision.
