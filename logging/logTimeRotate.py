import time
import logging
import logging.handlers
log_file_name = 'TimedRotatingFileHandler.log'
logging_level = logging.DEBUG
try:
    # set TimedRotatingFileHandler for root
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    # use very short interval for this example, typical 'when' would be 'midnight' and no explicit interval
    handler = logging.handlers.TimedRotatingFileHandler(log_file_name, when="S", interval=30, backupCount=10)
    handler.setFormatter(formatter)
    logger = logging.getLogger() # or pass string to give it a name
    logger.addHandler(handler)
    logger.setLevel(logging_level)
    # generate lots of example messages
    for i in range(10000):
        time.sleep(0.1)
        logger.debug('i=%d' % i)
        logger.info('i=%d' % i)
        logger.warn('i=%d' % i)
        logger.error('i=%d' % i)
        logger.critical('i=%d' % i)
except KeyboardInterrupt:
    # handle Ctrl-C
    logging.warn("Cancelled by user")
except Exception as ex:
    # handle unexpected script errors
    logging.exception("Unhandled error\n{}".format(ex))
    raise
finally:
    # perform an orderly shutdown by flushing and closing all handlers; called at application exit and no further use of the logging system should be made after this call.
    logging.shutdown()
