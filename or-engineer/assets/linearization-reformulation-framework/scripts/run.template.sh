#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print block name, reformulation pattern, approximation error,
# original-feasibility violation, elapsed time, and output paths.

python -m project.runners.reformulate \
  --phase run \
  --reformulation-config configs/reformulation_config.yaml \
  --validation-config configs/validation_config.yaml \
  --output-dir runs/run
