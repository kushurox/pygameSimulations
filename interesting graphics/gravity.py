"""
gravity between n particles, uses F = GMm/r^2
"""

import pygame
from pygame.time import Clock

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
BLUE = 0, 0, 255

G = 6.67E4


class Point:
    fixed = False

    def __init__(self, pos: pygame.Vector2, mass=1., color=WHITE):
        self.pos = pos
        self.mass = mass
        self.color = color
        self.acceleration = pygame.Vector2()
        self.velocity = pygame.Vector2()
        self.mass = mass

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, 20)

    def logic(self, force, dt):
        # print(hex(id(self.velocity)), hex(id(self.acceleration)), self.color)
        self.acceleration = force / self.mass
        self.velocity += self.acceleration * dt
        self.pos += self.velocity

    def GForce(self, ob2):
        # Calculating force towards ob2
        # print(hex(id(self.velocity)), hex(id(self.acceleration)), self.color)
        distance = ob2.pos - self.pos
        direction = distance.normalize()
        distance = distance.magnitude()
        distance = max(distance, 100)
        force = (G * self.mass * ob2.mass) / (distance ** 2)
        force = direction * force
        # self.logic(self.force, dt)
        return force


k = pygame.init()

clock = Clock()

display = pygame.display.set_mode((700, 700))

over = True

p1 = Point(pygame.Vector2(350, 50), 1, RED)
p3 = Point(pygame.Vector2(200, 350), 1, BLUE)
p2 = Point(pygame.Vector2(500, 350), 1, WHITE)  # Fixed point

while over:
    dt = clock.tick(30)/1000
    display.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
            break

    p1.draw(display)
    p2.draw(display)
    p3.draw(display)

    p1_to_p2 = p1.GForce(p2)  # Attracts RED towards WHITE
    p1_to_p3 = p1.GForce(p3)  # Attracts RED towards BLUE

    p3_to_p2 = p3.GForce(p2)  # Attracts BLUE towards WHITE
    p3_to_p1 = p3.GForce(p1)  # Attracts BLUE towards RED

    p1.logic(p1_to_p3, dt)    # Updates the acceleration for new force
    p1.logic(p1_to_p2, dt)

    # p3.logic(p3_to_p1, dt)
    # p3.logic(p3_to_p2, dt)

    pygame.display.update()
