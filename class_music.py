############### import module ###############
import pygame
from pygame import mixer

############### class music ###############
class Music():
    def __init__(self,path):
        self.path = path
    
    def play_once(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()
    
    def play_inf(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play(-1)

    def off(self):
        pygame.mixer.music.stop()