import pygame
import sys
from random import randint
pygame.init()
width, height = 640, 360
screen = pygame.display.set_mode((width, height), 0, 32)
img_avatar = pygame.image.load("Adobe.png")

clr1 = (22, 122, 211)
clr2 = (0, 44, 166)`
clr3 = (34, 55, 245)
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

while True:
    # PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # PROCESSES
    # LOGIC
    r += 0.1
    if r > 255:
        r %= 255
    # LOGIC
    # DRAW
    screen.blit(img_avatar, (200, 200))

    # screen.fill((r, g, b))
    # pygame.draw.line(screen, clr2, (0, 0), (640, 360), 5)
    # pygame.draw.rect(screen, clr3, (40, 40, 300, 45))
    # pygame.draw.circle(screen, clr1, (350, 200), 80, 40)
    pygame.display.flip()

    # DRAW
