# coding=utf-8

import pygame
import pygame.locals
from obiekt import Drawable


class Racket(Drawable):
    """
    Rakietka, porusza się w osi X z ograniczeniem prędkości.
    """

    def __init__(self, width, height, x, y, color=(0, 255, 0), max_speed=10):
        super(Racket, self).__init__(width, height, x, y, color)
        self.width = width
        self.max_speed = max_speed
        self.surface.fill(color)

    def move(self, x):
        """
        Przesuwa rakietkę w wyznaczone miejsce.
        """
        delta = x - self.rect.x
        if abs(delta) > self.max_speed:
            delta = self.max_speed if delta > 0 else -self.max_speed
        self.rect.x += delta