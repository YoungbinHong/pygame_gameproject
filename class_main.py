import pygame, sys, keyboard
from pygame.locals import *

############### system constants ###############

WINDOW_WIDTH, WINDOW_HEIGHT = 600,800
WHITE = (255,255,255)
BLACK = (0,0,0)
POWER_SWITCH = False

############### function for program contribute ###############

def program_icon():
    icon1 = pygame.image.load('./image/icon.png')
    pygame.display.set_icon(icon1)

def set_caption():
    pygame.display.set_caption('Super Action HUFS')

############### function for display components ###############

def home_display():
    image1 = pygame.image.load('./image/display_home.jpg')
    image1 = pygame.transform.scale(image1,(WINDOW_WIDTH,WINDOW_HEIGHT))
    screen.blit(image1,(0,0))

def select_map_display():
    image2 = pygame.image.load('./image/display_menu.jpg')
    image2 = pygame.transform.scale(image2,(WINDOW_WIDTH,WINDOW_HEIGHT))
    screen.blit(image2,(0,0))

def game_start_button():
    font1 = pygame.font.Font('./font/neodgm.ttf',60)
    start_button = font1.render("Press Enter!",True,BLACK)
    start_button_rect = start_button.get_rect(x=150,y=550)
    screen.blit(start_button,start_button_rect)

############### function for keyboard interrupt ###############

def key_press():
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP: print('UP key pressed'); return 'UP'
                if event.key == K_DOWN: print('DOWN key pressed'); return 'DOWN'
                if event.key == K_LEFT: print('LEFT key pressed'); return 'LEFT'
                if event.key == K_RIGHT: print('RIGHT key pressed'); return 'RIGHT'
                if event.key == K_RETURN: print('enter key pressed'); return 'enter'
                if event.key == K_1: print('NUM1 key pressed'); return 'NUM1'
                if event.key == K_2: print('NUM2 key pressed'); return 'NUM2'
                if event.key == K_3: print('NUM3 key pressed'); return 'NUM3'
                if event.key == K_4: print('NUM4 key pressed'); return 'NUM4'

############### function main ###############

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),HWSURFACE)    # variable window is instance of surface, hardware accelerated
    program_icon() # set program icon
    set_caption() # set name of program
    POWER_SWITCH = True     # turn on power
    current_display = 'home'    # start in home display

    while POWER_SWITCH:

        pygame.display.flip()   # display initialization

        if current_display == 'home':
            home_display()
            game_start_button()
        if current_display == 'select_map':
            select_map_display()
        
        if key_press() == 'enter': current_display = 'select_map'

    POWER_SWITCH = False    # turn off power
    pygame.quit()