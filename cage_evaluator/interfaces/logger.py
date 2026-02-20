from abc import ABC, abstractmethod
from cage_evaluator.models.pose_sample import PoseSample


class Logger(ABC):
    """Enregistrement des données et métriques."""

    @abstractmethod
    def log_pose(self, pose: PoseSample) -> None:
        """Enregistre une pose brute."""
        ...

    @abstractmethod
    def log_metrics(self, metrics: dict) -> None:
        """Enregistre un dictionnaire de métriques."""
        ...