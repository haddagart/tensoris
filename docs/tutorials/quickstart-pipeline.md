---
icon: material/rocket-launch
hide:
  - navigation
---

# Quickstart Training Pipeline

[← Back to Tutorials Overview](index.md)

<div style="display: flex; align-items: center; gap: 14px; margin-top: 16px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--md-default-fg-color--lightest);">
  <img src="../../assets/authors/haddagart.png" style="width: 46px; height: 46px; border-radius: 50%; object-fit: cover;" alt="Abdelkader Haddag" />
  <div>
    <div style="font-weight: 700; font-size: 1.05em;">Abdelkader Haddag</div>
    <div style="font-size: 0.85em; opacity: 0.85;">Deep Learning Engineer & Researcher • 📅 Aug 5, 2026</div>
  </div>
</div>

This tutorial provides a complete walkthrough for configuring hyperparameter YAML files, executing PyTorch model training workflows via `scripts/train.py`, tracking real-time metrics, and evaluating saved model checkpoints.

---

## 🛠️ Step 1: Inspecting Experiment Configuration

All training experiments are controlled via modular YAML configuration files located under `inputs/experiments/`.

Inspect [`inputs/experiments/default.yaml`](https://github.com/haddagart/haddag-dl-template-2/blob/main/inputs/experiments/default.yaml):

```yaml
experiment_name: "default_resnet_baseline"
seed: 42

data:
  batch_size: 64
  num_workers: 4
  image_size: 224

model:
  name: "VisionBackbone"
  num_classes: 10
  dropout: 0.2

training:
  epochs: 20
  learning_rate: 0.001
  weight_decay: 1e-4
  fp16: true
  checkpoint_dir: "outputs/checkpoints/"
  log_dir: "logs/metrics/"
```

---

## 🚀 Step 2: Executing Model Training

Run the training loop using the `uv` toolchain:

```bash
uv run python scripts/train.py --config inputs/experiments/default.yaml
```

### What Happens During Execution

1. **Environment Verification**: Detects CUDA GPU or Apple Silicon MPS device acceleration.
2. **Model Instantiation**: Builds the PyTorch `VisionBackbone` architecture (`src/models/cv/backbone.py`).
3. **Loss & Optimizer Setup**: Instantiates `FocalLoss` and AdamW optimizer with cosine learning rate scheduling.
4. **Training Loop**: Runs epochs, logging training and validation metrics to `logs/metrics/`.
5. **Checkpoint Saving**: Saves the best validation model weights to `outputs/checkpoints/best_model.pt`.

---

## 📊 Step 3: Evaluating Saved Checkpoints

Evaluate the trained checkpoint on the validation set using `scripts/evaluate.py`:

```bash
uv run python scripts/evaluate.py \
  --checkpoint outputs/checkpoints/best_model.pt \
  --config inputs/experiments/default.yaml
```

Expected output:

```text
Validation Accuracy: 94.25%
Top-5 Accuracy:      99.10%
Mean Loss:           0.142
```
