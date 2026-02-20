from cage_evaluator.interfaces.synchronizer import Synchronizer
from cage_evaluator.models.pose_sample import PoseSample


class SimpleSynchronizer(Synchronizer):
    """Synchroniseur dummy - accepte toujours (étape 3 - pipeline idiote)."""

    def synchronize(
        self,
        pose_a: PoseSample,
        pose_b: PoseSample,
        tolerance: float,
    ) -> bool:
        return True
