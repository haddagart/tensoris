"""Ultralytics YOLO Integration Helper."""

from pathlib import Path
from typing import Any

try:
    import ultralytics  # type: ignore
    _ULTRALYTICS_AVAILABLE = True
except ImportError:  # pragma: no cover
    _ULTRALYTICS_AVAILABLE = False
    ultralytics = None


class UltralyticsIntegration:
    """Ultralytics YOLO model helper for object detection, segmentation, and classification workflows.

    References:
        Ultralytics Documentation: https://docs.ultralytics.com/
    """

    def __init__(self, model_name: str = "yolov8n.pt") -> None:
        """Initialize Ultralytics YOLO model.

        Args:
            model_name: Pretrained YOLO weight file or config path (e.g. 'yolov8n.pt', 'yolov8x-seg.pt').
        """
        self.model_name = model_name
        self.model = None

    @property
    def is_available(self) -> bool:
        """Check if ultralytics package is installed."""
        return _ULTRALYTICS_AVAILABLE

    def load_model(self) -> Any:
        """Instantiate Ultralytics YOLO model class."""
        if not self.is_available:
            raise RuntimeError("ultralytics package is not installed. Install via `pip install ultralytics`.")
        self.model = ultralytics.YOLO(self.model_name) # type: ignore
        return self.model

    def train(self, data_yaml: str | Path, epochs: int = 50, imgsz: int = 640, batch: int = 16) -> Any:
        """Train YOLO model on dataset.

        Args:
            data_yaml: Path to dataset configuration YAML file.
            epochs: Training epoch count.
            imgsz: Target image resolution size.
            batch: Training batch size.

        Returns:
            Training results object.
        """
        if self.model is None:
            self.load_model()
        return self.model.train(data=str(data_yaml), epochs=epochs, imgsz=imgsz, batch=batch,) # type: ignore

    def export(self, format: str = "onnx") -> str:
        """Export trained YOLO model to deployment format (ONNX, TorchScript, Engine).

        Args:
            format: Output target format ('onnx', 'torchscript', 'engine', 'openvino').

        Returns:
            String path of exported model weight file.
        """
        if self.model is None:
            self.load_model()
        return self.model.export(format=format) # type: ignore
