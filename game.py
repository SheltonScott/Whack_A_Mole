import graphics
import unit
from random import *

graphics.init()
pygame.mixer.init()

def startScreen():
	global plane, banner, cloud1, cloud2, cloud3, cloud4, run, clock, play, instance

	instance = -1

	graphics.background = graphics.load("images/sky.jpg")

	cloud1 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))
	graphics.register(cloud1)
	cloud2 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))
	graphics.register(cloud2)

	banner = unit.Banner(530, 120)
	graphics.register(banner)

	play = unit.Play(560, 200)
	graphics.register(play)

	plane = unit.Plane(800, 100)
	graphics.register(plane)

	cloud3 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))
	graphics.register(cloud3)
	cloud4 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))
	graphics.register(cloud4)

	clock = pygame.time.Clock()
	run = True

	while (run):
		clock.tick(30)

		update_graphics()

	pygame.display.flip()

def gameSetup():
	global instance, plane, banner, cloud1, cloud2, cloud3, cloud4, clock, run, plane_sound, pyramid, pyramid2, sphere, sphere2, cone, cone2, cylinder, cylinder2, cube, cube2, blank, option_cloud, option_cloud2, option_cloud3, option_cloud4, correct, yay, stall, crash

	instance = randint(0, 4)

	plane = unit.Plane(800, 100)

	banner = unit.Banner(530, 120)

	cloud1 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))
	cloud2 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))
	cloud3 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))
	cloud4 = unit.Cloud(randrange(0, 1400, 10), randint(0, 600))

def render_graphics():
	#render background
	graphics.background = graphics.load("images/sky.jpg")

	#render background clouds
	graphics.register(cloud1)
	graphics.register(cloud3)

	#render banner
	graphics.register(banner)

	graphics.register(option_cloud)
	graphics.register(option_cloud2)
	graphics.register(option_cloud3)
	graphics.register(option_cloud4)

def update_graphics():
	event.update()

	plane.update()

	banner.update()

def quit(e):
	global run
	if e.type == pygame.QUIT:
		run = False
	elif e.type == pygame.KEYUP:
		if e.key == pygame.K_q:
			run = False

def clear():
	graphics.remove(plane)
	graphics.remove(banner)
	graphics.remove(cloud1)
	graphics.remove(cloud2)
	graphics.remove(cloud3)
	graphics.remove(cloud4)
	graphics.remove(play)

def reset():
	clear()
	gameLoop()

def click(e):
	if e.type == pygame.MOUSEBUTTONDOWN:
		pos = pygame.mouse.get_pos()
		if instance == -1:
			if 560 + 200 > pos[0] > 560 and 200 + 50 > pos[1] > 200:
				reset()
		if instance == 0:
			if 120 + 66 > pos[0] > 120 and 20 + 66 > pos[1] > 20:
				graphics.remove(cube)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				pyramid.moveDown()
				sphere.moveDown()
				pyramid2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(pyramid)
					graphics.remove(sphere)
					graphics.remove(pyramid2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()

import event
event.register(quit)
event.register(click)

def gameLoop():
	gameSetup()
	render_graphics()
	pygame.mixer.music.play(-1)
	while (run):
		clock.tick(30)

		update_graphics()

	pygame.display.flip()

startScreen()

pygame.display.quit()