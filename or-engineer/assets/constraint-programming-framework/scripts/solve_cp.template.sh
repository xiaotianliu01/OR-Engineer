#!/usr/bin/env bash
set -euo pipefail

# Copy this asset into a deployment workspace, implement the contracts,
# then replace the module path below with the task-specific CP solve entrypoint.

python -m project.runners.solve_cp \
  --model-config configs/cp_model_config.yaml \
  --solver-config configs/cp_solver_config.yaml
