import constants as CONST
import numpy as np
import Position

class Snake(object):

    # region 1. Init Object
    def __init__(self, head, rows):
        self.head = Position.Position(head.getX(), head.getY())
        self.tail = Position.Position(head.getX(), head.getY())
        self.rows = rows
        self.action = CONST.STOP
        self.newAction = CONST.STOP
        self.tailAction = CONST.STOP
        self.winning = True

    # endregion

    # region 2. Generators
    def creatMatrix(self):
        self.matrix = [[0 for col in range(self.rows)] for row in range(self.rows)]

        self.matrix[self.head.getX()][self.head.getY()] = CONST.BODY

    def generateApple(self):
        self.apple = Position.Position(0, 0)
        self.apple.generateRandomPosition()
        while(self.matrix[self.apple.getX()][self.apple.getY()] != 0):
            self.apple.generateRandomPosition()

        self.matrix[self.apple.getX()][self.apple.getY()] = CONST.APPLE

    # endregion

    # region 3. Getting new values inside the Class
    def replacingToTheNewAction(self):
        if(self.newAction == CONST.UP and self.action != CONST.DOWN):
            self.matrix[self.head.getX()][self.head.getY()] = CONST.UP

        elif (self.newAction == CONST.DOWN and self.action != CONST.UP):
            self.matrix[self.head.getX()][self.head.getY()] = CONST.DOWN

        elif (self.newAction == CONST.RIGHT and self.action != CONST.LEFT):
            self.matrix[self.head.getX()][self.head.getY()] = CONST.RIGHT

        elif (self.newAction == CONST.LEFT and self.action != CONST.RIGHT):
            self.matrix[self.head.getX()][self.head.getY()] = CONST.LEFT

        self.action = self.newAction

    def gettingNewHead(self):
        self.newHead = Position.Position(self.head.getX(), self.head.getY())

        if (self.action == CONST.UP):
            self.newHead.setY(self.head.getY() - 1)
        elif (self.action == CONST.DOWN):
            self.newHead.setY(self.head.getY() + 1)
        elif (self.action == CONST.RIGHT):
            self.newHead.setX(self.head.getX() + 1)
        elif (self.action == CONST.LEFT):
            self.newHead.setX(self.head.getX() - 1)

    def gettingNewTail(self):
        self.newTail = Position.Position(self.tail.getX(), self.tail.getY())

        if (self.tailAction == CONST.UP):
            self.newTail.setY(self.tail.getY() - 1)
        elif (self.tailAction == CONST.DOWN):
            self.newTail.setY(self.tail.getY() + 1)
        elif (self.tailAction == CONST.RIGHT):
            self.newTail.setX(self.tail.getX() + 1)
        elif (self.tailAction == CONST.LEFT):
            self.newTail.setX(self.tail.getX() - 1)

    # endregion

    # region 4. Movements
    def move(self):
        eatingApple = False

        if(self.action != self.newAction or self.action == CONST.STOP):
            self.replacingToTheNewAction()

        self.gettingNewHead()

        if(self.newHead.getX()< 0 or self.newHead.getY() < 0 or self.newHead.getX() >= self.rows or self.newHead.getY() >= self.rows):
            self.winning = False

        newPositionValue = self.matrix[self.newHead.getX()][self.newHead.getY()]
        if(newPositionValue != 0 and newPositionValue != CONST.APPLE):
            self.winning = False

        if(self.winning == True):
            if(self.newHead.getX() == self.apple.getX() and self.newHead.getY() == self.apple.getY()):
                eatingApple = True
                self.generateApple()

            self.head = self.newHead
            self.matrix[self.head.getX()][self.head.getY()] = self.action

            if(eatingApple == False):
                self.moveTail()

    def moveTail(self):
        newTailAction = self.matrix[self.tail.getX()][self.tail.getY()]
        if(newTailAction != CONST.BODY):
            self.tailAction = newTailAction

        self.gettingNewTail()
        self.matrix[self.tail.getX()][self.tail.getY()] = 0
        self.tail = self.newTail

    # endregion

    # region 5. Getters and Setters
    def setNewAction(self, newAction):
        self.newAction = newAction
    def getAction(self):
        return self.action
    def getNewAction(self):
        return self.newAction
    def getSnakeFromPosition(self, position):
        return self.matrix[position.getX()][position.getY()]
    def getWinning(self):
        return self.winning
    def getHead(self):
        return self.head
    def getTail(self):
        return self.tail
    def getApple(self):
        return self.apple

    # endregion
