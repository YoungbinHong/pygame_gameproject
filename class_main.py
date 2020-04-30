import pygame, sys, keyboard
from pygame.locals import *

WINDOW_WIDTH, WINDOW_HEIGHT = 600,800
WHITE = (255,255,255)
BLACK = (0,0,0)
POWER_SWITCH = False

def program_icon():
    icon1 = pygame.image.load('./image/icon.png')
    pygame.display.set_icon(icon1)

def set_caption():
    pygame.display.set_caption('Super Action HUFS')

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

def key_press():
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_a: print('a key pressed'); return 'a'
                if event.key == K_RETURN: print('enter key pressed'); return 'enter'
    
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