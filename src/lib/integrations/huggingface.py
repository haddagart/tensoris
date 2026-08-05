"""Hugging Face Hub Integration Helper."""

import os
from pathlib import Path

try:
    import huggingface_hub  # type: ignore
    _HF_AVAILABLE = True
except ImportError:  # pragma: no cover
    _HF_AVAILABLE = False
    huggingface_hub = None


class HuggingFaceIntegration:
    """Hugging Face Hub helper for downloading datasets/models and pushing PyTorch checkpoints.

    References:
        Hugging Face Hub Python SDK: https://huggingface.co/docs/huggingface_hub/
    """

    def __init__(self, token: str | None = None) -> None:
        """Initialize Hugging Face Hub client.

        Args:
            token: Optional Hugging Face User Access Token (defaults to HF_TOKEN env var).
        """
        self.token = token or os.environ.get("HF_TOKEN")

    @property
    def is_available(self) -> bool:
        """Check if huggingface_hub library is installed."""
        return _HF_AVAILABLE

    def push_model(self, repo_id: str, local_dir: str | Path, commit_message: str = "Upload model checkpoint") -> str:
        """Upload local model directory or checkpoint files to Hugging Face Hub repository.

        Args:
            repo_id: Target Hugging Face Hub repo ID (e.g. 'username/model-name').
            local_dir: Local folder path containing checkpoint weights and configs.
            commit_message: Git commit message on Hub repo.

        Returns:
            URL string of published Hugging Face repository.
        """
        if not self.is_available:
            raise RuntimeError(
                "huggingface_hub package is not installed. Install via `pip install huggingface_hub`."
            )
        api = huggingface_hub.HfApi(token=self.token)
        api.create_repo(repo_id=repo_id, exist_ok=True)
        return api.upload_folder(
            folder_path=str(local_dir),
            repo_id=repo_id,
            commit_message=commit_message,
        )

    def download_file(self, repo_id: str, filename: str, local_dir: str | Path = "inputs/models") -> Path:
        """Download a single model weight file from Hugging Face Hub.

        Args:
            repo_id: Source Hugging Face Hub repository ID.
            filename: Target file name (e.g. 'pytorch_model.bin').
            local_dir: Destination folder path.

        Returns:
            Path object pointing to downloaded file.
        """
        if not self.is_available:
            raise RuntimeError("huggingface_hub package is not installed.")
        downloaded = huggingface_hub.hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=str(local_dir),
            token=self.token,
        )
        return Path(downloaded)
