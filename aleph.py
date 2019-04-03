"""Module for testing recorder. Contains classes and functions to be
called and traced."""
import os


"""
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("aleph")
"""

class Logger():
    def __init__(self, name):
        self.name = name
    def debug(self, message):
        print(f'{self.name}: {message}')

logger = Logger('aleph')


class TheSimpleOne():
    """This is a simple class, without parents."""
    name = None

    def __init__(self, one):
        self.name = one
        logger.debug(f'{self} initilized')

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return self.name

def a():
    print('the a is called')
    return 1

def some_function(avar):
    logger.debug(f'Got var: {avar}')
    tos = TheSimpleOne(avar)
    logger.debug(tos)
    tos.name = avar + ' & ' + avar
    logger.debug(tos)
