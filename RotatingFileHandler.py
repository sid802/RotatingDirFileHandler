#-*- encoding: utf-8 -*-
__author__ = 'Sid'

from logging import handlers
import os

class MyRotatingFileHandler(handlers.RotatingFileHandler):
    """
    Custom RotatingFileHandler which allows saving rolled over files
    to be saved in another directory
    """
    def __init__(self, filename, target_dir='.', *args, **kwargs):
        super(RotatingFileHandler, self).__init__(filename, *args, **kwargs)
        abs_path = os.path.abspath(target_dir)
        if not os.path.isdir(abs_path):
            raise Exception("You didn't enter a valid target directory!: <{0}>".format(target_dir))
        self.target_dir = abs_path
        self.filename = os.path.basename(filename)

    def doRollover(self):
        """
        Reset method for better name formatting
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = self.rotation_filename("%s/%s.%d" % (self.target_dir, self.filename, i))  # sfn = source file name
                dfn = self.rotation_filename("%s/%s.%d" % (self.target_dir, self.filename,  # dfn = destiny file name
                                                           i + 1))
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)
            dfn = self.rotation_filename(os.path.join(self.target_dir, self.filename + ".1"))
            if os.path.exists(dfn):
                os.remove(dfn)
            self.rotate(self.baseFilename, dfn)
        if not self.delay:
            self.stream = self._open()
