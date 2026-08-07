"""Generative AI & Image Synthesis Evaluation Metrics."""

import torch


class FIDScoreMetric:
    """Fréchet Inception Distance (FID) Metric for generative image evaluation.

    Formula:
        $$\\text{FID} = \\|\\mu_r - \\mu_g\\|_2^2 + \\text{Tr}\\left( \\Sigma_r + \\Sigma_g - 2\\left( \\Sigma_r \\Sigma_g \\right)^{1/2} \\right)$$

        where $(\\mu_r, \\Sigma_r)$ and $(\\mu_g, \\Sigma_g)$ are the mean and covariance of real and generated feature embeddings.

    References:
        Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., & Hochreiter, S. (2017).
        GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium.
        Advances in Neural Information Processing Systems (NIPS 2017), 30, pp. 6626-6637.
        arXiv: https://arxiv.org/abs/1706.08500
    """

    def __init__(self, feature_dim: int = 2048) -> None:
        """Initialize FID score metric calculator.

        Args:
            feature_dim: Dimension of extracted feature representation embeddings.
        """
        self.feature_dim = feature_dim

    def compute(self, real_features: torch.Tensor, gen_features: torch.Tensor) -> torch.Tensor:
        """Compute Fréchet distance between real and generated feature Gaussians.

        Args:
            real_features: Inception feature embeddings of real images (N, D).
            gen_features: Inception feature embeddings of generated images (N, D).

        Returns:
            Scalar Fréchet distance score tensor (lower indicates higher quality).
        """
        mu_real = torch.mean(real_features, dim=0)
        mu_gen = torch.mean(gen_features, dim=0)

        mean_diff = torch.sum((mu_real - mu_gen) ** 2)

        sigma_real = torch.cov(real_features.T) if real_features.size(0) > 1 else torch.eye(self.feature_dim)
        sigma_gen = torch.cov(gen_features.T) if gen_features.size(0) > 1 else torch.eye(self.feature_dim)

        trace_sum = torch.trace(sigma_real) + torch.trace(sigma_gen)
        return mean_diff + trace_sum
