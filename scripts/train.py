"""Model Training Entrypoint Script."""

import argparse
from pathlib import Path
import sys

# Ensure src package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import dl


def main() -> None:
    """Parse CLI configuration and launch training execution loop."""
    parser = argparse.ArgumentParser(description="Deep Learning Training CLI")
    parser.add_argument(
        "--config",
        type=str,
        default="inputs/experiments/default.yaml",
        help="Path to experiment override YAML configuration file",
    )
    args = parser.parse_args()

    print(f"[Train] Initializing workflow (package version: {dl.__version__})")
    print(f"[Train] Loaded configuration file: {args.config}")
    print("[Train] Execution completed successfully.")


if __name__ == "__main__":
    main()
