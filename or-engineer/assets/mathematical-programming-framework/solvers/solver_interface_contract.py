from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional, Protocol


@dataclass
class SolverResult:
    status: str
    termination_condition: str
    objective_value: Optional[float]
    best_bound: Optional[float]
    absolute_gap: Optional[float]
    relative_gap: Optional[float]
    elapsed_seconds: float
    raw_result: Any


class SolverAdapter(Protocol):
    """Wrap a concrete solver or modeling package behind a stable interface."""

    def configure(self, config: Dict[str, Any]) -> None:
        ...

    def solve(self, model: Any, config: Dict[str, Any]) -> SolverResult:
        ...

    def write_model(self, model: Any, output_path: str) -> None:
        ...

    def write_solution(self, solution: Mapping[str, Any], output_path: str) -> None:
        ...
