import pygame , sys,time
from pygame.locals import *
import numpy as np

# parameters
Width,Height = 600,600      # height and width of game display
gameExit = False
white = (255,255,255)
black = (0,0,0)
purple = (75,0,130)
centers = [100,300,500]
gameGrid = np.array([[-1,-1,-1],
                     [-1,-1,-1],
                     [-1,-1,-1]])
delay = 1
# set up pygame
pygame.mixer.pre_init(22050, -16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
# set up the window
gameDisplay = pygame.display.set_mode((Width,Height))
# setting the title
pygame.display.set_caption('Tic Tac Toe(minimax version)')
# setting up sound
userMoveSound = pygame.mixer.Sound('Speech_Off.wav')
aiMoveSound = pygame.mixer.Sound('Speech_On.wav')
gameEndSound = pygame.mixer.Sound('tada.wav')

# a function to draw zero on screen at location given in argument
def drawZero(loc):
    y = centers[loc[0]]
    x = centers[loc[1]]
    pygame.draw.circle(gameDisplay,black,(x,y),50,5)

# a function to draw cross on screen at location given in argument
def drawCross(loc):
    y = centers[loc[0]]
    x = centers[loc[1]]
    pygame.draw.line(gameDisplay,black,(x+50,y+50),(x-50,y-50),5)
    pygame.draw.line(gameDisplay,black,(x+50,y-50),(x-50,y+50),5)

# a function to draw the '#' shaped game board and call drawZero and drawCross function.
def drawBoard():
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,purple,[195,0,10,600])
    pygame.draw.rect(gameDisplay,purple,[395,0,10,600])
    pygame.draw.rect(gameDisplay,purple,[0,195,600,10])
    pygame.draw.rect(gameDisplay,purple,[0,395,600,10])

    for i in range(0,3):
        for j in range(0,3):
            if gameGrid[i][j] == 0:     # whenever '0' is encountered in a gameGrid , drawZero is called
                drawZero((i,j))
            elif gameGrid[i][j]==1:     # whenever '1' is encountered in a gameGrid , drawCross is called
                drawCross((i,j))
    pygame.display.update()             # changes are then updated, kindly refer to pygame to see how it works.

# a function to tell the status of game : Human win , AI win , Tie , none.
def status(gameGrid):

    for i in range(0,3):
        if gameGrid[i][0]==1 and gameGrid[i][1]==1 and gameGrid[i][2]==1:
            #print(1)
            return 'AI'
        if gameGrid[i][0]==0 and gameGrid[i][1]==0 and gameGrid[i][2]==0:
            #print(2)
            return 'HUMAN'
        if gameGrid[0][i]==1 and gameGrid[1][i]==1 and gameGrid[2][i]==1:
            #print(3)
            return 'AI'
        if gameGrid[0][i]==0 and gameGrid[1][i]==0 and gameGrid[2][i]==0:
            #print(4)
            return 'HUMAN'
    if gameGrid[0][0]==1 and gameGrid[1][1]==1 and gameGrid[2][2]==1:
        #print(5)
        return 'AI'
    if gameGrid[0][0]==0 and gameGrid[1][1]==0 and gameGrid[2][2]==0:
        #print(6)
        return 'HUMAN'
    if (gameGrid[0][2]==1 and gameGrid[1][1]==1 and gameGrid[2][0]==1):
        #print(7)
        return 'AI'
    if (gameGrid[0][2]==0 and gameGrid[1][1]==0 and gameGrid[2][0]==0):
        #print(8)
        return 'HUMAN'

    for i in range(0,3):
        for j in range(0,3):
            if gameGrid[i][j]==-1:
                return 'notend'

    return 'TIE'

# Core function that implements minimax algorithm to output best possible moves for AI.
def getBotMove(gameGrid,level):
    s = status(gameGrid)
    if s =='AI':
        return [10,-1,-1]
    elif s=='HUMAN':
        return [-10,-1,-1]
    elif s=='TIE':
        return [0,-1,-1]
    else:
        scoreList = []
        for i in range(0,3):
            for j in range(0,3):
                if gameGrid[i][j] == -1:
                    gameGrid[i][j] = level
                    score = getBotMove(gameGrid,1-level)
                    scoreList.append([score[0],i,j])
                    gameGrid[i][j] = -1
        Min,Max,x,y=100,-100,-1,-1
        for move in scoreList:
            if level == 0 and move[0]<Min:
                Min = move[0]
                x,y = move[1],move[2]
            elif level==1 and move[0]>Max:
                Max = move[0]
                x,y = move[1],move[2]
        if level==0:
            return [Min,x,y]
        else:
            return [Max,x,y]

# game loop
drawBoard()
while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            userMove = int(chr(event.key))
            userMoveSound.play(0)                            # play user move sound
            gameGrid[(userMove-1)//3][(userMove-1)%3]=0      # set user move location to zero.
            drawBoard()                                      # draw the board.
            time.sleep(delay)
            gameState = status(gameGrid)                     # get the status of board after human move.
            if gameState=='HUMAN' or gameState=='TIE':       # check if human win or there is a tie.
                print(gameGrid,gameState)
                gameEndSound.play()                          # if game ends, play game end sound.
                time.sleep(delay)
                gameExit = True                              # exit from the game.
                break
            aiMove = getBotMove(gameGrid,1)                  # get AI move.
            aiMoveSound.play(0)                              # play AI move sound
            gameGrid[aiMove[1]][aiMove[2]]=1                 # set the AI move location to one   
            drawBoard()                                      # draw the board.
            time.sleep(delay)
            gameState = status(gameGrid)                     # get the status of the board. 
            if gameState=='AI' or gameState=='TIE':          # check if the AI wins or there is a tie.
                print(gameGrid,gameState)
                gameEndSound.play()
                time.sleep(delay)
                gameExit = True
                break

pygame.quit()                                                # end the pygame session.
quit()
