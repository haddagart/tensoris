"""Computer Vision ResNet Backbone Architecture."""

import torch
import torch.nn as nn

from src.backend.components.blocks.cv import ResidualBlock
from src.backend.components.layers.cv import ConvStem


class VisionBackbone(nn.Module):
    """Convolutional Neural Network ResNet Vision Backbone Model.

    References:
        He, K., Zhang, X., Ren, S., & Sun, J. (2016).
        Deep Residual Learning for Image Recognition.
        Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2016), pp. 770-778.
        DOI: https://doi.org/10.1109/CVPR.2016.90 | arXiv: https://arxiv.org/abs/1512.03385
    """

    def __init__(self, in_channels: int = 3, num_classes: int = 1000, hidden_dim: int = 64) -> None:
        """Initialize Vision Backbone model layers.

        Args:
            in_channels: Input image color channels (e.g. 3 for RGB).
            num_classes: Output class prediction logit dimension.
            hidden_dim: Convolutional channel dimension size.
        """
        super().__init__()
        self.stem = ConvStem(in_channels, hidden_dim)
        self.res_block1 = ResidualBlock(hidden_dim)
        self.res_block2 = ResidualBlock(hidden_dim)
        self.gap = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Execute forward pass feature extraction.

        Args:
            x: Input image tensor batch of shape (N, C, H, W).

        Returns:
            Class prediction logits tensor of shape (N, num_classes).
        """
        features = self.stem(x)
        features = self.res_block1(features)
        features = self.res_block2(features)
        pooled = self.gap(features).flatten(1)
        return self.fc(pooled)
