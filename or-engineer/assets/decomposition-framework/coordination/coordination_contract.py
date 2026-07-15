from typing import Any, Dict, Iterable, Mapping, Protocol


class CoordinationRule(Protocol):
    """Coordinate master and subproblems through cuts, columns, prices, or multipliers."""

    def generate_artifacts(self, master_result: Mapping[str, Any], subproblem_results: Iterable[Mapping[str, Any]], config: Dict[str, Any]) -> Iterable[Mapping[str, Any]]:
        ...

    def update_bounds(self, current_bounds: Mapping[str, float], artifacts: Iterable[Mapping[str, Any]], config: Dict[str, Any]) -> Mapping[str, float]:
        ...

    def check_convergence(self, history: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...
