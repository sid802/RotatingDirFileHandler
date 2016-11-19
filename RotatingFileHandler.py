#-*- encoding: utf-8 -*-
__author__ = 'Sid'

from logging import handlers
import os

class RotatingFileHandler(handlers.RotatingFileHandler):
    """
    Custom RotatingFileHandler which allows saving rolled over files
    to be saved in another directory
    """
    def __init__(self, filename, target_dir='.', *args, **kwargs):
        super(RotatingFileHandler, self).__init__(filename, *args, **kwargs)
        abs_path = os.path.abspath(target_dir)
        if not os.path.isdir(abs_path):
            dir_created = self._try_create_dir(abs_path)
            if not dir_created:
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
                sfn = "%s/%s.%d" % (self.target_dir, self.filename, i)
                dfn = "%s/%s.%d" % (self.target_dir, self.filename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)
                dfn = os.path.join(self.target_dir, self.filename + ".1")
             if os.path.exists(dfn):
                 os.remove(dfn)
             os.rename(os.path.join(self.target_dir, self.baseFilename), dfn)
        if not self.delay:
            self.stream = self._open()

    def _try_create_dir(self, target_dir):
        """
        :param target_dir: Absolute path to wanted dir
        Prompts the user if he want to create this dir
        :return: boolean - directory has been created or not
        """
        user_input = raw_input("The directory `{0}` doesn't exist, do you want it to be created? Y/N: ".format(target_dir))
        while user_input.lower() not in ['y', 'n']:
            user_input = raw_input("The directory `{0}` doesn't exist, do you want it to be created? Y/N: ".format(target_dir))

        if user_input == 'y':
            os.makedirs(target_dir)
            return True
        return False