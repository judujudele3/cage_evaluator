from abc import ABC, abstractmethod
from typing import Optional
from cage_evaluator.models.pose_sample import PoseSample


class DataAdapter(ABC):
    """Interface de base pour tous les adapteurs de données."""

    @abstractmethod
    def get_latest_pose(self) -> Optional[PoseSample]:
        """Retourne la dernière pose reçue ou None."""
        ...