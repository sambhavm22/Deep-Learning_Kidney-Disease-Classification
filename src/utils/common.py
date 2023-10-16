import os
from box.exceptions import BoxValueError
import yaml
from src import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(yaml_file:str) -> ConfigBox:
    try:
        with open(yaml_file, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {yaml_file} loaded successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(directories_path: list, verbose = True):
    for path in directories_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(json_file_path: Path, data: dict):
    with open('json_file_path', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    
    logger.info(f"json file is saved at: {json_file_path}")

@ensure_annotations
def load_json(json_file_path: Path) -> ConfigBox:
    with open(json_file_path) as path:
        content = json.load(path) 
    logger.info(f"json file loaded successfully from: {json_file_path       }")
    return ConfigBox(content)

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~the size file in {size_in_kb} KB"    


def decode_image(img_string, filename):
    img_data = base64.b64decode(img_string)
    with open(filename, 'wb') as f:
        f.write(img_data)
        f.close()

            