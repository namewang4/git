import pygame
import sys
import ship
import bullet
import settings
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
			
def update_screen(ai_setting,screen,ship,bullets,alien):
	"""更新屏幕上的图片，并切换新屏幕，这里要用到三个参数"""
	#每次循环时都重绘屏幕
	screen.fill(ai_setting.bg_color)
	ship.update()
	ship.blitme()
	alien.blitme()
	bullets.update(bullets,ai_setting)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()