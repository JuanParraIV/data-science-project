import os
import yaml
from src.datascienceproject.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Dict, List, Optional
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox object.
    Args:
        path_to_yaml (str): Path to the YAML file.

    Raises:
        ValueError: If the file does not exist or is not a YAML file.
        e: empty file exception.

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"YAML file {path_to_yaml} not found.")
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save Json Data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in the json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return its contents as a ConfigBox object.
    Args:
      path (Path): The path to the JSON file.
    Returns:
      ConfigBox: The contents of the JSON file wrapped in a ConfigBox object.
    Raises:
      FileNotFoundError: If the file at the given path does not exist.
      json.JSONDecodeError: If the file is not a valid JSON.
    Logs:
      Logs an info message indicating that the JSON file was loaded successfully.
    """
    try:

        with open(path) as f:
            content = json.load(f)
        logger.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"YAML file {path} not found.")
    except json.JSONDecodeError:
        raise ValueError("not a valid JSON")
    except Exception as e:
        raise e


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save data to a binary file using joblib.
    Args:
      data (Any): The data to be saved.
      path (Path): The file path where the data will be saved.
    Raises:
      Exception: If there is an error during the save process.
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"binary successfully saved at: {path}")
    except Exception as e:
        raise e


@ensure_annotations
def load_bin(path: Path):
    """
    Load a binary file from the specified path using joblib.
    Args:
        path (Path): The path to the binary file to be loaded.
    Returns:
        Any: The data loaded from the binary file.
    Raises:
        FileNotFoundError: If the binary file is not found at the specified path.
        Exception: If any other exception occurs during the loading process.
    """
    try:
        data = joblib.load(path)
        logger.info(f"binary successfully loaded from: {path}")
        return data
    except FileNotFoundError:
        logger.error(f"Binary file {path} not found.")
    except Exception as e:
        raise e
