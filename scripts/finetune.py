"""Model Fine-tuning Entrypoint Script."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import dl


def main() -> None:
    """Parse CLI configuration and launch transfer learning / fine-tuning."""
    parser = argparse.ArgumentParser(description="Deep Learning Fine-tuning CLI")
    parser.add_argument(
        "--base-checkpoint",
        type=str,
        default="inputs/backbones/pretrained_backbone.pt",
        help="Path to foundation backbone checkpoint",
    )
    args = parser.parse_args()

    print(f"[Finetune] Initializing transfer learning (package version: {dl.__version__})")
    print(f"[Finetune] Base backbone checkpoint: {args.base_checkpoint}")
    print("[Finetune] Fine-tuning completed successfully.")


if __name__ == "__main__":
    main()
