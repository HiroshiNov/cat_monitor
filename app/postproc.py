from typing import Optional
from .pipeline import InferenceResult


class EventLatch:
    """短時間のゆらぎで多重通知しないための簡易ラッチ。"""
    def __init__(self, cooldown_sec: int = 30):
        self.cooldown = cooldown_sec
        self._last_ts: int = 0


    def should_emit(self, now_ts: int) -> bool:
        if now_ts - self._last_ts >= self.cooldown:
            self._last_ts = now_ts
            return True
        return False


def decide_event(res: InferenceResult) -> Optional[str]:
    if not res.has_cat or not res.action:
        return None
    if res.confidence < 0.75:
        return None
    return res.action