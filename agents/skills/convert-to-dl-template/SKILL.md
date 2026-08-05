---
name: convert-to-dl-template
description: Converts an existing Python or Deep Learning codebase to strictly adhere to the modular Deep Learning project boilerplate structure. Automatically reorganizes source modules, updates pyproject.toml, mkdocs.yml, CITATION.cff, docker-compose, and GitHub Actions workflows, refactors imports to absolute src. imports, and generates automated docstrings and test suites.
---

# Convert Codebase to Deep Learning Boilerplate Structure

This skill provides step-by-step instructions for converting any existing Python/Deep Learning codebase into the modular **Deep Learning Project Boilerplate** (`haddag-dl-template-2` architecture).

---

## Migration Workflow

### Step 1: Codebase Audit & Mapping
Analyze the source repository and map existing components into the target architecture:

| Legacy Source Component | Target Boilerplate Location |
| :--- | :--- |
| Full neural network models | `src/models/<model_name>.py` |
| Sub-modules, blocks, custom layers | `src/backend/components/` (`layers/`, `blocks/`, `stages/`) |
| Training loops & trainers | `src/backend/trainers/<trainer_name>.py` |
| Custom losses & metrics | `src/backend/losses/` & `src/backend/metrics/` |
| Event hooks, callbacks, W&B/MLflow | `src/backend/callbacks/` |
| PyTorch `Dataset`, `DataLoader`, transforms | `src/data/` |
| Core utilities, file I/O, helpers | `src/lib/` (`core/`, `io/`, `utils/`) |
| Configurations (YAML, Hydra, OmegaConf) | `src/configs/` & `inputs/experiments/` |
| Top-level training/eval scripts | `scripts/` (`train.py`, `evaluate.py`, `finetune.py`, `inference.py`) |
| Jupyter / Marimo notebooks | `notebooks/jupyter/` (`.ipynb`) & `notebooks/marimo/` (`.py`) |
| Raw datasets & pretrained checkpoints | `inputs/datasets/` & `inputs/backbones/` |
| Test suite | `tests/` (`unit/`, `integration/`, `e2e/`) |

---

### Step 2: Configure Workspace Metadata & Build System

1. **Update `pyproject.toml`**:
   - Set `[project] name` to the target package name.
   - Set `dynamic = ["version"]` and configure `[tool.hatch.version] source = "vcs"`.
   - Ensure build backend is `hatchling.build` with `hatch-vcs`.
   - Populate `dependencies` from the legacy project requirements.

2. **Update `src/__init__.py`**:
   ```python
   from importlib.metadata import version, PackageNotFoundError

   try:
       __version__ = version("<package_name>")
   except PackageNotFoundError:
       __version__ = "0.0.0-dev"
   ```

3. **Update Documentation Configuration (`mkdocs.yml`)**:
   - Update `site_name`, `site_description`, `site_url`, `repo_name`, `repo_url`.
   - Update `nav` titles to match project features.

4. **Update Citation Metadata (`CITATION.cff` & `docs/citation-contact.md`)**:
   - Set `title`, `authors`, `orcid`, and repository `url`.

---

### Step 3: Import Refactoring & Docstring Standardisation

1. **Refactor Package Imports**:
   Convert relative or unmanaged imports to clean, absolute imports:
   ```python
   # BEFORE (Legacy)
   from models.net import MyNet
   from utils import load_data

   # AFTER (Refactored)
   from src.models.net import MyNet
   from src.lib.utils import load_data
   ```

2. **Standardize Docstrings**:
   Format Python class and function docstrings using **Google Docstring Style** so `mkdocstrings` and `docs/gen_ref_pages.py` automatically render API documentation pages:
   ```python
   def train_step(self, batch: tuple) -> float:
       """Executes a single forward and backward training pass.

       Args:
           batch: Tuple containing (inputs, targets) tensors.

       Returns:
           Computed scalar loss value.
       """
   ```

---

### Step 4: Infrastructure & CI/CD Integration

1. **Pre-commit Hooks**:
   Ensure `.pre-commit-config.yaml` is present and install hooks via `uv run pre-commit install`.

2. **GitHub Actions Workflows**:
   - Verify `.github/workflows/ci.yml` for pull request linting/testing.
   - Verify `.github/workflows/docs.yml` for multi-version documentation deployment (`mike`).
   - Verify `.github/workflows/release.yml` for automated wheel/sdist bundling on Git tags (`v*`).

3. **Docker Environment**:
   - Verify `docker/Dockerfile` and `docker/docker-compose.yml`.
   - Ensure volume mounts (`../src:/app/src`, `../inputs:/app/inputs`, `../outputs:/app/outputs`, `../logs:/app/logs`) are bound for hot-reloading and external data control.

---

### Step 5: Verification & Quality Audit

Execute the following verification sequence to confirm the migrated codebase:

```bash
# 1. Environment sync
uv sync --all-groups

# 2. Workspace diagnostic check
uv run python main.py

# 3. Code quality enforcement
uv run ruff check .
uv run ruff format --check .

# 4. Run automated test suite
uv run pytest tests/unit

# 5. Build documentation site
uv run properdocs build
```
