#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import logging.handlers
import os
logPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "myapp.log")

config = logging.basicConfig(
         level=logging.INFO,
         format='[%(asctime)s %(filename)s %(name)s (line:%(lineno)d) %(levelname)s] %(message)s',
         datefmt='%a, %d %b %Y %H:%M:%S',
         filename=logPath,
         filemode='ab+'
     )
handler = logging.handlers.TimedRotatingFileHandler(logPath, when='S',
                                                    interval=10,
                                                    backupCount=5,
                                                    encoding="utf8")
# handler.suffix = "%Y%m%d-%H:%M:%S.log"
handler.setFormatter(config)
logger = logging.getLogger("customLogger")
logger.addHandler(handler)
