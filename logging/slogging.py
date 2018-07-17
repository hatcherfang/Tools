import logging
import os
logPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "myapp.log")


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s %(filename)s %(name)s (line:%(lineno)d) %(levelname)s] %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=logPath,
    filemode='ab+'
)
