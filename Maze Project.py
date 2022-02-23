import pygame as pg

from sys import path
from sys import exit
import os

#my_path = os.path.dirname(os.path.realpath(__file__))
#os.chdir(my_path)
#path.append(my_path)

#Setup

pg.init()
screen = pg.display.set_mode((800,600)) #set your window size, (x,y)
pg.display.set_caption("Maze")
clock = pg.time.Clock()

def printToScreen(x,y,text,colour, size):
    timesnewroman = pg.font.SysFont('timesnewroman', size) #fontType, size
    text = str(text)
    label = timesnewroman.render(text, False, colour)
    screen.blit(label,(x,y))


black = (0,0,0)
white = (225,225,225)
Blue = (0,0,225)

shape = pg.Rect(100,150,40,40)
speed = 1

Maze = []

#Horzontal Walls
Maze.append(pg.Rect(100,500,690,10))
Maze.append(pg.Rect(100,50,600,10))
Maze.append(pg.Rect(180,130,400,10))
Maze.append(pg.Rect(180,210,100,10))
Maze.append(pg.Rect(290,300,180,10))
Maze.append(pg.Rect(470,400,160,10))
Maze.append(pg.Rect(580,330,120,10))
Maze.append(pg.Rect(175,400,150,10))


#Verical Walls
Maze.append(pg.Rect(100,60,10,80))
Maze.append(pg.Rect(100,200,10,300))
Maze.append(pg.Rect(780,50,10,450))
Maze.append(pg.Rect(360,130,10,80))
Maze.append(pg.Rect(280,210,10,100))
Maze.append(pg.Rect(460,210,10,200))
Maze.append(pg.Rect(540,400,10,100))
Maze.append(pg.Rect(580,130,10,200))
Maze.append(pg.Rect(690,60,10,280))
Maze.append(pg.Rect(170,210,10,100))

gameWon = 0

while not gameWon:
    pg.event.pump()

    #_____________INPUTS_____________#
    keys = pg.key.get_pressed()

    #_____________EVENTS_____________#
    if keys[pg.K_UP] == 1:
        shape[1] += -1

    if keys[pg.K_DOWN] == 1:
        shape[1] += 1

    if keys[pg.K_RIGHT] == 1:
        shape[0] += 1

    if keys[pg.K_LEFT] == 1:
        shape[0] += -1

    if shape[1] < 0 and shape[0] > 700:
        gameWon = 1

    #_____________DRAWING_____________#

    screen.fill(black)

    for maze in Maze:
        pg.draw.rect(screen,white,maze)
    pg.draw.rect(screen,Blue,shape)

    for wall in Maze:
        if shape.colliderect(wall):
            shape = pg.Rect(100,150,40,40)

    printToScreen(90,160,"Start",white,20)
    printToScreen(710,50,"Finish",white,20)
    pg.display.flip()

    #_____________CLOCKS_____________#
    clock.tick(60)

#Win Screen
screen.fill(white)
printToScreen(290,230,"You Won",black,50)
pg.display.flip()
