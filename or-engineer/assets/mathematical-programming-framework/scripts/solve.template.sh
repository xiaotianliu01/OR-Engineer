#!/usr/bin/env bash
set -euo pipefail

# Copy this asset into a deployment workspace, implement the contracts,
# then replace the module path below with the task-specific solve entrypoint.

python -m project.runners.solve \
  --model-config configs/model_config.yaml \
  --solver-config configs/solver_config.yaml
