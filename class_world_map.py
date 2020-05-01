import sys, keyboard
import pygame
import random
from pygame.locals import QUIT
from os import path
from pygame import *
#from pygame import K_RETURN, K_S, K_W, K_UP, K_DOWN
width = 600
height = 900
fps = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ALPHA = (0,255,0)
TILESIZE = 30
sprit_group = pygame.sprite.Group()

class block(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load('image/block.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y

def drawobject(obj,x,y):
    global screen
    screen.blit(obj,(x,y))

def airplane(x,y):
    global screen, aircraft
    aircraft = pygame.image.load('./image/plane.png')
    #screen.blit(aircraft,(x,y))

def runGame():
    global screen, clock
    global bat, fires
    fires = []
   
    background = pygame.image.load('./image/city_orange.png')
    background = pygame.transform.scale(background,(width,height))
    #aircraft = pygame.image.load('./image/plane.png')
    bat = pygame.image.load('./image/bat.png')
    fires.append(pygame.image.load('./image/fireball.png'))
    fires.append(pygame.image.load('./image/fireball2.png'))
    screen.blit(background,(0,0))
    
    x = width * 0.05
    y = height* 0.08
    y_change = 0
    
    for i in range(5):
        fires.append(None)

    bat_x = width
    bat_y = random.randrange(0,height)

    fire_x = width
    fire_y = random.randrange(0,height)
    random.shuffle(fires)
    fire = fires[0]
    
    while True:
        mk_block()
        sprit_group.draw(screen)
        
        bat_x = 7
        if bat_x <= 0:
            bat_x = width
            bat_y = random.randrange(0,height)
        if fire == None:
            fire_x -= 30
        else:
            fire_x -= 15
        if fire_x <= 0:
            fire_x = width
            fire_y = random.randrange(0,height)
            random.shuffle(fires)
            fire= fires[0]
        #drawobject(screen, screen, 0)
        drawobject(bat, bat_x, bat_y)
        if fire != None:
            drawobject(fire, fire_x, fire_y)
        for event in pygame.event.get():
            #screen.fill(BLACK)
            pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key== pygame.K_UP or event.key == K_DOWN:
                    y_change = 0

        y+=y_change
        airplane(x,y)           
        
        pygame.display.flip()
        pygame.display.update() 
     
def mk_block():
    map_data = []
    map = "./image/galaxy_map.txt"
    with open(map, 'r') as file:
        for line in file:
            map_data.append(line.strip('\n').split(' '))

    for col in range(0, len(map_data)):
        for row in range(0, len(map_data[col])):
            #print('map_data[col][row]', map_data[col][row])
            if map_data[col][row] == "b":
                map_block = block(col, row)
                sprit_group.add(map_block)

def initGame():
    global screen, clock
    global bat, fires    

    fires=[]

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Superhero")
    clock = pygame.time.Clock()
    sprit_group = pygame.sprite.Group()
    runGame()

initGame()    
