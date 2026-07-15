from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class MasterState:
    model: Any
    variables: Mapping[str, Any]
    incumbent_solution: Mapping[str, Any] | None
    lower_bound: float | None
    upper_bound: float | None
    metadata: Mapping[str, Any]


class MasterProblem(Protocol):
    def initialize(self, data: Any, config: Dict[str, Any]) -> MasterState:
        ...

    def add_cut_or_column(self, state: MasterState, artifact: Mapping[str, Any], config: Dict[str, Any]) -> MasterState:
        ...

    def solve(self, state: MasterState, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def extract_linking_decisions(self, state: MasterState, result: Mapping[str, Any]) -> Mapping[str, Any]:
        ...
