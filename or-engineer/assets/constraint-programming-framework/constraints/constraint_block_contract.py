from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class ConstraintBlockResult:
    constraints: Mapping[str, Any]
    soft_penalties: Mapping[str, Any]
    metadata: Mapping[str, Any]


class ConstraintBlock(Protocol):
    def validate_inputs(self, data: Any, variables: Mapping[str, Any], config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def add_to_model(self, model: Any, variables: Mapping[str, Any], config: Dict[str, Any]) -> ConstraintBlockResult:
        ...
