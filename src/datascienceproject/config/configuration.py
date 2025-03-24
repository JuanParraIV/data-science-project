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
        Retrieves the data ingestion configuration from the main configuration file.

        This method reads the data ingestion related settings from the configuration,
        creates necessary directories, and returns a DataIngestionConfig object 
        containing the configuration details.

        Returns:
            DataIngestionConfig: An object containing the data ingestion configuration 
            details such as root directory, source URL, local data file path, and 
            unzip directory.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Retrieves the data validation configuration.
        This method extracts the data validation configuration from the main
        configuration object and schema, creates necessary directories, and
        returns a DataValidationConfig object.
        Returns:
            DataValidationConfig: An object containing the data validation
            configuration settings.
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
    
        data_validation_config = DataValidationConfig(
          root_dir= config.root_dir,
          STATUS_FILE=config.STATUS_FILE,
          unzip_data_dir=config.unzip_data_dir,
          all_schema=schema,
        )
        return data_validation_config