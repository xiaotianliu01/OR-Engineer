from typing import Any, Dict, Mapping


CP_SOLVE_LOOP_STAGES = [
    "load config and data",
    "build domains",
    "build CP variables and intervals",
    "add global and task-specific constraints",
    "add objective and hints",
    "solve with configured CP solver",
    "parse status, objective, bound, conflicts, and branches",
    "extract and validate solution",
    "write progress, status, solution, logs, and artifact manifest",
]


class CPSolveLoopContract:
    def run_smoke(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run_pilot(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
