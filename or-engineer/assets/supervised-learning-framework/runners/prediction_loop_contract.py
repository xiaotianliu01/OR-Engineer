from typing import Any, Dict, Mapping


class PredictionLoopContract:
    """Generate deployable predictions with saved feature and model artifacts."""

    def load_prediction_data(self, config: Dict[str, Any]) -> Any:
        raise NotImplementedError

    def predict(self, data: Any, artifacts: Mapping[str, Any], config: Dict[str, Any]) -> Any:
        raise NotImplementedError

    def validate_predictions(self, predictions: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def save_predictions(self, predictions: Any, output_path: str) -> None:
        raise NotImplementedError
