import os
from src.datascienceproject.logging import logger
from src.datascienceproject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only train_test_splitting cz this data is already cleaned up

    def train_test_splitting(self):
        """
        Splits the dataset into training and test sets and saves them as CSV files.

        This method reads the dataset from the file path specified in the configuration,
        splits it into training and test sets using a default 75-25 split, and saves the
        resulting datasets as "train.csv" and "test.csv" in the root directory specified
        in the configuration.

        Logs the shapes of the training and test datasets for verification.

        Raises:
          Exception: If any error occurs during the data splitting or file operations.

        Returns:
          None
        """
        try:
            data = pd.read_csv(self.config.data_path)
            # Split the data into training and test sets. (0.75, 0.25) split.
            train, test = train_test_split(data)

            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info("Splitted data into training and test sets")
            logger.info(train.shape)
            logger.info(test.shape)

            print(train.shape)
            print(test.shape)
        except Exception as e:
            raise e
