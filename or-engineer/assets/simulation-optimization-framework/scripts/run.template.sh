#!/usr/bin/env bash
set -euo pipefail

# Foreground run template. Replace the module path after implementing the task.
# The command should print candidate id, replications, mean objective, uncertainty,
# baseline gap, current best, elapsed time, and output paths.

python -m project.runners.simulate_optimize \
  --phase run \
  --simulation-config configs/simulation_config.yaml \
  --search-config configs/search_config.yaml \
  --output-dir runs/run
