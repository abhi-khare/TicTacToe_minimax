import pygame , sys
from pygame.locals import *
import numpy as np

# parameters
Width,Height = 600,600
gameExit = False
white = (255,255,255)
black = (0,0,0)
purple = (75,0,130)
centers = [100,300,500]

gameGrid = np.array([[-1,-1,-1],
                     [-1,-1,-1],
                     [-1,-1,-1]])

# set up pygame
pygame.init()
# set up the window
gameDisplay = pygame.display.set_mode((Width,Height))
# setting the title
pygame.display.set_caption('Tic Tac Toe(minimax version)')

def drawBoard():
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,purple,[195,0,10,600])
    pygame.draw.rect(gameDisplay,purple,[395,0,10,600])
    pygame.draw.rect(gameDisplay,purple,[0,195,600,10])
    pygame.draw.rect(gameDisplay,purple,[0,395,600,10])

def drawZero(loc):
    y = centers[loc[0]]
    x = centers[loc[1]]
    pygame.draw.circle(gameDisplay,black,(x,y),50,5)

def drawCross(loc):
    y = centers[loc[0]]
    x = centers[loc[1]]
    pygame.draw.line(gameDisplay,black,(x+50,y+50),(x-50,y-50),5)
    pygame.draw.line(gameDisplay,black,(x+50,y-50),(x-50,y+50),5)

# game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    drawBoard()
    drawZero((1,2))
    drawCross((2,1))

    pygame.display.update()

pygame.quit()
quit()
