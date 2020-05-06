############### import module ###############
import pygame
import os
from math import floor

############### import my module ###############
import function_main as func

############### class player ###############
class Player(object):
    
    def __init__(self,x,y,width,height,velocity,stand_right_path,stand_left_path,move_right_path,move_left_path,dash_right_path,dash_left_path,dead_down_path,dash_gauge_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.hitbox = (self.x,self.y,self.x+self.width,self.y+self.height)
        self.is_jumping = False
        self.jump_power = func.CHARACTER_JUMP
        self.status = 'STAND'
        self.facing = 'RIGHT'
        self.is_dead = False
        self.image = ''
        self.dash_gauge = 0

        self.health = 30    
        self.median = (self.x+self.width/2,self.y+self.height/2)
        
        self.stand_right_path = stand_right_path
        self.stand_right_list = os.listdir(self.stand_right_path)
        self.stand_right_index = 0
        
        self.stand_left_path = stand_left_path
        self.stand_left_list = os.listdir(self.stand_left_path)
        self.stand_left_index = 0

        self.move_right_path = move_right_path
        self.move_right_list = os.listdir(self.move_right_path)
        self.move_right_index = 0

        self.move_left_path = move_left_path
        self.move_left_list = os.listdir(self.move_left_path)
        self.move_left_index = 0

        self.dash_right_path = dash_right_path
        self.dash_right_list = os.listdir(self.dash_right_path)
        self.dash_right_index = 0

        self.dash_left_path = dash_left_path
        self.dash_left_list = os.listdir(self.dash_left_path)
        self.dash_left_index = 0

        self.dead_down_path = dead_down_path
        self.dead_down_list = os.listdir(self.dead_down_path)
        self.dead_down_index = 0

        self.dash_gauge_path = dash_gauge_path
        self.dash_gauge_list = os.listdir(self.dash_gauge_path)

    def key_continuous_input(self,screen):
        pygame.event.pump() # initialize key press
        keys = pygame.key.get_pressed() # key press

        if 1 not in keys:
            self.status = 'STAND'

        if keys[pygame.K_RIGHT]:
            self.facing = 'RIGHT'
            self.status = 'MOVE'
            self.dash_gauge += 1
            self.x += self.velocity

        if keys[pygame.K_LEFT]:
            self.facing = 'LEFT'
            self.status = 'MOVE'
            self.dash_gauge += 1
            self.x -= self.velocity
        
        if keys[pygame.K_RIGHT] and keys[pygame.K_a] and self.dash_gauge >= 260:
            self.facing = 'RIGHT'
            self.status = 'DASH'
            self.dash_gauge = 0
            for i in range(10):
                self.image = pygame.image.load(self.dash_right_path+'/'+self.dash_right_list[0])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x += 10
            for i in range(10):
                self.image = pygame.image.load(self.dash_right_path+'/'+self.dash_right_list[1])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x += 5
            for i in range(10):
                self.image = pygame.image.load(self.dash_right_path+'/'+self.dash_right_list[2])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x += 2.5
            for i in range(10):
                self.image = pygame.image.load(self.dash_right_path+'/'+self.dash_right_list[3])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x += 1.25
            for i in range(10):
                self.image = pygame.image.load(self.dash_right_path+'/'+self.dash_right_list[4])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x += 0.625
            for i in range(10):
                self.image = pygame.image.load(self.dash_right_path+'/'+self.dash_right_list[5])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x += 0.3125
        
        if keys[pygame.K_LEFT] and keys[pygame.K_a] and self.dash_gauge >= 260:
            self.facing = 'LEFT'
            self.status = 'DASH'
            self.dash_gauge = 0
            for i in range(10):
                self.image = pygame.image.load(self.dash_left_path+'/'+self.dash_left_list[0])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x -= 10
            for i in range(10):
                self.image = pygame.image.load(self.dash_left_path+'/'+self.dash_left_list[1])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x -= 5
            for i in range(10):
                self.image = pygame.image.load(self.dash_left_path+'/'+self.dash_left_list[2])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x -= 2.5
            for i in range(10):
                self.image = pygame.image.load(self.dash_left_path+'/'+self.dash_left_list[3])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x -= 1.25
            for i in range(10):
                self.image = pygame.image.load(self.dash_left_path+'/'+self.dash_left_list[4])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x -= 0.625
            for i in range(10):
                self.image = pygame.image.load(self.dash_left_path+'/'+self.dash_left_list[5])
                self.image = pygame.transform.scale(self.image,(self.width,self.height))
                screen.blit(self.image,(self.x,self.y))
                self.x -= 0.3125
        
        if keys[pygame.K_RIGHT] and keys[pygame.K_s]:
            self.facing = 'RIGHT'
            self.status = 'ATTACK'

        if keys[pygame.K_LEFT] and keys[pygame.K_s]:
            self.facing = 'LEFT'
            self.status = 'ATTACK'

        if not self.is_jumping:
            if keys[pygame.K_UP]:
                self.is_jumping = True
        else:
            if self.jump_power >= -1*func.CHARACTER_JUMP:
                neg = 1
                if self.jump_power < 0:
                    neg = -1
                    
                self.y -= (self.jump_power ** 2) * 0.5 * neg 
                self.jump_power -= 1
            
            else:
                self.is_jumping = False

                self.jump_power = func.CHARACTER_JUMP

    def character_district(self):
        if self.x < 0: self.x = 0
        if self.x > func.WINDOW_WIDTH - self.width : self.x = func.WINDOW_WIDTH - self.width
    
    def hit(self,other):
        self.hitbox = (self.x,self.y,self.x+self.width,self.y+self.height)  # declare more for initialize player's hitbox
        if (other.median[0] < self.hitbox[2]) and (other.median[0] > self.hitbox[0]) and (other.median[1] < self.hitbox[3]) and (other.median[1] > self.hitbox[1]) and self.status != 'DASH': # if monster's median touches player's hitbox
            self.health -= 1

        if self.health >= 30:
            self.image = pygame.image.load('./image/healthbar/RedHP3.png')
            self.image = pygame.transform.scale(self.image,(200,20))
            func.screen.blit(self.image,(self.x+80, self.y+30))
        elif self.health >= 20 and self.health < 30:
            self.image = pygame.image.load('./image/healthbar/RedHP2.png')
            self.image = pygame.transform.scale(self.image,(200,20))
            func.screen.blit(self.image,(self.x+80, self.y+30)) 
        elif self.health > 0:
            self.image = pygame.image.load('./image/healthbar/RedHP1.png')
            self.image = pygame.transform.scale(self.image,(200,20))  
            func.screen.blit(self.image,(self.x+80, self.y+30))            

        return True if self.health == 0 else False

    def draw_components(self,screen):
        
        if not self.is_dead:
            if self.status == 'STAND' and self.facing == 'RIGHT':
                self.stand_right(screen)
            if self.status == 'STAND' and self.facing == 'LEFT':
                self.stand_left(screen)
            if self.status == 'MOVE' and self.facing == 'RIGHT':
                self.move_right(screen)
            if self.status == 'MOVE' and self.facing == 'LEFT':
                self.move_left(screen)
            '''
            if self.status == 'DASH' and self.facing == 'RIGHT':
                self.dash_right(screen)
            if self.status == 'DASH' and self.facing == 'LEFT':
                self.dash_left(screen)
            '''

        if self.dash_gauge < 20:
            self.draw_dash_gauge(screen,0)
        elif self.dash_gauge < 40:
            self.draw_dash_gauge(screen,1)
        elif self.dash_gauge < 60:
            self.draw_dash_gauge(screen,2)
        elif self.dash_gauge < 80:
            self.draw_dash_gauge(screen,3)
        elif self.dash_gauge < 100:
            self.draw_dash_gauge(screen,4)
        elif self.dash_gauge < 120:
            self.draw_dash_gauge(screen,5)
        elif self.dash_gauge < 140:
            self.draw_dash_gauge(screen,6)
        elif self.dash_gauge < 160:
            self.draw_dash_gauge(screen,7)
        elif self.dash_gauge < 180:
            self.draw_dash_gauge(screen,8)
        elif self.dash_gauge < 200:
            self.draw_dash_gauge(screen,9)
        elif self.dash_gauge < 220:
            self.draw_dash_gauge(screen,10)
        elif self.dash_gauge < 240:
            self.draw_dash_gauge(screen,11)
        else:
            self.draw_dash_gauge(screen,12)
            
    def draw_dash_gauge(self,screen,index):
        self.image = pygame.image.load(self.dash_gauge_path+'/'+self.dash_gauge_list[index])
        self.image = pygame.transform.scale(self.image,(250,50))
        screen.blit(self.image,(func.WINDOW_WIDTH-290,30))

    def stand_right(self,screen):
        self.stand_right_list = os.listdir(self.stand_right_path)
        self.image = pygame.image.load(self.stand_right_path+'/'+self.stand_right_list[floor(self.stand_right_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        self.stand_right_index += 0.05
        if self.stand_right_index >= len(self.stand_right_list)-1: self.stand_right_index = 0

    def stand_left(self,screen):
        self.stand_left_list = os.listdir(self.stand_left_path)
        self.image = pygame.image.load(self.stand_left_path+'/'+self.stand_left_list[floor(self.stand_left_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        self.stand_left_index += 0.05
        if self.stand_left_index >= len(self.stand_left_list)-1: self.stand_left_index = 0
    
    def move_right(self,screen):
        self.move_right_list = os.listdir(self.move_right_path)
        self.image = pygame.image.load(self.move_right_path+'/'+self.move_right_list[floor(self.move_right_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        self.move_right_index += 0.1
        if self.move_right_index >= len(self.move_right_list)-1: self.move_right_index = 0
    
    def move_left(self,screen):
        self.move_left_list = os.listdir(self.move_left_path)
        self.image = pygame.image.load(self.move_left_path+'/'+self.move_left_list[floor(self.move_left_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        self.move_left_index += 0.1
        if self.move_left_index >= len(self.move_left_list)-1: self.move_left_index = 0
    '''
    def dash_right(self,screen):
        self.dash_right_list = os.listdir(self.dash_right_path)
        self.image = pygame.image.load(self.dash_right_path+'/'+self.dash_right_list[floor(self.dash_right_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        self.dash_right_index += 0.01
        if self.dash_right_index >= len(self.dash_right_list)-1: self.dash_right_index = 0
        
    def dash_left(self,screen):
        self.dash_left_list = os.listdir(self.dash_left_path)
        self.image = pygame.image.load(self.dash_left_path+'/'+self.dash_left_list[floor(self.dash_left_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        self.dash_left_index += 0.01
        if self.dash_left_index >= len(self.dash_left_list)-1: self.dash_left_index = 0
    '''
    def dead_down(self,screen):
        self.dead_down_list = os.listdir(self.dead_down_path)
        self.image = pygame.image.load(self.dead_down_path+'/'+self.dead_down_list[floor(self.dead_down_index)])
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,(self.x,self.y))
        if self.dead_down_index < len(self.dead_down_list)-0.1:
            self.dead_down_index += 0.1
        