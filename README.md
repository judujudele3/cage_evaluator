# cage_evaluator

Package ROS2 d'évaluation des performances d'un bras robotisé dans un environnement de capture optique OptiTrack.

## Contexte

Dans le cadre du développement d'un bras robotisé autonome destiné à évoluer en environnement domestique, une plateforme expérimentale basée sur un système de motion capture optique (OptiTrack) est utilisée pour :

- mesurer avec précision la position réelle du robot et des objets manipulés,
- comparer ces mesures avec les estimations issues du contrôleur du robot et des algorithmes de vision par caméra.

Ce package constitue le cœur logiciel de l'**équipe cage**, chargée de l'évaluation quantitative des performances du robot.

---

## Fonctionnalités

- **Monitoring temps réel** : comparaison des poses cage / robot / vision dans un repère commun
- **Analyse offline** : rejeu de bags ROS2 et recalcul des métriques
- **Métriques** : erreur de position, erreur d'orientation, erreur RMS, erreur maximale, répétabilité
- **Extensible** : ajout facile de nouvelles sources de données ou de nouvelles métriques

---

## Architecture

```
cage_evaluator/
├── models/
│   └── pose_sample.py          # Format interne commun (PoseSample)
├── interfaces/
│   ├── data_adapter.py         # Interface adapteur de données
│   ├── temporal_buffer.py      # Interface buffer temporel
│   ├── synchronizer.py         # Interface synchronisation temporelle
│   ├── frame_transformer.py    # Interface transformation de repère
│   ├── metric_computer.py      # Interface calcul des métriques
│   ├── evaluation_engine.py    # Interface moteur d'évaluation
│   └── logger.py               # Interface logging
├── implementations/
│   ├── cage_adapter.py         # Adapteur OptiTrack (mocap_optitrack)
│   ├── robot_adapter.py        # Adapteur robot (PoseStamped)
│   ├── temporal_buffer.py      # Buffer glissant thread-safe
│   ├── synchronizer.py         # Synchronisation par tolérance temporelle
│   ├── frame_transformer.py    # Transformation via tf2
│   ├── metric_computer.py      # Calcul des erreurs position / orientation
│   ├── evaluation_engine.py    # Orchestration du pipeline
│   └── logger.py               # Logger console / fichier
└── evaluation_node.py          # Node ROS2 principale
```

---

## Prérequis

- Ubuntu 22.04
- ROS2 Humble
- Image Docker `ros_optitrack` (inclut le driver `mocap_optitrack`)
- VSCode + extension Dev Containers

---

## Installation

```bash
# Cloner le dépôt dans le workspace ROS2
cd ~/ros2_ws/src
git clone https://github.com/judujudele3/cage_evaluator.git

# Builder le package
cd ~/ros2_ws
colcon build --packages-select cage_evaluator
source install/setup.bash
```

---

## Utilisation

### Lancer la node d'évaluation temps réel

```bash
ros2 run cage_evaluator evaluation_node
```

### Analyse offline (rejeu de bag)

```bash
# Dans un terminal : rejouer le bag
ros2 bag play <chemin_du_bag>

# Dans un autre terminal : lancer la node
ros2 run cage_evaluator evaluation_node
```

---

## Données requises des équipes

### Équipe robot
| Donnée | Description |
|--------|-------------|
| Pose TCP | `geometry_msgs/PoseStamped` dans le repère base du robot |
| Timestamp | Horodatage ROS2 |
| Repère | Nom du frame d'expression |
| Convention orientation | Quaternion (x, y, z, w) |

### Équipe vision *(à venir)*
| Donnée | Description |
|--------|-------------|
| Pose objet détecté | `geometry_msgs/PoseStamped` |
| Timestamp | Horodatage ROS2 |
| Repère | Nom du frame d'expression |

---

## Avancement

| Étape | Description | Statut |
|-------|-------------|--------|
| 1 | Workspace ROS2 & squelette du package | ✅ |
| 2 | Interfaces & classes abstraites | ✅ |
| 3 | Implémentations idiotes & pipeline complet | ✅ |
| 4 | Adapters réels (OptiTrack & robot) | 🔄 |
| 5 | TemporalBuffer & Synchronizer réels | ⏳ |
| 6 | FrameTransformer & calibrage statique (tf2) | ⏳ |
| 7 | MetricComputer & EvaluationEngine réels | ⏳ |
| 8 | Logger & module offline | ⏳ |
| 9 | Tests, configuration YAML & documentation | ⏳ |

---

## Licence

MIT