from abc import ABC, abstractmethod


class EvaluationEngine(ABC):
    """Orchestre le pipeline complet d'évaluation."""

    @abstractmethod
    def run_once(self) -> None:
        """Exécute un cycle d'évaluation : sync → transform → métriques."""
        ...