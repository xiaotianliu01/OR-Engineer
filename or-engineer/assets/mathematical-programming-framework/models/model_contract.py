from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class OptimizationModelArtifacts:
    model: Any
    variables: Mapping[str, Any]
    constraints: Mapping[str, Any]
    objective: Any
    metadata: Mapping[str, Any]


class ModelBuilder(Protocol):
    """Build a mathematical program from verified task data."""

    def build_sets(self, data: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def build_parameters(self, data: Any, sets: Mapping[str, Any], config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def build_model(self, sets: Mapping[str, Any], params: Mapping[str, Any], config: Dict[str, Any]) -> OptimizationModelArtifacts:
        ...

    def extract_solution(self, artifacts: OptimizationModelArtifacts, solver_result: Mapping[str, Any]) -> Mapping[str, Any]:
        ...
