#entity is anything but the return type of any function

from pathlib import Path
from dataclasses import dataclass
from src.constants import *

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_classes: int
    params_batch_size: int
    params_learning_rate: float
    params_include_top: bool
    params_weights: str

@dataclass(frozen=True)
class TrainingConfig:
    root_dir:Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_batch_size: int
    params_image_size: list
    params_is_augmentation: bool
    params_epochs: int
    


