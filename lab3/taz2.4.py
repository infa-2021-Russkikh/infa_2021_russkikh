import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1980, 1080))
rect(screen,(100,100,230),(0,0,1980,540),)
rect(screen,(0,100,0),(0,540,1980,540))
rect(screen,(200,100,0),(400,500,350,300))
rect(screen,(50,50,255),(530,600,100,100))
rect(screen,(0,0,0),(530,645,100,10))
rect(screen,(0,0,0),(575,600,10,100))
polygon(screen, (100,10,10.1),[(400,500),(750,500),(580,350)])
def obl(x,y):
    circle(screen,(250,250,250),(x,y),50)
    circle(screen,(0,0,0),(x,y),50,width =1)
def list(x,y,Z):
    circle(screen,(0,150,0),(x+20,y),50*Z)
    circle(screen,(0,0,0),(x+20,y),50*Z,width =1)
def apple (x,y):
    circle(screen,(200,0,0),(x-20,y+20),10)

def sun(x,y):
    circle(screen,(100,100,0),(x,y),10)
    

def derevo(x,y,Z):
    rect(screen,(100,0,30),(x+5,y+5,Z*50,Z*400))
    list((x-40*Z),y+40*Z,Z)
    list(x+40*Z,y+40*Z,Z)
    list(x,y+40*Z,Z)
    list(x-80*Z,y,Z)
    list(x+80*Z,y,Z)
    list(x-40*Z,y,Z)
    list(x+40*Z,y,Z)
    list(x,y,Z)
    list(x,y-40*Z,Z)
    list(x-40*Z,y-40*Z,Z)
    list(x+40*Z,y-40*Z,Z)
    #apple(x-Z*20,y+Z*60)



sun(1000,500)

obl(1430,200)
obl(1400,230)
obl(1450,230)
obl(1500,230)
obl(1480,200)
obl(1430,200)

obl(1400-300,230-10)
obl(1450-300,230-10)
obl(1500-300,230-10)
obl(1480-300,200-10)
obl(1430-300,200-10)

derevo(1000,500,1)
derevo(1400,600,0.5)









pygame.display.update()
