# Splitting And Leakage Notes

Choose splits before model tuning.

Common split types:

- Random split for exchangeable observations.
- Grouped split when entities must not leak across train and test.
- Time split when predictions will be made after a cutoff date.
- Rolling-origin split for forecasting.
- Nested cross-validation when hyperparameter tuning risk is high.

Leakage checks:

- Remove target-derived columns from features.
- Remove future observations from lag or rolling-window features.
- Fit scalers, encoders, imputers, target encoders, and feature selectors on training data only.
- Keep test data untouched until the final selected model is evaluated.
- Record every split key and cutoff in the run config.
