import pygame

import Position
import constants as CONST
import Window
import Snake


def main():

    randomPos = Position.Position(0, 0)
    randomPos.generateRandomPosition()
    tempPos = Position.Position(0, 0)

    window = Window.Window(CONST.WIDTH, CONST.ROWS)
    snake = Snake.Snake(tempPos, CONST.ROWS)
    snake.creatMatrix()
    snake.generateApple()

    gameIsOn = True

    while(gameIsOn):


        pressedKey = window.getKey()
        if(pressedKey == chr(pygame.K_ESCAPE) or snake.getWinning() == False):
            gameIsOn = False

        if(pressedKey == 'a'):
            snake.setNewAction(CONST.LEFT)
        elif(pressedKey == 's'):
            snake.setNewAction(CONST.DOWN)
        elif(pressedKey == 'd'):
            snake.setNewAction(CONST.RIGHT)
        elif(pressedKey == 'w'):
            snake.setNewAction(CONST.UP)

        if (snake.getNewAction() != CONST.STOP):
            snake.move()

        window.setClock(CONST.FPS)
        window.redrawWindow()

        window.drawSnake(snake)
        print(snake.getHead().getX(), snake.getHead().getY())
        print(snake.getTail().getX(), snake.getTail().getY(), end="\n\n")


        window.delay(CONST.DELAY)



main()