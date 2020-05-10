############### import module ###############
import pygame
from math import floor

############### import my module ###############
import function_main as func

############### class score display ###############
class Score_Display():
    def __init__(self):
        self.score = 0

    def draw_components(self):
        font_30 = pygame.font.SysFont('FixedSys',30,True,False)
        text_score = font_30.render('Score : ' + str(floor(self.score/10)), True, func.BLACK)
        func.screen.blit(text_score,(15,15))
        
