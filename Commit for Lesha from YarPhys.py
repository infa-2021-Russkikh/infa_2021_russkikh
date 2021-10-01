import pygame as pg

pg.init()

a = 1920
b = 1080
screen = pg.display.set_mode((a, b))  # Full HD screen


def background(x, y):  # Drawing background
    pg.rect(screen, (100, 100, 230), (0, 0, x, y/2))
    pg.rect(screen, (0, 100, 0), (0, y/2, x, y/2))


def house(x, y):  # Drawing house
    pg.rect(screen,(200,100,0),(x, y, 350, 300))
    pg.rect(screen,(50,50,255),(x + 130, y + 100,100,100))
    pg.rect(screen,(0,0,0),(x + 130, y + 145,100,10))
    pg.rect(screen,(0,0,0),(x + 175, x + 100,10,100))
    pg.polygon(screen, (100,10,10.1),[(x,y),(x + 350, y),(x + 180, y - 150)])

def obl(x,y):  # Drawing subcloud
    pg.circle(screen,(250,250,250),(x,y),50)
    pg.circle(screen,(0,0,0),(x,y),50,width = 1)
    
def leaves(x,y,Z):  # Drawing leaves of tree
    pg.circle(screen,(0,150,0),(x+20, y), 50*Z)
    pg.circle(screen,(0,0,0),(x+20, y), 50*Z, width = 1)
    
def tree(x,y,Z):  # Drawing tree
    pg.rect(screen,(100,0,30),(x+5,y+5,Z*50,Z*400))
    leaves((x-40*Z),y+40*Z,Z)
    leaves(x+40*Z,y+40*Z,Z)
    leaves(x,y+40*Z,Z)
    leaves(x-80*Z,y,Z)
    leaves(x+80*Z,y,Z)
    leaves(x-40*Z,y,Z)
    leaves(x+40*Z,y,Z)
    leaves(x,y,Z)
    leaves(x,y-40*Z,Z)
    leaves(x-40*Z,y-40*Z,Z)
    leaves(x+40*Z,y-40*Z,Z)
    
def sun(x,y):  # Drawing sun
    pg.circle(screen,(100,100,0),(x,y),10)
    

background(a, b)
    
house(400, 500)

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

tree(1000,500,1)
tree(1400,600,0.5)

pg.display.update()import pygame as pg

pg.init()

a = 1920
b = 1080
screen = pg.display.set_mode((a, b))  # Full HD screen


def background(x, y):  # Drawing background
    pg.rect(screen, (100, 100, 230), (0, 0, x, y/2))
    pg.rect(screen, (0, 100, 0), (0, y/2, x, y/2))


def house(x, y):  # Drawing house
    pg.rect(screen,(200,100,0),(x, y, 350, 300))
    pg.rect(screen,(50,50,255),(x + 130, y + 100,100,100))
    pg.rect(screen,(0,0,0),(x + 130, y + 145,100,10))
    pg.rect(screen,(0,0,0),(x + 175, x + 100,10,100))
    pg.polygon(screen, (100,10,10.1),[(x,y),(x + 350, y),(x + 180, y - 150)])

def obl(x,y):  # Drawing subcloud
    pg.circle(screen,(250,250,250),(x,y),50)
    pg.circle(screen,(0,0,0),(x,y),50,width = 1)
    
def leaves(x,y,Z):  # Drawing leaves of tree
    pg.circle(screen,(0,150,0),(x+20, y), 50*Z)
    pg.circle(screen,(0,0,0),(x+20, y), 50*Z, width = 1)
    
def tree(x,y,Z):  # Drawing tree
    pg.rect(screen,(100,0,30),(x+5,y+5,Z*50,Z*400))
    leaves((x-40*Z),y+40*Z,Z)
    leaves(x+40*Z,y+40*Z,Z)
    leaves(x,y+40*Z,Z)
    leaves(x-80*Z,y,Z)
    leaves(x+80*Z,y,Z)
    leaves(x-40*Z,y,Z)
    leaves(x+40*Z,y,Z)
    leaves(x,y,Z)
    leaves(x,y-40*Z,Z)
    leaves(x-40*Z,y-40*Z,Z)
    leaves(x+40*Z,y-40*Z,Z)
    
def sun(x,y):  # Drawing sun
    pg.circle(screen,(100,100,0),(x,y),10)
    

background(a, b)
    
house(400, 500)

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

tree(1000,500,1)
tree(1400,600,0.5)

pg.display.update()
