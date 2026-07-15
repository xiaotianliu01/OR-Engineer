# Simulation Optimization Framework Guide

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a general scaffold for optimizing decisions through simulation. It is intentionally not runnable until the task-specific simulator, policy class, search method, baselines, and evaluation logic are implemented.

## Industrial Implementation Contract

Do not use this asset to present naive random search or one noisy simulation replication as an industrial solution. A serious deployment must implement the actual simulator interface, stochastic seed control, replications, common random numbers when useful, strong baseline policies, confidence intervals or uncertainty estimates, separate optimization and final-evaluation seeds, and a justified policy parameterization. If the search space is narrow, label it as baseline or interim unless higher-ceiling alternatives are rejected with evidence.

Use it for:

- discrete-event simulation optimization,
- stochastic rollout evaluation,
- black-box policy search,
- Bayesian optimization,
- SPSA and stochastic approximation,
- ranking and selection,
- evolutionary or local search with simulation evaluations,
- surrogate-assisted optimization,
- common-random-number benchmark studies.

Adaptation flow:

1. Define simulator state, inputs, stochastic processes, outputs, and feasibility checks.
2. Define candidate decision or policy parameterization in `policies/`.
3. Select search method from `search/search_catalog.md`.
4. Implement strong baseline policies in `baselines/`.
5. Implement replication, seed, and common-random-number control.
6. Implement pilot and `run` selection logic in `runners/`.
7. Evaluate final candidates with fresh out-of-sample replications and confidence intervals.
8. Save trajectories, metrics, seed manifests, candidate history, and selection decisions under `run_records/`.

Minimum acceptance criteria:

- Compare against meaningful baselines, not only do-nothing or arbitrary random candidates.
- Use multiple replications and confidence intervals when noise matters.
- Keep optimization and final evaluation random seeds separated.
- Label narrow policy search as baseline or limited-ceiling unless the policy class is justified.
