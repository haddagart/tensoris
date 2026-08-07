# Tensoris

[![CI](https://github.com/haddagart/tensoris/actions/workflows/ci.yml/badge.svg)](https://github.com/haddagart/tensoris/actions/workflows/ci.yml)
[![Docs](https://github.com/haddagart/tensoris/actions/workflows/docs.yml/badge.svg)](https://haddagart.github.io/tensoris/)
[![PyPI](https://img.shields.io/pypi/v/tensoris.svg)](https://pypi.org/project/tensoris/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
<br/>
[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-rSpkNpYAAAAJ-4285F4?logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=rSpkNpYAAAAJ)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--6481--0999-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-6481-0999)
[![GitHub](https://img.shields.io/badge/GitHub-haddagart-181717?logo=github&logoColor=white)](https://github.com/haddagart)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdelkader%20Haddag-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/haddagart/)
[![X](https://img.shields.io/badge/X-haddagart-000000?logo=x&logoColor=white)](https://x.com/haddagart)

**Tensoris** is a production-ready PyTorch deep learning library and framework featuring modular neural components, automated multi-version documentation via `mike`, pre-commit quality checks, and automated PyPI CI/CD releases.

---

## Minimum System Requirements

Before getting started, ensure your local environment meets the following requirements:

- **Python**: `>= 3.11`
- **Package & Environment Manager**: [**`uv`**](https://github.com/astral-sh/uv) (recommended) or `pip`
- **Version Control**: `Git`
- **Container Runtime** _(Optional)_: `Docker` + `NVIDIA Container Toolkit` (for GPU containerization)

---

## Pre-Coding Setup Checklist

Complete this manual checklist before writing project code:

- [ ] **Project Metadata**: Update `name`, `version`, `description`, and `requires-python` in [`pyproject.toml`](pyproject.toml).
- [ ] **Environment Synchronization**: Run `uv sync --all-groups` to create the virtual environment and install the source package in editable mode (`-e .`).
- [ ] **Git Pre-commit Hooks**: Run `uv run pre-commit install` to enable automatic formatting and linting on git commits.
- [ ] **Secrets & Environment Variables**: Verify `.env` files are ignored in [`.gitignore`](.gitignore) before storing sensitive API keys or credentials.
- [ ] **Documentation URLs & Metadata**: Update `site_name`, `site_url`, and `repo_url` in [`properdocs.yml`](properdocs.yml).
- [ ] **Citation Info**: Update author details and ORCID in [`CITATION.cff`](CITATION.cff) and [`docs/citation-contact.md`](docs/citation-contact.md).

---

## Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/haddagart/tensoris.git
cd tensoris

# 2. Sync dependencies & setup virtual environment
uv sync --all-groups

# 3. Install pre-commit hooks
uv run pre-commit install

# 4. Launch training workflow
uv run python scripts/train.py --config inputs/experiments/default.yaml

# 5. Serve documentation site locally
uv run properdocs serve
```

### Or Run via GPU Docker Container (Hot-Reloaded)

```bash
# Launch training inside hot-reloaded GPU Docker environment
docker compose -f docker/docker-compose.yml up dev
```

---

## Template Flexibility

This project structure is designed as a **generic, modular boilerplate** suitable for both academic research and production-ready applications.

> [!TIP]
> Developers are encouraged to delete or remove any unnecessary folders or template files (e.g., `docker/`, `notebooks/marimo/`, `toolkit/`, or unused entrypoint scripts) to tailor the workspace to your specific project needs.

---

## Project Structure & Architecture

For a complete breakdown of all directories and architectural guidelines, see the [**Project Structure Overview**](docs/file-tree.md).

---

## Automatic Versioning & Releases

This project features tag-based dynamic versioning and automated bundling:

- **Dynamic Python Versioning**: Version is computed automatically from Git tags via `hatch-vcs` and exposed in `src/__init__.__version__`.
- **Automated GitHub Releases**: Pushing a tag (`git tag v1.0.0 && git push origin v1.0.0`) triggers `.github/workflows/release.yml` to compile `.whl` and `.tar.gz` bundles and publish a GitHub Release.
- **Multi-Version Docs**: `.github/workflows/docs.yml` uses `mike` to build and deploy multi-version documentation with an interactive version dropdown selector.

For full details, see the [**Versioning Guide**](docs/versioning.md).

---

## Social Responsibility & Environmental Commitment

[![Environment: Green Computing](https://img.shields.io/badge/environment-green%20computing-2b9348.svg)](#social-responsibility--environmental-commitment)
[![Equality: Anti-Discrimination](https://img.shields.io/badge/equality-anti--racism%20%26%20anti--discrimination-black.svg)](#social-responsibility--environmental-commitment)
[![Open Science: Free Access](https://img.shields.io/badge/open%20science-free%20%26%20accessible-0284c7.svg)](#social-responsibility--environmental-commitment)
[![AI Ethics: Responsible Science](https://img.shields.io/badge/AI%20Ethics-scientific%20integrity-8A2BE2.svg)](#ai--agentic-coding-in-research-ethics--scientific-deontology)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](docs/community.md)

### 🌿 Environmental Sustainability & Green Computing

We advocate for sustainable and energy-efficient practices in Artificial Intelligence and Deep Learning. High-performance GPU training carries a tangible environmental and carbon footprint. Developers using this boilerplate are encouraged to:

- Monitor compute energy consumption and carbon emissions (e.g., via tools like [`CodeCarbon`](https://codecarbon.io/)).
- Leverage efficient hyperparameter search, mixed precision (`fp16`/`bf16`), gradient accumulation, and early stopping to avoid wasted GPU compute cycles.

### 🔬 Support Free Science & Open Access

We stand in solidarity with researchers, scientists, and students worldwide affected by funding cuts, institutional constraints, or prohibitive paywalls. We believe scientific knowledge, open-source code, preprints, and open datasets should be freely accessible to everyone—without financial or geographical barriers.

### 🤝 Stand Against Discrimination & Racism

We stand firmly against all forms of racism, discrimination, harassment, and social inequality. Open-source science and technology thrive when everyone can participate safely, equitably, and with dignity. We are committed to fostering an inclusive, welcoming, and empowering research community for all.

### 🤖 AI & Agentic Coding in Research: Ethics & Scientific Deontology

Artificial Intelligence and Agentic Coding assistants are transformative catalysts for modern science—accelerating software setup, streamlining boilerplate engineering, and freeing researchers to focus on core domain insights.

However, technology serves as an amplifier of human intent, not a substitute for human responsibility. We advocate for the ethical and transparent use of AI in scientific research:

- **Human Accountability**: Authors and researchers remain fully accountable for their code correctness, mathematical proofs, experimental results, and scientific claims.
- **Scientific Rigor & Deontology**: AI-generated code, algorithms, and analytical logic must be thoroughly audited, verified, and validated against empirical ground truth.
- **Transparency & Attribution**: We encourage open declaration of AI tools used during software development and manuscript preparation, upholding the highest standards of academic honesty, reproducibility, and scientific ethics.

---

## Citation & Attribution

If you use **Tensoris** in your academic research or production applications, please consider citing it as below:

### BibTeX Entry

```bibtex
@software{haddag_tensoris_2026,
  author       = {Haddag, Abdelkader},
  title        = {Tensoris: Production-Ready PyTorch Framework},
  abstract     = {Production-ready PyTorch library with automated CI/CD, multi-version docs, and PyPI packaging. Made for researchers and coders in mind first.},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/haddagart/tensoris}}
}
```

### APA Style

> Haddag, A. (2026). _Tensoris: Production-Ready PyTorch Framework_. GitHub. https://github.com/haddagart/tensoris

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
