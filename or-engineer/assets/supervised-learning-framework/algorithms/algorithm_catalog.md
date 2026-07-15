# Algorithm Catalog

Use this catalog to choose candidate supervised learning families. Do not default to a deep model unless it has a plausible advantage over simpler baselines.

## Mean Regression

- Linear regression, ridge, lasso, elastic net.
- Generalized linear models for non-Gaussian targets.
- Generalized additive models or spline models when smooth nonlinear effects matter.
- Random forest, extra trees, gradient boosted trees.
- Neural MLPs for dense tabular features.
- Multi-task or multi-output regressors for correlated targets.

## Quantile And Distributional Regression

- Linear quantile regression.
- Gradient boosted quantile regression.
- Neural quantile regression with pinball loss.
- Distributional models predicting parameters of a likelihood.
- Conformalized quantile regression or split conformal intervals.
- Mixture density networks when the conditional distribution is multi-modal.

## Forecasting

- Naive, seasonal naive, moving average, exponential smoothing, ARIMA/SARIMAX.
- Tree or linear models with lag, rolling-window, calendar, and exogenous features.
- Sequence neural networks: RNN, GRU, LSTM, TCN.
- Attention or Transformer-style forecasters.
- N-BEATS, N-HiTS, DeepAR-style probabilistic forecasting, Temporal Fusion Transformer-style models.
- Global models trained across many related series.

## Classification And Ranking

- Logistic regression, calibrated linear classifiers.
- Tree ensembles and gradient boosting.
- Neural classifiers for dense, sequence, image, text, or embedding inputs.
- Pairwise or listwise ranking models.
- Cost-sensitive classification when downstream costs are asymmetric.

## Surrogate And Decision-Aware Models

- Supervised surrogate models for expensive simulation or optimization.
- Learned priority scores or imitation of expert or solver decisions.
- Two-stage predict-then-optimize models.
- Decision-aware losses when downstream objective gradients or counterfactual evaluation are available.

## Selection Heuristics

- Start with a strong simple baseline and one high-capacity candidate.
- Prefer tree ensembles for medium tabular data with mixed feature types.
- Prefer deep sequence models when long histories, many related series, embeddings, or high-dimensional inputs matter.
- Prefer quantile or distributional objectives when downstream decisions need risk, service-level, or interval information.
- Use calibration and downstream decision metrics when prediction errors have asymmetric consequences.
