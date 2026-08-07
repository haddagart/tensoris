"""Data Loading and Transformation Module."""


class BaseDataset:
    """Base dataset class for handling input data transformations."""

    def __init__(self, data_path: str) -> None:
        """Initialize dataset from storage path.

        Args:
            data_path: Path to dataset files or directory.
        """
        self.data_path = data_path

    def __len__(self) -> int:
        """Return total sample count in dataset."""
        return 0
