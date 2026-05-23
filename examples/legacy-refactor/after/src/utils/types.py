"""Shared type definitions for the pipeline."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PipelineConfig:
    """Configuration for the data processing pipeline."""

    data_path: Path
    feature_cols: list[str]
    label_col: str
    model_path: Path
    n_estimators: int = 100
    random_state: int = 42
