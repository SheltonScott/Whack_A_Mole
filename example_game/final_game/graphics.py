import pygame

width = 1400
height = 600
assets = {}
renderables = []
background = None
screen = None
x = 0
y = 0

# x1 = width
# y1 = 0

def update():
	global screen, background, renderables, width, height, x, y, x1, y1

	# x1 -= 25
	# x -= 25

	screen.fill((0,0,0))

	if background:
		screen.blit(background, ((x, y, width, height)))
		# screen.blit(background, ((x1, y1, width, height)))
		# if x < -width:
		# 	x = width
		# if x1 < -width:
		# 	x1 = width

	for r in renderables:
		r.render(screen)

	pygame.display.flip()

def register(renderable):
	global renderables
	if renderable not in renderables:
		renderables.append(renderable)

def remove(renderable):
	global renderables
	if renderable in renderables:
		renderables.remove(renderable)

def init():
	global screen
	pygame.display.init()
	screen = pygame.display.set_mode((width, height))

def load(file):
	global assets
	if file in assets:
		return assets[file]
	else:
		image = pygame.image.load(file)
		assets[file] = image
		return image