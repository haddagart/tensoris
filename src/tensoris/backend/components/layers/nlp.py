"""Natural Language Processing Positional Encoding Layers."""

import math

import torch
import torch.nn as nn


class PositionalEncoding(nn.Module):
    """Sinusoidal Positional Encoding Layer for Sequence Transformers.

    References:
        Vaswani, A. et al. (2017). Attention Is All You Need. NIPS 2017.
        arXiv: https://arxiv.org/abs/1706.03762
    """

    def __init__(self, d_model: int, max_len: int = 5000) -> None:
        """Initialize PositionalEncoding layer.

        Args:
            d_model: Token embedding vector dimension.
            max_len: Maximum sequence length.
        """
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)
        )

        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe.unsqueeze(0))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Add positional encodings to token embeddings."""
        return x + self.pe[:, : x.size(1)]
