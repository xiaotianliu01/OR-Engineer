#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print scenario count, solver status, objective, violation rate,
# risk metric, baseline gap, elapsed time, and output paths.

python -m project.runners.solve_uncertain \
  --phase run \
  --uncertainty-config configs/uncertainty_config.yaml \
  --optimization-config configs/optimization_config.yaml \
  --output-dir runs/run
