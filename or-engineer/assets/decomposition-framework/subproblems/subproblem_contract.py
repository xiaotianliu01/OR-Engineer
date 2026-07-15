from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class SubproblemResult:
    partition_id: str
    status: str
    objective_value: float | None
    bound_contribution: float | None
    feasibility_artifact: Mapping[str, Any] | None
    optimality_artifact: Mapping[str, Any] | None
    primal_solution: Mapping[str, Any] | None
    metadata: Mapping[str, Any]


class Subproblem(Protocol):
    def build(self, partition_data: Any, linking_decisions: Mapping[str, Any], config: Dict[str, Any]) -> Any:
        ...

    def solve(self, subproblem_model: Any, config: Dict[str, Any]) -> SubproblemResult:
        ...

    def validate(self, result: SubproblemResult, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...
