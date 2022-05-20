"""
procedural generation of 2d terrain using sin function and random function
"""

import pygame
from pygame.time import Clock
import random
import math


class Land(pygame.Surface):
    pos = (0, 0)


k = pygame.init()

width, height = 1275, 650

screen = pygame.display.set_mode((width, height))

run = True

clock = Clock()


def map_origin(x, y):
    return x, height - y


ts = 13
row = []

hill_height = 300

angle = 31  # in degrees

_x = 0

upper_bound = height//ts
upper_bound //= 2

sign = False
interval = 0

for land in range(width // ts):
    temp_land = Land([ts, ts])
    temp_land.fill((255, 0, 255))
    _height = round(math.sin(math.radians(angle)) * upper_bound) * ts
    temp_land.pos = (_x, _height)
    lower_angel = random.randint(30, 35)
    if angle >= 90:
        angle = 89
        sign = not sign
        interval = 5
    elif angle <= lower_angel:
        angle = lower_angel+1
        sign = not sign
        interval = 5

    if interval <= 0:
        if not sign:
            angle += 2
        else:
            angle -= 2

    interval -= 1

    _x += ts
    row.append(temp_land)

while run:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    for land in row:
        x, y = map_origin(*land.pos)
        y = y - ts
        screen.blit(land, (x, y))
        while y < height:
            y += ts
            screen.blit(land, (x, y))
    pygame.display.update()

pygame.quit()
