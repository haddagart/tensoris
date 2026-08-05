"""Kaggle Platform Integration Helper."""

import os
from pathlib import Path

try:
    import kaggle  # type: ignore
    _KAGGLE_AVAILABLE = True
except (ImportError, Exception):  # pragma: no cover
    _KAGGLE_AVAILABLE = False
    kaggle = None


class KaggleIntegration:
    """Kaggle API Helper for downloading datasets and submitting competition predictions.

    References:
        Kaggle API Documentation: https://github.com/Kaggle/kaggle-api
    """

    def __init__(self, api_key: str | None = None, username: str | None = None) -> None:
        """Initialize Kaggle API client.

        Args:
            api_key: Optional Kaggle API key (defaults to KAGGLE_KEY env var).
            username: Optional Kaggle username (defaults to KAGGLE_USERNAME env var).
        """
        if api_key:
            os.environ["KAGGLE_KEY"] = api_key
        if username:
            os.environ["KAGGLE_USERNAME"] = username

    @property
    def is_available(self) -> bool:
        """Check if Kaggle library is installed and authenticated."""
        return _KAGGLE_AVAILABLE

    def download_dataset(self, dataset_handle: str, output_dir: str | Path = "inputs/datasets") -> Path:
        """Download and unzip a Kaggle dataset.

        Args:
            dataset_handle: Kaggle dataset identifier (e.g. 'zillow/zecon').
            output_dir: Destination directory path.

        Returns:
            Path object pointing to the output directory.
        """
        if not self.is_available:
            raise RuntimeError(
                "Kaggle package is not installed or configured. Install via `pip install kaggle` "
                "and set KAGGLE_USERNAME and KAGGLE_KEY environment variables."
            )
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        kaggle.api.dataset_download_files(dataset_handle, path=str(output_path), unzip=True)
        return output_path

    def submit_competition(self, file_path: str | Path, competition: str, message: str) -> None:
        """Submit a prediction CSV file to a Kaggle competition.

        Args:
            file_path: Path to submission CSV file.
            competition: Kaggle competition handle.
            message: Submission description message.
        """
        if not self.is_available:
            raise RuntimeError("Kaggle package is not available.")
        kaggle.api.competition_submit(str(file_path), message=message, competition=competition)
