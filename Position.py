from random import seed
from random import randint
import constants as CONST


class Position(object):

    # region 1. Init Object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # endregion

    # region 2. Random generator
    def generateRandomPosition(self):

        randomX = randint(0, CONST.ROWS-1)
        randomY = randint(0, CONST.ROWS-1)
        self.x = randomX
        self.y = randomY
        return Position(randomX, randomY)

    # endregion

    # region 3. Getters and Setters
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

    # endregion