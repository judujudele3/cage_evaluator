from typing import Optional

from cage_evaluator.interfaces.frame_transformer import FrameTransformer
from cage_evaluator.models.pose_sample import PoseSample


class SimpleFrameTransformer(FrameTransformer):
    """Transformateur de repère dummy - retourne la pose sans transformation (étape 3)."""

    def transform(self, pose: PoseSample, target_frame: str) -> Optional[PoseSample]:
        # Retourne la pose telle quelle, juste on met à jour le frame_id
        return PoseSample(
            x=pose.x, y=pose.y, z=pose.z,
            qx=pose.qx, qy=pose.qy, qz=pose.qz, qw=pose.qw,
            timestamp=pose.timestamp,
            frame_id=target_frame,
            source=pose.source,
        )
