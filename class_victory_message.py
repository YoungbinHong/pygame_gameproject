############### import module ###############
import pygame

############### import my module ###############
import function_main as func

############### class victory message ###############
class Victory_Message():
    def __init__(self,x,y,width,height,image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.median = ((func.WINDOW_WIDTH-self.width)/2,(func.WINDOW_HEIGHT-self.height)/2)
        self.image = pygame.image.load(image)

    def draw_components(self,screen):
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        screen.blit(self.image,self.median)