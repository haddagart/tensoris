---
icon: material/bug
---

# Reporting a Bug

Thank you for helping improve this deep learning boilerplate repository!

---

## 🐛 Bug Report Guidelines

Before filing an issue, please verify the following:

1. **Search Existing Issues**: Search [GitHub Issues](https://github.com/haddagart/tensoris/issues) to ensure the bug hasn't already been reported.
2. **Isolate the Problem**: Provide a minimal reproduction script (see [Creating a Minimal Reproduction](reproduction.md)).
3. **Include System Details**:
   - Python version (`python3 --version`)
   - PyTorch version (`python3 -c "import torch; print(torch.__version__)"`)
   - Operating System & CUDA / MPS hardware details

---

## 📋 Submission Template

```markdown
### Bug Description
A clear and concise description of what the bug is.

### Steps to Reproduce
1. Run `python3 scripts/train.py --config ...`
2. Observe error output...

### Expected Behavior
A clear description of what you expected to happen.

### Error Stacktrace
```text
Paste full, untruncated error traceback here
```
```