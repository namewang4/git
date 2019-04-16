import pygame
import sys
import ship
import bullet
import settings
import alien
from alien import Alien
"""ship飞船实例统一为ship，设置统一为ai_setting"""
def check_keydown_events(ai_setting,screen,event,ship,bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
		"""飞船右移"""
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		"""飞船左移"""
	elif event.key == pygame.K_UP:
		ship.moving_up = True
		"""飞船上移"""
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
		"""飞船下移"""
	elif event.key == pygame.K_SPACE:
		if len(bullets) <=ai_setting.bullet_allows:
			new_bullet = bullet.Bullet(ai_setting,screen,ship)
			bullets.add(new_bullet)
			"""新增子弹"""
	elif event.key == pygame.K_q:
		sys.exit()	
	
def check_keyup_events(event,ship):
	"""响应松开按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False		

def check_event(ai_setting,screen,ship,bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(ai_setting,screen,event,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
def update_screen(ai_setting,screen,ship,bullets,aliens):
	"""更新屏幕上的图片，并切换新屏幕，这里要用到三个参数"""
	#每次循环时都重绘屏幕
	screen.fill(ai_setting.bg_color)
	ship.update()
	ship.blitme()
	aliens.draw(screen)
	bullets.update(bullets,ai_setting)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()
	
	
# def create_fleet(ai_setting,screen,aliens):
	# """创建外星人群初始代码，下面为重构后"""
	# #创建一个外星人，并计算一行可容纳多少外星人
	# #外星人间距为外星人宽度
	# alien = Alien(ai_setting,screen)
	# alien_width = alien.rect.width
	# """为避免反复访问rect,将这个值赋值给alien_width"""
	# available_space_x = ai_setting.screen_width - alien_width * 2
	# """可用宽度为屏幕宽带减去两个外星人宽度，留白"""
	# number_aliens_x = int(available_space_x/(2 * alien_width))
	# """一行可以放的外星人等于可用宽度除以两倍外星人宽度（间距为外星人宽带）"""
	# for alien_number in range(number_aliens_x):
		# alien = Alien(ai_setting,screen)
		# alien.rect.x = alien_width + 2 *alien_width * alien_number
		# """设置外星人的横坐标"""
		# aliens.add(alien)
		
		
		
def get_number_aliens_x(ai_setting,alien_width):
	"""获取每行可容纳的外星人函数"""
	available_space_x = ai_setting.screen_width - alien_width * 2
	"""可用宽度为屏幕宽带减去两个外星人宽度，留白"""
	number_aliens_x = int(available_space_x/(2 * alien_width))
	"""一行可以放的外星人等于可用宽度除以两倍外星人宽度（间距为外星人宽带）"""
	return number_aliens_x

def create_alien(ai_setting,screen,aliens,alien_number):
	alien = Alien(ai_setting,screen)
	alien_width = alien.rect.width
	alien_x = alien_width + 2 *alien_width * alien_number
	"""设定并记下外星人的 初始位置"""
	alien.rect.x = alien_x
	aliens.add(alien)

def create_fleet(ai_setting,screen,aliens):
	alien = Alien(ai_setting,screen)
	number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
	
	#创建一行外星人
	for alien_number in range(number_aliens_x):
		create_alien(ai_setting,screen,aliens,alien_number)
