#!/usr/bin/env bash
set -euo pipefail

# Copy this asset into a deployment workspace, implement the contracts,
# then replace the module path below with the task-specific simulation optimization entrypoint.

python -m project.runners.simulate_optimize \
  --simulation-config configs/simulation_config.yaml \
  --search-config configs/search_config.yaml
