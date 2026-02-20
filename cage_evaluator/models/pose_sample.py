from dataclasses import dataclass
import rclpy.time


@dataclass
class PoseSample:
    """Format interne commun pour toutes les poses."""
    x: float
    y: float
    z: float
    qx: float
    qy: float
    qz: float
    qw: float
    timestamp: rclpy.time.Time
    frame_id: str
    source: str