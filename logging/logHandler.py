import os
import logging
import logging.handlers


file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '{name}.log'.format(name="myapp"))
file_handler = logging.handlers.TimedRotatingFileHandler(filename=file_name,
                                                         when='S',
                                                         interval=1,
                                                         backupCount=3)
file_handler.suffix = '%Y%m%d_%H:%M:%S.log'
formatter = logging.Formatter('[%(asctime)s %(filename)s %(name)s (line:%(lineno)d) %(levelname)s] %(message)s')

file_handler.setFormatter(formatter)
logger = logging.getLogger("customLogger")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
