import sys  # Needed for capturing exception details like line number and file name
from src.logging import logger

print(logger.logging.info)
# Custom exception class to handle project-specific errors
class ProjectException(Exception):
    
    # Constructor (should be __init__, not _init_)
    def __init__(self, error_message, error_details: sys):
        # Store the error message
        self.error_message = error_message
        
        # Get the traceback object from the exception details

        _,_, exc_tb = error_details.exc_info()
        
        # Extract line number where the exception occurred
        self.lineno = exc_tb.tb_lineno
        
        # Extract filename where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    # String representation of the exception for printing/logging
    def __str__(self):
        return (
            f"Error occurred in Python script name [{self.file_name}] "
            f"line number [{self.lineno}] error message: {self.error_message}"
        )

