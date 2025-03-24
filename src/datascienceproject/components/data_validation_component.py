import pandas as pd
from src.datascienceproject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates that all columns in the dataset match the expected schema.

        Reads the dataset from the configured directory and checks if each column
        in the dataset exists in the expected schema. Writes the validation status
        to a status file.

        Returns:
          bool: True if all columns are valid, False otherwise.

        Raises:
          Exception: If there is an error during the validation process.
        """
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
