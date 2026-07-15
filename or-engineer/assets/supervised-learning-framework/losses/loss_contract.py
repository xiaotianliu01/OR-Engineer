from typing import Any, Dict, Protocol


class LossFunction(Protocol):
    """Loss functions should return scalar training objectives and named diagnostics."""

    def __call__(self, predictions: Any, targets: Any, weights: Any, config: Dict[str, Any]) -> Any:
        ...


class MetricFunction(Protocol):
    """Metrics should be computable on validation, test, and benchmark outputs."""

    def __call__(self, predictions: Any, targets: Any, weights: Any, config: Dict[str, Any]) -> Dict[str, float]:
        ...
