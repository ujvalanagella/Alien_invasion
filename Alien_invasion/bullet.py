import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	'''A class to manage the ship.'''
	def __init__(self,ai_game):
		'''Initialization the ship and set its starting position.'''
		super().__init__()
		self.screen = ai_game.screen
		self.setting = ai_game.setting
		self.color = self.setting.bullet_color

		#Create a bullet rect at (0,0) and then set correct position.
		self.rect = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		#Store the bullet's position as a decimal value.
		self.y=float(self.rect.y)
		
	def update(self):
		'''Move the bullet up the screen.'''
		#Update the decimal position of the bullet.
		self.y-=self.setting.bullet_speed
		# Update the rect position
		self.rect.y=self.y

	def draw_bullet(self):
		'''Draw the ship at its current location.'''
		pygame.draw.rect(self.screen,self.color,self.rect)

