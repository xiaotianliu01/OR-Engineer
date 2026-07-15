# Data Interface Notes

Use this folder for task-specific data loading after copying the asset.

Every solver deployment should define:

- source tables and files,
- entity sets and index keys,
- time horizon and time units,
- parameter units and default values,
- missing-value handling,
- deterministic versus uncertain parameters,
- validation checks before model construction.

Keep raw data outside the reusable asset. Record deployment data paths and schema summaries in `run_records/run_config.json`.
