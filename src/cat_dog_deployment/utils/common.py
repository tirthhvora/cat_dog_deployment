import os                                   # For making directories
from box.exceptions import BoxValueError    # For error messages
import yaml                                 # For reading from yaml
from cat_dog_deployment import logger       # For logging
import json                                 # For reading from json
import joblib
from ensure import ensure_annotations       # for specifying data types
from box import ConfigBox                   # For accessing keys using . operator
from pathlib import Path
from typing import Any
import base64


# Now we will create a function to read contents from a yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    """

    Need: I want to read the contents from a yaml file and i only have its path

    Outline:
    This function takes a yaml file path, opens it in 'r' mode, loads the content into a dictionary format
    and then returns a configbox type

    Output: We use configbox as the output because further when we use the import, 
    we will need to access the methods using . operator

    Input: Path to the yaml file (Path object)

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            # Content is of type dictionary

            logger.info(f"Content successfully loaded from the yaml_file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("File is empty")
    # This error is associated with ConfigBox

    except Exception as e:
        raise e
    

# Now we will create a function to create directories whenever needed

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):

    """
    This function is used to create directories
    input: List containing paths of directories to create
    output: directories at particular location created
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at path: {path}")\
            

# Now we will create a function to save data into a json file

@ensure_annotations
def save_json(path: Path, data: dict):

    """
    Need: I have some data in a dictionary and want to save it into a json file at a particular path
    outline: This function will take a path and the dictionary data,
    then it will open the path in write mode and dump the data into the path

    Input: Path("directory", 'new_file.json'), data = {'key':'value}

    """
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        # Indent for pretty printing
    
    logger.info(f"Json file created at path : {path}")


# Function to load data from json to a useable dictionary form

@ensure_annotations
def load_json(path: Path) -> ConfigBox:

    with open(path, 'r') as file:

        json_content = json.load(file)

    logger.info(f"Json file loaded at path : {path}")
    return ConfigBox(json_content)

# Function to save any object, model, file in binary form

def save_bin(data: Any, path: Path):

    joblib.dump(value = data, filename = path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:

    content = joblib.load(path)
    return content

def decode_image(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)

    with open(fileName, 'wb') as file:
        file.write(imgdata)
        file.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as file:
        return base64.b64encode(file.read())
    
