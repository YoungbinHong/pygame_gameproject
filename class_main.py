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

def disp(location):
    image = pygame.image.load(location)
    image = pygame.transform.scale(image,(WINDOW_WIDTH,WINDOW_HEIGHT))
    screen.blit(image,(0,0))

############### function for keyboard interrupt ###############

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

############### function main ###############

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),HWSURFACE)    # variable screen is instance of surface, hardware accelerated
    program_icon() # set program icon
    set_caption() # set name of program
    POWER_SWITCH = True     # turn on power

    current_display = './image/home.png'    # start in home display
    log = open('./log/play_log.txt','a')    # generate log file to review error

    while POWER_SWITCH:
        pygame.display.flip()   # display initialization

        key = key_press()
        if key != None: print(key); log.write(key+'\n')     # player record
        if key == 'DELETE': POWER_SWITCH = False            # emergency escape

        
        disp(current_display)
        print(current_display)
        if current_display == './image/home.png':
            if key == 'UP': current_display = './image/home_game_exit.png'
            if key == 'DOWN': current_display = './image/home_game_start.png'
            continue

        if current_display == './image/home_game_start.png':
            if key == 'UP': current_display = './image/home.png'
            if key == 'DOWN': current_display = './image/home_game_exit.png'
            if key == 'ENTER': current_display = './image/select_map.png'
            continue
        
        if current_display == './image/home_game_exit.png':
            if key == 'UP': current_display = './image/home_game_start.png'
            if key == 'DOWN': current_display = './image/home.png'
            if key == 'ENTER': current_display = './image/home_game_exit_option.png'
            continue

        if current_display == './image/home_game_exit_option.png':
            if key == 'ENTER': POWER_SWITCH = False
            if key == 'ESC' : current_display = './image/home_game_exit.png'
            continue

        if current_display == './image/select_map.png':
            if key == 'ESC' : current_display = './image/home.png'
            if key == 'UP' or key == 'DOWN' or key == 'LEFT' or key == 'RIGHT': current_display = './image/select_map_1.png'
            continue

        if current_display == './image/select_map_1.png':
            if key == 'ESC' : current_display = './image/select_map.png'
            if key == 'DOWN' : current_display = './image/select_map_3.png'
            if key == 'RIGHT' : current_display = './image/select_map_2.png'
            continue

        if current_display == './image/select_map_2.png':
            if key == 'ESC' : current_display = './image/select_map.png'
            if key == 'DOWN' : current_display = './image/select_map_4.png'
            if key == 'LEFT' : current_display = './image/select_map_1.png'
            continue

        if current_display == './image/select_map_3.png':
            if key == 'ESC' : current_display = './image/select_map.png'
            if key == 'UP' : current_display = './image/select_map_1.png'
            if key == 'RIGHT' : current_display = './image/select_map_4.png'
            continue

        if current_display == './image/select_map_4.png':
            if key == 'ESC' : current_display = './image/select_map.png'
            if key == 'UP' : current_display = './image/select_map_2.png'
            if key == 'LEFT' : current_display = './image/select_map_3.png'
            continue

    pygame.quit()
    log.close()
