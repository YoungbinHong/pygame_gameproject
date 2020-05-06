############### import module ###############
import pygame
import os
from math import floor

############### import my module ###############
import function_main as func

############### class loading ###############
class Loading():
    def __init__(self,path):
        self.path = path
        self.list = os.listdir(self.path)
        self.index = 0
        self.image = ''

    def draw_components(self,screen):
        self.image = pygame.image.load(self.path+'/'+self.list[floor(self.index)])
        self.image = pygame.transform.scale(self.image,(func.WINDOW_WIDTH,func.WINDOW_HEIGHT))
        func.screen.blit(self.image,(0,0))
        self.index += 0.25
        if self.index >= 89: self.index = 89