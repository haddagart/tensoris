"""Computer Vision Evaluation Metrics."""

import torch


class MeanIoU:
    """Mean Intersection over Union (mIoU) metric for semantic segmentation.

    Formula:
        $$\\text{mIoU} = \\frac{1}{C} \\sum_{c=1}^C \\frac{|A_c \\cap B_c|}{|A_c \\cup B_c|} = \\frac{1}{C} \\sum_{c=1}^C \\frac{TP_c}{TP_c + FP_c + FN_c}$$

        where $TP_c$, $FP_c$, and $FN_c$ represent True Positives, False Positives, and False Negatives for class $c$.

    References:
        Long, J., Shelhamer, E., & Darrell, T. (2015).
        Fully Convolutional Networks for Semantic Segmentation.
        Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2015), pp. 3431-3440.
        DOI: https://doi.org/10.1109/CVPR.2015.7298965 | arXiv: https://arxiv.org/abs/1411.4038
    """

    def __init__(self, num_classes: int) -> None:
        """Initialize mIoU metric accumulator.

        Args:
            num_classes: Total number of semantic categories.
        """
        self.num_classes = num_classes
        self.reset()

    def reset(self) -> None:
        """Reset confusion matrix counts."""
        self.confusion_matrix = torch.zeros((self.num_classes, self.num_classes), dtype=torch.int64)

    def update(self, predictions: torch.Tensor, targets: torch.Tensor) -> None:
        """Accumulate confusion matrix for predictions vs targets.

        Args:
            predictions: Class predictions tensor of shape (N, H, W) or (N, C, H, W).
            targets: Ground truth class target tensor of shape (N, H, W).
        """
        if predictions.ndim == 4:
            predictions = torch.argmax(predictions, dim=1)

        mask = (targets >= 0) & (targets < self.num_classes)
        preds = predictions[mask]
        targs = targets[mask]

        indices = self.num_classes * targs.to(torch.int64) + preds.to(torch.int64)
        counts = torch.bincount(indices, minlength=self.num_classes**2)
        self.confusion_matrix += counts.reshape(self.num_classes, self.num_classes)

    def compute(self) -> torch.Tensor:
        """Compute final mean IoU across all classes.

        Returns:
            Scalar mIoU score tensor between 0.0 and 1.0.
        """
        intersection = torch.diag(self.confusion_matrix).float()
        total_pred = torch.sum(self.confusion_matrix, dim=0).float()
        total_target = torch.sum(self.confusion_matrix, dim=1).float()
        union = total_pred + total_target - intersection

        iou = torch.where(union > 0, intersection / union, torch.tensor(float("nan")))
        return torch.nanmean(iou)


class TopKAccuracy:
    """Top-K Classification Accuracy Metric.

    Formula:
        $$\\text{Top-K Acc} = \\frac{1}{N} \\sum_{i=1}^N \\mathbb{1}\\left( y_i \\in \\text{top}_k(\\hat{y}_i) \\right)$$

        where $\\text{top}_k(\\hat{y}_i)$ denotes the $k$ highest logit prediction indices for sample $i$.

    References:
        Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012).
        ImageNet Classification with Deep Convolutional Neural Networks.
        Advances in Neural Information Processing Systems (NIPS 2012), pp. 1097-1105.
    """

    def __init__(self, k: int = 5) -> None:
        """Initialize Top-K accuracy.

        Args:
            k: Top k predicted logit indices to match ground truth.
        """
        self.k = k

    def __call__(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """Compute percentage of targets matched within top-K predicted logits.

        Args:
            logits: Predicted class probability or logit tensor of shape (N, C).
            targets: Ground truth target indices tensor of shape (N).

        Returns:
            Scalar top-k accuracy score tensor between 0.0 and 1.0.
        """
        with torch.no_grad():
            topk_preds = torch.topk(logits, k=self.k, dim=-1).indices
            expanded_targets = targets.unsqueeze(-1).expand_as(topk_preds)
            correct = torch.eq(topk_preds, expanded_targets).any(dim=-1).float()
            return correct.mean()
