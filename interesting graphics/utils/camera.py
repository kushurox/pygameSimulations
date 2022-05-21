import pygame


class Camera:

    def __init__(self):
        self.offset = pygame.Vector2(0, 0)
        self.follow = pygame.Vector2(0, 0)
        self.relative = pygame.Vector2(0, 0)

    def attach(self, obj):
        self.follow.x = obj.pos.x
        self.follow.y = obj.pos.y
        obj.observer = self

    def __str__(self):
        return f"({self.follow.x}, {self.follow.y}, {self.offset.x}, {self.offset.y})"
