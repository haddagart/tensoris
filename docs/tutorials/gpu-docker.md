---
icon: material/docker
hide:
  - navigation
---

# Hot-Reloaded GPU Docker Development

[← Back to Tutorials Overview](index.md)

<div style="display: flex; align-items: center; gap: 14px; margin-top: 16px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--md-default-fg-color--lightest);">
  <img src="../../assets/authors/haddagart.png" style="width: 46px; height: 46px; border-radius: 50%; object-fit: cover;" alt="Abdelkader Haddag" />
  <div>
    <div style="font-weight: 700; font-size: 1.05em;">Abdelkader Haddag</div>
    <div style="font-size: 0.85em; opacity: 0.85;">Deep Learning Engineer & Researcher • 📅 Aug 5, 2026</div>
  </div>
</div>

This tutorial explains how to containerize your workstation environment using GPU acceleration, live volume mounts for instant hot-reloading, and interactive notebook services via `docker/docker-compose.yml`.

---

## 🐳 Step 1: Docker Architecture Overview

The `docker/docker-compose.yml` file defines three dedicated services:

1. **`dev`**: Hot-reloaded PyTorch training & development container with GPU access.
2. **`docs`**: Live ProperDocs / MaterialX documentation server on port `8942`.
3. **`notebook`**: Interactive Marimo / Jupyter reactive notebook server on port `8888`.

---

## 🚀 Step 2: Launching Development Containers

Launch the GPU-accelerated training service with live volume mounting:

```bash
# Start primary training service
docker compose -f docker/docker-compose.yml up dev
```

### Live Volume Mount Mapping

- `src/` $\rightarrow$ `/app/src`: Source code changes hot-reload instantly without rebuilding Docker images.
- `inputs/` $\rightarrow$ `/app/inputs`: Host datasets and hyperparameter YAML configs.
- `outputs/` $\rightarrow$ `/app/outputs`: Generated checkpoints output directly to host filesystem.
- `logs/` $\rightarrow$ `/app/logs`: Metric logs output to host.

---

## 📚 Step 3: Serving Documentation in Docker

Launch the documentation server container:

```bash
docker compose -f docker/docker-compose.yml up docs
```

Open **[http://localhost:8942](http://localhost:8942)** in your browser to inspect your live rendered ProperDocs + MaterialX documentation site.
