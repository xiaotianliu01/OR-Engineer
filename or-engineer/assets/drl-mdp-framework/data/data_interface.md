# Data Interface Notes

Use this folder only for general loaders or small task-local examples after copying the asset.

Common data inputs:

- simulator parameters,
- transition model parameters,
- offline state-action-reward trajectories,
- expert demonstrations,
- exogenous scenario traces,
- train/evaluation seeds,
- benchmark trajectories.

Do not store large operational data in the reusable asset. Store task data in the deployment workspace and record paths in `run_records/run_config.json`.
