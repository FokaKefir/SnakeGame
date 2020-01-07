import pygame
import constants as CONST
import Position

class Window():

    def __init__(self, width, rows):
        self.width = width
        self.rows = rows
        self.win = pygame.display.set_mode((width, width))
        self.clock = pygame.time.Clock()

    def delay(self, milliseconds):
        pygame.time.delay(milliseconds)

    def setClock(self, fps):
        self.clock.tick(fps)

    def drawGrid(self):
        size = self.width // self.rows

        x = 0
        y = 0
        for r in range(self.rows):
            x = x + size
            y = y + size

            pygame.draw.line(self.win, CONST.WHITE, (x, 0), (x, self.width))
            pygame.draw.line(self.win, CONST.WHITE, (0, y), (self.width, y))

    def redrawWindow(self):
        self.win.fill(CONST.BLACK)
        self.drawGrid()
        pygame.display.update()

    def drawCube(self, color, position):
        size = self.width // self.rows

        xBeg = position.getX() * size
        yBeg = position.getY() * size

        pygame.draw.rect(self.win, color, (xBeg + 1, yBeg + 1, size - 1, size - 1))
        pygame.display.update()

    def drawSnake(self, snake):
        for x in range(self.rows):
            for y in range(self.rows):
                pos = Position.Position(x, y)
                value = snake.getSnakeFromPosition(pos)
                if(value != 0):
                    self.drawCube(CONST.GRAY, pos)

    def getKey(self):
        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.KEYDOWN):
                return chr(event.key)
