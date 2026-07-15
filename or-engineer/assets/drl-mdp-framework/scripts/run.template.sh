#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print step, elapsed time, reward/cost, losses, feasibility metrics,
# current best metric, and output paths while appending structured records to run_records/.

python -m project.runners.train \
  --phase run \
  --config configs/experiment_config.yaml \
  --output-dir runs/run
