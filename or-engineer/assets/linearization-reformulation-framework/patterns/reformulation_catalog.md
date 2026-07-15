# Reformulation Catalog

Exact or near-exact patterns:

- Binary-continuous product: use linking constraints or McCormick with binary bounds.
- Continuous bilinear product: use McCormick relaxation over bounded boxes.
- Logical implication: use indicator constraints when supported, otherwise calibrated big-M.
- Either-or disjunction: use binary activation and convex hull or big-M formulation.
- Absolute value and max/min: use epigraph formulations when convex.
- Piecewise-linear convex functions: use epigraph, SOS2, or lambda formulation.
- Piecewise-linear nonconvex functions: use binary segment selection.
- Fixed-charge terms: use binary activation and tight variable upper bounds.
- Perspective strengthening: use for on/off convex costs when a binary activates a convex expression.
- Complementarity: use big-M, SOS1, indicator constraints, or MPEC handling with clear risk notes.
- Norm and quadratic constraints: use SOCP or convex QP when structure permits.

Documentation required:

- original expression,
- transformed constraints,
- exactness class,
- required bounds,
- solver feature requirements,
- known numerical risks,
- validation tests.
