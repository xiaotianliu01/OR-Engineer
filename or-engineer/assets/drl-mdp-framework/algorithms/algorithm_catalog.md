# Algorithm Catalog

Use this catalog during method selection and deployment planning. Do not implement every algorithm. Select the smallest set that can plausibly meet the confirmed quality target.

## Single-Agent Online RL

- Value-based: DQN, Double DQN, Dueling DQN, Prioritized Replay DQN, NoisyNet DQN, Rainbow, QR-DQN, C51.
- Policy gradient: REINFORCE, vanilla policy gradient, natural policy gradient.
- Actor-critic: A2C, A3C, PPO, TRPO.
- Continuous control: DDPG, TD3, SAC, MPO.
- Recurrent or partial-observation variants: DRQN, recurrent PPO, recurrent SAC.
- Constrained RL: primal-dual PPO, CPO, Lagrangian SAC, safety-layer methods.
- Risk-sensitive RL: CVaR policy optimization, distributional objectives, robust MDP methods.

## Single-Agent Offline, Imitation, And Hybrid RL

- Offline RL: BCQ, BEAR, CQL, IQL, TD3+BC, AWAC.
- Imitation: behavior cloning, DAgger, GAIL, AIRL.
- Hybrid: behavior-cloning warm start, residual RL around a baseline, RL with exact feasibility repair, model-predictive rollout policy improvement.

## Model-Based And Planning

- Dyna-style model-based RL.
- MBPO and learned dynamics ensembles.
- Dreamer-style latent dynamics when observations are high-dimensional.
- MCTS, AlphaZero-style planning, and learned value-guided tree search.
- MPC with learned value terminal costs.

## Multi-Agent RL

- Independent learners: IQL, IPPO, independent SAC.
- Centralized training with decentralized execution: MADDPG, MATD3, MAPPO, HAPPO, HATRPO, COMA.
- Value decomposition: VDN, QMIX, QTRAN, QPLEX, WQMIX.
- Communication and coordination: CommNet, DIAL, TarMAC, MAAC, graph-based MARL.
- Mean-field MARL for many-agent systems.
- Opponent modeling and self-play for competitive or mixed games.

## Selection Notes

- Use value-based methods for small discrete action spaces.
- Use PPO or SAC as strong defaults for continuous or high-dimensional actions.
- Use constrained RL when feasibility cannot be handled by simple projection.
- Use offline RL only when logged trajectories cover the relevant state-action distribution.
- Use MAPPO or CTDE methods when agents share global objectives or require coordination.
- Use value decomposition for cooperative discrete-action multi-agent tasks.
- Use model-based RL or planning when simulator calls are expensive and a predictive model can be learned safely.

