from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol


@dataclass
class UncertaintyModel:
    random_variables: Mapping[str, Any]
    distribution_spec: Mapping[str, Any]
    dependence_spec: Mapping[str, Any]
    support_bounds: Mapping[str, Any]
    metadata: Mapping[str, Any]


class UncertaintyModelBuilder(Protocol):
    def fit_or_specify(self, data: Any, config: Dict[str, Any]) -> UncertaintyModel:
        ...

    def validate(self, model: UncertaintyModel, data: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        ...
