# Model Catalog

Implement only the families selected for the confirmed task.

Linear and statistical:

- linear, ridge, lasso, elastic net,
- logistic regression,
- GLM and GAM,
- ARIMA/SARIMAX and state-space models.

Tree and ensemble:

- decision trees,
- random forest and extra trees,
- gradient boosting,
- XGBoost, LightGBM, CatBoost when available,
- quantile forests or quantile boosting.

Neural:

- MLP for tabular or embedding features,
- CNN for spatial or image-like inputs,
- RNN, GRU, LSTM, TCN for sequences,
- Transformer-style encoders,
- N-BEATS and N-HiTS style forecasting blocks,
- multi-task heads,
- quantile heads,
- distributional heads.

Model selection rule:

- A complex model should be kept only if it improves the relevant validation and downstream metrics enough to justify implementation, runtime, maintenance, and interpretability cost.
