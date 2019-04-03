# coding: utf-8
# processlock.py
# process lock - Inter process exclusive lock

import logging
import traceback
try:
    import fcntl
    LOCK_EX = fcntl.LOCK_EX
    LOCK_NB = fcntl.LOCK_NB
except ImportError:
    # There is no fcntl module under the Windows platform
    fcntl = None


class Lock:
    """process lock
    """

    def __init__(self, filename='/tmp/processlock.txt'):
        self.filename = filename
        self.handle = None
        # If the file does not exist, create it
        try:
            self.handle = open(filename, 'w')
        except IOError, e:
            # e.errno == 2 means 'No such file or directory', we don't need
            # write it down or we will raise the exception
            if e.errno != 2:
                raise Exception(e.args)
            else:
                logging.debug("open lock file error error args:%r", e.args)
        except:
            logging.warn('open file:%r error!:%r',
                         self.filename,
                         traceback.format_exc())

    def acquire(self):
        # lock file
        try:
            if fcntl:
                fcntl.flock(self.handle.fileno(), LOCK_EX | LOCK_NB)
            return True
        except AttributeError, e:
            logging.debug("acquire() function AttributeError exception:%r",
                          e.args)
        except IOError, e:
            # e.errno == 11 means "Resource temporarily unavailable" and the
            # file is locked we need or we will raise exception
            if e.errno != 11:
                raise Exception(e.args)
            else:
                logging.debug("acquire IOError e.args:%r", e.args)
        except:
            logging.warn("lock file:%r failed :( :%r", self.filename,
                         traceback.format_exc())
            return False

    def release(self):
        # unlock file
        try:
            if fcntl:
                fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
            return True
        except AttributeError, e:
            logging.debug("release() function AttributeError exception:%r",
                          e.args)
        except:
            logging.warn("unlock file:%r failed :( :%r", self.filename,
                         traceback.format_exc())
            return False

    def __del__(self):
        try:
            self.handle.close()
        except AttributeError, e:
            # we need add the logging package or exception will happend
            import logging
            logging.debug("__del__() function AttributeError exception:%r",
                          e.args)
        except:
            logging.debug("__del__() exception: %r", traceback.format_exc())

if __name__ == '__main__':
    # test: In proper sequence to run multiple instances of the program,
    # the first instance of the N run time is the first N times
    import time
    print 'Time: %s' % time.time()

    try:
        lock = Lock()
        try:
            if lock.acquire():
                time.sleep(200)
        finally:
            lock.release()
    except:
        print traceback.format_exc()

    print 'Time: %s' % time.time()
