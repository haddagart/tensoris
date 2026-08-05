---
name: dl-paper-to-code
description: Guides AI agents in translating novel Deep Learning papers, mathematical equations, or pseudo-code into modular components (src/backend/components/), full models (src/models/), and unit tests.
---

# Deep Learning Paper-to-Code Implementation Skill

This skill guides AI agents in converting academic papers, equations, or novel architectural descriptions into clean, modular code within the project boilerplate.

---

## Workflow

### 1. Component Modularization
Decompose the paper architecture into reusable primitives:
- Layers & Attention mechanisms $\rightarrow$ `src/backend/components/layers/`
- Residual / Multi-layer blocks $\rightarrow$ `src/backend/components/blocks/`
- Multi-block stages $\rightarrow$ `src/backend/components/stages/`

### 2. Full Model Assembly
Combine backbones and components into `src/models/<paper_model_name>.py`.

### 3. Verification & Unit Testing
Write unit tests in `tests/unit/test_<model_name>.py` to verify forward pass output shapes, parameter counts, and gradient flow.
