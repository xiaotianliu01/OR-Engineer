#!/usr/bin/env bash
set -euo pipefail

# Foreground result-collection template. Keep final analysis data compact.

python -m project.runners.collect_results \
  --run-dir runs/run \
  --progress runs/run/progress.csv \
  --status runs/run/status.json \
  --output runs/run/results/summary.json
