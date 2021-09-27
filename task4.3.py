import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 600))
screen.fill((255, 255, 255))
def fon(x, y):
  rect(screen, (128, 128, 0), (x, y, 1000, 300))
  rect(screen, (184, 134, 11), (x, y+300, 1000, 300))
  
def klubok(x, y, r):	
	circle(screen, (128, 128, 128), (x, y), r)
	circle(screen, (0, 0, 0), (x, y), r, 1)
	arc(screen, (0, 0, 0), (x-r, y-r, 4*r, 4*r), 19*np.pi/32, 29*np.pi/32)
	arc(screen, (0, 0, 0), (x-r, y-r/2, 4*r, 4*r), 17*np.pi/32, 55*np.pi/64)
	arc(screen, (0, 0, 0), (x-r, y, 4*r, 4*r), 4*np.pi/8, 13*np.pi/16)
	

def okno(x, y):
	rect(screen, (99, 66, 33), (x, y, 180, 220))
	rect(screen, (0, 0, 0), (x, y, 180, 220), 1)
	
	rect(screen, (0, 250, 154), (x+20, y+20, 60, 80))
	rect(screen, (0, 0, 0), (x+20, y+20, 60, 80), 1)

	rect(screen, (0, 250, 154), (x+100, y+20, 60, 80))
	rect(screen, (0, 0, 0), (x+100, y+20, 60, 80), 1)

	rect(screen, (0, 250, 154), (x+20, y+120, 60, 80))
	rect(screen, (0, 0, 0), (x+20, y+120, 60, 80), 1)

	rect(screen, (0, 250, 154), (x+100, y+120, 60, 80))
	rect(screen, (0, 0, 0), (x+100, y+120, 60, 80), 1)

def cat(screen, x, y, k, color):	
	surf = pygame.Surface((k*20, k*57))
	surf.fill((255, 255, 255))
	surf.set_colorkey((255, 255, 255))
	bigger = pygame.Rect(0, 0, k*20, k*57)
	ellipse(surf, color, bigger)
	ellipse(surf, (0, 0, 0), bigger, 1)
	rotatedSurf = pygame.transform.rotate(surf, 75)
	screen.blit(rotatedSurf, (x+k*120, y-k*45))

	ellipse(screen, color, (x+k*40, y-k*60, k*90, k*50)) #тело
	ellipse(screen, (0, 0, 0), (x+k*40, y-k*60, k*90, k*50), 1)
	
	circle(screen, color, (x+k*30, y-k*40), k*20) #голова
	circle(screen, (0, 0, 0), (x+k*30, y-k*40), k*20, 1)
	
	ellipse(screen, color, (x+k*40, y-k*23, k*28, k*15)) #нога 2
	ellipse(screen, (0, 0, 0), (x+k*40, y-k*23, k*28, k*15), 1)
	
	ellipse(screen, color, (x+k*100, y-k*23, k*28, k*15)) #нога 1
	ellipse(screen, (0, 0, 0), (x+k*100, y-k*23, k*28, k*15), 1)
	
	circle(screen, (0, 255, 0), (x+k*19, y-k*40), k*5) #глаза
	circle(screen, (0, 0, 0), (x+k*19, y-k*40), k*5, 1)
	ellipse(screen, (0, 0, 0), (x+k*18, y-k*45, k*2, k*10))
	circle(screen, (0, 255, 0), (x+k*41, y-k*40), k*5)
	circle(screen, (0, 0, 0), (x+k*41, y-k*40), k*5, 1)
	ellipse(screen, (0, 0, 0), (x+k*40, y-k*45, k*2, k*10))

	polygon(screen, (0, 0, 0), [(x+k*37, y-k*59),(x+k*44,y-k*54),(x+k*42, y-k*70)]) #уши
	polygon(screen, (0, 0, 0), [(x+k*23, y-k*59),(x+k*16,y-k*54),(x+k*18, y-k*70)])

	circle(screen, (0, 0, 0), (x+k*23, y-k*33), k*7, 1, False, False, False, True) #рот
	circle(screen, (0, 0, 0), (x+k*37, y-k*33), k*7, 1, False, False, True, False)
	circle(screen, (255, 105, 180), (x+k*30, y-k*33), k*2)


fon (0, 0)
klubok(450, 500, 50)
okno (350, 30)
okno(100, 30)
okno(600, 30)
cat(screen, 70, 500, 2, (139, 69, 19))
cat(screen, 450, 400, 1, (150, 150, 150))
klubok(530, 450, 30)

surf = pygame.Surface((300, 300))
surf.fill((255, 255, 255))
surf.set_colorkey((255, 255, 255))
cat(surf, 50, 70, 1, (139, 69, 19))
rotatedSurf = pygame.transform.flip(surf, True, False)
screen.blit(rotatedSurf, (600, 450))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()