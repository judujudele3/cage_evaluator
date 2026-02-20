from abc import ABC, abstractmethod
from typing import Optional
from cage_evaluator.models.pose_sample import PoseSample


class FrameTransformer(ABC):
    """Conversion de poses dans un repère commun."""

    @abstractmethod
    def transform(self, pose: PoseSample, target_frame: str) -> Optional[PoseSample]:
        """Transforme une pose dans le repère cible. Retourne None si impossible."""
        ...