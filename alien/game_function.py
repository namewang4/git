import pygame
import sys
import ship
import bullet
import settings
import alien
from time import sleep
from alien import Alien
"""ship飞船实例统一为ship，设置统一为ai_setting"""
def check_keydown_events(ai_setting,screen,event,ship,bullets,aliens):
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
			new_bullet = bullet.Bullet(ai_setting,screen,ship,aliens)
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

def check_event(ai_setting,screen,ship,bullets,aliens):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(ai_setting,screen,event,ship,bullets,aliens)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
def update_screen(ai_setting,screen,ship,bullets,aliens):
	"""更新屏幕上的图片，并切换新屏幕，这里要用到三个参数"""
	#每次循环时都重绘屏幕
	screen.fill(ai_setting.bg_color)
	ship.update()
	ship.blitme()

	bullets.update(ai_setting,screen,ship,aliens,bullets)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	
	aliens.draw(screen)
	"""在屏幕上画出外星飞船群"""
	for alien in aliens.sprites():
		alien.update()
	
	
	"""更新飞船位置"""
	pygame.display.flip()
	
def update_aliens_ship(ship,aliens):
	"""检查飞船更新为止后是否与飞船有碰撞，如有则结束游戏"""
	if pygame.sprite.spritecollideany(ship,aliens):
		print("游戏结束")
		sleep(0.5)
	"""方法spritecollideany()接受两个实参：一个精灵和一个编组。
	它检查编组是否有成员与精灵发生了碰撞，
	并在找到与精灵发生了碰撞的成员后就停止遍历编组。在这里，它遍历编组aliens
	，并返回它找到的第一个与飞船发生了碰撞的外星人。 如果没有发生碰撞，
	spritecollideany()将返回None，因此Ø处的if代码块不会执行。如果找到了
	与飞船发生碰撞的外星人，它就返回这个外星人，因此if代码块将执行：
	打印“Ship hit!!!”（见）。（有外星人撞到飞船时，需要执行"""
	


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
	
def get_number_aliens_row(ai_setting,alien_height,ship_height):
	"""获取屏幕可以容纳的行数将屏幕高度减去第一行外星人的上边距（外星人高度）、
	飞船的高度以及最初外星人群与飞船的距离（外星人高度的两倍）： """
	available_space_y = (ai_setting.screen_height - 
		alien_height * 3 - ship_height)
	
	number_aliens_y = int(available_space_y/(2 * alien_height))
	return number_aliens_y


def create_alien(ai_setting,screen,aliens,alien_number,row_number):
	#创建外星人函数
	alien = Alien(ai_setting,screen)
	alien_width = alien.rect.width
	alien_x = alien_width + 2 *alien_width * alien_number
	"""设定并记下外星人的 初始位置"""
	alien.rect.x = alien_x
	
	alien_height = alien.rect.height
	alien_y = alien_height + 2 * alien_height * row_number
	"""计算外星人的y坐标，并记下初始位置"""
	alien.rect.y = alien_y
	aliens.add(alien)

def create_fleet(ai_setting,screen,aliens,ship):
	#创建一屏幕行外星人函数
	alien = Alien(ai_setting,screen)
	"""先初始化一个外星人用于获取相关数据"""
	number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
	"""使用函数获取一行外星人列数"""
	number_rows = get_number_aliens_row(ai_setting,alien.rect.height,ship.rect.height)
	"""使用函数获取外星人行数"""
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_setting,screen,aliens,alien_number,row_number)
