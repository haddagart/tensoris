"""Generative AI Encoder and Decoder Blocks."""

import torch
import torch.nn as nn


class VAEEncoderBlock(nn.Module):
    """Encoder Block for Variational Autoencoders."""

    def __init__(self, in_features: int, hidden_dim: int, latent_dim: int) -> None:
        """Initialize VAEEncoderBlock.

        Args:
            in_features: Input sample features.
            hidden_dim: Hidden dimension size.
            latent_dim: Latent z space dimension.
        """
        super().__init__()
        self.fc = nn.Linear(in_features, hidden_dim)
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Encode input into mean and log variance parameters."""
        h = torch.relu(self.fc(x))
        return self.fc_mu(h), self.fc_logvar(h)


class VAEDecoderBlock(nn.Module):
    """Decoder Block for Variational Autoencoders."""

    def __init__(self, latent_dim: int, hidden_dim: int, out_features: int) -> None:
        """Initialize VAEDecoderBlock.

        Args:
            latent_dim: Latent z space dimension.
            hidden_dim: Hidden dimension size.
            out_features: Output sample feature dimension.
        """
        super().__init__()
        self.fc = nn.Linear(latent_dim, hidden_dim)
        self.fc_out = nn.Linear(hidden_dim, out_features)

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        """Decode latent vector z to reconstructed sample space."""
        h = torch.relu(self.fc(z))
        return torch.sigmoid(self.fc_out(h))
