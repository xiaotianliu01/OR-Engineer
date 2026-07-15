from typing import Any, Dict, Mapping


REFORMULATION_LOOP_STAGES = [
    "load original formulation",
    "load bounds and operating ranges",
    "select reformulation patterns",
    "build transformed model blocks",
    "classify exactness and approximation direction",
    "validate approximation error or relaxation gap",
    "export transformed model specification",
    "write run records and artifact manifest",
]


class ReformulationLoopContract:
    def run_design(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run_validation(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
