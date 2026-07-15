# Evaluation Protocol

Every DRL deployment should define:

- primary metric,
- strong baseline policies,
- lower-bound or hindsight benchmark when available,
- fixed evaluation seeds or trajectories,
- evaluation interval used during training,
- best-checkpoint selection metric and direction,
- number of episodes or scenarios,
- confidence intervals or seed variability,
- feasibility threshold,
- stress tests and out-of-distribution checks,
- acceptance, failure, redesign, and fallback activation rules.

Recommended output tables:

- per-episode or per-trajectory metrics,
- aggregate mean, median, standard deviation, best, worst,
- baseline gap for each baseline policy separately,
- fallback-method metrics and selection decision when training is unstable or fails,
- lower-bound gap,
- constraint diagnostics,
- runtime and inference latency.

Checkpoint selection:

- evaluate the policy periodically during training on fixed held-out seeds or scenarios,
- save a new best checkpoint whenever the primary validation/evaluation metric improves,
- record best metric, best step, best checkpoint path, and last checkpoint path in run records,
- run final evaluation from the best checkpoint by default,
- report best-versus-last behavior when policy quality degrades after the best checkpoint.

Baseline reporting:

- define every baseline policy separately, including state information used, action rule, tuning, seed/evaluation episodes, and feasibility repair,
- report each baseline policy's episode/trajectory and aggregate metrics,
- do not report an aggregate baseline value across several policies,
- interpret which policy performed better by pointing to the individual baseline rows.

Fallback reporting:

- define the fallback candidate before training pilots, including method id, role, implementation, dependency status, and configuration,
- evaluate the fallback on the same seeds, trajectories, horizon, feasibility repair, and metric convention as the learned policy unless a documented reason makes this impossible,
- activate or recommend the fallback when the best checkpoint fails the quality gate, learning curves are unstable, seed variability exceeds the declared tolerance, dependency setup fails, or redesign attempts are exhausted,
- report whether the selected handoff method is `primary`, `fallback`, `hybrid`, `preliminary`, or `none`.
