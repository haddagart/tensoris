---
icon: material/share-variant
---

# Integrations & Platform Helpers

This boilerplate includes automated integrations for Kaggle, Weights & Biases (W&B), Hugging Face Hub, Ultralytics YOLO, and Roboflow under `src/lib/integrations/`.

---

## 🔌 Supported Platforms

- **Kaggle**: Automatic dataset download and competition prediction submission (`KaggleIntegration`).
- **Weights & Biases**: Experiment tracking, loss curve dashboards, and checkpoint artifact uploads (`WandbIntegration`).
- **Hugging Face Hub**: Push PyTorch model checkpoints and download pretrained weights (`HuggingFaceIntegration`).
- **Ultralytics YOLO**: Train, evaluate, and export object detection/segmentation models (`UltralyticsIntegration`).
- **Roboflow**: Download computer vision datasets directly into `inputs/datasets/` (`RoboflowIntegration`).