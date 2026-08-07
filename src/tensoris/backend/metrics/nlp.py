"""Natural Language Processing Evaluation Metrics."""

import torch


class PerplexityMetric:
    """Perplexity metric for language model evaluation.

    Formula:
        $$\\text{PPL} = \\exp\\left( -\\frac{1}{N} \\sum_{i=1}^N \\log p(x_i \\mid x_{<i}) \\right) = \\exp\\left( \\mathcal{L}_{\\text{CE}} \\right)$$

        where $\\mathcal{L}_{\\text{CE}}$ is the average cross-entropy loss per token.

    References:
        Jelinek, F., Mercer, R. L., Bahl, L. R., & Baker, J. K. (1977).
        Perplexity—a measure of the difficulty of speech recognition tasks.
        Journal of the Acoustical Society of America, 62(S1), S63-S63.
    """

    def __init__(self) -> None:
        """Initialize perplexity accumulator."""
        self.reset()

    def reset(self) -> None:
        """Reset accumulated loss counts."""
        self.total_loss = 0.0
        self.total_count = 0

    def update(self, cross_entropy_loss: torch.Tensor | float, token_count: int) -> None:
        """Accumulate token cross-entropy loss.

        Args:
            cross_entropy_loss: Average batch cross-entropy loss.
            token_count: Number of active non-padding tokens in batch.
        """
        loss_val = cross_entropy_loss.item() if hasattr(cross_entropy_loss, "item") else float(cross_entropy_loss)
        self.total_loss += loss_val * token_count
        self.total_count += token_count

    def compute(self) -> float:
        """Compute exponentiated mean cross-entropy perplexity.

        Returns:
            Scalar perplexity value exp(mean_loss).
        """
        if self.total_count == 0:
            return 0.0
        mean_loss = self.total_loss / self.total_count
        return torch.exp(torch.tensor(mean_loss)).item()
