import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = 'cat_dog'

list_of_directories = [
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_directories:
    filepath = Path(filepath)

    file_directory, filename = os.path.split(filepath)

    if file_directory != "":
        os.makedirs(file_directory, exist_ok=True)
        logging.info("Creating directory: {} for file {}".format(file_directory,filename))

    
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info("Creating empty file: {}".format(filepath))
    else:
        logging.info(f"{filename} already exists")

