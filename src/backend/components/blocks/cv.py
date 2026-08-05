"""Computer Vision Network Blocks."""

import torch
import torch.nn as nn


class ResidualBlock(nn.Module):
    """Residual Skip Connection Block for ResNet architectures.

    References:
        He, K., Zhang, X., Ren, S., & Sun, J. (2016).
        Deep Residual Learning for Image Recognition. IEEE CVPR 2016.
        arXiv: https://arxiv.org/abs/1512.03385
    """

    def __init__(self, channels: int) -> None:
        """Initialize ResidualBlock.

        Args:
            channels: Feature map channel dimension.
        """
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Execute ResidualBlock forward pass with identity shortcut."""
        residual = x
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual
        return self.relu(out)
