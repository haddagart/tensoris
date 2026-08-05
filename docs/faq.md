---
icon: material/help-circle
---

# Frequently Asked Questions (FAQ)

Common questions and troubleshooting solutions for working with this deep learning boilerplate.

---

### Q1: How do I add a new loss function or metric?
Place atomic layers in `src/backend/components/layers/`, building blocks in `src/backend/components/blocks/`, loss functions in `src/backend/losses/`, and evaluation metrics in `src/backend/metrics/`. Make sure to include Google-style docstrings with peer-reviewed paper citations under a `References:` section.

---

### Q2: Why is PyTorch GPU memory not clearing between validation runs?
Ensure you wrap all evaluation loops in `with torch.no_grad():` and call `torch.cuda.empty_cache()` if operating near peak VRAM limits.

---

### Q3: How do I run Docker GPU containers with live code updates?
Run the following command:
```bash
docker compose -f docker/docker-compose.yml up
```
The `./src`, `./scripts`, `./inputs`, and `./outputs` directories are live volume-mounted into `/app/`, so any edits to host Python files take effect immediately inside the running container without rebuilding.

---

### Q4: How do I export my trained PyTorch model for deployment?
Use the built-in `dl-model-exporter` skill or export manually via ONNX:
```python
import torch

model.eval()
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, "outputs/checkpoints/model.onnx", opset_version=17)
```

---

### Q5: How do I convert an existing PyTorch project to this template structure?
Use the automated `convert-to-dl-template` agent skill to reorganize raw modules, update `pyproject.toml`, and generate test suites automatically.