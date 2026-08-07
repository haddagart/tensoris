---
icon: material/hub
hide:
  - navigation
---

# Platform Integrations (W&B, Hugging Face, Kaggle)

[← Back to Tutorials Overview](index.md)

<div style="display: flex; align-items: center; gap: 14px; margin-top: 16px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--md-default-fg-color--lightest);">
  <img src="../../assets/authors/haddagart.png" style="width: 46px; height: 46px; border-radius: 50%; object-fit: cover;" alt="Abdelkader Haddag" />
  <div>
    <div style="font-weight: 700; font-size: 1.05em;">Abdelkader Haddag</div>
    <div style="font-size: 0.85em; opacity: 0.85;">Deep Learning Engineer & Researcher • 📅 Aug 5, 2026</div>
  </div>
</div>

This tutorial covers how to utilize the pre-built platform helpers in `src/lib/integrations/` to connect training runs to **Weights & Biases (W&B)**, upload model weights to **Hugging Face Hub**, and download datasets from **Kaggle** and **Roboflow**.

---

## 📊 Weights & Biases (W&B) Experiment Tracking

Enable real-time loss curves, system metrics, and artifact logging:

```python
from src.lib.integrations.wandb import WandbIntegration

# Initialize W&B run
wandb_logger = WandbIntegration(
    project="deep-learning-boilerplate",
    name="experiment_resnet_v1",
    config={"learning_rate": 0.001, "batch_size": 64},
)

# Log training step metrics
wandb_logger.log_metrics({"train/loss": 0.245, "val/accuracy": 0.942}, step=epoch)

# Save checkpoint artifact
wandb_logger.log_artifact(
    name="model-checkpoint",
    type_name="model",
    filepath="outputs/checkpoints/best_model.pt",
)
wandb_logger.finish()
```

---

## 🤗 Hugging Face Hub Checkpoint Export

Upload trained PyTorch model checkpoints directly to the Hugging Face Model Hub:

```python
from src.lib.integrations.huggingface import HuggingFaceIntegration

hf_helper = HuggingFaceIntegration(repo_id="your-username/my-resnet-model")

# Upload model checkpoint
hf_helper.upload_model(
    checkpoint_path="outputs/checkpoints/best_model.pt",
    commit_message="Upload trained ResNet baseline checkpoint",
)
```

---

## 🏆 Kaggle & Roboflow Dataset Automation

Download datasets directly into `inputs/datasets/`:

```python
from src.lib.integrations.kaggle import KaggleIntegration
from src.lib.integrations.roboflow import RoboflowIntegration

# Download Kaggle competition dataset
kaggle = KaggleIntegration()
kaggle.download_dataset(dataset_name="cifar10", output_dir="inputs/datasets/cifar10")

# Download Roboflow object detection dataset
rf = RoboflowIntegration(api_key="YOUR_ROBOFLOW_KEY")
rf.download_dataset(
    workspace="vision-research",
    project="object-detection-v1",
    version=1,
    output_dir="inputs/datasets/roboflow_dataset",
)
```
