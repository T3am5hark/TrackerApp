import logging
import os
import sys

DEFAULT_LOGGER_NAME = os.getenv('LOGGER_NAME', 'TrackerApp')

def init_logging(logger_name=DEFAULT_LOGGER_NAME,
                 log_level=logging.DEBUG,
                 stream=None):
    # logging
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # create console handler and set level to debug
    if stream is None:
        stream = sys.stderr
    ch = logging.StreamHandler(stream=stream)
    ch.setLevel(log_level)
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger
