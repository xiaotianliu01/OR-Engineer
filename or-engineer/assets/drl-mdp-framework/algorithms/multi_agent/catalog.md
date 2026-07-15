# Multi-Agent Algorithm Slot

Place selected multi-agent implementations here.

Typical subfolders to add when needed:

- `independent_q_learning/`
- `independent_ppo/`
- `maddpg/`
- `matd3/`
- `mappo/`
- `happo_hatrpo/`
- `coma/`
- `vdn/`
- `qmix/`
- `qtran/`
- `qplex/`
- `communication/`
- `mean_field/`

For CTDE methods, define:

- per-agent observations,
- shared global state if available,
- per-agent action spaces,
- centralized critic inputs,
- decentralized execution policy outputs,
- agent masks and unavailable-action masks when relevant,
- team reward or individual rewards,
- coordination diagnostics.

