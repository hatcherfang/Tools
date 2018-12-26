#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from logHandler import logger
while True:
    logger.info('test')
    logger.info(u'中文测试')
    time.sleep(2)
