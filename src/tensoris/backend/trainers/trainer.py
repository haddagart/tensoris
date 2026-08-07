"""Standard PyTorch Deep Learning Model Trainer."""

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


class ModelTrainer:
    """Standard Deep Learning Model Trainer managing forward passes, backpropagation, and evaluation.

    Execution Workflow Flowchart:

    ```mermaid
    graph TD
        A["DataLoader Batch (inputs, targets)"] --> B["Transfer Tensors to Device (CUDA / MPS / CPU)"]
        B --> C["Optimizer.zero_grad()"]
        C --> D["Model Forward Pass: outputs = model(inputs)"]
        D --> E["Loss Calculation: loss = criterion(outputs, targets)"]
        E --> F["Backpropagation: loss.backward()"]
        F --> G["Optimizer Step: optimizer.step()"]
        G --> H["Accumulate & Return Epoch Mean Loss"]
    ```
    """

    def __init__(
        self,
        model: nn.Module,
        optimizer: torch.optim.Optimizer,
        criterion: nn.Module,
        device: str | torch.device = "cpu",
    ) -> None:
        """Initialize Model Trainer.

        Args:
            model: PyTorch neural network model instance.
            optimizer: PyTorch optimizer instance.
            criterion: PyTorch loss function instance.
            device: Compute device ('cuda', 'mps', or 'cpu').
        """
        self.model = model.to(device)
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device

    def train_epoch(self, dataloader: DataLoader) -> float:
        """Execute a single training epoch optimization loop.

        Args:
            dataloader: PyTorch DataLoader supplying training batches.

        Returns:
            Mean training loss across all batches.
        """
        self.model.train()
        total_loss = 0.0

        for inputs, targets in dataloader:
            inputs, targets = inputs.to(self.device), targets.to(self.device)

            self.optimizer.zero_grad()
            outputs = self.model(inputs)
            loss = self.criterion(outputs, targets)
            loss.backward()
            self.optimizer.step()

            total_loss += loss.item()

        return total_loss / max(1, len(dataloader))

    def evaluate(self, dataloader: DataLoader) -> float:
        """Execute evaluation loop without gradient computation.

        Args:
            dataloader: PyTorch DataLoader supplying evaluation batches.

        Returns:
            Mean evaluation loss across all batches.
        """
        self.model.eval()
        total_loss = 0.0

        with torch.no_grad():
            for inputs, targets in dataloader:
                inputs, targets = inputs.to(self.device), targets.to(self.device)
                outputs = self.model(inputs)
                loss = self.criterion(outputs, targets)
                total_loss += loss.item()

        return total_loss / max(1, len(dataloader))
