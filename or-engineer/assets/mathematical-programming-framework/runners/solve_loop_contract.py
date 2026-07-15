from typing import Any, Dict, Mapping


SOLVE_LOOP_STAGES = [
    "load config",
    "load and validate data",
    "build sets and parameters",
    "build model",
    "write model export when supported",
    "solve with configured solver",
    "parse solver status and gap",
    "extract and validate solution",
    "write progress, status, solution, logs, and artifact manifest",
]


class SolveLoopContract:
    def run_smoke(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run_pilot(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
