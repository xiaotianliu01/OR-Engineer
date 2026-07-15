from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Optional, Protocol


@dataclass
class SupervisedBatch:
    features: Any
    targets: Any
    weights: Optional[Any] = None
    entity_ids: Optional[Any] = None
    timestamps: Optional[Any] = None
    metadata: Optional[Mapping[str, Any]] = None


class SupervisedEstimator(Protocol):
    """Common interface for linear, tree, and neural supervised models."""

    def fit(
        self,
        train_batches: Iterable[SupervisedBatch],
        validation_batches: Optional[Iterable[SupervisedBatch]],
        config: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Train the estimator and return structured training diagnostics."""
        ...

    def predict(self, batches: Iterable[SupervisedBatch], config: Dict[str, Any]) -> Any:
        """Return task-specific predictions, such as mean, quantiles, probabilities, or scores."""
        ...

    def save(self, path: str) -> None:
        """Persist model weights, preprocessing metadata, and inference settings."""
        ...

    def load(self, path: str) -> None:
        """Load persisted model artifacts for evaluation or prediction."""
        ...
