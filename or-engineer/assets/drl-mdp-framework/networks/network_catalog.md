# Network Catalog

Select architectures from the confirmed observation, action, and algorithm requirements.

Common modules:

- MLP policy/value networks for vector observations.
- CNN encoders for image-like observations.
- RNN, GRU, or LSTM encoders for partial observability.
- Transformer or attention encoders for sets, sequences, graphs, or many entities.
- Graph neural networks for relational state.
- Gaussian, beta, categorical, multi-discrete, or autoregressive action heads.
- Q networks, twin Q networks, dueling heads, distributional heads.
- Centralized critics for CTDE multi-agent methods.
- World models for model-based RL.
- Constraint or feasibility heads for safety layers.

Document:

- input shapes,
- output distributions,
- action squashing or scaling,
- normalization,
- initialization,
- parameter count,
- shared vs per-agent weights,
- save/load format.

