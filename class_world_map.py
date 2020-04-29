import sys
import pygame
from pygame.locals import QUIT
#pygame.init()
#SURFACE = pygame.display.set_mode((1000,1000))
class world_map:
    def __init__(self):#init에서 배경생성 
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
    
    #def 캐릭터관리(좌표, 스킬, 좌 우 점프 공격등등)
    
    #def 카메라시점 => 할수있으면
    
    #def 
    
while True:
    map = world_map()

