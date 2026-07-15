#!/usr/bin/env bash
set -euo pipefail

# Copy this asset into a deployment workspace, implement the contracts,
# then replace the module path below with the task-specific training entrypoint.

python -m project.runners.train \
  --experiment-config configs/experiment_config.yaml \
  --model-config configs/model_config.yaml
