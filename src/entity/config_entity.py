from pathlib import Path
from src import logger
from dataclasses import dataclass
from src.constants import *

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


