import pygame
import graphics
from random import *

class unit(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.frame = 0.0

class Plane(unit):
	def __init__(self, x, y):
		super(Plane, self).__init__(x, y)
		self.spritesheet = graphics.load("images/plane.png")
		self.mapping = {
				"flying" : [(300 * i, 0, 300, 200) for i in range(2)],
		}
		self.facing = "flying"
		self.speed = 1

	def update(self):
		self.frame = (self.frame + self.speed) % 2

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 256, 256),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	def crashing(self):
		if self.y == 400:
			return True

	# def handler(self, event):
	# 	if event.type == pygame.KEYDOWN:
	# 		if event.key == pygame.K_SPACE:
	# 			pygame.mixer.Sound.play(self.boost_sound)