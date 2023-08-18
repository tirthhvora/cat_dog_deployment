import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_directory = 'logs'
log_filepath = os.path.join(log_directory,'logs.log')
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(level=logging.INFO, format = logging_str,
                    handlers = [logging.FileHandler(log_filepath),
                    logging.StreamHandler(sys.stdout)])

logger = logging.getLogger("cat_dog_deployment")

