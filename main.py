
import sys 
from src.exception.exception import ProjectException
from src.logging import logger

# Import the DataIngestion class from the data ingestion component
from src.components.dataingestion import DataIngestion

# Import the DataIngestionArtifact dataclass
from src.components.dataingestion import DataIngestionArtifact

# Import the DataIngestionConfig dataclass
from src.components.dataingestion import DataIngestionConfig


# Entry point of the script
if __name__ == "__main__":
    # Instantiate the DataIngestion class
    data_ingestion = DataIngestion()

    # Start the data ingestion process and retrieve train and test data paths
    train_data, test_data = data_ingestion.initiate_data_ingestion()
