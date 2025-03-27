from src.datascienceproject.entity.config_entity import *
from src.datascienceproject.constants import *
from src.datascienceproject.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves the data ingestion configuration and ensures necessary directories are created.

        This method reads the data ingestion configuration from the main configuration object,
        creates the required directories, and initializes a DataIngestionConfig object with
        the relevant parameters.

        Returns:
            DataIngestionConfig: An object containing the configuration details for data ingestion,
            including root directory, source URL, local data file path, and unzip directory.

        Raises:
            Exception: If an error occurs while retrieving or processing the configuration.
        """
        try:
            config = self.config.data_ingestion
            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir,
            )
            return data_ingestion_config
        except Exception as e:
            raise e

    def get_data_validation_config(self) -> DataValidationConfig:

        """
        Retrieves the data validation configuration.
        This method extracts the data validation configuration from the main
        configuration object and schema, creates necessary directories, and
        returns a DataValidationConfig object.
        Returns:
            DataValidationConfig: An object containing the data validation
            configuration settings.
        Raises:
            Exception: If an error occurs during the retrieval or creation of the
            data validation configuration.
        """
        try:

            config = self.config.data_validation
            schema = self.schema.COLUMNS
            create_directories([config.root_dir])

            data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                unzip_data_dir=config.unzip_data_dir,
                all_schema=schema,
            )
            return data_validation_config
        except Exception as e:
            raise e

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Retrieves the data transformation configuration and ensures the necessary directories exist.

        This method accesses the `data_transformation` section of the configuration,
        creates the required directories, and initializes a `DataTransformationConfig` object
        with the specified root directory and data path.

        Returns:
            DataTransformationConfig: An object containing the configuration for data transformation.

        Raises:
            Exception: If an error occurs while retrieving or processing the configuration.
        """

        try:
            config = self.config.data_transformation
            create_directories([config.root_dir])
            data_transformation_config = DataTransformationConfig(
                root_dir=config.root_dir, data_path=config.data_path
            )
            return data_transformation_config
        except Exception as e:
            raise e

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Retrieves the configuration for the model trainer and initializes a ModelTrainerConfig object.

        This method extracts the necessary configuration details for training a model, including
        file paths, model parameters, and target column schema. It also ensures that the required
        directories for storing model-related files are created.

        Returns:
            ModelTrainerConfig: An object containing the configuration details for the model trainer.

        Raises:
            Exception: If any error occurs during the retrieval or initialization of the configuration.
        """
        try:
            config = self.config.model_trainer
            params = self.params.ElasticNet
            schema = self.schema.TARGET_COLUMN

            create_directories([config.root_dir])

            model_trainer_config = ModelTrainerConfig(
                root_dir=config.root_dir,
                train_data_path=config.train_data_path,
                test_data_path=config.test_data_path,
                model_name=config.model_name,
                alpha=params.alpha,
                l1_ratio=params.l1_ratio,
                target_column=schema.name,
            )
            return model_trainer_config
        except Exception as e:
            raise e
