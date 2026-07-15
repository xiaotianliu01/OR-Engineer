# Data Interface Notes

Simulation optimization inputs may include:

- simulation instance files,
- stochastic process parameters,
- initial states,
- candidate policy definitions,
- scenario traces,
- optimization seed sets,
- final evaluation seed sets,
- baseline definitions.

Keep large trajectories outside the reusable asset. Store run paths and seed manifests in `run_records/run_config.json`.
