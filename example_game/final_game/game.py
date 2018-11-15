import pygame
import graphics
import unit
from random import *

background = None
plane = None
banner = None
cloud1 = None
cloud2 = None
cloud3 = None
cloud4 = None
run = None
clock = None
instance = None
plane_sound = None
thunderstorm = None
pyramid = None
pyramid2 = None
sphere = None
sphere2 = None
cone = None
cone2 = None
cylinder = None
cylinder2 = None
cube = None
cube2 = None
blank = None
option_cloud = None
option_cloud2 = None
option_cloud3 = None
option_cloud4 = None
correct = None
yay = None
stall = None
crash = None
play = None

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

def endScreen():
	global plane, run, clock, play, instance

	instance = -1

	graphics.background = graphics.load("images/grassy_hill.jpg")

	play = unit.Play(560, 200)
	graphics.register(play)

	plane = unit.Crashed_Plane(800, 300)
	graphics.register(plane)

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

	if instance == 0:
		pyramid = unit.Pyramid(550, 190)
		sphere = unit.Sphere(600, 190)
		pyramid2 = unit.Pyramid(650, 190)

		cube = unit.Cube(120, 20)
		sphere2 = unit.Sphere(450, 20)
		cone = unit.Cone(770, 20)
		cylinder = unit.Cylinder(1100, 20)

	if instance == 1:
		cone = unit.Cone(550, 190)
		cylinder = unit.Cylinder(600, 190)
		cone2 = unit.Cone(650, 190)

		sphere = unit.Sphere(120, 20)
		cube = unit.Cube(450, 20)
		pyramid = unit.Pyramid(770, 20)
		cylinder2 = unit.Cylinder(1100, 20)

	if instance == 2:
		cylinder = unit.Cylinder(550, 190)
		cube = unit.Cube(600, 190)
		cylinder2 = unit.Cylinder(650, 190)

		sphere = unit.Sphere(120, 20)
		cone = unit.Cone(450, 20)
		cube2 = unit.Cube(770, 20)
		pyramid = unit.Pyramid(1100, 20)

	if instance == 3:
		cube = unit.Cube(550, 190)
		pyramid = unit.Pyramid(600, 190)
		cube2 = unit.Cube(650, 190)

		pyramid2 = unit.Pyramid(120, 20)
		cone = unit.Cone(450, 20)
		sphere = unit.Sphere(770, 20)
		cylinder = unit.Cylinder(1100, 20)

	if instance == 4:
		sphere = unit.Sphere(550, 190)
		cone = unit.Cone(600, 190)
		sphere2 = unit.Sphere(650, 190)

		cube = unit.Cube(120, 20)
		cone2 = unit.Cone(450, 20)
		pyramid = unit.Pyramid(770, 20)
		cylinder = unit.Cylinder(1100, 20)

	option_cloud = unit.Cloud(0, 0)
	option_cloud2 = unit.Cloud(330, 0)
	option_cloud3 = unit.Cloud(650, 0)
	option_cloud4 = unit.Cloud(980, 0)

	blank = unit.Blank(700, 190)
	
	plane_sound = pygame.mixer.music.load("sounds/plane_sound.wav")
	pygame.mixer.music.set_volume(.3)

	yay = pygame.mixer.Sound("sounds/yay.wav")
	yay.set_volume(1)

	stall = pygame.mixer.Sound("sounds/no_dear.wav")
	stall.set_volume(1)

	crash = pygame.mixer.Sound("sounds/crash.wav")
	crash.set_volume(1)
	
	clock = pygame.time.Clock()
	run = True

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

	#render pattern
	if instance == 0:
		graphics.register(pyramid)
		graphics.register(sphere)
		graphics.register(pyramid2)

		graphics.register(cube)
		graphics.register(sphere2)
		graphics.register(cone)
		graphics.register(cylinder)

	if instance == 1:
		graphics.register(cone)
		graphics.register(cylinder)
		graphics.register(cone2)

		graphics.register(sphere)
		graphics.register(cylinder2)
		graphics.register(pyramid)
		graphics.register(cube)

	if instance == 2:
		graphics.register(cylinder)
		graphics.register(cube)
		graphics.register(cylinder2)

		graphics.register(sphere)
		graphics.register(cone)
		graphics.register(cube2)
		graphics.register(pyramid)

	if instance == 3:
		graphics.register(cube)
		graphics.register(pyramid)
		graphics.register(cube2)

		graphics.register(pyramid2)
		graphics.register(cone)
		graphics.register(sphere)
		graphics.register(cylinder)

	if instance == 4:
		graphics.register(sphere)
		graphics.register(cone)
		graphics.register(sphere2)

		graphics.register(cube)
		graphics.register(cone2)
		graphics.register(pyramid)
		graphics.register(cylinder)

	graphics.register(blank)

	#render plane
	graphics.register(plane)

	#render clouds
	graphics.register(cloud2)
	graphics.register(cloud4)

