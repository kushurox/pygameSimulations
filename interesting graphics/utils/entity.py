import pygame

from .camera import Camera
from .colors import WHITE


class Entity:
    def __init__(self, pos: pygame.Vector2, observer: Camera = None):
        self.observer = observer
        self.pos = pos

    def update(self):
        """
        call this method if you want to update the observer's offset values
        :return: None
        """
        self.observer.offset = self.pos - self.observer.follow + self.observer.relative


if __name__ == '__main__':
    print(pygame.Vector2(100, 100)-(50, 60))
