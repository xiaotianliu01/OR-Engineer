from typing import Any, Dict, Mapping


class FeaturePipelineContract:
    """Feature pipelines must be fit on training data only."""

    def fit(self, train_data: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def transform(self, data: Any, fitted_state: Mapping[str, Any], config: Dict[str, Any]) -> Any:
        raise NotImplementedError

    def save(self, fitted_state: Mapping[str, Any], output_path: str) -> None:
        raise NotImplementedError

    def load(self, input_path: str) -> Mapping[str, Any]:
        raise NotImplementedError
