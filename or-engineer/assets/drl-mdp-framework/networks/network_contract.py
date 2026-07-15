"""Neural network module contract.

Implement selected modules with PyTorch, JAX, TensorFlow, or another framework
chosen in the deployment report.
"""

from typing import Any, Protocol


class PolicyNetwork(Protocol):
    def __call__(self, observation: Any, state: Any | None = None) -> Any:
        """Return action distribution parameters or deterministic actions."""
        ...


class ValueNetwork(Protocol):
    def __call__(self, observation_or_state: Any) -> Any:
        """Return state value, action value, or distributional value."""
        ...


class WorldModel(Protocol):
    def predict(self, state: Any, action: Any) -> Any:
        """Return next-state and reward/cost prediction."""
        ...

