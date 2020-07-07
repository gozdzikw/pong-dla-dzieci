# coding=utf-8

import pygame
import pygame.locals

class Computer(object):
    """
    Przeciwnik, steruje swoją rakietką na podstawie obserwacji piłeczki.
    """
    def __init__(self, racket, ball):
        self.ball = ball
        self.racket = racket

    def move(self):
        x = self.ball.rect.centerx
        self.racket.move(x)