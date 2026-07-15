from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class CandidatePolicy:
    candidate_id: str
    parameters: Mapping[str, Any]
    policy_class: str
    metadata: Mapping[str, Any]


class PolicyFactory(Protocol):
    def sample_or_construct(self, config: Dict[str, Any]) -> CandidatePolicy:
        ...

    def repair_or_project(self, policy: CandidatePolicy, config: Dict[str, Any]) -> CandidatePolicy:
        ...

    def explain_capacity(self, policy: CandidatePolicy, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...
