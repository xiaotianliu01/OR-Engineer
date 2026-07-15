# Environment Design Notes

Fill this section for every concrete MDP:

- State: variables needed for Markov sufficiency.
- Observation: what the policy sees.
- Action: discrete, continuous, hybrid, bounded, or constrained.
- Feasibility: projection, repair, rejection, safety layer, or constrained policy.
- Transition: deterministic and stochastic parts.
- Exogenous process: demand, arrivals, disturbances, opponents, market states, sensor noise, or scenario generator.
- Reward/cost: sign convention, scaling, terminal terms, penalties, and constraint costs.
- Episode: horizon, terminal states, truncation, reset distribution.
- Info dict: diagnostics required for evaluation and debugging.
- Baselines: simple policies, current policy, lower bounds, or expert demonstrations.

