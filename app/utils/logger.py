import logging.config
import logging
from logging.config import fileConfig


def get_logger():
    #fileConfig('example.log')
    logger = logging.getLogger()
    #logger.debug('often makes a very good meal of %s', 'visiting tourists')
    return logger
