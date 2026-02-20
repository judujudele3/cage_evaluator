from abc import ABC, abstractmethod
from cage_evaluator.models.pose_sample import PoseSample


class Synchronizer(ABC):
    """Alignement temporel entre deux sources de poses."""

    @abstractmethod
    def synchronize(
        self,
        pose_a: PoseSample,
        pose_b: PoseSample,
        tolerance: float
    ) -> bool:
        """Retourne True si les deux poses sont suffisamment proches dans le temps."""
        ...