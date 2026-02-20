from typing import Optional

import rclpy.time

from cage_evaluator.interfaces.temporal_buffer import TemporalBuffer
from cage_evaluator.models.pose_sample import PoseSample


class SimpleTemporalBuffer(TemporalBuffer):
    """Buffer temporel dummy (étape 3 - pipeline idiote)."""

    def __init__(self) -> None:
        self._poses: list[PoseSample] = []

    def add(self, pose: PoseSample) -> None:
        self._poses.append(pose)

    def get_around(self, timestamp: rclpy.time.Time, tolerance: float) -> Optional[PoseSample]:
        if self._poses:
            return self._poses[-1]
        return None

    def clear_before(self, timestamp: rclpy.time.Time) -> None:
        self._poses.clear()
