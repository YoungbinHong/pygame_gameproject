import sys
import pygame
from pygame.locals import QUIT
from os import path
#import block
width = 600
height = 900
fps = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
TILESIZE = 30

pad_width = 600
pad_height = 900

x = pad_width *0.05
y = pad_width *0.8

#class Map(self):
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Superhero") #game title
#background = pygame.image.load('./image/galaxy_map.png')
#background = pygame.transform.scale(background,(width,height))
char = pygame.image.load('./image/char.png')
#background = pygame.transform.scale(background,(width,height))
char.blit(char,(0,0))
#screen.blit(background,(0,0))

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

while True:
    # screen.fill(GREEN) # clear screen
    screen.fill(WHITE)
    # draw_grid()

    map_data = []
    #read map_file
    map = "./image/galaxy_map.txt"
    with open(map, 'r') as file:
        for line in file:
            map_data.append(line.strip('\n').split(' '))

    for col in range(0, len(map_data)):
        for row in range(0, len(map_data[col])):
            print('map_data[col][row]', map_data[col][row])
            if map_data[col][row] == "b":
                tut_big = block(col, row)
                sprit_group.add(tut_big)
    sprit_group.draw(screen)
    pygame.display.flip()
    
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
