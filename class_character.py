import pygame
from class_main import *

class character:
    def __init__(self):
        self.create()
        self.color = BLACK

    def create(self):
        self.length = 5
        self.positions = [(WINDOW_WIDTH/2),0]
    