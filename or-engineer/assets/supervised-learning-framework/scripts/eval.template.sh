#!/usr/bin/env bash
set -euo pipefail

# Replace the module path with the task-specific evaluation entrypoint.

python -m project.runners.evaluate \
  --run-dir runs/selected_run \
  --split test
