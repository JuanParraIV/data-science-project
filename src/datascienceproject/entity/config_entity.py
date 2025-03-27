from dataclasses import dataclass
from pathlib import Path


"""
DataIngestionConfig is a configuration class for data ingestion process.

Attributes:
    root_dir (Path): The root directory for data ingestion.
    source_URL (str): The URL from which to download the data.
    local_data_file (Path): The local file path where the downloaded data will be stored.
    unzip_dir (Path): The directory where the data will be unzipped.
"""
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


"""
DataValidationConfig is a data class that holds configuration settings for data validation.

Attributes:
    root_dir (Path): The root directory where data validation operations will be performed.
    STATUS_FILE (str): The name of the status file used to track validation status.
    unzip_data_dir (Path): The directory where unzipped data will be stored.
    all_schema (dict): A dictionary containing schema definitions for data validation.
"""
@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


"""
DataTransformationConfig is a configuration entity class that holds the paths 
required for the data transformation process.

Attributes:
    root_dir (Path): The root directory where the data transformation artifacts 
        and outputs will be stored.
    data_path (Path): The path to the input data that will be used for 
        transformation.
"""
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


"""
ModelTrainerConfig is a data class that holds configuration parameters for training a machine learning model.

Attributes:
    root_dir (Path): The root directory where all training-related files and outputs are stored.
    train_data_path (Path): The file path to the training dataset.
    test_data_path (Path): The file path to the testing dataset.
    model_name (str): The name of the machine learning model to be trained.
    alpha (float): The regularization strength parameter for the model.
    l1_ratio (float): The ElasticNet mixing parameter, with 0 <= l1_ratio <= 1.
    target_column (str): The name of the target column in the dataset.
"""
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str
