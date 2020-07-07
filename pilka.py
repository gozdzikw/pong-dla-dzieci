# coding=utf-8

import pygame
import pygame.locals
from obiekt import Drawable

class Ball(Drawable):
    """
    Piłeczka, sama kontroluje swoją prędkość i kierunek poruszania się.
    """
    def __init__(self, width, height, x, y, color=(255, 0, 0), x_speed=3, y_speed=3):
        super(Ball, self).__init__(width, height, x, y, color)
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.start_x = x
        self.start_y = y

    def bounce_y(self):
        # Odwraca wektor prędkości w osi Y

        self.y_speed *= -1

    def bounce_x(self):
         # Odwraca wektor prędkości w osi X
        self.x_speed *= -1

    def move(self, board, *args):
        print("Dlaczego ta piłeczka się nie przesuwa?")
        #miejsce na Twój kod:



        

        """
        Potrzebne informacje:
        self.rect.x <- polożenie piłeczki w osi X
        self.rect.y <- położenie piłeczki w osi Y
        self.rect.colliderect(racket.rect) <- kolizja obiekt
        """

        #Piłeczka odbija się jak trafi na rakietke
        for racket in args:
            if self.rect.colliderect(racket.rect):
                self.bounce_y()
