import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WHITE = (255,255,255)
BLACK = (0,0,0)

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Super Action Hero')
    