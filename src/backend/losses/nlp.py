"""Natural Language Processing Loss Functions."""

import torch
import torch.nn as nn
import torch.nn.functional as F


class LabelSmoothingCrossEntropy(nn.Module):
    """Cross Entropy loss with label smoothing for sequence modeling and classification.

    Formula:
        $$y_k^{\\text{smooth}} = (1 - \\epsilon) \\cdot y_k + \\frac{\\epsilon}{K}$$

        $$\\mathcal{L}_{\\text{LSCE}} = -\\sum_{k=1}^K y_k^{\\text{smooth}} \\log(p_k)$$

        where $\\epsilon$ is the smoothing factor, $K$ is the total number of classes,
        and $p_k = \\text{softmax}(z)_k$.

    References:
        Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., & Wojna, Z. (2016).
        Rethinking the Inception Architecture for Computer Vision.
        Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2016), pp. 2818-2826.
        DOI: https://doi.org/10.1109/CVPR.2016.308 | arXiv: https://arxiv.org/abs/1512.00567

        Vaswani, A. et al. (2017). Attention Is All You Need. NIPS 2017.
    """

    def __init__(self, smoothing: float = 0.1, ignore_index: int = -100) -> None:
        """Initialize Label Smoothing Cross Entropy loss.

        Args:
            smoothing: Label smoothing factor epsilon between 0.0 and 1.0.
            ignore_index: Target index ignored during loss computation (padding token).
        """
        super().__init__()
        self.smoothing = smoothing
        self.ignore_index = ignore_index

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """Compute label smoothed cross-entropy loss.

        Args:
            logits: Predicted vocabulary logits tensor of shape (N, C) or (N, T, C).
            targets: Ground truth token indices tensor of shape (N) or (N, T).

        Returns:
            Scalar smoothed cross entropy loss tensor.
        """
        if logits.ndim == 3:
            logits = logits.view(-1, logits.size(-1))
            targets = targets.view(-1)

        return F.cross_entropy(
            logits,
            targets,
            label_smoothing=self.smoothing,
            ignore_index=self.ignore_index,
        )
