# Data Interface Notes

Use this folder for general loaders and task-local examples after copying the asset.

Common inputs:

- tabular feature tables,
- target or label tables,
- time-series panels,
- exogenous covariates,
- historical forecasts or decisions,
- expert or solver-generated labels,
- train, validation, test, and prediction-set keys.

Do not store large task data in the reusable asset. Store task data in the deployment workspace and record paths in `run_records/run_config.json`.

Every supervised task should define:

- entity key,
- time key when relevant,
- target columns,
- feature columns,
- sample weights,
- unavailable-at-prediction-time columns,
- train/validation/test split logic.
