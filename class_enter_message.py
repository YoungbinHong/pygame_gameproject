############### import module ###############
import pygame

############### import my module ###############
import function_main as func

############### class enter ###############
class Enter_Message():
    def __init__(self):
        self.message = "Press Enter!"
        self.blink = 0
    
    def draw_components(self):
        self.blink += 1
        if self.blink <= 100:
            font = pygame.font.SysFont('FixedSys',50,True,False)
            text_score = font.render(self.message, True, func.WHITE)
            func.screen.blit(text_score,(func.WINDOW_WIDTH-350,func.WINDOW_HEIGHT-60))
        if self.blink == 200: self.blink = 0