# Supervised Learning Framework Guide

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a general scaffold for supervised learning in OR workflows. It is intentionally not runnable until task-specific data, features, labels, models, and evaluation logic are implemented.

## Industrial Implementation Contract

Do not use this asset to create a toy predictor, a tiny arbitrary neural network, or a model that only reports training loss. A serious deployment must implement leakage-safe data splits, prediction-time feature availability checks, strong statistical or business baselines, calibrated metrics for the target type, downstream decision metrics when predictions feed optimization, reproducible configs, terminal progress output, a credible fallback model or rule, and compact result records. Training must monitor validation or downstream metrics at intervals, save the best model when the selected metric improves, and run final evaluation from that best saved model rather than the last epoch. Keep a simpler model when it beats the deep model under the acceptance criteria. If neural or high-variance training remains unstable after targeted redesign attempts, evaluate and select or recommend the pre-declared fallback model rather than handing off an unstable last model.

Use it for:

- mean regression,
- quantile or interval regression,
- demand and time-series forecasting,
- classification,
- ranking or scoring,
- surrogate models that feed an optimizer,
- imitation targets derived from historical decisions.

Adaptation flow:

1. Define the supervised target: mean, quantile, probability, class, rank, score, or vector output.
2. Define data schema, entity keys, time keys, grouping keys, and leakage boundaries.
3. Choose train/validation/test splitting rules before model selection.
4. Select candidate model families from `algorithms/algorithm_catalog.md`.
5. Implement feature generation in `features/`.
6. Implement data loading in `data/`.
7. Implement models in `models/`.
8. Implement task losses and metrics in `losses/`.
9. Implement training, evaluation, and prediction loops in `runners/`.
10. Define the fallback model, rule, or optimizer-assisted route before pilot runs. Record its id, dependency status, feature requirements, metric threshold, and trigger condition in the run configuration.
11. Run smoke and pilot configurations locally, including validation monitoring and best-model saving, then prepare user-facing `run` commands using `scripts/`.
11. Save structured run artifacts under `run_records/` compatible output folders.

Minimum acceptance criteria:

- Compare against a simple but meaningful baseline, such as naive seasonal forecast, historical mean, current business rule, linear model, or strong tree model.
- Report out-of-sample metrics on the split that matches deployment timing.
- For quantile or interval models, report both accuracy and calibration or coverage.
- For models feeding optimization, report downstream decision quality, not only prediction loss.
- If a deep model does not beat a strong simpler model, keep the simpler model or redesign the deep model before final deployment. When approved runtime remains, do a few targeted redesign attempts before declaring the training route failed; typical changes include learning rate, batch size, model capacity, regularization, feature set, target transform, loss, early-stopping patience, training epochs, and split or leakage corrections.
- Provide a credible fallback for training instability. Prefer a strong statistical model, tree/boosting model, linear/regularized model, incumbent business rule, naive or seasonal forecast when appropriate, or downstream optimizer with conservative inputs. The fallback must be evaluated with the same split, leakage rules, target timing, and downstream OR metric when relevant.
