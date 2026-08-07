"""Unit tests for Tensoris neural network models."""

import pytest

try:
    import torch

    from tensoris.models.cv.backbone import VisionBackbone
    from tensoris.models.genai.vae import VariationalAutoencoder
    from tensoris.models.nlp.transformer import TransformerClassifier

    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

pytestmark = pytest.mark.skipif(
    not HAS_TORCH, reason="PyTorch is required for model unit tests"
)


def test_vision_backbone_forward():
    """Verify VisionBackbone output tensor shape."""
    model = VisionBackbone(in_channels=3, num_classes=10, hidden_dim=32)
    inputs = torch.randn(4, 3, 64, 64)
    logits = model(inputs)
    assert isinstance(logits, torch.Tensor)
    assert logits.shape == (4, 10)


def test_transformer_classifier_forward():
    """Verify TransformerClassifier sequence output shape."""
    model = TransformerClassifier(
        vocab_size=1000, num_classes=5, hidden_dim=64, num_heads=2, num_layers=2
    )
    input_ids = torch.randint(0, 1000, (2, 16))
    logits = model(input_ids)
    assert isinstance(logits, torch.Tensor)
    assert logits.shape == (2, 5)


def test_variational_autoencoder_forward():
    """Verify VAE encoding, reparameterization, and reconstruction output shapes."""
    model = VariationalAutoencoder(input_dim=100, hidden_dim=32, latent_dim=8)
    inputs = torch.randn(4, 100)
    recon_x, mu, logvar = model(inputs)
    assert recon_x.shape == (4, 100)
    assert mu.shape == (4, 8)
    assert logvar.shape == (4, 8)
