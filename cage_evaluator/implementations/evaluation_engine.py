from cage_evaluator.interfaces.evaluation_engine import EvaluationEngine
from cage_evaluator.interfaces.data_adapter import DataAdapter
from cage_evaluator.interfaces.synchronizer import Synchronizer
from cage_evaluator.interfaces.frame_transformer import FrameTransformer
from cage_evaluator.interfaces.metric_computer import MetricComputer
from cage_evaluator.interfaces.logger import Logger

TARGET_FRAME = 'map'
SYNC_TOLERANCE = 0.05  # secondes


class SimpleEvaluationEngine(EvaluationEngine):
    """Moteur d'évaluation dummy (étape 3 - pipeline idiote)."""

    def __init__(
        self,
        cage_adapter: DataAdapter,
        robot_adapter: DataAdapter,
        synchronizer: Synchronizer,
        transformer: FrameTransformer,
        metric_computer: MetricComputer,
        logger: Logger,
    ) -> None:
        self._cage_adapter = cage_adapter
        self._robot_adapter = robot_adapter
        self._synchronizer = synchronizer
        self._transformer = transformer
        self._metric_computer = metric_computer
        self._logger = logger

    def run_once(self) -> None:
        cage_pose = self._cage_adapter.get_latest_pose()
        robot_pose = self._robot_adapter.get_latest_pose()

        if cage_pose is None or robot_pose is None:
            print("[ENGINE] Données manquantes, cycle ignoré.")
            return

        if not self._synchronizer.synchronize(cage_pose, robot_pose, SYNC_TOLERANCE):
            print("[ENGINE] Poses non synchronisées, cycle ignoré.")
            return

        cage_transformed = self._transformer.transform(cage_pose, TARGET_FRAME)
        robot_transformed = self._transformer.transform(robot_pose, TARGET_FRAME)

        self._logger.log_pose(cage_transformed)
        self._logger.log_pose(robot_transformed)

        metrics = {
            'position_error': self._metric_computer.position_error(cage_transformed, robot_transformed),
            'orientation_error': self._metric_computer.orientation_error(cage_transformed, robot_transformed),
        }

        self._logger.log_metrics(metrics)
