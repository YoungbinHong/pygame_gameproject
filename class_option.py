import pygame as pg #pyamge 모듈 import
from pygame.locals import * #pygame.locals 하위 모듈 import
import keyboard
from class_main import *

class option:
    def __init__(self):
        self.option = ''
        self.color = BLACK
        self.option_image = pg.image.load('') #main에서 구현?

        self.background = pg.image.load('') #배경 이미지
        self.sound_ON_button = pg.image.load('') #사운드 ON 버튼 이미지
        self.sound_OFF_button = pg.image.load('') #사운드 OFF 버튼 이미지
        self.back_to_menu_button = pg.image.load('') #메인 메뉴로 돌아가는 버튼 이미지
        self.how_to_play = pg.image.load('') #플레이 설명서(이미지에 설명을 넣거나, 배경만 넣고 나중에 글을 적던가)
        
        self.LEFT = 1
        self.RIGHT = 3



    def mouse_event(self): #마우스 처리 -> 다른 메서드에 넣을수도
        if event.type == MOUSEBUTTONDOWN and event.botton == self.LEFT:
            pass #마우스 왼쪽 클릭
        elif event.type == MOUSEBUTTONUP and event.botton == self.LEFT:
            pass #마우스 왼쪽 뗄때
        elif event.type == MOUSEBUTTONDOWN and event.botton == self.RIGHT:
            pass #마우스 오른쪽 클릭
        elif event.type == MOUSEBUTTONUP and event.botton == self.RIGHT:
            pass #마우스 오른쪽 뗄때
        elif event.type == pg.MOUSEMOTION:
            pass #마우스 이동

    def sound_ONOFF(self): # 사운드 ON/OFF
        pass