import pygame
import settings
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_setting,screen):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load('D:\python\\alien\\alien2.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_setting = ai_setting
		
		"""定下外星人位置都在屏幕的左上角附近"""
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#存储外星人的准确位置
		self.x = float(self.rect.x)
	def blitme(self):
		self.screen.blit(self.image,self.rect)