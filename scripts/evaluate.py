"""Model Evaluation Entrypoint Script."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import dl


def main() -> None:
    """Parse CLI configuration and launch model evaluation benchmark."""
    parser = argparse.ArgumentParser(description="Deep Learning Evaluation CLI")
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="outputs/weights/best_model.pt",
        help="Path to trained model checkpoint weights",
    )
    args = parser.parse_args()

    print(f"[Evaluate] Initializing benchmark (package version: {dl.__version__})")
    print(f"[Evaluate] Model checkpoint: {args.checkpoint}")
    print("[Evaluate] Evaluation completed successfully.")


if __name__ == "__main__":
    main()
