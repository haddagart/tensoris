---
icon: material/history
---

# Changelog

All notable changes to **Tensoris** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [PEP 440](https://peps.python.org/pep-0440/).

## [1.0.0] - 2026-08-07

### Added
- **Official Production Release**: First production-ready release of Tensoris published to PyPI and GitHub Releases.
- **Interactive Release Script (`release.sh`)**: One-command release automation supporting PEP 440 versioning, pre-commit verification checks, git merges, and major version branch management (`release/v1`).
- **Master CI/CD Pipeline (`release.yml`)**: Unified 5-stage GitHub Actions workflow executing CI verification (`Ruff`, `Mypy`, `Pytest`), GitHub Release creation, PyPI Trusted Publishing, multi-version docs building (`mike`), and GitHub Pages deployment.
- **Top-Level Package API Exports (`src/tensoris/__init__.py`)**: Implemented PEP 562 lazy exports allowing direct imports like `from tensoris import VisionBackbone, ModelTrainer, BaseDataset`.
- **Expanded Unit Test Suite**: Added `tests/unit/test_models.py` and `tests/unit/test_backend.py` covering model output shapes, loss functions, evaluation metrics, and trainer execution loops.

### Changed
- **Enforced Workspace Branching Policy**: Standardized `working` branch as primary active development workspace, leaving `dev`, `main`, and `release/vX` strictly for release management.
- **Multi-Version Docs Selector (`mike`)**: Integrated `mike` version selector dropdown menu for seamless switching between `dev` and `latest` versions.
- **Repository Rename & Branding**: Fully migrated all URLs, documentation headers, and citations from `haddag-dl-template-2` to `https://github.com/haddagart/tensoris`.
- **Pre-Commit Auto-Formatting**: Integrated automatic code formatting (`ruff format`) and import sorting (`ruff check --fix`) directly into `release.sh`.

---

## [1.0.0rc1] - 2026-08-07

### Added
- Release Candidate dress rehearsal baseline for PyPI publishing, multi-version docs, and master pipeline validation.

---

## [1.0.0b1] - 2026-08-07

### Added
- **PyPI Distribution Readiness**: Full PyPI compatibility and automated publication workflow configured via PyPI Trusted Publishers (OIDC) in `.github/workflows/release.yml`.
- **Hatch VCS Configuration**: Configured `no-local-version` scheme in `pyproject.toml` to ensure clean, PyPI-compliant version strings without local commit suffixes.

### Changed
- **Package Renaming (`tensoris`)**: Renamed project and package from `dl`/`src` to `tensoris` using standard Python `src-layout` (`src/tensoris/`).
- **Refactored Module Imports**: Updated all internal modules, model architectures (`backbone.py`, `vae.py`, `transformer.py`), CLI scripts (`train.py`, `inference.py`, `evaluate.py`, `finetune.py`), and diagnostic scripts to `import tensoris`.
- **Unit Tests & Test Suites**: Updated `tests/unit/test_workspace.py` to test package initialization and version attributes of `tensoris`.

---

## [1.0.0a1] - 2026-08-05

> [!NOTE]
> Initial alpha release introducing modular architecture, loss functions, metrics, trainers, and containerization.