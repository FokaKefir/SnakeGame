from random import seed
from random import randint
import constants as CONST


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generateRandomPosition(self):

        randomX = randint(0, CONST.ROWS-1)
        randomY = randint(0, CONST.ROWS-1)
        self.x = randomX
        self.y = randomY

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y