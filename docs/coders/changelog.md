---
icon: material/history
---

# Changelog

All notable changes to this project boilerplate will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-beta] - 2026-08-07

### Added
- **PyPI Distribution Readiness**: Full PyPI compatibility and automated publication workflow configured via PyPI Trusted Publishers (OIDC) in `.github/workflows/release.yml`.
- **Hatch VCS Configuration**: Configured `no-local-version` scheme in `pyproject.toml` to ensure clean, PyPI-compliant version strings without local commit suffixes.

### Changed
- **Package Renaming (`tensoris`)**: Renamed project and package from `dl`/`src` to `tensoris` using standard Python `src-layout` (`src/tensoris/`).
- **Refactored Module Imports**: Updated all internal modules, model architectures (`backbone.py`, `vae.py`, `transformer.py`), CLI scripts (`train.py`, `inference.py`, `evaluate.py`, `finetune.py`), and diagnostic scripts to `import tensoris`.
- **Unit Tests & Test Suites**: Updated `tests/unit/test_workspace.py` to test package initialization and version attributes of `tensoris`.
- **Documentation Engine**: Updated `mkdocs.yml` site title to `Tensoris Documentation` and `docs/gen_ref_pages.py` API generator to parse `src/tensoris`.

---

## [1.0.0-alpha] - 2026-08-05

> [!WARNING]
> **Alpha Release Disclaimer**: All implemented neural network modules, loss functions, metrics, and trainers in this initial `v1.0.0-alpha` release are provided in alpha stage for structural reference and rapid prototyping. They have not yet undergone rigorous production verification or empirical validation, and will be continuously hardened and stabilized in upcoming releases.

### Added
- **Modular Deep Learning Architecture**: Clean 3-tier decoupling across `layers`, `blocks`, `losses`, `metrics`, `trainers`, `models`, and `datasets`.
- **Mathematical Docstrings & Formulations**: LaTeX equations rendering for `FocalLoss`, `DiceLoss`, `LabelSmoothingCrossEntropy`, `InfoNCELoss`, `PerceptualLoss`, `MeanIoU`, `TopKAccuracy`, `Perplexity`, and `FIDScore`.
- **Interactive Mermaid Flowcharts**: Embedded flowcharts for `BaseModel` architecture and `ModelTrainer` execution loops.
- **Third-Party Integrations**: Modules for Kaggle, Weights & Biases (W&B), Hugging Face Hub, Roboflow, and Ultralytics YOLO.
- **Documentation Suite**: ProperDocs + MaterialX theme with auto-generated API tree, `git-revision-date-localized` timestamps, and `MathJax` rendering.
- **AI Agent Skills**: Custom skills for template conversion, experiment tracking, ONNX/TorchScript export, and paper-to-code translation.
- **Docker & Workstation Tooling**: NVIDIA GPU-accelerated container setups with hot-reloaded volume mounts.