---
icon: material/home
---

<div align="center">
  <img src="assets/logos/logo.svg" alt="Tensoris Logo" width="420" />
  <p><strong>A Production-Grade, Academic-First PyTorch Framework & Architecture Library</strong></p>
  
  <p>
    <a href="https://github.com/haddagart/tensoris"><img src="https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github" alt="GitHub Repo" /></a>
    <a href="https://pypi.org/project/tensoris/"><img src="https://img.shields.io/pypi/v/tensoris?style=flat-square" alt="PyPI" /></a>
    <a href="https://pytorch.org/"><img src="https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" /></a>
    <a href="https://astral.sh/uv"><img src="https://img.shields.io/badge/Package%20Manager-uv-261230?style=flat-square" alt="uv" /></a>
    <a href="https://docker.com"><img src="https://img.shields.io/badge/Container-Docker%20GPU-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" /></a>
  </p>
</div>

---

## 🌟 Executive Summary

**Tensoris** (`tensoris`) is a standardized, high-performance architecture framework tailored for AI researchers, scientific engineers, and deep learning practitioners. It bridges the gap between theoretical peer-reviewed research papers and production-ready PyTorch implementations by enforcing strict modularity, automated API documentation, Docker GPU reproducibility, and domain-grouped deep learning primitives.

---

## 🏗️ Architectural Design System

The repository enforces a clean 3-tier separation of concerns across neural network building blocks:

```
src/
└── tensoris/
    ├── backend/
    │   ├── components/
    │   │   ├── layers/      <-- Atomic neural network layers (ConvStem, PositionalEncoding)
    │   │   └── blocks/      <-- Reusable multi-layer blocks (ResidualBlock, TransformerEncoderBlock, VAE Blocks)
    │   ├── losses/          <-- Peer-reviewed loss functions (Focal, Dice, LabelSmoothing, InfoNCE, Perceptual)
    │   ├── metrics/         <-- Evaluation metrics (mIoU, Top-K Accuracy, Perplexity, FID Score)
    │   └── trainers/        <-- Robust ModelTrainer execution loop
    ├── models/              <-- Complete composite end-to-end architectures (VisionBackbone, Transformer, VAE)
├── data/                <-- Dataset loaders and data pipeline abstractions
└── lib/                 <-- Utility helpers, seed managers, and system diagnostics
```

---

## 🔬 Scientific Domains & Implemented Primitives

Every primitive included in this template is implemented in PyTorch and documented with official peer-reviewed paper citations in its docstring:

| Domain | Neural Block / Layer | Loss Function | Evaluation Metric | Reference Paper |
| :--- | :--- | :--- | :--- | :--- |
| **Computer Vision** | `ConvStem`, `ResidualBlock` | `FocalLoss`, `DiceLoss` | `MeanIoU`, `TopKAccuracy` | Lin et al. (ICCV 2017), Milletari et al. (3DV 2016), Long et al. (CVPR 2015) |
| **Natural Language Processing** | `PositionalEncoding`, `TransformerEncoderBlock` | `LabelSmoothingCrossEntropy` | `PerplexityMetric` | Vaswani et al. (NIPS 2017), Szegedy et al. (CVPR 2016), Jelinek et al. (1977) |
| **Generative AI & Multimodal** | `VAEEncoderBlock`, `VAEDecoderBlock` | `ContrastiveInfoNCELoss`, `PerceptualLoss` | `FIDScoreMetric` | Kingma & Welling (ICLR 2014), Oord et al. (2018), Heusel et al. (NIPS 2017) |

---

## 🚀 Workflow Entrypoints & Commands

| Command | Purpose | Target Script |
| :--- | :--- | :--- |
| `python3 main.py` | Run environment diagnostics (Python, PyTorch, GPU device) | [`main.py`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/main.py) |
| `python3 scripts/train.py` | Launch PyTorch model training loop | [`scripts/train.py`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/scripts/train.py) |
| `python3 scripts/evaluate.py` | Compute evaluation metrics on validation set | [`scripts/evaluate.py`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/scripts/evaluate.py) |
| `uv run properdocs serve` | Launch live local documentation server | [`properdocs.yml`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/properdocs.yml) |
| `docker compose -f docker/docker-compose.yml up` | Launch GPU Docker container with live volume mounts | [`docker/docker-compose.yml`](file:///Users/haddagart/Developer/haddagart/templates/tensoris/docker/docker-compose.yml) |

---

## 🛠️ Specialized AI Agent Skills

This repository includes custom AI agent skills designed for automated project conversion, hyperparameter sweeps, checkpoint export, and paper translation:

- **`convert-to-dl-template`**: Reorganizes raw PyTorch codebases to adhere strictly to this boilerplate layout.
- **`dl-experiment-runner`**: Launches automated hyperparameter sweeps and tracks metric outputs.
- **`dl-model-exporter`**: Converts trained PyTorch checkpoints (`.pt`) to ONNX and TorchScript deployment formats.
- **`dl-paper-to-code`**: Translates novel scientific paper equations into modular `backend/components/` and unit tests.

---

## 📖 Navigation & Documentation Layout

- **Getting Started**: System requirements, setup guide, project structure, Docker workflow, AI skills, and documentation guide.
- **For Academics**: Key references, citation formats (`CITATION.cff`), and researcher contact details.
- **API Reference**: Dynamically generated, human-readable module hierarchy displaying docstrings and paper citations.

---

<div align="center" style="margin-top: 40px; padding: 18px; background-color: rgba(99, 102, 241, 0.08); border: 1px solid rgba(99, 102, 241, 0.25); border-radius: 12px;">
  <p style="margin: 0; font-size: 0.9em; color: #64748B;">
    ⚡ <strong>AI Pair Programming Acknowledgment</strong><br />
    This deep learning boilerplate template and documentation ecosystem was elaborated through AI pair programming powered by <strong>Google's Gemini</strong> and <strong>Antigravity</strong> in collaboration with <strong>Abdelkader Haddag</strong>.
  </p>
</div>