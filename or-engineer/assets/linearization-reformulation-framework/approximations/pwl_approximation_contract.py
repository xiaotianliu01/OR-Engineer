from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol, Sequence


@dataclass
class BreakpointPlan:
    breakpoints: Sequence[float]
    segment_count: int
    domain: Sequence[float]
    construction_rule: str
    expected_error_bound: float | None = None


class PiecewiseApproximation(Protocol):
    """Build and validate piecewise approximations for scalar or separable functions."""

    def design_breakpoints(self, function_spec: Mapping[str, Any], domain: Sequence[float], config: Dict[str, Any]) -> BreakpointPlan:
        ...

    def add_to_model(self, model: Any, variables: Mapping[str, Any], plan: BreakpointPlan, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def evaluate_error(self, function_spec: Mapping[str, Any], plan: BreakpointPlan, test_points: Any) -> Mapping[str, float]:
        ...
