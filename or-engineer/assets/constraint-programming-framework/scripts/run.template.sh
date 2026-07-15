#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print solver status, objective, bound, gap, conflicts, branches,
# feasibility metrics, elapsed time, and output paths.

python -m project.runners.solve_cp \
  --phase run \
  --model-config configs/cp_model_config.yaml \
  --solver-config configs/cp_solver_config.yaml \
  --output-dir runs/run
