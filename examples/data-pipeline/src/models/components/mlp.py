"""MLP architecture — pure PyTorch, no training logic.

Training logic lives in module.py (LightningModule).
This separation makes the architecture independently testable.
"""

from __future__ import annotations

import torch
import torch.nn as nn


class MLP(nn.Module):
    """Multi-layer perceptron for tabular classification.

    Builds a sequential network of [Linear → ReLU → Dropout] blocks
    followed by a final Linear output layer.

    Args:
        input_dim: Number of input features.
        hidden_dims: Width of each hidden layer.
        output_dim: Number of output classes.
        dropout: Dropout probability applied after each hidden activation.

    Example:
        >>> net = MLP(input_dim=10, hidden_dims=[64, 128, 64], output_dim=2)
        >>> logits = net(torch.randn(16, 10))  # shape: (16, 2)
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dims: list[int],
        output_dim: int,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        dims = [input_dim, *hidden_dims, output_dim]
        layers: list[nn.Module] = []
        for in_dim, out_dim in zip(dims[:-2], dims[1:-1]):
            layers.extend([nn.Linear(in_dim, out_dim), nn.ReLU(), nn.Dropout(dropout)])
        layers.append(nn.Linear(dims[-2], dims[-1]))

        self.network = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Run forward pass.

        Args:
            x: Input tensor of shape (batch_size, input_dim).

        Returns:
            Logits tensor of shape (batch_size, output_dim).
        """
        return self.network(x)
