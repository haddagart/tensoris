---
icon: material/robot
---

# AI & Agentic Coding Skills

This repository includes a suite of specialized **AI Agent Skills** located in `agents/skills/`. These skills provide structured workflows for AI coding assistants (e.g., Antigravity, Claude, Copilot) to automate complex Deep Learning engineering tasks.

---

## Available AI Skills Overview

| Skill Name | Purpose & Function | Location |
| :--- | :--- | :--- |
| **`convert-to-dl-template`** | Converts any legacy Python/DL codebase to strictly match this boilerplate architecture | [`agents/skills/convert-to-dl-template/`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/agents/skills/convert-to-dl-template/SKILL.md) |
| **`dl-experiment-runner`** | Automates hyperparameter configuration, training execution, and metric reporting | [`agents/skills/dl-experiment-runner/`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/agents/skills/dl-experiment-runner/SKILL.md) |
| **`dl-model-exporter`** | Exports trained PyTorch checkpoints (`.pt`) into ONNX & TorchScript production formats | [`agents/skills/dl-model-exporter/`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/agents/skills/dl-model-exporter/SKILL.md) |
| **`dl-paper-to-code`** | Translates novel academic paper architectures and equations into modular PyTorch components | [`agents/skills/dl-paper-to-code/`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/agents/skills/dl-paper-to-code/SKILL.md) |

---

## 🛠️ Skill Details & Usage

### 1. `convert-to-dl-template`
* **Trigger**: When converting a legacy repository or setting up a new project from raw scripts.
* **Actions**:
  - Reorganizes raw PyTorch models into `src/models/` and sub-blocks into `src/backend/components/`.
  - Refactors all imports to absolute `src.` paths.
  - Generates build configuration (`pyproject.toml`, `mkdocs.yml`, `CITATION.cff`) and CI/CD pipelines.

### 2. `dl-experiment-runner`
* **Trigger**: When running hyperparameter sweeps, benchmarking, or comparing model variants.
* **Actions**:
  - Generates YAML config overrides in `inputs/experiments/`.
  - Executes `python scripts/train.py --config ...`.
  - Parses logs and outputs comparative Markdown tables with loss and accuracy progressions.

### 3. `dl-model-exporter`
* **Trigger**: When preparing trained models for deployment.
* **Actions**:
  - Loads PyTorch weights from `outputs/weights/best_model.pt`.
  - Traces forward pass with dummy inputs and exports to ONNX/TorchScript in `outputs/artifacts/`.
  - Verifies ONNX runtime inference correctness.

### 4. `dl-paper-to-code`
* **Trigger**: When translating a paper, equation, or pseudo-code into PyTorch.
* **Actions**:
  - Breaks down paper modules into layers (`src/backend/components/layers/`), blocks (`blocks/`), and stages (`stages/`).
  - Assembles the complete model wrapper in `src/models/`.
  - Writes unit tests in `tests/unit/` to verify tensor shapes and parameter counts.