---
icon: material/scale-balance
---

# Ethics & Scientific Deontology

This document outlines the ethical guidelines, scientific deontology principles, and standards of academic integrity governing research software developed with this deep learning boilerplate template.

---

## 📜 Scientific Deontology Principles

Scientific software engineering requires the same rigor, transparency, and reproducibility as empirical experiment design.

### 1. Transparency & Reproducibility
- All hyperparameter configurations, random seeds, data preprocessing steps, and model weights must be explicitly logged and archived.
- Deterministic flags (`torch.use_deterministic_algorithms(True)`) should be enabled for published baseline benchmarks.

### 2. Peer-Reviewed Citations & Provenance
- Every neural layer, loss function, and architectural primitive implemented in this repository includes peer-reviewed paper citations (Author, Venue, Year, DOI/arXiv URL) directly in class docstrings.
- Developers extending this codebase must maintain citation provenance for external algorithms and baseline implementations.

### 3. Ethical AI & Automated Assistance
- AI pair programming assistants (e.g. Google's Gemini, Antigravity) are recognized as productivity tools.
- Authors remain solely responsible for the scientific validity, correctness, and accuracy of published models and experimental claims.

---

## ⚖️ Research Integrity Checklist

- [x] **No Ghost Writing**: All automated code generation is audited by domain experts.
- [x] **Citation Transparency**: Original paper authors are credited in docstrings and documentation.
- [x] **Data Integrity**: Datasets are accessed legally according to publisher licenses.
- [x] **Open Access**: Code and benchmarks are published openly under MIT License.