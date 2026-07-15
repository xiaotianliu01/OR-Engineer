# Loss And Metric Catalog

Mean regression:

- MSE, RMSE, MAE, Huber, Poisson or Gamma deviance, weighted variants.

Quantile and interval regression:

- pinball loss,
- weighted pinball loss,
- quantile crossing penalty,
- interval score,
- prediction interval coverage,
- conformal calibration diagnostics.

Forecasting:

- MAE, RMSE, MAPE, sMAPE, WAPE, MASE,
- horizon-weighted errors,
- rolling-origin aggregate metrics,
- service-level or inventory-cost proxy metrics when forecasts feed decisions.

Classification:

- cross entropy, focal loss, Brier score,
- accuracy, precision, recall, F1,
- ROC-AUC, PR-AUC,
- calibration error and reliability curves.

Ranking:

- pairwise logistic loss,
- NDCG, MAP, recall at K,
- downstream value or cost at K.

Decision-aware evaluation:

- report the downstream objective, feasibility, and regret whenever predictions drive optimization or operational decisions.
