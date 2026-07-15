# Forecasting Algorithm Slot

Fill this folder when observations have a deployment-time ordering.

Recommended candidates:

- naive and seasonal naive baselines,
- rolling mean or exponential smoothing,
- ARIMA/SARIMAX or state-space models,
- lag-feature linear or tree models,
- global gradient boosting models across many series,
- RNN, LSTM, GRU, TCN, Transformer, N-BEATS, N-HiTS, DeepAR-style, or Temporal Fusion Transformer-style neural models,
- quantile or distributional forecasting when decisions require risk-aware forecasts.

Document:

- forecast horizon,
- lookback length,
- known future covariates,
- unknown future covariates,
- rolling-origin evaluation,
- leakage boundaries,
- reconciliation or hierarchy rules if forecasts must aggregate.
