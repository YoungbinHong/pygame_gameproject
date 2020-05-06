############### import module ###############
import pygame
import os

############### import my module ###############            -> have to solve circular import error (using wildcard is not recommended)
from class_player import *
from class_monster import *
from class_dead_message import *
from class_restart_message import *
from class_score_display import *
from class_moving_background import *
from class_music import *
from class_enter_message import *
from class_victory_message import *
from class_loading import *
from class_ghost import *
from class_quit_message import *

############### system constants ###############
WHITE = (255,255,255)
BLACK = (0,0,0)

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 500

CHARACTER_JUMP = 8

MONSTER_MOVING_RANGE = 300

##### SWITCHES #####
POWER_SWITCH = True
START_DISPLAY_SWITCH = True
HELP_DISPLAY_SWITCH = True
PLAYING_DISPLAY_ALIVE_SWITCH = True
PLAYING_DISPLAY_DEAD_SWITCH = True
RESTART_SWITCH = True
VICTORY_SWITCH = False

##### display control #####
pygame.init()                                                       # initializing pygame package
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))      # screen booting
pygame.display.set_caption('Captian America')                     # name of program
program_icon = pygame.image.load('./image/icon.png')
pygame.display.set_icon(program_icon)

############### function main ###############
if __name__ == '__main__':

    ##### make instance #####
    player1 = Player(20,240,340,300,2,'./image/player/stand_right','./image/player/stand_left','./image/player/move_right','./image/player/move_left','./image/player/dash_right','./image/player/dash_left','./image/player/dead_down','./image/player/dash_gauge')

    monster1 = Monster(800,300,132,186,2,'./image/monster/move_right','./image/monster/move_left')
    monster2 = Monster(500,300,132,186,5,'./image/monster/move_right','./image/monster/move_left')
    monster3 = Monster(650,300,132,186,3,'./image/monster/move_right','./image/monster/move_left')

    ghost1 = Ghost(10,200,200,300,0.1,'./image/ghost')
    
    enter_message = Enter_Message()
    dead_message = Dead_Message(450,200,600,350,'./image/caution/you_died.png')
    victory_message = Victory_Message(450,200,600,350,'./image/caution/victory.png')
    restart_message = Restart_Message()
    quit_message = Quit_Message()
    
    loading = Loading('./image/loading_bar')

    Background = Moving_Background('./image/display1.png')

    score_disp = Score_Display()

    bgm1 = Music('./music/start_display.ogg')
    bgm2 = Music('./music/help_display.ogg')
    bgm3 = Music('./music/playing_display_alive.ogg')
    bgm4 = Music('./music/playing_display_dead.ogg')
    death_effect = Music('./music/death_effect.ogg')

    ##### infinite loop for program #####
    while POWER_SWITCH:
        #---------------------------------------------------------------------------------------------------------
        ##### start display components control #####
        START_DISPLAY_SWITCH = True
        bgm1.play_inf()
        start_display = pygame.image.load('./image/start_display.jpg')
        start_display = pygame.transform.scale(start_display,(WINDOW_WIDTH, WINDOW_HEIGHT))

        ##### infinite loop for start display #####
        while START_DISPLAY_SWITCH:
            pygame.display.flip()
            screen.blit(start_display,(0,0))
            enter_message.draw_components()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    START_DISPLAY_SWITCH = False

        #---------------------------------------------------------------------------------------------------------
        ##### loading display #####
        
        bgm1.off()
        loading.index = 0
        while loading.index < 89:
            pygame.display.flip()
            loading.draw_components(screen)
        
        #---------------------------------------------------------------------------------------------------------
        ##### help display components control #####
        HELP_DISPLAY_SWITCH = True
        bgm2.play_inf()
        help_display = pygame.image.load('./image/help_display.jpg')
        help_display = pygame.transform.scale(help_display,(WINDOW_WIDTH, WINDOW_HEIGHT))

        ##### infinite loop for help display #####
        while HELP_DISPLAY_SWITCH:
            pygame.display.flip()
            screen.blit(help_display,(0,0))
            enter_message.draw_components()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    HELP_DISPLAY_SWITCH = False

        #---------------------------------------------------------------------------------------------------------
        ##### loading display #####

        bgm2.off()
        loading.index = 0
        while loading.index < 89:
            pygame.display.flip()
            loading.draw_components(screen)
        
        #---------------------------------------------------------------------------------------------------------
        ##### playing display alive components control #####
        PLAYING_DISPLAY_ALIVE_SWITCH = True

        player1.is_dead = False
        player1.health = 30
        player1.x = 20
        player1.y = 250
        player1.dash_gauge = 0

        monster1.is_dead = False
        monster2.is_dead = False
        monster3.is_dead = False
        monster1.median = (monster1.x+monster1.width/2,monster1.y+monster1.height/2)
        monster1.median = (monster1.x+monster1.width/2,monster1.y+monster1.height/2)
        monster1.median = (monster1.x+monster1.width/2,monster1.y+monster1.height/2)

        ghost1.x = 10
        ghost1.median = (ghost1.x + ghost1.width * 2/3, func.WINDOW_HEIGHT)

        score_disp.score = 0
        bgm3.play_inf()

        ##### infinite loop for playing display alive #####
        while PLAYING_DISPLAY_ALIVE_SWITCH:
            
            ##### score board #####
            score_disp.score += 0.1
            score_disp.draw_components()

            ##### display initialization ##### 
            pygame.display.flip()

            ##### background display #####
            Background.move()

            if not player1.is_dead: # alive
                # hit #
                player1.is_dead = player1.hit(monster1) or player1.hit(monster2) or player1.hit(monster3)
                if monster1.hit(player1) and player1.status == 'DASH':
                    monster1.is_dead = True
                    monster1.median = (0,0)
                if monster2.hit(player1) and player1.status == 'DASH':
                    monster2.is_dead = True
                    monster2.median = (0,0)
                if monster3.hit(player1) and player1.status == 'DASH':
                    monster3.is_dead = True
                    monster3.median = (0,0)

                # key input #
                player1.key_continuous_input(screen)
                # character district #
                player1.character_district()
                # draw components #
                player1.draw_components(screen)
                if not monster1.is_dead:
                    monster1.move()
                    monster1.draw_components(screen)
                if not monster2.is_dead:
                    monster2.move()
                    monster2.draw_components(screen)
                if not monster3.is_dead:
                    monster3.move()
                    monster3.draw_components(screen)
                ##### ghost #####
                if not player1.is_dead:
                    ghost1.move()
                    ghost1.draw_components(screen)
                
            if player1.is_dead: # dead
                PLAYING_DISPLAY_ALIVE_SWITCH = False
                PLAYING_DISPLAY_DEAD_SWITCH = True
                VICTORY_SWITCH = False
            if monster1.is_dead and monster2.is_dead and monster3.is_dead:
                PLAYING_DISPLAY_ALIVE_SWITCH = False
                PLAYING_DISPLAY_DEAD_SWITCH = False
                VICTORY_SWITCH = True

        #---------------------------------------------------------------------------------------------------------
        ##### playing display dead components control #####
        player1.dead_down_index = 0
        bgm3.off()
        bgm4.play_inf()

        ##### infinite loop for playing display dead #####
        while PLAYING_DISPLAY_DEAD_SWITCH:
            
            ##### display initialization #####
            pygame.display.flip()

            ##### score board #####
            score_disp.draw_components()

            ##### background display #####
            Background.move()

            ##### draw components #####
            player1.dead_down(screen)
            dead_message.draw_components(screen)
            restart_message.draw_components(dead_message)

            ##### push event #####
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    PLAYING_DISPLAY_DEAD_SWITCH = False
                    bgm4.off()
        
        #---------------------------------------------------------------------------------------------------------        
        ##### playing display victory components control #####
        player1.dead_down_index = 0
        bgm3.off()
        bgm4.play_inf()
        
        ##### infinite loop for playing display victory #####
        while VICTORY_SWITCH:
            
            ##### display initialization #####
            pygame.display.flip()

            ##### score board #####
            score_disp.draw_components()

            ##### background display #####
            Background.move()

            ##### draw components #####
            player1.status = 'STAND'
            player1.draw_components(screen)
            victory_message.draw_components(screen)
            restart_message.draw_components(victory_message)
            quit_message.draw_components(victory_message)

            ##### push event #####
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    VICTORY_SWITCH = False
                    bgm4.off()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    VICTORY_SWITCH = False
                    POWER_SWITCH = False

        #---------------------------------------------------------------------------------------------------------
        ##### loading display #####
        bgm4.off()
        loading.index = 0
        while loading.index < 89:
            pygame.display.flip()
            loading.draw_components(screen)
        