# Detrin YOLO 🚀, AGPL-3.0 license

__version__ = "8.2.75"

import os

# Set ENV Variables (place before imports)
os.environ["OMP_NUM_THREADS"] = "1"  # reduce CPU utilization during training

from detrin.data.explorer.explorer import Explorer
from detrin.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld
from detrin.utils import ASSETS, SETTINGS
from detrin.utils.checks import check_yolo as checks
from detrin.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
    "Explorer",
)
