---
icon: material/file-document
---

# Workflow Scripts & Execution Loop

This page details the primary entrypoint scripts under `scripts/` used for PyTorch model training, hyperparameter tuning, evaluation, and exporting.

---

## 📊 Trainer & BaseModel Execution Flowchart

The diagram below illustrates the end-to-end execution loop managed by `scripts/train.py`, connecting hyperparameter configuration, dataset batch loading, `BaseModel` forward pass, loss computation, backward pass, gradient updates, metric logging, and checkpoint saving.

```mermaid
flowchart TD
    subgraph Initialization ["1. Setup & Configuration"]
        A["CLI Config (`inputs/experiments/default.yaml`)"] --> B["Initialize Hardware (CUDA GPU / MPS)"]
        B --> C["Instantiate BaseModel & Optimizer"]
    end

    subgraph DataPipeline ["2. Data Loading Pipeline"]
        C --> D["Dataset Loader (`src/data/dataset.py`)"]
        D --> E["Batch Transformation & Augmentation"]
    end

    subgraph TrainingLoop ["3. Forward & Backward Training Loop"]
        E --> F["BaseModel.forward(inputs)"]
        F --> G["Compute Loss (Focal / Dice / CrossEntropy)"]
        G --> H["Loss.backward() & Gradients"]
        H --> I["Optimizer.step() & Learning Rate Schedule"]
    end

    subgraph EvaluationLogging ["4. Evaluation & Artifact Logging"]
        I --> J["Compute Metrics (mIoU / Top-K Acc / PPL)"]
        J --> K{"Validation Metric Improved?"}
        K -- Yes --> L["Save Checkpoint (`outputs/checkpoints/best.pt`)"]
        K -- No --> M["Log Metrics (W&B / Console / File)"]
        L --> M
    end

    style Initialization fill:#1e1e2e,stroke:#74c7ec,stroke-width:2px,color:#cdd6f4
    style DataPipeline fill:#1e1e2e,stroke:#a6e3a1,stroke-width:2px,color:#cdd6f4
    style TrainingLoop fill:#1e1e2e,stroke:#f9e2af,stroke-width:2px,color:#cdd6f4
    style EvaluationLogging fill:#1e1e2e,stroke:#cba6f7,stroke-width:2px,color:#cdd6f4
```

---

## 🛠️ Execution Entrypoints

- `scripts/train.py`: Primary PyTorch model training loop supporting YAML configuration overrides, mixed precision (`fp16`), and metric logging.
- `scripts/evaluate.py`: Validation set evaluation and metric calculation (Accuracy, MeanIoU, Perplexity, FID Score).
- `scripts/export.py`: Trained PyTorch checkpoint exporter to ONNX and TorchScript deployment binaries.