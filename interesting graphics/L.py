"""
visualisation of conservation of angular momentum on change of radius
"""

import pygame
from pygame.time import Clock
from math import sin, cos, pi


k = pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
YELLOW = 255, 255, 0
GREEN = 0, 255, 0

FONT = pygame.font.Font(pygame.font.get_default_font(), 15)


def render_font(text: str, pos: tuple, surface, color=RED):
    text = FONT.render(text, True, color)
    textRect = text.get_rect()
    textRect.topleft = pos
    surface.blit(text, textRect)


def get_angular_pos(angle: float, radius: float, c: pygame.Vector2) -> pygame.Vector2:
    x = (radius * cos(angle)) + c.x
    y = (radius * sin(angle)) + c.y
    return pygame.Vector2(x, y)


class Point:

    def __init__(self, pos: pygame.Vector2, color=WHITE):
        self.color = color
        self.pos = pos

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, 5)


clock = Clock()

disp = pygame.display.set_mode((600, 600))
CENTER = pygame.Vector2(300, 300)
center = Point(CENTER)
notOver = True

mass = 1  # some random mass, not a real electron afterall
angle = pi / 2
radius = 100
electron_p = get_angular_pos(angle, radius, CENTER)
angular_velocity = pi / 6
linear_velocity = angular_velocity * radius

L = mass * linear_velocity * radius

electron = Point(electron_p, YELLOW)

while notOver:

    angular_momentum = f"L: {L}"
    V = f"V: {linear_velocity}"
    R = f"radius: {radius}"
    M = f"mass: {mass}"

    dt = clock.tick(30) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notOver = False
            break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                radius += 50

            elif event.key == pygame.K_DOWN:
                radius = max(50, radius-50)

            linear_velocity = L / (mass * radius)
            angular_velocity = linear_velocity / radius

    disp.fill(BLACK)

    render_font("UP ARROW KEY: increases radius by 50px", (20, 95), disp, GREEN)
    render_font("DOWN ARROW KEY: decreases radius by 50px (minimum: 50)", (20, 110), disp, GREEN)
    render_font(angular_momentum, (20, 10), disp)
    render_font(V, (20, 30), disp)
    render_font(R, (20, 50), disp)
    render_font(M, (20, 70), disp)

    center.draw(disp)
    electron.draw(disp)

    angle += angular_velocity * dt
    electron_p = get_angular_pos(angle, radius, CENTER)
    electron.pos = electron_p

    pygame.display.update()

pygame.quit()
