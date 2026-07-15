# Replication And Randomness Notes

Simulation optimization must control stochastic noise.

Record:

- random seed streams,
- replication count,
- optimization seed set,
- final evaluation seed set,
- common-random-number pairing,
- warm-up period,
- horizon length,
- stochastic process assumptions,
- trajectory-level outputs retained for audit.

Use separate random seeds for search and final evaluation unless the method explicitly requires paired comparisons.
