from cage_evaluator.interfaces.logger import Logger
from cage_evaluator.models.pose_sample import PoseSample


class ConsoleLogger(Logger):
    """Logger dummy - affiche en console (étape 3 - pipeline idiote)."""

    def log_pose(self, pose: PoseSample) -> None:
        print(f"[POSE] source={pose.source} frame={pose.frame_id} "
              f"pos=({pose.x:.3f}, {pose.y:.3f}, {pose.z:.3f})")

    def log_metrics(self, metrics: dict) -> None:
        print(f"[METRICS] {metrics}")
