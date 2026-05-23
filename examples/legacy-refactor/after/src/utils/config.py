"""Default pipeline configuration factory."""

from pathlib import Path

from .types import PipelineConfig


def default_config(data_path: Path, model_path: Path) -> PipelineConfig:
    """Return a sensible default PipelineConfig.

    Args:
        data_path: Path to the input CSV file.
        model_path: Path where the trained model will be saved.

    Returns:
        PipelineConfig with standard feature columns and default hyperparameters.
    """
    return PipelineConfig(
        data_path=data_path,
        feature_cols=["feat1", "feat2", "feat3"],
        label_col="label",
        model_path=model_path,
    )
