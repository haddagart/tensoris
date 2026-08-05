---
name: dl-experiment-runner
description: Automates deep learning hyperparameter configuration, launches training runs via scripts/train.py, tracks metrics across outputs/ and logs/, and generates comparative Markdown analysis reports.
---

# Deep Learning Experiment Runner Skill

This skill guides AI agents in configuring, launching, tracking, and reporting Deep Learning experiments within the boilerplate architecture.

---

## Workflow

### 1. Create Experiment Configuration
Create a dedicated YAML override file in `inputs/experiments/<experiment_name>.yaml`:

```yaml
project:
  name: "experiment-lr-sweep"
  seed: 42

model:
  architecture: "resnet18"
  pretrained: true

training:
  epochs: 15
  learning_rate: 0.0005
  optimizer: "adamw"
```

### 2. Launch Training Run
Execute the standard training entrypoint:

```bash
uv run python scripts/train.py --config inputs/experiments/<experiment_name>.yaml
```

### 3. Parse & Summarize Metrics
Extract training and validation metrics from `outputs/artifacts/` and `logs/`. Generate comparative Markdown summary tables with loss and accuracy progressions.
