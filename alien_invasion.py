import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from game_stats import GameStats


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的示例
    stats = GameStats(ai_settings)

    """创建一艘飞船、一个子弹编组、一个外星人编组"""
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    """开始游戏的主循环"""
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            """若游戏处于激活状态，更新飞船位置/子弹/外星人"""
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)
        # 刷新主屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
