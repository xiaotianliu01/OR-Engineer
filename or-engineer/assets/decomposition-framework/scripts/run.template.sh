#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print iteration, lower/upper bounds, gap, cut/column counts,
# feasibility, elapsed time, and output paths.

python -m project.runners.decompose \
  --phase run \
  --decomposition-config configs/decomposition_config.yaml \
  --solver-config configs/solver_config.yaml \
  --output-dir runs/run
