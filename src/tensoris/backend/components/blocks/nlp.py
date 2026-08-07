"""Natural Language Processing Transformer Encoder Blocks."""

import torch
import torch.nn as nn


class TransformerEncoderBlock(nn.Module):
    """Transformer Encoder Block with Multi-Head Self Attention and FeedForward network.

    References:
        Vaswani, A. et al. (2017). Attention Is All You Need. NIPS 2017.
        arXiv: https://arxiv.org/abs/1706.03762
    """

    def __init__(self, d_model: int = 256, nhead: int = 4, dim_feedforward: int = 512, dropout: float = 0.1) -> None:
        """Initialize TransformerEncoderBlock parameters.

        Args:
            d_model: Feature embedding dimension.
            nhead: Number of parallel attention heads.
            dim_feedforward: Hidden dimension of feedforward network.
            dropout: Dropout probability.
        """
        super().__init__()
        self.encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout, batch_first=True
        )

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        """Execute TransformerEncoderBlock forward pass."""
        return self.encoder_layer(x, src_key_padding_mask=mask)
