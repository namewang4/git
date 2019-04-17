class Setting():
	"""外星人游戏的所有设置类"""
	def __init__(self):
		"""初始化游戏屏幕的设置，宽度，高度，背景色"""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		"""飞船的移动像素的相关"""
		self.ship_speed_factor = 5
		"""子弹的相关"""
		self.bullet_speed_factor = 2
		self.bullet_width = 5
		self.bullet_height = 10
		self.bullet_color = 140,60,60
		self.bullet_allows = 3
		"""限制子弹的数量"""
		
		self.alien_speed_factor = 2
		"""外星人横向速度"""
		self.fleet_drop_speed = 10
		"""外星人群的下坠速度"""
		self.fleet_direction = 1
		"""外星人的左右方向"""
		