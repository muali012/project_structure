import os
import sys
from src.exception.exception import ProjectException
from src.logging import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    # Path to the raw data CSV file
    raw_data_path: str = os.path.join("raw_file", "data.csv")


@dataclass
class DataIngestionArtifact:
    # Path to the raw data CSV file
    raw_data_path: str = os.path.join("raw_file", "data.csv")
    # Path where the training data CSV will be saved
    train_data_path: str = os.path.join("artifacts", "train.csv")
    # Path where the testing data CSV will be saved
    test_data_path: str = os.path.join("artifacts", "test.csv")
    # Path where the validation data CSV will be saved
    valid_data_path: str = os.path.join("artifacts", "valid.csv")


class DataIngestion:
    def __init__(self):
        """
        Initialize DataIngestion with necessary configuration and artifact instances.
        """
        self.ingestion_config = DataIngestionConfig()
        self.artifact_config = DataIngestionArtifact()

    def initiate_data_ingestion(self):
        """
        Starts the data ingestion process by reading the dataset.
        Logs progress and handles exceptions.
        """
        logger.logging.info("Data Ingestion started")  # Log the start of the ingestion process

        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv("notebooks/data.csv")

            # Log dataset successfully read
            logger.logging.info("Dataset read")

            # Create necessary directories
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.artifact_config.train_data_path), exist_ok=True)

            # Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            # Split the dataset into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the split datasets
            train_set.to_csv(self.artifact_config.train_data_path)
            train_set.to_csv(self.artifact_config.test_data_path)

            # Return the paths to the training and testing datasets
            return (
                self.artifact_config.train_data_path,
                self.artifact_config.test_data_path
            )

        except Exception as e:
            # Raise custom project exception with context
            raise ProjectException(e, sys)
