import pygame, sys
from pygame.locals import *
from pygame import mixer

sound_on = True
move = False
hit = False
game_over = False
'''
class Music:
    def __init__(self, sound_on = False):
        self.sound_on = sound_on
        
        if sound_on:
            self.sample = { "hit" : pygame.mixer.Sound("./music/hit.ogg"),
                            "move" : pygame.mixer.Sound("./music/move.wav")
                            "game_over" : pygame.mixer.Sound("./game over.ogg")

    def play_sample(self,name):
        if self.sound_on:
            self.sample[name].play()

    def play_music
'''
def hit(soundfile):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    sound= pygame.mixer.Sound(hit_sound)
    sound.play()
    while pygame.mixer.get_busy():
        print("hit!")
        clock.tick(1000)

def move(soundfile):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    sound= pygame.mixer.Sound(moving_sound)
    sound.play()
    while pygame.mixer.get_busy():
        print("move!")
        clock.tick(1000)
 
def playmusic(soundfile):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():
        print("Playing BGM")
        clock.tick(1000)

def game_over(soundfile):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    sound= pygame.mixer.Sound(end)
    sound.play()
    while pygame.mixer.get_busy():
        print("game_over")
        clock.tick(1000)
        
def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()
 
def getmixerargs():
    pygame.mixer.init()
    freq, size, chan= pygame.mixer.get_init()
    return freq, size, chan

 
def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN= getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN,BUFFER)



while sound_on == True:
    initMixer()
    background = './music/background.ogg'
    playmusic(background)

if move == True:
    initMixer()
    moving_sound = './music/move.wav'
    move(moving_sound)
    
if hit == True:
    initMixer()
    hit_sound = './music/hit.ogg'
    hit(hit_sound)
    
if game_over == True:
    initMixer()
    end = './music/game over.ogg'
    game_over(gameover)

