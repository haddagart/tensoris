---
icon: material/layers-triple
hide:
  - navigation
---

# Adding Custom Neural Blocks & Losses

[← Back to Tutorials Overview](index.md)

<div style="display: flex; align-items: center; gap: 14px; margin-top: 16px; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--md-default-fg-color--lightest);">
  <img src="../../assets/authors/haddagart.png" style="width: 46px; height: 46px; border-radius: 50%; object-fit: cover;" alt="Abdelkader Haddag" />
  <div>
    <div style="font-weight: 700; font-size: 1.05em;">Abdelkader Haddag</div>
    <div style="font-size: 0.85em; opacity: 0.85;">Deep Learning Engineer & Researcher • 📅 Aug 5, 2026</div>
  </div>
</div>

This tutorial demonstrates how to extend the 3-tier modular architecture by implementing a custom neural block (`src/backend/components/blocks/`), adding a paper-cited loss function (`src/backend/losses/`), and writing automated unit tests.

---

## 🏗️ Step 1: Implementing a Custom Neural Block

Create a new file `src/backend/components/blocks/custom.py`:

```python
"""Custom residual squeeze-and-excitation neural block."""

import torch
import torch.nn as nn

class CustomSEBlock(nn.Module):
    """Squeeze-and-Excitation Residual Block.

    Reference:
        Hu et al., "Squeeze-and-Excitation Networks", CVPR 2018.
        DOI: 10.1109/CVPR.2018.00745
    """

    def __init__(self, in_channels: int, reduction: int = 16) -> None:
        super().__init__()
        reduced_dim = max(1, in_channels // reduction)
        self.fc = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(in_channels, reduced_dim, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(reduced_dim, in_channels, bias=False),
            nn.Sigmoid(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b, c, _, _ = x.shape
        w = self.fc(x).view(b, c, 1, 1)
        return x * w
```

---

## ⚖️ Step 2: Adding a Custom Paper-Cited Loss Function

Add your loss function under `src/backend/losses/cv.py`:

```python
class CustomDiceLoss(nn.Module):
    """Dice Loss for Volumetric / Semantic Image Segmentation.

    Reference:
        Milletari et al., "V-Net: Fully Convolutional Neural Networks for Volumetric
        Medical Image Segmentation", 3DV 2016. arXiv: 1606.04797
    """

    def __init__(self, smooth: float = 1.0) -> None:
        super().__init__()
        self.smooth = smooth

    def forward(self, inputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        inputs = torch.sigmoid(inputs)
        intersection = (inputs * targets).sum()
        dice = (2.0 * intersection + self.smooth) / (inputs.sum() + targets.sum() + self.smooth)
        return 1.0 - dice
```

---

## 🧪 Step 3: Writing Automated Unit Tests

Add a unit test in `tests/unit/test_custom_block.py`:

```python
import torch
from src.backend.components.blocks.custom import CustomSEBlock

def test_custom_se_block_shape() -> None:
    block = CustomSEBlock(in_channels=64)
    x = torch.randn(2, 64, 32, 32)
    out = block(x)
    assert out.shape == x.shape
```

Run tests via `pytest`:

```bash
uv run pytest tests/unit/test_custom_block.py
```
