import pygame
import sys
import keyboard

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

def main_display():
    image1 = pygame.image.load('./image/display_main.jpg')
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

def key_event():
    for event in pygame.event.get():
        if event.type == K_UP:       # key up
            pass
        elif event.type == K_DOWN:     # key down
            pass
        elif event.type == K_LEFT:     # key left
            pass
        elif event.type == K_RIGHT:     # key right
            pass


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),HWSURFACE)    # variable window is instance of surface, hardware accelerated
    program_icon() # set program icon
    set_caption() # set name of program
    POWER_SWITCH = True     # turn on power
    
    while POWER_SWITCH:
        pygame.display.flip()   # display initialization
        main_display()
        game_start_button()
        key_event()

    POWER_SWITCH = False    # turn off power
    pygame.quit()