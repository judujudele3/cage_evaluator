import rclpy
from rclpy.node import Node

from cage_evaluator.implementations.cage_adapter import CageAdapter
from cage_evaluator.implementations.robot_adapter import RobotAdapter
from cage_evaluator.implementations.synchronizer import SimpleSynchronizer
from cage_evaluator.implementations.frame_transformer import SimpleFrameTransformer
from cage_evaluator.implementations.metric_computer import SimpleMetricComputer
from cage_evaluator.implementations.logger import ConsoleLogger
from cage_evaluator.implementations.evaluation_engine import SimpleEvaluationEngine


class EvaluationNode(Node):
    """Node ROS2 principale d'évaluation."""

    def __init__(self) -> None:
        super().__init__('evaluation_node')
        self.get_logger().info('Evaluation node démarrée.')

        engine = SimpleEvaluationEngine(
            cage_adapter=CageAdapter(),
            robot_adapter=RobotAdapter(),
            synchronizer=SimpleSynchronizer(),
            transformer=SimpleFrameTransformer(),
            metric_computer=SimpleMetricComputer(),
            logger=ConsoleLogger(),
        )

        # Cycle d'évaluation toutes les 100ms
        self.create_timer(0.1, engine.run_once)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = EvaluationNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
