# Data Interface Notes

Uncertainty optimization data should separate:

- historical observations,
- forecasts,
- residuals or errors,
- scenario generation inputs,
- in-sample optimization scenarios,
- out-of-sample evaluation scenarios,
- scenario probabilities,
- known future covariates,
- realized trajectory samples for evaluation.

Record the timing of information: what is known at each decision stage and what is revealed later.
