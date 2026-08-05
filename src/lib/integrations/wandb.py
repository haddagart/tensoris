"""Weights & Biases (W&B) Experiment Tracking Integration."""

from typing import Any

try:
    import wandb  # type: ignore
    _WANDB_AVAILABLE = True
except ImportError:  # pragma: no cover
    _WANDB_AVAILABLE = False
    wandb = None


class WandbIntegration:
    """Weights & Biases Logger for metric tracking, artifact logging, and hyperparameter sweeps.

    References:
        Weights & Biases Python SDK Documentation: https://docs.wandb.ai/
    """

    def __init__(
        self,
        project: str = "deep-learning-project",
        entity: str | None = None,
        config: dict[str, Any] | None = None,
        name: str | None = None,
        mode: str = "online",
    ) -> None:
        """Initialize W&B run.

        Args:
            project: W&B project name.
            entity: W&B username or team entity.
            config: Hyperparameter configuration dictionary.
            name: Display name for the run.
            mode: Run mode ('online', 'offline', or 'disabled').
        """
        self.project = project
        self.entity = entity
        self.config = config or {}
        self.name = name
        self.mode = mode
        self.run = None

    @property
    def is_available(self) -> bool:
        """Check if wandb library is installed."""
        return _WANDB_AVAILABLE

    def init(self) -> Any:
        """Initialize W&B run context."""
        if not self.is_available:
            raise RuntimeError("wandb package is not installed. Install via `pip install wandb`.")
        self.run = wandb.init(
            project=self.project,
            entity=self.entity,
            config=self.config,
            name=self.name,
            mode=self.mode,
        )
        return self.run

    def log(self, metrics: dict[str, Any], step: int | None = None) -> None:
        """Log metric key-value dictionary to W&B dashboard.

        Args:
            metrics: Dictionary of numerical metrics or media logs.
            step: Optional global training step number.
        """
        if self.is_available and self.run is not None:
            wandb.log(metrics, step=step)

    def log_artifact(self, file_path: str, artifact_name: str, artifact_type: str = "model") -> None:
        """Upload checkpoint file or artifact to W&B.

        Args:
            file_path: Local file path to upload.
            artifact_name: W&B artifact name identifier.
            artifact_type: Artifact category ('model', 'dataset', 'checkpoint').
        """
        if self.is_available and self.run is not None:
            artifact = wandb.Artifact(artifact_name, type=artifact_type)
            artifact.add_file(file_path)
            self.run.log_artifact(artifact)

    def finish(self) -> None:
        """Finish W&B run."""
        if self.is_available and self.run is not None:
            wandb.finish()
