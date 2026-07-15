from typing import Any, Dict, Mapping


class EvaluationLoopContract:
    """Evaluate selected models, fallback models, and benchmarks on held-out slices."""

    def load_artifacts(self, run_dir: str) -> Mapping[str, Any]:
        raise NotImplementedError

    def evaluate_split(self, artifacts: Mapping[str, Any], split_data: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def compare_baselines(self, model_metrics: Mapping[str, Any], baseline_metrics: Mapping[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def compare_fallback(self, model_metrics: Mapping[str, Any], fallback_metrics: Mapping[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def save_evaluation(self, results: Mapping[str, Any], output_dir: str) -> None:
        raise NotImplementedError
