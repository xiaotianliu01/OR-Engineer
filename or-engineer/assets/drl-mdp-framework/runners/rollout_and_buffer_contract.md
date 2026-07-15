# Rollout And Buffer Contract

On-policy methods typically need rollout buffers with:

- observations,
- actions,
- rewards or costs,
- next observations,
- dones or truncation flags,
- values,
- log probabilities,
- masks,
- recurrent states when used,
- centralized states for CTDE.

Off-policy methods typically need replay buffers with:

- transitions,
- priorities when used,
- n-step returns when used,
- behavior policy metadata for offline or importance sampling,
- episode identifiers.

Multi-agent methods often need:

- per-agent observations,
- global state,
- joint actions,
- agent masks,
- unavailable-action masks,
- team and individual rewards.

