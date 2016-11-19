#-*- encoding: utf-8 -*-
__author__ = 'Sid'

import logging
from random import randint, randrange
from RotatingFileHandler import RotatingFileHandler

def example():
    logger = logging.getLogger('loggerExample')

    rotating_handler = RotatingFileHandler('example.log', './rotations', backupCount=100, maxBytes=1024 * 5)
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
    rotating_handler.setFormatter(formatter)
    rotating_handler.setLevel(logging.DEBUG)

    logger.addHandler(rotating_handler)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    for i in xrange(3000):
        word_length = randrange(4, 15)
        word = generate_word(word_length)
        logger.info("WORD: {0}".format(word))

def generate_word(word_length):
    """
    :param word_length: Length we want for the generated word
    """

    word = ""
    for i in xrange(word_length):
        word += chr(randint(65, 90))
    return word

if __name__ == '__main__':
    example()