# Evaluation Protocol

Before training:

- define primary metric,
- define secondary diagnostics,
- define baseline models,
- define fallback model or rule for training instability,
- define acceptance threshold,
- define split logic and leakage checks.

During training:

- monitor train and validation loss,
- monitor the primary deployment metric,
- monitor calibration or coverage when predictions include probabilities or intervals,
- save best model by validation or downstream metric whenever that metric improves,
- record best epoch/step, best metric, best model path, and last model path,
- stop or redesign when validation quality degrades or fails to beat a strong baseline.
- evaluate the fallback model when the best model fails the quality gate, validation is unstable, leakage checks fail, or redesign attempts are exhausted.

Final evaluation:

- load the best saved model by default and report test metrics only once for that selected model,
- report last-model metrics separately only when diagnosing overfitting or degradation,
- include baseline comparison with one row per baseline model or rule,
- include fallback comparison and activation status when training instability is possible,
- report confidence intervals, bootstrap intervals, or repeated-split variability when useful,
- report subgroup, horizon, or entity-level slices,
- report downstream OR objective when predictions feed optimization.

Baseline reporting:

- define every baseline with a unique id, model/rule description, feature set, split protocol, fixed settings or tuning budget, and status,
- report every baseline separately on the same metrics and splits as the selected model,
- do not replace multiple baselines with an aggregate baseline result,
- interpret which baseline performed better by pointing to the individual baseline rows.

Fallback reporting:

- define the fallback model before training pilots, including model id, role, feature set, dependency status, and configuration,
- evaluate the fallback under the same train/validation/test split, leakage rules, target timing, and downstream OR metric when relevant,
- activate or recommend the fallback when the best saved model fails the quality gate, validation curves are unstable, split variability exceeds tolerance, leakage checks fail, or redesign attempts are exhausted,
- report whether the selected handoff model is `primary`, `fallback`, `ensemble_or_hybrid`, `preliminary`, or `none`.

For forecasting:

- use rolling-origin or cutoff-based evaluation that matches deployment timing,
- report per-horizon metrics,
- compare against naive and seasonal naive baselines.

For quantile or interval models:

- report pinball loss,
- report empirical coverage,
- report interval width,
- check quantile crossing.
