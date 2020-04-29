import sys
import pygame
from pygame.locals import QUIT
#pygame.init()
#SURFACE = pygame.display.set_mode((1000,1000))
class world_map:
    def __init__(self):
        pygame.init()
        width,height = 1024, 512
        self.gamepad = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Superhero')
        self.clock = pygame.time.Clock()
        WHITE = (255,255,255)
        self.gamepad.fill(WHITE)
        background = pygame.image.load('image/background.png')
        self.gamepad.blit(background,(0,0))
        pygame.display.update()
        self.clock.tick(60)

while True:
    map = world_map()

