############### import module ###############
import pygame

############### import my module ###############
import function_main as func

############### class Moving Background ###############
class Moving_Background():
    def __init__(self, image):
        self.background = pygame.image.load(image)   # background display
        self.background_copy = self.background.copy()       
        self.background_x = 0
        self.background_copy_x = 1200
    
    def move(self):
        self.background_x -= 2
        self.background_copy_x -= 2

        if self.background_x == -1 * func.WINDOW_WIDTH:
            self.background_x = func.WINDOW_WIDTH
        
        if self.background_copy_x == -1 * func.WINDOW_WIDTH:
            self.background_copy_x = func.WINDOW_WIDTH

        self.background = pygame.transform.scale(self.background,(func.WINDOW_WIDTH,func.WINDOW_HEIGHT))
        func.screen.blit(self.background,(self.background_x,0))
        func.screen.blit(self.background_copy,(self.background_copy_x,0))
        
