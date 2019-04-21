import pygame
#from pygame.sprite import Group
import sys
from ship import Ship
from alien import Alien
import alien
from settings import Setting
from game_stats import GameStats
import game_function as gf
import bullet
from alien import Alien

#通过导入模块 便于日和维护
def run_game():
	#初始化一个游戏，并创建一个屏幕对象通过导入设置类Setting
	pygame.init()
	ai_setting = Setting()
	"""通过导入的设置模块初始化屏幕实例"""
	screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption("外星人")
	ship = Ship(ai_setting,screen)
	"""通过ship模块实例化飞船"""
	bullets = pygame.sprite.Group()
	"""实例化子弹集"""
	aliens = pygame.sprite.Group()
	"""实例化外星人集"""
	stats = GameStats(ai_setting)
	"""实例化游戏状态类"""
	
	gf.create_fleet(ai_setting,screen,aliens,ship)
	
	while True:
		"""游戏主循环，监控游戏的事件及刷新屏幕交给两个函数"""
		gf.check_event(ai_setting,screen,ship,bullets,aliens)

		gf.update_screen(ai_setting,screen,ship,bullets,aliens)
		gf.update_aliens_ship(ship,aliens)
		"""检查飞船是否碰到飞机，碰到就结束游戏"""
run_game()



