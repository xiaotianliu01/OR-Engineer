#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print status, incumbent objective, bound, gap, nodes/iterations,
# elapsed time, and output paths while appending structured records to run_records/.

python -m project.runners.solve \
  --phase run \
  --model-config configs/model_config.yaml \
  --solver-config configs/solver_config.yaml \
  --output-dir runs/run
