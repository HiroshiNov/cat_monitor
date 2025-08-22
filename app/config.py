from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Tuple


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')


    ENV: str = 'dev'
    CAMERA_BACKEND: str = 'opencv' # 'opencv' | 'gstreamer'
    CAMERA_DEVICE: str | int = '0'
    FRAME_WIDTH: int = 1280
    FRAME_HEIGHT: int = 720
    FPS: int = 30
    INFER_DEVICE: str = 'cpu'
    LITTER_POLY: list[list[int]] = [[120,200],[900,200],[900,650],[120,650]]
    DATA_DIR: str = '/app/data'
    MODELS_DIR: str = '/app/models'
    HOST: str = '0.0.0.0'
    PORT: int = 8000


settings = Settings()