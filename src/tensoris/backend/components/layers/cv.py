"""Computer Vision Atomic Neural Network Layers."""

import torch
import torch.nn as nn


class ConvStem(nn.Module):
    """Convolutional Stem Layer for Computer Vision Backbones."""

    def __init__(self, in_channels: int = 3, out_channels: int = 64) -> None:
        """Initialize ConvStem layer.

        Args:
            in_channels: Input image channels (3 for RGB).
            out_channels: Output feature map channels.
        """
        super().__init__()
        self.stem = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=7, stride=2, padding=3, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Execute ConvStem forward pass."""
        return self.stem(x)
