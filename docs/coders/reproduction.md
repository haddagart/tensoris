---
icon: material/test-tube
---

# Creating a Minimal Reproduction

When reporting a bug or requesting assistance, providing a minimal reproduction script accelerates debugging and resolution.

---

## 🧪 Minimal Reproduction Guidelines

1. **Self-Contained Script**: Ensure the code runs independently without requiring external unpublished datasets.
2. **Synthetic Data**: Use dummy PyTorch tensors (e.g. `torch.randn(2, 3, 224, 224)`) to reproduce shape or loss computation errors.
3. **Environment Info**: Include the exact terminal output of `python3 main.py` or system info.