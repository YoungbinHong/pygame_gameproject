import pygame
 
def playsound(soundfile):
     
    pygame.init()
    pygame.mixer.init()
    sound= pygame.mixer.Sound(soundfile)
    clock= pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        print("Playing... - func => playsound")
        clock.tick(1000)
 
def playmusic(soundfile):
    pygame.init()
    pygame.mixer.init()
    clock= pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing... - func => playingmusic")
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
             
try:
    initMixer()
    filename= './music/background.ogg'
    playmusic(filename)
except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
    stopmusic()
    print("\nPlay Stopped by user")
except Exception:
    print("unknown error")
     
print("Done")