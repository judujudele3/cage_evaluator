from abc import ABC, abstractmethod
from typing import Optional
import rclpy.time
from cage_evaluator.models.pose_sample import PoseSample


class TemporalBuffer(ABC):
    """Stockage temporel des poses par source."""

    @abstractmethod
    def add(self, pose: PoseSample) -> None:
        """Ajoute une pose dans le buffer."""
        ...

    @abstractmethod
    def get_around(self, timestamp: rclpy.time.Time, tolerance: float) -> Optional[PoseSample]:
        """Retourne la pose la plus proche du timestamp dans la tolérance donnée."""
        ...

    @abstractmethod
    def clear_before(self, timestamp: rclpy.time.Time) -> None:
        """Supprime les poses antérieures au timestamp."""
        ...