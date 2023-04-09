from flask import Blueprint
from birajwebapp.config import Config
import logging

# Creating a blueprint named 'benfordapp'
logger = Blueprint('logger', __name__)

logging.basicConfig(filename=Config.LOG_FILENAME, level=Config.LOG_LEVEL)
def log_debug(message):
    logging.debug(message)
    return True


def log_info(message):
    logging.info(message)
    return True


def log_error(message):
    logging.error(message)
    return True