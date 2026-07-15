from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class SimulationResult:
    objective_value: float
    constraint_violations: Mapping[str, float]
    metrics: Mapping[str, float]
    trajectory_summary: Mapping[str, Any]
    seed: int
    metadata: Mapping[str, Any]


class Simulator(Protocol):
    """Task-specific simulator interface for simulation optimization."""

    def reset(self, instance: Any, seed: int, config: Dict[str, Any]) -> None:
        ...

    def run(self, policy_or_decision: Any, config: Dict[str, Any]) -> SimulationResult:
        ...

    def validate_inputs(self, instance: Any, policy_or_decision: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...
