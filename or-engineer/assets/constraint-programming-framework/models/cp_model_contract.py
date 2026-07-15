from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class CPModelArtifacts:
    model: Any
    variables: Mapping[str, Any]
    intervals: Mapping[str, Any]
    constraints: Mapping[str, Any]
    objective: Any
    metadata: Mapping[str, Any]


class CPModelBuilder(Protocol):
    def build_domains(self, data: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def build_model(self, data: Any, domains: Mapping[str, Any], config: Dict[str, Any]) -> CPModelArtifacts:
        ...

    def extract_solution(self, artifacts: CPModelArtifacts, solver_result: Mapping[str, Any]) -> Mapping[str, Any]:
        ...
