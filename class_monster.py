############### import module ###############
import pygame
import os
from math import floor

############### import my module ###############
import function_main as func

############### class monster ###############

class Monster():

    def __init__(self,x,y,width,height,velocity,move_right_path,move_left_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity 
        self.image = '' 
        self.direction = 'RIGHT'
        self.set = x
        self.median = (self.x+self.width/2,self.y+self.height/2)
        self.is_dead = False

        self.move_right_path = move_right_path
        self.move_right_list = os.listdir(self.move_right_path)
        self.move_right_index = 0
        
        self.move_left_path = move_left_path 
        self.move_left_list = os.listdir(self.move_left_path)
        self.move_left_index = 0

    def move(self):
        self.median = (self.x+self.width/2,self.y+self.height/2)  # declare more for initialize monster's location
        if self.set <= self.x and self.x <= self.set + func.MONSTER_MOVING_RANGE:
            if self.direction == 'RIGHT': self.x += self.velocity
            if self.x == self.set + func.MONSTER_MOVING_RANGE - self.velocity: self.direction = 'LEFT'
            if self.direction == 'LEFT': self.x -= self.velocity
            if self.x == self.set + self.velocity: self.direction = 'RIGHT'

    def draw_components(self,screen):
        if self.direction == 'RIGHT':
            self.move_right(screen)
        
        if self.direction == 'LEFT':
            self.move_left(screen)
    
    def hit(self,other):
        self.hitbox = (self.x,self.y,self.x+self.width,self.y+self.height)
        if (self.median[0] < other.hitbox[2]) and (self.median[0] > other.hitbox[0]) and (self.median[1] < other.hitbox[3]) and (self.median[1] > other.hitbox[1]): # if monster's median touches player's hitbox
            return True
        return False
    
    def move_right(self,screen):
        self.move_right_list = os.listdir(self.move_right_path)
        self.image = pygame.image.load(self.move_right_path + '/' + self.move_right_list[floor(self.move_right_index)])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, self.y))
        self.move_right_index += 0.1
        if self.move_right_index >= len(self.move_right_list) - 1: self.move_right_index = 0

    def move_left(self, screen):
        self.move_left_list = os.listdir(self.move_left_path)
        self.image = pygame.image.load(self.move_left_path + '/' + self.move_left_list[floor(self.move_left_index)])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, self.y))
        self.move_left_index += 0.1
        if self.move_left_index >= len(self.move_left_list) - 1: self.move_left_index = 0
            
