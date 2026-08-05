"""Workspace Environment Validation Script."""

import sys
import dl


def main() -> None:
    """Print system, PyTorch, and package version diagnostics."""
    print("=" * 60)
    print("      Deep Learning Project Workspace Diagnostic Check      ")
    print("=" * 60)
    print(f"Python Version : {sys.version.split()[0]} ({sys.executable})")
    print(f"Package Version: {dl.__version__}")

    try:
        import torch

        print(f"PyTorch Version: {torch.__version__}")
        if torch.cuda.is_available():
            print(f"GPU Accelerator: CUDA ({torch.cuda.get_device_name(0)})")
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            print("GPU Accelerator: Apple Silicon (MPS)")
        else:
            print("GPU Accelerator: CPU (No CUDA/MPS GPU detected)")
    except ImportError:
        print("PyTorch Status : Not installed (run 'uv sync --all-groups')")

    print("-" * 60)
    print("Workspace environment is configured and ready!")
    print("=" * 60)


if __name__ == "__main__":
    main()
