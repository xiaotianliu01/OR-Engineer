#!/usr/bin/env bash
set -euo pipefail

# Copy this asset into a deployment workspace, implement the contracts,
# then replace the module path below with the task-specific reformulation entrypoint.

python -m project.runners.reformulate \
  --reformulation-config configs/reformulation_config.yaml \
  --validation-config configs/validation_config.yaml
