"""
wanted to implement storing of rotations using Complex numbers in a 2d plane
"""

import pygame
from pygame.time import Clock

CENTER = 200, 200


class Point:
    rotation = complex(1, 0)
    dist = 100

    def draw(self, surface):
        pygame.draw.circle(surface,
                           (255, 255, 255),
                           ((self.dist*self.rotation.real)+CENTER[0], (self.dist*self.rotation.imag)+CENTER[1]),
                           2)

    def rotate(self, new: complex):
        self.rotation = self.rotation * new


k = pygame.init()

clock = Clock()

display = pygame.display.set_mode((400, 400))

rotation2 = complex(-1, 1)  # -1 + i


over = True

p = Point()
p.rotate(rotation2)

while over:
    dt = clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
            break

    p.draw(display)

    pygame.display.update()
