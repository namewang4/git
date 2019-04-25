import pygame

class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self,ai_setting):
		"""初始化游戏的统计信息"""
		self.ai_setting = ai_setting
		self.ship_over = False
		self.reset_stats()
		
		"""在这个游戏运行期间，我们只创建一个GameStats实例，
		但每当玩家开始新游戏时，需要重置一些统计信息。为此，
		我们在方法reset_stats()中初始化大部分统计信息，
		而不是在__init__()中直接初始化它们。我们在__init__()
		中调用这个方法，这样创建GameStats实例时将妥善地设置这
		些统计信息（见Ø），同时在玩家开始新游戏时也能调用reset_stats()"""
		
		
	def reset_stats(self):
		"""初始化在游戏运行期间可能重置的信息"""
		self.ship_left = self.ai_setting.ship_limit