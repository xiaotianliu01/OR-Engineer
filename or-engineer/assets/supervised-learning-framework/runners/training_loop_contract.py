from typing import Any, Dict, Mapping


TRAINING_LOOP_STAGES = [
    "load config",
    "load and validate data",
    "create leakage-safe splits",
    "fit feature pipeline on train only",
    "build or load the declared fallback model or rule",
    "build model",
    "train with validation monitoring",
    "evaluate validation or downstream metric at intervals",
    "save/update best model when the selected metric improves",
    "compare against baselines",
    "if pilot is weak and budget remains, run targeted redesign attempts on high-impact settings",
    "if redesign attempts fail or validation remains unstable, evaluate and activate the declared fallback when it meets its acceptance threshold",
    "apply pilot acceptance check before recommending the user-facing run",
    "save best model, last model when useful, feature state, metrics, and run records",
]


class TrainingLoopContract:
    def run_smoke(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run_pilot(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
