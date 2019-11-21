import os
import logging

from ..core.config import trainerConfig

LOG_DIR = trainerConfig.Trainer_LOG_DIR

def build_trainerapp_log():
    
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)

    logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
    logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
    logging_format += "%(message)s"

    logging.basicConfig(
        format=logging_format,
        level=logging.INFO
    )
    logger = logging.getLogger()
    handler = logging.FileHandler(os.path.join(LOG_DIR,"webserver.log.txt"))
    handler.setLevel(logging.INFO)

    logger.addHandler(handler)
    return logger