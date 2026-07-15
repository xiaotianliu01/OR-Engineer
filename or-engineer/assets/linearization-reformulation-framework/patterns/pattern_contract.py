from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class ReformulationResult:
    variables: Mapping[str, Any]
    constraints: Mapping[str, Any]
    metadata: Mapping[str, Any]
    exactness: str
    required_bounds: Mapping[str, Any]


class ReformulationPattern(Protocol):
    """Implement one exact reformulation, relaxation, or approximation block."""

    def validate_inputs(self, expression: Any, bounds: Mapping[str, Any], config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def apply(self, model: Any, expression: Any, bounds: Mapping[str, Any], config: Dict[str, Any]) -> ReformulationResult:
        ...

    def describe(self) -> Mapping[str, Any]:
        ...
