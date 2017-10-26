import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s %(filename)s %(name)s (line:%(lineno)d) %(levelname)s] %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='myapp.log',
    filemode='ab+'
)