def update_graphics():
	event.update()

	plane.update()

	banner.update()

	if instance == 0:
		pyramid.update()
		sphere.update()
		pyramid2.update()

		cube.update()
		sphere2.update()
		cone.update()
		cylinder.update()

	if instance == 1:
		cone.update()
		cylinder.update()
		cone2.update()

		sphere.update()
		cylinder2.update()
		pyramid.update()
		cube.update()

	if instance == 2:
		cylinder.update()
		cube.update()
		cylinder2.update()

		sphere.update()
		cone.update()
		cube2.update()
		pyramid.update()

	if instance == 3:
		cube.update()
		pyramid.update()
		cube2.update()

		pyramid2.update()
		cone.update()
		sphere.update()
		cylinder.update()

	if instance == 4:
		sphere.update()
		cone.update()
		sphere2.update()

		cube.update()
		cone2.update()
		pyramid.update()
		cylinder.update()

	cloud1.update()
	cloud2.update()
	cloud3.update()
	cloud4.update()

	graphics.update()

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

	if instance == 0:
		graphics.remove(pyramid)
		graphics.remove(sphere)
		graphics.remove(pyramid2)
		graphics.remove(option_cloud)
		graphics.remove(option_cloud2)
		graphics.remove(option_cloud3)
		graphics.remove(option_cloud4)
		graphics.remove(cube)
		graphics.remove(sphere2)
		graphics.remove(cone)
		graphics.remove(cylinder)
		graphics.remove(blank)
	if instance == 1:
		graphics.remove(cone)
		graphics.remove(cylinder)
		graphics.remove(cone2)
		graphics.remove(option_cloud)
		graphics.remove(option_cloud2)
		graphics.remove(option_cloud3)
		graphics.remove(option_cloud4)
		graphics.remove(cube)
		graphics.remove(sphere)
		graphics.remove(pyramid)
		graphics.remove(cylinder2)
		graphics.remove(blank)
	if instance == 2:
		graphics.remove(cylinder)
		graphics.remove(cube)
		graphics.remove(cylinder2)
		graphics.remove(option_cloud)
		graphics.remove(option_cloud2)
		graphics.remove(option_cloud3)
		graphics.remove(option_cloud4)
		graphics.remove(cube2)
		graphics.remove(sphere)
		graphics.remove(pyramid)
		graphics.remove(cone)
		graphics.remove(blank)
	if instance == 3:
		graphics.remove(cube)
		graphics.remove(pyramid)
		graphics.remove(cube2)
		graphics.remove(option_cloud)
		graphics.remove(option_cloud2)
		graphics.remove(option_cloud3)
		graphics.remove(option_cloud4)
		graphics.remove(pyramid2)
		graphics.remove(sphere)
		graphics.remove(cylinder)
		graphics.remove(cone)
		graphics.remove(blank)
	if instance == 4:
		graphics.remove(sphere)
		graphics.remove(cone)
		graphics.remove(sphere2)
		graphics.remove(option_cloud)
		graphics.remove(option_cloud2)
		graphics.remove(option_cloud3)
		graphics.remove(option_cloud4)
		graphics.remove(cone2)
		graphics.remove(pyramid)
		graphics.remove(cylinder)
		graphics.remove(cube)
		graphics.remove(blank)

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
			elif 450 + 66 > pos[0] > 450 and 20 + 66 > pos[1] > 20:
				graphics.remove(sphere2)
				pygame.mixer.Sound.play(yay)
				reset()
			elif 770 + 66 > pos[0] > 770 and 20 + 66 > pos[1] > 20:
				graphics.remove(cone)
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
			elif 1100 + 66 > pos[0] > 1100 and 20 + 66 > pos[1] > 20:
				graphics.remove(cylinder)
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
		
		if instance == 1:
			if 120 + 66 > pos[0] > 120 and 20 + 66 > pos[1] > 20:
				graphics.remove(sphere)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cone.moveDown()
				cylinder.moveDown()
				cone2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cone)
					graphics.remove(cylinder)
					graphics.remove(cone2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 450 + 66 > pos[0] > 450 and 20 + 66 > pos[1] > 20:
				graphics.remove(cube)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cone.moveDown()
				cylinder.moveDown()
				cone2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cone)
					graphics.remove(cylinder)
					graphics.remove(cone2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 770 + 66 > pos[0] > 770 and 20 + 66 > pos[1] > 20:
				graphics.remove(pyramid)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cone.moveDown()
				cylinder.moveDown()
				cone2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cone)
					graphics.remove(cylinder)
					graphics.remove(cone2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 1100 + 66 > pos[0] > 1100 and 20 + 66 > pos[1] > 20:
				graphics.remove(cylinder2)
				pygame.mixer.Sound.play(yay)
				reset()
		if instance == 2:
			if 120 + 66 > pos[0] > 120 and 20 + 66 > pos[1] > 20:
				graphics.remove(sphere)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cylinder.moveDown()
				cube.moveDown()
				cylinder2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cylinder)
					graphics.remove(cube)
					graphics.remove(cylinder2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 450 + 66 > pos[0] > 450 and 20 + 66 > pos[1] > 20:
				graphics.remove(cone)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cylinder.moveDown()
				cube.moveDown()
				cylinder2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cylinder)
					graphics.remove(cube)
					graphics.remove(cylinder2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 770 + 66 > pos[0] > 770 and 20 + 66 > pos[1] > 20:
				graphics.remove(cube2)
				pygame.mixer.Sound.play(yay)
				reset()
			elif 1100 + 66 > pos[0] > 1100 and 20 + 66 > pos[1] > 20:
				graphics.remove(pyramid)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cylinder.moveDown()
				cube.moveDown()
				cylinder2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cylinder)
					graphics.remove(cube)
					graphics.remove(cylinder2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
		
		if instance == 3:
			if 120 + 66 > pos[0] > 120 and 20 + 66 > pos[1] > 20:
				graphics.remove(pyramid2)
				pygame.mixer.Sound.play(yay)
				reset()
			elif 450 + 66 > pos[0] > 450 and 20 + 66 > pos[1] > 20:
				graphics.remove(cone)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cube.moveDown()
				pyramid.moveDown()
				cube2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cube)
					graphics.remove(pyramid)
					graphics.remove(cube2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 770 + 66 > pos[0] > 770 and 20 + 66 > pos[1] > 20:
				graphics.remove(sphere)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cube.moveDown()
				pyramid.moveDown()
				cube2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cube)
					graphics.remove(pyramid)
					graphics.remove(cube2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 1100 + 66 > pos[0] > 1100 and 20 + 66 > pos[1] > 20:
				graphics.remove(cylinder)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				cube.moveDown()
				pyramid.moveDown()
				cube2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(cube)
					graphics.remove(pyramid)
					graphics.remove(cube2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()

		elif instance == 4:
			if 120 + 66 > pos[0] > 120 and 20 + 66 > pos[1] > 20:
				graphics.remove(cube)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				sphere.moveDown()
				cone.moveDown()
				sphere2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(sphere)
					graphics.remove(cone)
					graphics.remove(sphere2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 450 + 66 > pos[0] > 450 and 20 + 66 > pos[1] > 20:
				graphics.remove(cone2)
				pygame.mixer.Sound.play(yay)
				reset()
			elif 770 + 66 > pos[0] > 770 and 20 + 66 > pos[1] > 20:
				graphics.remove(pyramid)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				sphere.moveDown()
				cone.moveDown()
				sphere2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(sphere)
					graphics.remove(cone)
					graphics.remove(sphere2)
					graphics.remove(blank)
					pygame.mixer.music.stop()
					pygame.mixer.Sound.play(crash)
					clear()
					endScreen()
			elif 1100 + 66 > pos[0] > 1100 and 20 + 66 > pos[1] > 20:
				graphics.remove(cylinder)
				pygame.mixer.Sound.play(stall)
				plane.moveDown()
				banner.moveDown()
				sphere.moveDown()
				cone.moveDown()
				sphere2.moveDown()
				blank.moveDown()
				if plane.crashing():
					graphics.remove(plane)
					graphics.remove(banner)
					graphics.remove(sphere)
					graphics.remove(cone)
					graphics.remove(sphere2)
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