import pygame
import settings
from pygame.sprite import Sprite
class Ship():
	def __init__(self,ai_setting,screen):
	
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.image = pygame.image.load('D:\python\\alien\plane.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_setting = ai_setting
		self.ship_left = ai_setting.ship_limit
		"""导入设置的飞船速度"""
		
		#将每搜飞船放在屏幕底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#设置一个参数接收飞船初始的位置并随时更新
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.bottom)
		#设置移动标识
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	def update(self):
		"""更新飞船位置函数"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_setting.ship_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.centerx -= self.ai_setting.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery -= self.ai_setting.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_setting.ship_speed_factor		
		self.rect.centerx = self.centerx
		self.rect.bottom = self.centery
		
	def center_ship(self):
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom
	
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
		
		
		
# screen = pygame.display.set_mode((500,200))	
# pygame.display.flip()
# ship = Ship(screen)
# print(ship.rect,ship.screen_rect)
# print(ship.rect.centerx ,ship.rect.bottom )
# ship.blitme()