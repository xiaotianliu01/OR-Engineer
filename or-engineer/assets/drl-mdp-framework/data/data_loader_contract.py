"""Data loader contract for DRL/MDP tasks.

Leave empty when the environment is fully generative. Implement only the pieces
needed by the confirmed problem.
"""

from typing import Any, Dict, Protocol


class DataLoader(Protocol):
    def load(self, path: str) -> Dict[str, Any]:
        """Load structured data, trajectories, scenarios, or simulator parameters."""
        ...

    def split(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Return train/validation/test or train/evaluation splits when relevant."""
        ...

    def describe(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Return schema, dimensions, missingness, and unit information."""
        ...


DATA_LOADER_OPTIONS = [
    "no data loader: simulator is fully parameterized in code or config",
    "structured parameter loader",
    "offline trajectory loader",
    "scenario generator",
    "expert-demonstration loader",
    "world-model training dataset loader",
]

