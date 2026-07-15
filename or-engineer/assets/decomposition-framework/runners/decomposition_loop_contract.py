from typing import Any, Dict, Mapping


DECOMPOSITION_LOOP_STAGES = [
    "load config and partition data",
    "initialize master",
    "solve master",
    "solve subproblems",
    "generate cuts, columns, or multiplier updates",
    "update bounds and incumbent",
    "check convergence",
    "recover primal solution",
    "write progress, status, artifacts, and manifest",
]


class DecompositionLoopContract:
    def run_smoke(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run_pilot(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
