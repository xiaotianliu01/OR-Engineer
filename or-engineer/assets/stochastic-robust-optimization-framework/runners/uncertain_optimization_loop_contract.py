from typing import Any, Dict, Mapping


UNCERTAIN_OPTIMIZATION_STAGES = [
    "load config and data",
    "fit or specify uncertainty model",
    "generate in-sample scenarios or uncertainty set",
    "build stochastic, robust, or DRO model",
    "solve model",
    "evaluate solution on out-of-sample scenarios",
    "compare baselines with common random numbers",
    "write scenario manifests, metrics, status, and artifact manifest",
]


class UncertainOptimizationLoopContract:
    def run_smoke(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run_pilot(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
