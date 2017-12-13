import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


# 主程序
def run_game():
    # pygame必须初始化才能使用
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen,ai_settings)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        #监视键盘和鼠标事件
        #关闭游戏
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,ship,aliens)


        gf.update_screen(ai_settings,screen,ship,aliens,bullets)






run_game()