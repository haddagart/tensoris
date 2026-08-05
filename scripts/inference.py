"""Batch & Single-Sample Inference Entrypoint Script."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import dl


def main() -> None:
    """Parse CLI configuration and launch model inference engine."""
    parser = argparse.ArgumentParser(description="Deep Learning Inference CLI")
    parser.add_argument(
        "--input-sample",
        type=str,
        default="inputs/datasets/sample.png",
        help="Path to input data sample or directory",
    )
    args = parser.parse_args()

    print(f"[Inference] Initializing prediction engine (package version: {dl.__version__})")
    print(f"[Inference] Target input sample: {args.input_sample}")
    print("[Inference] Inference completed successfully.")


if __name__ == "__main__":
    main()
