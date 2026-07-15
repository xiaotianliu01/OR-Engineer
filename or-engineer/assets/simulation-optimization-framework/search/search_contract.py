from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Protocol


@dataclass
class CandidateEvaluation:
    candidate_id: str
    mean_objective: float
    standard_error: float | None
    replications: int
    metrics: Mapping[str, float]
    metadata: Mapping[str, Any]


class SimulationSearchMethod(Protocol):
    def propose(self, history: Iterable[CandidateEvaluation], config: Dict[str, Any]) -> Iterable[Any]:
        ...

    def update(self, history: Iterable[CandidateEvaluation], config: Dict[str, Any]) -> Mapping[str, Any]:
        ...

    def select_incumbent(self, history: Iterable[CandidateEvaluation], config: Dict[str, Any]) -> CandidateEvaluation:
        ...
