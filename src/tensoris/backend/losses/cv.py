"""Computer Vision Loss Functions."""

import torch
import torch.nn as nn
import torch.nn.functional as F


class FocalLoss(nn.Module):
    """Focal Loss for addressing class imbalance in computer vision tasks.

    Formula:
        $$\\text{FL}(p_t) = -\\alpha_t (1 - p_t)^\\gamma \\log(p_t)$$

        where $p_t$ is the model's estimated probability for the ground-truth class,
        $\\alpha_t$ is the class balancing factor, and $\\gamma$ is the focusing factor.

    References:
        Lin, T. Y., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017).
        Focal Loss for Dense Object Detection. Proceedings of the IEEE International
        Conference on Computer Vision (ICCV 2017), pp. 2980-2988.
        DOI: https://doi.org/10.1109/ICCV.2017.324 | arXiv: https://arxiv.org/abs/1708.02002
    """

    def __init__(self, alpha: float = 0.25, gamma: float = 2.0, reduction: str = "mean") -> None:
        """Initialize Focal Loss.

        Args:
            alpha: Weighting factor for class balancing.
            gamma: Focusing parameter for modulating easy example down-weighting.
            reduction: Reduction mode ('mean', 'sum', or 'none').
        """
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """Compute Focal Loss over logits and targets.

        Args:
            logits: Predicted class logits tensor of shape (N, C) or (N, C, H, W).
            targets: Ground truth class index tensor of shape (N) or (N, H, W).

        Returns:
            Computed Focal loss tensor.
        """
        ce_loss = F.cross_entropy(logits, targets, reduction="none")
        pt = torch.exp(-ce_loss)
        focal_loss = self.alpha * ((1 - pt) ** self.gamma) * ce_loss

        if self.reduction == "mean":
            return focal_loss.mean()
        elif self.reduction == "sum":
            return focal_loss.sum()
        return focal_loss


class DiceLoss(nn.Module):
    """Dice Loss for semantic image segmentation tasks.

    Formula:
        $$\\mathcal{L}_{\\text{Dice}} = 1 - \\frac{2 \\sum_{i} p_i y_i + \\epsilon}{\\sum_{i} p_i + \\sum_{i} y_i + \\epsilon}$$

        where $p_i$ is the predicted probability and $y_i$ is the ground-truth mask label.

    References:
        Milletari, F., Navab, N., & Ahmadi, S. A. (2016).
        V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation.
        Fourth International Conference on 3D Vision (3DV 2016), pp. 565-571.
        DOI: https://doi.org/10.1109/3DV.2016.79 | arXiv: https://arxiv.org/abs/1606.04797
    """

    def __init__(self, smooth: float = 1.0) -> None:
        """Initialize Dice Loss.

        Args:
            smooth: Smoothing epsilon factor to prevent division by zero.
        """
        super().__init__()
        self.smooth = smooth

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """Compute Dice Loss score.

        Args:
            logits: Predicted logits tensor of shape (N, C, H, W) or (N, H, W).
            targets: Ground truth target binary mask tensor of matching shape.

        Returns:
            Scalar Dice loss value (1.0 - Dice coefficient).
        """
        probs = F.softmax(logits, dim=1) if logits.ndim > 2 and logits.shape[1] > 1 else torch.sigmoid(logits)

        if targets.ndim == logits.ndim - 1:
            targets = F.one_hot(targets, num_classes=logits.shape[1]).permute(0, 3, 1, 2).float()

        dims = (0,) + tuple(range(2, probs.ndim))
        intersection = torch.sum(probs * targets, dim=dims)
        cardinality = torch.sum(probs + targets, dim=dims)

        dice_score = (2.0 * intersection + self.smooth) / (cardinality + self.smooth)
        return 1.0 - dice_score.mean()
