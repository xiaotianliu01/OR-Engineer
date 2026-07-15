from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class UncertainOptimizationModel:
    model: Any
    first_stage_variables: Mapping[str, Any]
    recourse_variables: Mapping[str, Any]
    uncertainty_metadata: Mapping[str, Any]
    risk_metadata: Mapping[str, Any]


class UncertainOptimizationBuilder(Protocol):
    def build_deterministic_equivalent(self, data: Any, scenarios: Any, config: Dict[str, Any]) -> UncertainOptimizationModel:
        ...

    def build_robust_counterpart(self, data: Any, uncertainty_set: Any, config: Dict[str, Any]) -> UncertainOptimizationModel:
        ...

    def extract_policy_or_solution(self, model: UncertainOptimizationModel, solver_result: Mapping[str, Any]) -> Mapping[str, Any]:
        ...
