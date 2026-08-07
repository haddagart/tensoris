"""Unit tests for Tensoris backend engines, losses, metrics, and trainer."""

import pytest

try:
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader, TensorDataset

    from tensoris.backend.losses.cv import focal_loss
    from tensoris.backend.losses.genai import vae_loss
    from tensoris.backend.metrics.cv import calculate_accuracy
    from tensoris.backend.trainers.trainer import ModelTrainer

    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

pytestmark = pytest.mark.skipif(
    not HAS_TORCH, reason="PyTorch is required for backend unit tests"
)


def test_calculate_accuracy():
    """Verify classification accuracy score calculation."""
    logits = torch.tensor([[2.0, 0.5], [0.1, 3.0], [4.0, 1.0]])
    targets = torch.tensor([0, 1, 0])
    acc = calculate_accuracy(logits, targets)
    assert acc == pytest.approx(1.0)


def test_focal_loss():
    """Verify focal loss scalar computation."""
    logits = torch.tensor([[1.0, -1.0], [-2.0, 2.0]])
    targets = torch.tensor([0, 1])
    loss = focal_loss(logits, targets)
    assert isinstance(loss, torch.Tensor)
    assert loss.dim() == 0  # scalar
    assert loss.item() > 0.0


def test_vae_loss():
    """Verify VAE compound loss computation."""
    recon_x = torch.randn(4, 50)
    x = torch.randn(4, 50)
    mu = torch.randn(4, 10)
    logvar = torch.randn(4, 10)
    loss = vae_loss(recon_x, x, mu, logvar)
    assert isinstance(loss, torch.Tensor)
    assert loss.item() > 0.0


def test_model_trainer_step():
    """Verify ModelTrainer single epoch training and validation step."""
    model = nn.Sequential(nn.Linear(10, 2))
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()

    trainer = ModelTrainer(
        model=model, optimizer=optimizer, criterion=criterion, device="cpu"
    )

    x = torch.randn(16, 10)
    y = torch.randint(0, 2, (16,))
    dataset = TensorDataset(x, y)
    loader = DataLoader(dataset, batch_size=4)

    train_loss = trainer.train_epoch(loader)
    val_loss, val_acc = trainer.evaluate(loader)

    assert train_loss > 0.0
    assert val_loss > 0.0
    assert 0.0 <= val_acc <= 1.0
