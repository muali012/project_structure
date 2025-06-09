import logging
import os
from datetime import datetime

# Define the log file name using current timestamp in the format: Month_Day_Year_Hour_Minute_Second.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the path for the logs directory in the current working directory
logs_path=os.path.join(os.getcwd(),"logs", LOG_FILE)

# Create the logs directory if it doesn't exist
os.makedirs(logs_path,exist_ok=True)

# Create the full path for the log file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)