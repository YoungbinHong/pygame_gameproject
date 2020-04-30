import sys, keyboard
import pygame
from pygame.locals import QUIT
from os import path
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

#class Map(self):
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Superhero") #game title
#background = pygame.image.load('./image/galaxy_map.png')
#background = pygame.transform.scale(background,(width,height))
#char = pygame.image.load('./image/char.png')
#background = pygame.transform.scale(background,(width,height))
#char.blit(char,char_pos)
#screen.blit(background,(0,0))

sprit_group = pygame.sprite.Group()
keys = [False, False, False, False, False]

char_pos = [0, 0]
char = pygame.image.load('./image/char.png')

class block(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.grid_x = row * TILESIZE
        self.grid_y = col * TILESIZE
        self.image = pygame.image.load('image/block.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.grid_x
        self.rect.y = self.grid_y
'''#####이걸로 했을때 KEYDOWN이 에러가 생겨버려서 이거 말고 다른것으로 했어요#####
def key_press():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP: return 'UP'
            if event.key == K_DOWN: return 'DOWN'
            if event.key == K_LEFT: return 'LEFT'
            if event.key == K_RIGHT: return 'RIGHT'
            if event.key == K_1: return 'NUM1'
            if event.key == K_2: return 'NUM2'
            if event.key == K_3: return 'NUM3'
            if event.key == K_4: return 'NUM4'
            if event.key == K_RETURN: return 'ENTER'
            if event.key == K_ESCAPE: return 'ESC'
            if event.key == K_DELETE: return 'DELETE'
'''

while True:
    screen.fill(WHITE)
    # draw_grid()

    map_data = []
    #read map_file
    map = "./image/galaxy_map.txt"
    #key = key_press()
    #if key != None: print(key); log.write(key+'\n')     # player record
    #if key == 'DELETE': POWER_SWITCH = False            # emergency escape
    
    with open(map, 'r') as file:
        for line in file:
            map_data.append(line.strip('\n').split(' '))

    for col in range(0, len(map_data)):
        for row in range(0, len(map_data[col])):
            #print('map_data[col][row]', map_data[col][row])
            if map_data[col][row] == "b":
                tut_big = block(col, row)
                sprit_group.add(tut_big)
    
    sprit_group.draw(screen)
    char = pygame.image.load('./image/char.png')
    screen.blit(char,char_pos)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
    
    if keys[0]:
        char_pos[1] = char_pos[1]-10
        print(char_pos)
    elif keys[2]:
        char_pos[1] = char_pos[1]+10    
        print(char_pos)
    if keys[1]:
        char_pos[0] = char_pos[0]-10
        print(char_pos)
    elif keys[3]:
        char_pos[0] = char_pos[0]+10
        print(char_pos) 
    #####이부분 하면 더이상 캐릭터가 내려가지 않아야하는데 게임이 종료되어버려요#####
    if char_pos[1] >=690:
        char_pos = 690
 
    
    
