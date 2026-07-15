#!/usr/bin/env bash
set -euo pipefail

# Copy this asset into a deployment workspace, implement the contracts,
# then replace the module path below with the task-specific decomposition entrypoint.

python -m project.runners.decompose \
  --decomposition-config configs/decomposition_config.yaml \
  --solver-config configs/solver_config.yaml
