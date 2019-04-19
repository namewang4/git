import pygame
from pygame.sprite import Sprite
import settings
import math 
import game_function as gf
class Bullet(Sprite):
	"""一个对子弹进行管理的类"""
	def __init__(self,ai_setting,screen,ship,aliens):
		"""在飞船位置创建一个子弹对象，调用三个参数,aliens
		参数用于检测碰撞"""
		super().__init__()
		"""继承Sprite类"""
		self.screen = screen
		#在0,0 处用pygame的Rect方法实例化一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.a = ship.rect.centerx
		self.rect.bottom = ship.rect.top
		self.y = float(self.rect.y)
		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor
		self.xx = 0
		
	def update(self,ai_setting,screen,ship,aliens,bullets):
		"""通过更新self.y展现向上移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y
		
		
		self.rect.x = math.sin(self.xx) * 100 + self.a
		self.xx += 0.05
		"""螺旋轨迹子弹"""
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
				print(len(bullets))
		#检查是否有子弹击中了飞船，如果有删除飞船
		collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
		if len(aliens) < 10 :
			gf.create_fleet(ai_setting,screen,aliens,ship)

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
		