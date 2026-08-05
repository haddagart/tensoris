---
icon: fontawesome/solid/code-pull-request
---

# Contributing Guidelines

We welcome contributions to enhance this deep learning boilerplate template! Follow these guidelines to ensure consistency, high code quality, and proper scientific attribution.

---

## 1. Development Principles

1. **Modular Architectural Integrity**: Keep atomic layers in `src/backend/components/layers/`, multi-layer blocks in `src/backend/components/blocks/`, loss functions in `src/backend/losses/`, evaluation metrics in `src/backend/metrics/`, and composite models in `src/models/`.
2. **Academic Rigor**: Always include official peer-reviewed paper citations (Authors, Venue, Year, Title, DOI/arXiv URL) in the docstrings of newly added neural primitives.
3. **Type Annotations**: Provide strict Python type hints for all function arguments and return types.

---

## 2. Code Quality & Formatting

Before opening a pull request, format your code and run syntax validation:

```bash
# Run pytest unit test suite
pytest tests/unit/

# Run static syntax analysis across src/
python3 -c "import ast, pathlib; [ast.parse(p.read_text()) for p in pathlib.Path('src').rglob('*.py')]"

# Build documentation locally
uv run properdocs serve
```

---

## 3. Pull Request Checklist

- [ ] Code follows Google Python Style Guide.
- [ ] Added docstrings with academic references for new loss functions or architectures.
- [ ] Updated `NAV_TITLES` in `docs/gen_ref_pages.py` if adding a new package directory.
- [ ] Unit tests added in `tests/unit/` and verified clean with `pytest`.
- [ ] Local documentation builds cleanly with zero broken links.