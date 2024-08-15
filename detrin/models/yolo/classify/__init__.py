# Detrin YOLO 🚀, AGPL-3.0 license

from detrin.models.yolo.classify.predict import ClassificationPredictor
from detrin.models.yolo.classify.train import ClassificationTrainer
from detrin.models.yolo.classify.val import ClassificationValidator

__all__ = "ClassificationPredictor", "ClassificationTrainer", "ClassificationValidator"
