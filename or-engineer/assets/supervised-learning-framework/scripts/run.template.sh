#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print epoch/step, elapsed time, train loss, validation metric,
# current best metric, and output paths while appending structured records to run_records/.

python -m project.runners.train \
  --phase run \
  --experiment-config configs/experiment_config.yaml \
  --model-config configs/model_config.yaml \
  --output-dir runs/run
