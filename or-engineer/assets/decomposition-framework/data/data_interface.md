# Data Interface Notes

Define decomposition partitions explicitly.

Record:

- partition dimension: scenario, time block, resource, customer, route, asset, or region,
- coupling variables and coupling constraints,
- subproblem data files or slices,
- master data files or slices,
- shared parameter assumptions,
- parallel execution requirements,
- deterministic seed and partition ordering.

Keep raw data outside the reusable asset and store partition manifests in the deployment run folder.
