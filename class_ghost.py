############### import module ###############
import pygame
import os
from math import floor

############### import my module ###############
import function_main as func

############### class ghost ###############
class Ghost():
    
    def __init__(self,x,y,width,height,vel,ghost_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.hitbox = (self.x,0,self.width,func.WINDOW_HEIGHT)
        self.ghost_path = ghost_path
        self.ghost_list = os.listdir(self.ghost_path)
        self.ghost_index = 0
        self.image = ''
        self.median = (self.x+self.width * 2/3,func.WINDOW_HEIGHT)

    def draw_components(self,screen):
        self.ghost_list = os.listdir(self.ghost_path)
        self.image = pygame.image.load(self.ghost_path+'/'+self.ghost_list[floor(self.ghost_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        self.ghost_index += 0.1
        if self.ghost_index >= len(self.ghost_list)-1: self.ghost_index = 0


    def move(self):
        self.median = (self.x+self.width/2,self.y+self.height/2)
        self.x += self.vel