# Single-Agent Algorithm Slot

Place selected single-agent implementations here.

Typical subfolders to add when needed:

- `dqn/`
- `rainbow/`
- `ppo/`
- `trpo/`
- `a2c_a3c/`
- `ddpg/`
- `td3/`
- `sac/`
- `constrained_rl/`
- `model_based/`
- `planning/`

Each implementation should expose:

- policy or actor,
- value/Q/critic module,
- replay or rollout buffer,
- update function,
- save/load functions,
- metric dictionary with losses, entropy, value estimates, constraint diagnostics, and timing.

