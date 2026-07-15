# Data Interface Notes

Reformulation quality depends on valid bounds and representative operating ranges.

Record:

- variable lower and upper bounds,
- units and scaling,
- empirical ranges from data,
- theoretical bounds from constraints,
- domain truncation choices,
- breakpoint generation rules,
- calibration or validation samples.

Do not use arbitrary big-M constants. If a bound is unknown, record it as a blocker or derive a conservative bound from the confirmed formulation.
