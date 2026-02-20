from typing import Optional

import rclpy.time

from cage_evaluator.interfaces.data_adapter import DataAdapter
from cage_evaluator.models.pose_sample import PoseSample


class CageAdapter(DataAdapter):
    """Adapteur dummy pour les données OptiTrack (étape 3 - pipeline idiote)."""

    def get_latest_pose(self) -> Optional[PoseSample]:
        return PoseSample(
            x=0.0, y=0.0, z=0.0,
            qx=0.0, qy=0.0, qz=0.0, qw=1.0,
            timestamp=rclpy.time.Time(),
            frame_id='map',
            source='cage',
        )
