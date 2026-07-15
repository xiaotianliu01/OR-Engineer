from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional, Protocol


@dataclass
class CPSolverResult:
    status: str
    objective_value: Optional[float]
    best_bound: Optional[float]
    relative_gap: Optional[float]
    conflicts: Optional[int]
    branches: Optional[int]
    elapsed_seconds: float
    raw_result: Any


class CPSolverAdapter(Protocol):
    def configure(self, config: Dict[str, Any]) -> None:
        ...

    def solve(self, model: Any, config: Dict[str, Any]) -> CPSolverResult:
        ...

    def export_solution(self, solution: Mapping[str, Any], output_path: str) -> None:
        ...
