from abc import ABC, abstractmethod
from cage_evaluator.models.pose_sample import PoseSample


class MetricComputer(ABC):
    """Calcul des métriques d'erreur entre deux poses."""

    @abstractmethod
    def position_error(self, ref: PoseSample, estimated: PoseSample) -> float:
        """Erreur euclidienne de position en mètres."""
        ...

    @abstractmethod
    def orientation_error(self, ref: PoseSample, estimated: PoseSample) -> float:
        """Erreur d'orientation en radians."""
        ...