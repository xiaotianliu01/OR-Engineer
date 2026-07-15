# General DRL-MDP Framework Asset

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a reusable scaffold for solving Markov decision process, partially observed MDP, constrained MDP, and multi-agent MDP problems with deep reinforcement learning. It is intentionally general and is not expected to run before a concrete task supplies the missing task-specific pieces.

## Industrial Implementation Contract

Do not use this asset to create a toy RL demo, a tiny arbitrary policy, or a run that only proves the training loop starts. A serious deployment must implement the real state/action/reward/transition contract, feasibility handling, baseline policies, evaluation scenarios, convergence diagnostics, seed control, checkpointing, a credible fallback policy or method, and compact run records. Training must periodically evaluate the policy on fixed validation/evaluation seeds, save the best checkpoint whenever the selected metric improves, and run final evaluation from that best checkpoint rather than the last training state. The pilot must show meaningful learning or objective improvement against at least one strong baseline before handing off the user-facing `run` command. If learning remains unstable or underperforms after the allowed redesign attempts, the deployment must evaluate and select or recommend the pre-declared fallback method instead of packaging an unstable RL policy as production-ready.

Concrete tasks must supply:

- an environment implementation,
- state and observation definitions,
- action spaces and feasibility rules,
- reward or cost functions,
- data loaders or simulators,
- selected algorithm implementations,
- training and evaluation budgets.

Use it as the default layout when an OR task selects DRL, approximate dynamic programming, actor-critic, PPO-style training, or multi-agent RL as the deployment method.

## Development Flow

1. Copy this whole asset into the task workspace.
2. Fill `envs/` with the confirmed MDP or multi-agent MDP interface.
3. Fill `data/` only if the problem needs offline trajectories, historical logs, scenario files, simulator parameters, or exogenous processes.
4. Select an algorithm family from `algorithms/algorithm_catalog.md`.
5. Implement policy, value, Q, world-model, or centralized-critic networks under `networks/`.
6. Implement training and evaluation loops under `runners/`.
7. Configure experiments under `configs/`.
8. Define the fallback policy or method before pilot runs. Record its id, implementation route, dependencies, evaluation protocol, acceptance threshold, and trigger condition in the run configuration.
9. Run smoke and pilot configurations locally, including periodic evaluation and best-checkpoint saving, then prepare user-facing `run` commands using `scripts/`.
10. Record every run with the templates under `run_records/`.
11. Evaluate against strong baselines, lower bounds, fallback candidates, or task-specific benchmarks using `evaluation/`.

## Non-Negotiable Contracts

- Do not treat a successful script start as policy quality.
- Define acceptance criteria before `run` training.
- Save and finally evaluate the best validation/evaluation checkpoint; keep the last checkpoint only as a diagnostic artifact unless it is also the best.
- Record learning curves, evaluation curves, losses where available, feasibility violations, and seed variability.
- Keep the online policy and any hindsight or lower-bound benchmark clearly separated.
- If a pilot only beats a weak diagnostic baseline or loses to a strong baseline, run a few targeted redesign attempts when the approved budget allows before recommending the user-facing `run`. Typical first changes are evaluation interval, reward scaling, observation normalization, action encoding, exploration/entropy, learning rate, rollout or batch size, model capacity, total timesteps, warm start, residual anchor, or feasibility projection.
- Provide a credible fallback method for training instability. Prefer a tuned structural policy, myopic or rolling-horizon optimization, incumbent policy, residual anchor policy, exact-repair policy, fitted value/tree policy, or other lower-risk method that can be evaluated under the same seeds and feasibility rules. A do-nothing policy is only a fallback when it is the real incumbent or a valid operational policy; otherwise it is just a diagnostic baseline.
