"""Natural Language Processing Transformer Models."""

import torch
import torch.nn as nn
from src.backend.components.blocks.nlp import TransformerEncoderBlock
from src.backend.components.layers.nlp import PositionalEncoding


class TransformerClassifier(nn.Module):
    """Transformer Encoder Sequence Classifier Model.

    References:
        Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N.,
        Kaiser, Ł., & Polosukhin, I. (2017).
        Attention Is All You Need.
        Advances in Neural Information Processing Systems (NIPS 2017), 30, pp. 5998-6008.
        arXiv: https://arxiv.org/abs/1706.03762
    """

    def __init__(
        self,
        vocab_size: int = 30522,
        hidden_dim: int = 256,
        num_heads: int = 4,
        num_classes: int = 2,
        max_seq_len: int = 512,
    ) -> None:
        """Initialize Transformer Classifier parameters.

        Args:
            vocab_size: Vocabulary token size.
            hidden_dim: Token embedding dimension.
            num_heads: Number of parallel self-attention heads.
            num_classes: Classification target categories.
            max_seq_len: Maximum sequence token length.
        """
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_dim)
        self.pos_encoder = PositionalEncoding(hidden_dim, max_len=max_seq_len)
        self.block1 = TransformerEncoderBlock(d_model=hidden_dim, nhead=num_heads)
        self.block2 = TransformerEncoderBlock(d_model=hidden_dim, nhead=num_heads)
        self.classifier = nn.Linear(hidden_dim, num_classes)

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor | None = None) -> torch.Tensor:
        """Execute forward pass sequence classification.

        Args:
            input_ids: Token ID sequences tensor of shape (N, T).
            attention_mask: Mask tensor indicating active non-padding tokens.

        Returns:
            Classification prediction logits tensor of shape (N, num_classes).
        """
        embeddings = self.pos_encoder(self.embedding(input_ids))
        encoded = self.block1(embeddings, mask=attention_mask)
        encoded = self.block2(encoded, mask=attention_mask)

        # Pooled mean representation across sequence
        pooled = encoded.mean(dim=1)
        return self.classifier(pooled)
