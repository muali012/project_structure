import os
from pathlib import Path

# Define the root name of the project
project_name = "MLproject"

# List of file paths to create as part of the project structure
list_of_files = [
    f"{project_name}/__init__.py",                               # Package initializer
    f"{project_name}/components/__init__.py",                    # Components module initializer
    f"{project_name}/components/data_ingestion.py",              # Script for data ingestion
    f"{project_name}/components/data_validation.py",             # Script for data validation
    f"{project_name}/components/data_transformation.py",         # Script for data transformation
    f"{project_name}/components/model_trainer.py"                # Script for model training
]


# Iterate over each file path in the list_of_files
for path in list_of_files:
    
    # Convert the string path to a Path object (for better path manipulation)
    filepath = Path(path)
    
    # Split the path into directory and file name
    filedir, filename = os.path.split(path)
    
    # If there is a directory path, create it (if it doesn't exist)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    # If the file doesn't exist OR its size is 0 (i.e., empty)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file at that path
        with open(filepath, "w") as f:
            pass  # 'pass' ensures file is created but nothing is written

