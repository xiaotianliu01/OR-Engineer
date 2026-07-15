# Evaluation Protocol

Evaluate both formulation quality and solve quality.

Formulation quality:

- exactness or approximation direction,
- safe bounds and big-M tightness,
- approximation error by region,
- relaxation strength,
- numerical scaling.

Solve quality:

- solver status and gap,
- feasibility in transformed model,
- feasibility in original model,
- objective value in transformed and original objective when different,
- sensitivity to reformulation settings.

Baseline reporting:

- compare original nonlinear, relaxed, approximated, heuristic, and exact-small-instance benchmarks separately when they are available,
- include each comparator's formulation meaning, approximation direction, settings, objective, feasibility, and status,
- do not report an aggregate comparator result across different formulations,
- interpret which formulation performed better by pointing to the individual comparator rows.

Do not report a transformed model as valid unless the approximation or relaxation meaning is explicit.
