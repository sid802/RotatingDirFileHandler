# RotatingFileHander

Internal RotatingFileHandler from Python's `logging` module.
This class does exactly the same but puts the rolled over logger files in a target directory.

Usage example (Full example in example.py file):

    logger = logging.getLogger('loggerExample')

    rotating_handler = RotatingFileHandler('loggerExample.log', './rotations', backupCount=100, maxBytes=1024 * 5)
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

