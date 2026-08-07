"""Generative AI & Multimodal Loss Functions."""

import torch
import torch.nn as nn
import torch.nn.functional as F


class ContrastiveInfoNCELoss(nn.Module):
    """InfoNCE Loss for self-supervised contrastive learning and multimodal alignment (CLIP).

    Formula:
        $$\\mathcal{L}_{\\text{InfoNCE}} = -\\log \\frac{\\exp(\\text{sim}(z_i, z_j) / \\tau)}{\\sum_{k=1}^{2N} \\mathbb{1}_{[k \\neq i]} \\exp(\\text{sim}(z_i, z_k) / \\tau)}$$

        where $\\text{sim}(u, v) = \\frac{u^T v}{\\|u\\|_2 \\|v\\|_2}$ and $\\tau$ is the temperature hyperparameter.

    References:
        Oord, A. v. d., Li, Y., & Vinyals, O. (2018).
        Representation Learning with Contrastive Predictive Coding.
        arXiv preprint arXiv:1807.03748. https://arxiv.org/abs/1807.03748

        Radford, A. et al. (2021). Learning Transferable Visual Models From Natural Language Supervision.
        Proceedings of the International Conference on Machine Learning (ICML 2021).
    """

    def __init__(self, temperature: float = 0.07) -> None:
        """Initialize InfoNCE Loss.

        Args:
            temperature: Scaling temperature parameter for logit normalization.
        """
        super().__init__()
        self.temperature = temperature

    def forward(
        self, image_features: torch.Tensor, text_features: torch.Tensor
    ) -> torch.Tensor:
        """Compute InfoNCE contrastive alignment loss.

        Args:
            image_features: Normalized image feature representations of shape (N, D).
            text_features: Normalized text feature representations of shape (N, D).

        Returns:
            Scalar contrastive loss value.
        """
        image_norm = F.normalize(image_features, dim=-1)
        text_norm = F.normalize(text_features, dim=-1)

        logits = (image_norm @ text_norm.T) / self.temperature
        labels = torch.arange(logits.size(0), device=logits.device)

        loss_img = F.cross_entropy(logits, labels)
        loss_txt = F.cross_entropy(logits.T, labels)
        return (loss_img + loss_txt) / 2.0


class PerceptualLoss(nn.Module):
    """Perceptual Reconstruction Loss for image synthesis and latent diffusion.

    Formula:
        $$\\mathcal{L}_{\\text{perceptual}}(\\hat{x}, x) = \\sum_{l} \\frac{1}{H_l W_l} \\left\\| \\phi^l(\\hat{x}) - \\phi^l(x) \\right\\|_1$$

        where $\\phi^l$ denotes feature maps extracted from layer $l$ of a pre-trained feature extractor network.

    References:
        Johnson, J., Alahi, A., & Fei-Fei, L. (2016).
        Perceptual Losses for Real-Time Style Transfer and Super-Resolution.
        European Conference on Computer Vision (ECCV 2016), pp. 694-711.
        DOI: https://doi.org/10.1007/978-3-319-46475-6_43 | arXiv: https://arxiv.org/abs/1603.08155
    """

    def __init__(self) -> None:
        """Initialize Perceptual Loss."""
        super().__init__()

    def forward(self, generated: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        """Compute feature representation L1 difference.

        Args:
            generated: Generated sample tensor of shape (N, C, H, W).
            target: Ground truth target sample tensor of shape (N, C, H, W).

        Returns:
            Scalar perceptual loss value.
        """
        return F.l1_loss(generated, target)
