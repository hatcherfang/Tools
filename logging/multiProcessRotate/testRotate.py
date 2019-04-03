import logging
import os
import time
from safeRotatingFileHandler import SafeRotatingFileHandler
logger = logging.getLogger("KeywordFinder2.0")
logger.setLevel(logging.INFO)

logpath = os.path.join(os.path.dirname(__file__),
                       'test.log')
# log_file_name, when="S", interval=30, backupCount=10
handler = SafeRotatingFileHandler(logpath,
                                  when="S",
                                  interval=3,
                                  backupCount=30)

handler.suffix = "%Y%m%d"
handler.setFormatter(
        logging.Formatter(
            '[%(asctime)s %(filename)s %(lineno)s %(levelname)s]: %(message)s'
            )
        )
logger.addHandler(handler)
while True:
    time.sleep(1)
    logger.info("fang")
