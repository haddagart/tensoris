"""Tensoris core package entrypoint."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("tensoris")
except PackageNotFoundError:
    __version__ = "0.0.0-dev"


def __getattr__(name: str):
    if name == "VisionBackbone":
        from tensoris.models.cv.backbone import VisionBackbone

        return VisionBackbone
    elif name == "TransformerClassifier":
        from tensoris.models.nlp.transformer import TransformerClassifier

        return TransformerClassifier
    elif name == "VariationalAutoencoder":
        from tensoris.models.genai.vae import VariationalAutoencoder

        return VariationalAutoencoder
    elif name == "BaseModel":
        from tensoris.models.model import BaseModel

        return BaseModel
    elif name == "ModelTrainer":
        from tensoris.backend.trainers.trainer import ModelTrainer

        return ModelTrainer
    elif name == "BaseDataset":
        from tensoris.data.dataset import BaseDataset

        return BaseDataset
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


__all__ = [
    "__version__",
    "VisionBackbone",
    "TransformerClassifier",
    "VariationalAutoencoder",
    "BaseModel",
    "ModelTrainer",
    "BaseDataset",
]
