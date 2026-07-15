#!/usr/bin/env bash
set -euo pipefail

# Replace the module path with the task-specific prediction entrypoint.

python -m project.runners.predict \
  --run-dir runs/selected_run \
  --input-path data/prediction_input.parquet \
  --output-path runs/selected_run/predictions/predictions.parquet
