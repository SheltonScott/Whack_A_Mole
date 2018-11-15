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

class Crashed_Plane(unit):
	def __init__(self, x, y):
		super(Crashed_Plane, self).__init__(x, y)
		self.spritesheet = graphics.load("images/crashed_plane.png")
		self.mapping = {
				"crashed" : [(0, 0, 200, 200) for i in range(1)],
		}
		self.facing = "crashed"
		self.speed = 1

	def update(self):
		self.frame = (self.frame + self.speed) % 1

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 200, 150),
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

class Cloud(unit):
	def __init__(self, x, y):
		super(Cloud, self).__init__(x, y)
		self.spritesheet = graphics.load("images/cloud.png")
		self.mapping = {
				"cloud" : [(0, 0, 298, 123) for i in range(1)],
		}
		self.facing = "cloud"
		self.speed = .2

	def update(self):
		self.frame = (self.frame + self.speed) % 1
		if self.x >= -299:
			self.x -= 10
		if self.x == -300:
			self.x = 1400
			self.y = randint(0, 600)

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 298, 123),
						self.mapping[self.facing][int(self.frame)])

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Banner(unit):
	def __init__(self, x, y):
		super(Banner, self).__init__(x, y)
		self.spritesheet = graphics.load("images/moving_banner.png")
		self.mapping = {
				"banner" : [(302 * i, 0, 302, 202) for i in range(2)],
		}
		self.facing = "banner"
		self.speed = .2

	def update(self):
		self.frame = (self.frame + self.speed) % 2

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 302, 202),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Cube(unit):
	def __init__(self, x, y):
		super(Cube, self).__init__(x, y)
		self.spritesheet = graphics.load("images/cube.png")
		self.mapping = {
				"cube" : [(66 * i, 0, 66, 66) for i in range(60)],
		}
		self.facing = "cube"
		self.speed = .5

	def update(self):
		self.frame = (self.frame + self.speed) % 60

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 66, 66),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Sphere(unit):
	def __init__(self, x, y):
		super(Sphere, self).__init__(x, y)
		self.spritesheet = graphics.load("images/sphere.png")
		self.mapping = {
				"sphere" : [(66 * i, 0, 66, 66) for i in range(60)],
		}
		self.facing = "sphere"
		self.speed = .5

	def update(self):
		self.frame = (self.frame + self.speed) % 60

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 66, 66),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Pyramid(unit):
	def __init__(self, x, y):
		super(Pyramid, self).__init__(x, y)
		self.spritesheet = graphics.load("images/pyramid.png")
		self.mapping = {
				"pyramid" : [(66 * i, 0, 66, 66) for i in range(60)],
		}
		self.facing = "pyramid"
		self.speed = .5

	def update(self):
		self.frame = (self.frame + self.speed) % 60

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 66, 66),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Cylinder(unit):
	def __init__(self, x, y):
		super(Cylinder, self).__init__(x, y)
		self.spritesheet = graphics.load("images/cylinder.png")
		self.mapping = {
				"cylinder" : [(66 * i, 0, 66, 66) for i in range(60)],
		}
		self.facing = "cylinder"
		self.speed = .5

	def update(self):
		self.frame = (self.frame + self.speed) % 60

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 66, 66),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Cone(unit):
	def __init__(self, x, y):
		super(Cone, self).__init__(x, y)
		self.spritesheet = graphics.load("images/cone.png")
		self.mapping = {
				"cone" : [(66 * i, 0, 66, 66) for i in range(60)],
		}
		self.facing = "cone"
		self.speed = .5

	def update(self):
		self.frame = (self.frame + self.speed) % 60

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 66, 66),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Blank(unit):
	def __init__(self, x, y):
		super(Blank, self).__init__(x, y)
		self.spritesheet = graphics.load("images/blank.png")
		self.mapping = {
				"blank" : [(0, 0, 64, 64) for i in range(60)],
		}
		self.facing = "blank"
		self.speed = .5

	def update(self):
		self.frame = (self.frame + self.speed) % 60

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 64, 64),
						self.mapping[self.facing][int(self.frame)])

	def moveDown(self):
		self.y += 100

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400

class Play(unit):
	def __init__(self, x, y):
		super(Play, self).__init__(x, y)
		self.spritesheet = graphics.load("images/play.png")
		self.mapping = {
				"play" : [(0, 0, 200, 50) for i in range(1)],
		}
		self.facing = "play"
		self.speed = .2

	def update(self):
		self.frame = (self.frame + self.speed) % 1

	def render(self, surface):
		surface.blit(self.spritesheet,
						(self.x, self.y, 200, 50),
						self.mapping[self.facing][int(self.frame)])

	# def handler(self, event):
	# 	if self.x > 0:
	# 		self.x -= 20
	# 		if self.x < 0:
	# 			self.x = 1400