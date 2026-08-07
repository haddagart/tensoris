"""Roboflow Computer Vision Dataset Integration Helper."""

import os
from pathlib import Path
from typing import Any

try:
    import roboflow  # type: ignore
    _ROBOFLOW_AVAILABLE = True
except ImportError:  # pragma: no cover
    _ROBOFLOW_AVAILABLE = False
    roboflow = None


class RoboflowIntegration:
    """Roboflow Helper for downloading computer vision datasets in YOLO, COCO, or Pascal VOC formats.

    References:
        Roboflow Python SDK Documentation: https://docs.roboflow.com/
    """

    def __init__(self, api_key: str | None = None) -> None:
        """Initialize Roboflow client.

        Args:
            api_key: Optional Roboflow API key (defaults to ROBOFLOW_API_KEY env var).
        """
        self.api_key = api_key or os.environ.get("ROBOFLOW_API_KEY")

    @property
    def is_available(self) -> bool:
        """Check if roboflow package is installed."""
        return _ROBOFLOW_AVAILABLE

    def download_dataset(
        self,
        workspace: str,
        project_id: str,
        version: int,
        model_format: str = "yolov8",
        output_dir: str | Path = "inputs/datasets",
    ) -> Any:
        """Download dataset version from Roboflow Universe or Workspace.

        Args:
            workspace: Roboflow workspace identifier.
            project_id: Roboflow project ID.
            version: Dataset version number integer.
            model_format: Export format ('yolov8', 'coco', 'pascal_voc', 'tfrecord').
            output_dir: Destination directory.

        Returns:
            Roboflow dataset download object containing dataset location.
        """
        if not self.is_available:
            raise RuntimeError(
                "roboflow package is not installed. Install via `pip install roboflow` "
                "and set ROBOFLOW_API_KEY environment variable."
            )
        if not self.api_key:
            raise ValueError("ROBOFLOW_API_KEY is required to download datasets from Roboflow.")

        rf = roboflow.Roboflow(api_key=self.api_key)
        proj = rf.workspace(workspace).project(project_id)
        dataset = proj.version(version).download(model_format, location=str(output_dir))
        return dataset
