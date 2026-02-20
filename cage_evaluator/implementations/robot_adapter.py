from typing import Optional

import rclpy.time

from cage_evaluator.interfaces.data_adapter import DataAdapter
from cage_evaluator.models.pose_sample import PoseSample


class RobotAdapter(DataAdapter):
    """Adapteur dummy pour les données robot (étape 3 - pipeline idiote)."""

    def get_latest_pose(self) -> Optional[PoseSample]:
        return PoseSample(
            x=0.1, y=0.1, z=0.1,
            qx=0.0, qy=0.0, qz=0.0, qw=1.0,
            timestamp=rclpy.time.Time(),
            frame_id='base_link',
            source='robot',
        )
