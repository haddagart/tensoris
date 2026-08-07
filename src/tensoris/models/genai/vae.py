"""Generative AI Variational Autoencoder (VAE) Model Architecture."""

import torch
import torch.nn as nn

from tensoris.backend.components.blocks.genai import VAEDecoderBlock, VAEEncoderBlock


class VariationalAutoencoder(nn.Module):
    """Variational Autoencoder (VAE) for generative image modeling and latent space sampling.

    References:
        Kingma, D. P., & Welling, M. (2014).
        Auto-Encoding Variational Bayes.
        International Conference on Learning Representations (ICLR 2014).
        arXiv: https://arxiv.org/abs/1312.6114
    """

    def __init__(self, input_dim: int = 784, hidden_dim: int = 400, latent_dim: int = 20) -> None:
        """Initialize VAE encoder and decoder parameters.

        Args:
            input_dim: Flattened input sample feature dimension.
            hidden_dim: Hidden representation layer dimension.
            latent_dim: Dimensionality of latent Gaussian z space.
        """
        super().__init__()
        self.encoder = VAEEncoderBlock(input_dim, hidden_dim, latent_dim)
        self.decoder = VAEDecoderBlock(latent_dim, hidden_dim, input_dim)

    def encode(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Encode input into mean and log variance parameters."""
        return self.encoder(x)

    def reparameterize(self, mu: torch.Tensor, logvar: torch.Tensor) -> torch.Tensor:
        """Apply Gaussian reparameterization trick: z = mu + std * epsilon."""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z: torch.Tensor) -> torch.Tensor:
        """Decode latent vector z back to original feature space."""
        return self.decoder(z)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Execute full VAE forward encoding, reparameterization, and reconstruction.

        Args:
            x: Input tensor batch of shape (N, input_dim).

        Returns:
            Tuple of (reconstructed_x, mu, logvar).
        """
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar
