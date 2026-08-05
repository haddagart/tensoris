---
icon: fontawesome/brands/git-alt
---

# Making a Pull Request

Thank you for contributing code or documentation to this repository!

---

## 🔀 Pull Request Checklist

Before submitting a Pull Request (PR):

- [ ] **Branch Naming**: Use descriptive branch names (`feature/focal-loss`, `fix/gradient-clip`).
- [ ] **Code Formatting**: Run `uv run ruff check .` and `uv run ruff format .`.
- [ ] **Type Checking**: Run `uv run mypy src`.
- [ ] **Unit Tests**: Pass all unit tests via `uv run pytest tests/unit`.
- [ ] **Documentation**: Ensure new classes have Google-style docstrings with paper citations.