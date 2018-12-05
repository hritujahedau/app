from logger import get_logger


logger = get_logger()
logger.info("This is done")





"""

# logging.config.fileConfig('example.log')


# create logger
logger = logging.getLogger('main')
#logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s %(name)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.info("This is info")



logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s %(name)s',
                    datefmt='%a, %d %b %y %H:%M:%S',
                    filename='example.log',
                    level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('pack my box with %d dozen %s', 5, 'liquor jugs')
"""