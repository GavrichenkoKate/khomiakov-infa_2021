import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 0, 255), (100, 100, 200, 200))

circle(screen, (255, 255, 0), (200, 175), 50)
circle(screen, (255, 0, 0), (180, 160), 10)
circle(screen, (0, 0, 0), (180, 160), 10, 1)
circle(screen, (0, 0, 0), (180, 160), 5)
circle(screen, (255, 0, 0), (220, 160), 15)
circle(screen, (0, 0, 0), (220, 160), 15, 1)
circle(screen, (0, 0, 0), (220, 160), 5)
rect(screen, (0, 0, 0), (180, 190, 45, 10))
polygon(screen, (0, 0, 0), [(195, 160), (200, 155), (150, 115), (145, 120)])
pygame.draw.line(screen, (0, 0, 0), [200, 160], [240, 120], 7)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
