---
icon: material/ruler
---

# Coding Standards & Conventions

This document specifies the code style guidelines, formatting rules, static typing requirements, and quality checks enforced across this repository.

---

## 🛠️ Tools & Enforcers

| Tool | Category | Standard | Command |
| :--- | :--- | :--- | :--- |
| **`ruff`** | Formatter & Linter | Line length 88, `isort`, `pyupgrade`, `bugbear` | `uv run ruff check . && uv run ruff format .` |
| **`mypy`** | Static Type Checker | Python 3.11+ type annotations | `uv run mypy src` |
| **`pytest`** | Unit Test Runner | Test suite under `tests/unit/` | `uv run pytest tests/unit` |
| **`pre-commit`** | Git Hook Manager | Automatic pre-commit hook enforcement | `uv run pre-commit install` |

---

## 📝 Docstring Style

All Python classes, methods, and functions must adhere strictly to **Google Docstring Format** with explicit argument types, return descriptions, and peer-reviewed citations where applicable:

```python
def forward(self, inputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """Compute Focal Loss between predictions and ground truth labels.

    Args:
        inputs: Predictions tensor of shape (N, C) or (N, C, H, W).
        targets: Target ground-truth labels tensor of shape (N,) or (N, H, W).

    Returns:
        Scalar loss tensor computed across batch dimensions.
    """
```