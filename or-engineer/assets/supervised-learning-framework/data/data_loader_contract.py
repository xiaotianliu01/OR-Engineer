from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional


@dataclass
class DatasetBundle:
    train: Any
    validation: Any
    test: Any
    prediction: Optional[Any]
    schema: Mapping[str, Any]
    split_manifest: Mapping[str, Any]


class DataLoaderContract:
    """Task-specific loader should implement this shape after copying the asset."""

    def load_raw(self, config: Dict[str, Any]) -> Any:
        raise NotImplementedError

    def validate_schema(self, raw_data: Any, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def make_splits(self, raw_data: Any, config: Dict[str, Any]) -> DatasetBundle:
        raise NotImplementedError

    def save_split_manifest(self, bundle: DatasetBundle, output_path: str) -> None:
        raise NotImplementedError
