#!/usr/bin/env bash
set -euo pipefail

# Copy this asset into a deployment workspace, implement the contracts,
# then replace the module path below with the task-specific uncertainty optimization entrypoint.

python -m project.runners.solve_uncertain \
  --uncertainty-config configs/uncertainty_config.yaml \
  --optimization-config configs/optimization_config.yaml
