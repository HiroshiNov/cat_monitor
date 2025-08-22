"""パイプラインのダミー実装。後で YOLO / reID / Keypoint / TCN に置き換え。
"""
from dataclasses import dataclass
from typing import Any, Dict
import time


@dataclass
class InferenceResult:
    has_cat: bool
    cat_id: str | None
    action: str | None # 'urination' | 'defecation' | None
    confidence: float


class CatPipeline:
    def __init__(self, models_dir: str, infer_device: str = 'cpu'):
        self.models_dir = models_dir
        self.device = infer_device
        # TODO: load onnx models here


    def infer_frame(self, frame) -> InferenceResult:
        # TODO: real inference
        # ダミー：1秒ごとに何か起きたことにする
        ts = int(time.time())
        if ts % 7 == 0:
            return InferenceResult(True, 'Bell', 'urination', 0.86)
        if ts % 11 == 0:
            return InferenceResult(True, 'Bell', 'defecation', 0.91)
        return InferenceResult(False, None, None, 0.0)