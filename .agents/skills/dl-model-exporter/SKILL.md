---
name: dl-model-exporter
description: Guides AI agents in exporting trained PyTorch model checkpoints (.pt, .ckpt) into production deployment formats like ONNX and TorchScript, verifying output tensor shapes and inference speed.
---

# Deep Learning Model Exporter Skill

This skill guides AI agents in exporting PyTorch model weights from `outputs/weights/` into production-ready deployment artifacts (ONNX / TorchScript) in `outputs/artifacts/`.

---

## Workflow

### 1. Load Model & Checkpoint
Import the target model architecture from `src/models/` and load weights from `outputs/weights/best_model.pt`.

### 2. Export to ONNX / TorchScript
Run trace or script exporting with dummy input tensors:

```python
import torch
from src.models.my_model import MyModel

model = MyModel()
model.load_state_dict(torch.load("outputs/weights/best_model.pt"))
model.eval()

dummy_input = torch.randn(1, 3, 224, 224)

# Export to ONNX
torch.onnx.export(
    model,
    dummy_input,
    "outputs/artifacts/model.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
)
```

### 3. Verify Inference Correctness
Load exported ONNX model with `onnxruntime` and verify outputs match PyTorch eager execution.
