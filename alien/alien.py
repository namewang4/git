import pygame
import settings
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_setting,screen):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load('D:\python\\alien\\alien2.jpg')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_setting = ai_setting
		self.speed_factor = ai_setting.alien_speed_factor
		self.fleet_direction = ai_setting.fleet_direction
		self.fleet_drop_speed = ai_setting.fleet_drop_speed
		"""定下外星人位置都在屏幕的左上角附近"""
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#存储外星人的准确位置
		self.x = float(self.rect.x)
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	# def update1(self):
		# if self.rect.right >= self.screen_rect.right:
			# self.fleet_direction *= -1
			# self.rect.y += self.fleet_drop_speed
		# if self.rect.left <= 0:
			# self.fleet_direction *= -1
			# self.rect.y += self.fleet_drop_speed
			
	def update(self):
		# if alien.check_edges():
			# self.fleet_direction *= -1
			# self.rect.y += self.fleet_drop_speed
		self.rect.x +=(self.speed_factor * self.fleet_direction)
		if self.rect.right >= self.screen_rect.right:
			self.fleet_direction *= -1
			self.rect.y += self.fleet_drop_speed
		if self.rect.left <= 0:
			self.fleet_direction *= -1
			self.rect.y += self.fleet_drop_speed
	

	# def updata(self):
		# # if alien.check_edges():
			# # self.fleet_direction *= -1
			# # self.rect.y += self.fleet_drop_speed
		# self.rect.x +=(self.speed_factor * self.fleet_direction)
	