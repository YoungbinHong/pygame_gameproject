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
        self.current_character = 1 #초기 캐릭터 (첫번째 캐릭터)

        '''#####버튼을 구현할지 그냥 이미지로 노가다할지 견적좀 재보겠읍니다#####

        self.sound_ON_button = pg.image.load('') #사운드 ON 버튼 이미지
        self.sound_OFF_button = pg.image.load('') #사운드 OFF 버튼 이미지
        self.back_to_menu_button = pg.image.load('') #메인 메뉴로 돌아가는 버튼 이미지

        '''
        self.how_to_play = pg.image.load('') #플레이 설명서(이미지에 설명을 넣거나, 배경만 넣고 나중에 글을 적던가)

        ##### 볼륨 설정 창에서 현재 볼륨을 표시해줍니다. ######
        self.fontObj = pygame.font.Font('', )                  # 디렉토리로부터 .ttf 폰트 파일을 로딩한다. 텍스트 크기를 로 한다
        self.show_volume = self.fontObj.render(self.current_volume * 10, True, BLACK)   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
        self.textRectObj = self.show_volume.get_rect();                      # 텍스트 객체의 출력 위치를 가져온다
        self.textRectObj.center = (, )                               # 텍스트 객체의 출력 중심 좌표를 설정한다
        screen.blit(self.show_volume, self.textRectObj)                      # 설정한 위치에 텍스트 객체를 출력한다

    def option_display(self):
        self.key = key_press()
        if self.key != None: print(key); log.write(key+'\n')

        self.current_display = '' # 옵션 초기 화면 (= 볼륨조절 버튼에 위치)
        self.current_volume = 0.6

        ############  이미지는 로직좀 더 보고 임시로 만들어서 시험해보겠습니다 ##################

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
                if self.key == 'ENTER': self.current_display = '' # 옵션 메인(볼륨 조절)으로 돌아가기
                continue

            if self.current_display == '': #캐릭터 선택 화면(초기화면 = 첫번째 캐릭터)
                if self.key == 'UP': self.current_display = '' # 뒤로가기
                if self.key == 'DOWN': self.current_display = '' # 두번째 캐릭터
                if self.key == 'ENTER':
                    self.current_character = 1 #첫번째 캐릭터 선택
                    self.current_display = '' # 옵션 메인(캐릭터 선택)으로 돌아가기
                continue

            if self.current_display == '':  #캐릭터 선택 화면(두번째 캐릭터)
                if self.key == 'UP': self.current_display = '' # 첫번째 캐릭터
                if self.key == 'DOWN': self.current_display = '' # 세번째 캐릭터
                if self.key == 'ENTER':
                    self.current_character = 2 #두번째 캐릭터 선택
                    self.current_display = '' # 옵션 메인(캐릭터 선택)으로 돌아가기
                continue

            if self.current_display == '':  #캐릭터 선택 화면(세번째 캐릭터)
                if self.key == 'UP': self.current_display = '' # 두번째 캐릭터
                if self.key == 'DOWN': self.current_display = '' # 뒤로가기
                if self.key == 'ENTER':
                    self.current_character = 3 # 세번째 캐릭터 선택
                    self.current_display = '' # 옵션 메인(캐릭터 선택)으로 돌아가기
                continue

            if self.current_display == '': #캐릭터 선택 화면(뒤로 가기)
                if self.key == 'UP': self.current_display = '' # 세번째 캐릭터
                if self.key == 'DOWN': self.current_display = '' # 첫번째 캐릭터
                if self.key == 'ENTER': self.current_display = '' # 옵션 메인(캐릭터 선택)으로 돌아가기
                continue

                


        


    def help_display(self):
        self.how_to_play = pg.image.load('./image/help_image.png')
        self.how_to_play = pg.transform.scale(self.how_to_play,(450, 600))
        self.rect = self.how_to_play.get_rect()
        self.rect.center = (300, 400)
        screen.blit(self.how_to_play, self.rect)
