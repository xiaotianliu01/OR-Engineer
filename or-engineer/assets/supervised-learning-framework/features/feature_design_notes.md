# Feature Design Notes

Feature logic is task-specific and should be implemented after copying the asset.

Common feature families:

- static entity attributes,
- calendar and event features,
- lag and rolling-window features,
- known future covariates,
- historical forecasts and errors,
- categorical encodings,
- embeddings,
- text, image, or sensor-derived representations.

Feature governance:

- Mark each feature as available or unavailable at prediction time.
- Keep target transformations reversible when predictions must be reported in original units.
- Save encoder, scaler, imputer, vocabulary, and feature-order metadata with the model.
- Record feature importance, ablations, or sensitivity checks when they affect trust or deployment.
