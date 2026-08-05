# Base image with PyTorch and CUDA support
FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt-lists/*

# Install uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    UV_SYSTEM_PYTHON=1

# Copy dependency specifications
COPY pyproject.toml /app/

# Install dependencies using uv in system Python
RUN uv pip install --no-cache -e .[dev]

# Expose ports for Jupyter/Marimo (8888), TensorBoard (6006), MkDocs (8000)
EXPOSE 8888 6006 8000

# Default command
CMD ["python", "scripts/train.py"]
