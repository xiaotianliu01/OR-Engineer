from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional


@dataclass
class PredictionOutput:
    point: Optional[Any] = None
    quantiles: Optional[Mapping[float, Any]] = None
    probabilities: Optional[Any] = None
    scores: Optional[Any] = None
    intervals: Optional[Any] = None
    metadata: Optional[Mapping[str, Any]] = None


class PredictionModelContract:
    """Implement this contract for linear, tree, statistical, or neural models."""

    def build(self, config: Dict[str, Any], schema: Mapping[str, Any]) -> Any:
        raise NotImplementedError

    def forward_or_predict(self, model: Any, features: Any, config: Dict[str, Any]) -> PredictionOutput:
        raise NotImplementedError

    def save_artifacts(self, model: Any, output_dir: str, metadata: Mapping[str, Any]) -> None:
        raise NotImplementedError

    def load_artifacts(self, model_dir: str) -> Any:
        raise NotImplementedError
