from cage_evaluator.interfaces.metric_computer import MetricComputer
from cage_evaluator.models.pose_sample import PoseSample


class SimpleMetricComputer(MetricComputer):
    """Calculateur de métriques dummy - retourne zéro (étape 3 - pipeline idiote)."""

    def position_error(self, ref: PoseSample, estimated: PoseSample) -> float:
        return 0.0

    def orientation_error(self, ref: PoseSample, estimated: PoseSample) -> float:
        return 0.0
