"""Algorithm implementation contract.

This file is intentionally a scaffold. Replace Protocol-style placeholders with
the selected algorithm implementation for the concrete MDP.
"""

from typing import Any, Dict, Iterable, Protocol


class RLAlgorithm(Protocol):
    """Minimal contract expected by the runner."""

    def act(self, observations: Any, deterministic: bool = False) -> Any:
        """Return actions compatible with the environment action space."""
        ...

    def update(self, batch: Dict[str, Any]) -> Dict[str, float]:
        """Run one optimization update and return train metrics."""
        ...

    def save(self, path: str) -> None:
        """Save all trainable state needed for evaluation and restart."""
        ...

    def load(self, path: str) -> None:
        """Restore trainable state."""
        ...


class ReplayOrRolloutBuffer(Protocol):
    """Storage contract for on-policy rollouts or off-policy replay."""

    def add(self, transition: Dict[str, Any]) -> None:
        ...

    def sample(self, batch_size: int) -> Dict[str, Any]:
        ...

    def iter_batches(self) -> Iterable[Dict[str, Any]]:
        ...

