---
icon: material/flash
---

# TL;DR Quickstart Guide

A concise, high-speed quickstart guide for getting up and running with the **Modular Deep Learning Project Boilerplate Template**!

---

## ⚡ 5-Minute Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/haddagart/haddag-dl-template-2.git
cd haddag-dl-template-2

# 2. Sync dependencies & setup virtual environment
uv sync --all-groups

# 3. Install pre-commit hooks
uv run pre-commit install

# 4. Launch PyTorch model training workflow
uv run python scripts/train.py --config inputs/experiments/default.yaml

# 5. Serve live local documentation server
uv run properdocs serve
```

---

## 🚀 Hot-Reloaded GPU Docker Environment

```bash
# Launch training inside hot-reloaded GPU Docker container
docker compose -f docker/docker-compose.yml up dev
```

---

## 🐍 Changing Python Version with `uv`

To switch your environment to a specific, lower, or higher Python version (e.g., Python 3.10, 3.12, or 3.13):

```bash
# Pin project to a specific Python version
uv python pin 3.12

# Re-sync virtual environment with the target Python version
uv sync --all-groups --python 3.12
```

> [!TIP]
> Remember to update `requires-python` in [`pyproject.toml`](https://github.com/haddagart/haddag-dl-template-2/blob/main/pyproject.toml) if targeting a lower or higher Python version (e.g., `requires-python = ">=3.10"`).

---

## 📋 Pre-Coding Setup Checklist

- [x] **Project Metadata**: Update `name`, `version`, and `requires-python` in [`pyproject.toml`](https://github.com/haddagart/haddag-dl-template-2/blob/main/pyproject.toml).
- [x] **Environment Sync**: Run `uv sync --all-groups`.
- [x] **Git Hooks**: Run `uv run pre-commit install`.
- [x] **Documentation Settings**: Update `site_name` and `site_url` in [`properdocs.yml`](https://github.com/haddagart/haddag-dl-template-2/blob/main/properdocs.yml).
- [x] **Citation Information**: Update author details in [`CITATION.cff`](https://github.com/haddagart/haddag-dl-template-2/blob/main/CITATION.cff) and [Citation & Contact](citation-contact.md).