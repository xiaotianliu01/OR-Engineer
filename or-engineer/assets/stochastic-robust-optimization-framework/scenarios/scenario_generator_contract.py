from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol, Sequence


@dataclass
class ScenarioSet:
    scenarios: Sequence[Mapping[str, Any]]
    probabilities: Sequence[float]
    scenario_ids: Sequence[str]
    metadata: Mapping[str, Any]


class ScenarioGenerator(Protocol):
    def generate_in_sample(self, uncertainty_model: Any, config: Dict[str, Any]) -> ScenarioSet:
        ...

    def generate_out_of_sample(self, uncertainty_model: Any, config: Dict[str, Any]) -> ScenarioSet:
        ...

    def save_manifest(self, scenario_set: ScenarioSet, output_path: str) -> None:
        ...
