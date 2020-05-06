############### import module ###############
import pygame

############### import my module ###############
import function_main as func

############### class restart ###############
class Restart_Message():
    def __init__(self):
        self.message = "Press R to restart game!"
        self.blink = 0
    
    def draw_components(self,other):
        self.blink += 1
        if self.blink <= 50:
            font = pygame.font.SysFont('FixedSys',50,True,False)
            text_score = font.render(self.message, True, func.WHITE)
            func.screen.blit(text_score,(func.WINDOW_WIDTH/3-30,func.WINDOW_HEIGHT/2+100))
        if self.blink == 100: self.blink = 0