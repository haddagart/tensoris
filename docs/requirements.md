---
icon: material/check-circle
---

# System & Hardware Requirements

This section outlines hardware recommendations and software dependencies required to run training and inference workloads reproducibly.

---

## Software Prerequisites

- **Python**: `>= 3.11`
- **Package & Environment Manager**: `uv` (recommended) or `pip`
- **Container Runtime** (Optional): `Docker` + `nvidia-docker` (NVIDIA Container Toolkit)

---

## 🐍 Changing Python Version with `uv`

`uv` allows seamless switching to any lower, higher, or specific Python release without manually installing external Python distributions:

```bash
# 1. Download and pin a specific Python version (e.g., 3.10, 3.12, or 3.13)
uv python pin 3.12

# 2. Re-sync virtual environment with the target Python version
uv sync --all-groups --python 3.12
```

> [!NOTE]
> If switching to a lower Python version (e.g., Python 3.10), update the `requires-python` constraint in [`pyproject.toml`](https://github.com/haddagart/tensoris/blob/main/pyproject.toml):
> ```toml
> [project]
> requires-python = ">=3.10"
> ```

---

## Hardware Recommendations

| Component | Minimum               | Recommended                     |
| :-------- | :-------------------- | :------------------------------ |
| **CPU**   | 4 Cores               | 16+ Cores                       |
| **RAM**   | 16 GB                 | 64 GB+                          |
| **GPU**   | NVIDIA GPU (8GB VRAM) | NVIDIA A100 / H100 (40GB+ VRAM) |
| **CUDA**  | 11.8+ / 12.1+         | 12.2+                           |

---

## CUDA & PyTorch GPU Environment

To containerize GPU workloads reproducibly, inspect the provided [GPU Docker Tutorial](tutorials/gpu-docker.md):

```bash
# Build CUDA container
docker build -t dl-template:latest docker/
```