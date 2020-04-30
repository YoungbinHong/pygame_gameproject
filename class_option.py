import pygame as pg #pyamge 모듈 import
from pygame.locals import * #pygame.locals 하위 모듈 import
import keyboard, sys
from class_main import *

class option:
    def __init__(self):
        self.option = ''
        self.color = BLACK
        self.option_image = pg.image.load('') #main에서 구현?
        self.current_display = '' # 옵션 창 초기 이미지
        self.current_volume = 0.6 # 초기 볼륨

        '''#####버튼을 구현할지 그냥 이미지로 노가다할지 견적좀 재보겠읍니다#####

        self.sound_ON_button = pg.image.load('') #사운드 ON 버튼 이미지
        self.sound_OFF_button = pg.image.load('') #사운드 OFF 버튼 이미지
        self.back_to_menu_button = pg.image.load('') #메인 메뉴로 돌아가는 버튼 이미지

        '''
        self.how_to_play = pg.image.load('') #플레이 설명서(이미지에 설명을 넣거나, 배경만 넣고 나중에 글을 적던가)



    def option_display(self):
        self.key = key_press()
        if self.key != None: print(key); log.write(key+'\n')

        self.current_display = '' # 옵션 초기 화면 (= 볼륨조절 버튼에 위치)
        self.current_volume = 0.6

        ############ 볼륨에 따라 self.current_volume * 10 의 숫자를 출력하는 부분도 추가하겠습니다 & 이미지는 로직좀 더 보고 임시로 만들어서 시험해보겠습니다 ##################

        while POWER_SWITCH == True:

            if self.current_display == '': # 볼륨 조절
                if self.key == 'UP': self.current_display = '' # 뒤로가기
                if self.key == 'DOWN': self.current_display = '' # 캐릭터 선택 
                if self.key == 'ENTER': self.current_display = '' # 볼륨 조절 화면
                continue
            
            if self.current_display == '': # 캐릭터 선택
                if self.key == 'UP': self.current_display = '' # 볼륨 조절
                if self.key == 'DOWN': self.current_display = '' # 뒤로가기
                if self.key == 'ENTER': self.current_display = '' # 캐릭터 선택 화면
                continue

            if self.current_display == '': # 뒤로가기
                if self.key == 'UP': self.current_display = '' # 캐릭터 선택
                if self.key == 'DOWN': self.current_display = '' # 볼륨 조절
                if self.key == 'ENTER': self.current_display = '' # 메인 메뉴로 돌아가기
                continue

            if self.current_display == '': # 볼륨 조절 화면 (초기화면 = ON/OFF 조절 ON 버튼)
                if self.key == 'UP': self.current_display = '' # 뒤로가기
                if self.key == 'DOWN': self.current_display = '' # 볼륨 조절
                if self.key == 'ENTER': pygame.mix.music.play() # 음악 ON
                if self.key == 'RIGHT' or 'LEFT': self.current_display = '' # OFF 버튼
                continue

            if self.current_display == '': # 볼륨 조절 화면 (OFF 버튼)
                if self.key == 'UP': self.current_display = '' # 뒤로가기
                if self.key == 'DOWN': self.current_display = '' # 볼륨 조절
                if self.key == 'ENTER': pygame.mix.music.stop() # 음악 OFF
                if self.key == 'RIGHT' or 'LEFT': self.current_display = '' # ON 버튼
                continue

            if self.current_display == '': # 볼륨 조절 화면 (볼륨 작게 버튼)
                if self.key == 'UP': self.current_display = '' # 볼륨 조절
                if self.key == 'DOWN': self.current_display = '' # 뒤로가기
                if self.key == 'ENTER':
                    if self.current_volume == 0.0: # 볼륨이 최소일때는 통과
                        pass
                    else:
                        pygame.mix.music.set_volume(self.current_volume - 0.2)
                if self.key == 'RIGHT' or 'LEFT': self.current_display = '' # 볼륨 크게 버튼
                continue

            if self.current_display == '': # 볼륨 조절 화면 (볼륨 크게 버튼)
                if self.key == 'UP': self.current_display = '' # 볼륨 조절
                if self.key == 'DOWN': self.current_display = '' # 뒤로가기
                if self.key == 'ENTER':
                    if self.current_volume == 1.0: # 볼륨이 최대일때는 통과
                        pass
                    else:
                        pygame.mix.music.set_volume(self.current_volume + 0.2)
                if self.key == 'RIGHT' or 'LEFT': self.current_display = '' # 볼륨 크게 버튼
                continue

            if self.current_display == '': #볼륨 조절 화면(뒤로 가기 버튼)
                if self.key == 'UP': self.current_display = '' # 볼륨 조절 화면(볼륨 작게 버튼)
                if self.key == 'DOWN': self.current_display = '' # 볼륨 조절 화면(OFF)
                if self.key == 'ENTER': self.current_display = '' # 옵션 메인(볼륨 조절)로 돌아가기
                continue


        


    def help_display(self):
        self.how_to_play = pg.image.load('./image/help_image.png')
        self.how_to_play = pg.transform.scale(self.how_to_play,(450, 600))
        self.rect = self.how_to_play.get_rect()
        self.rect.center = (300, 400)
        screen.blit(self.how_to_play, self.rect)
