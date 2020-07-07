# coding=utf-8

import pygame
import pygame.locals
from pilka import Ball
from plansza import Board
from rakietka import Racket
from przeciwnik import Computer
from punktacja import Scoring

class PongGame(object):
    """
    GRA
    """

    def __init__(self, width, height):
        pygame.init()
        self.board = Board(width, height)
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        self.fps_clock = pygame.time.Clock()
        self.ball = Ball(width=20, height=20, x=width/2, y=height/2)
        self.player1 = Racket(width=80, height=20, x=width/2 - 40, y=height - 40)
        self.player2 = Racket(width=80, height=20, x=width/2 - 40, y=20, color=(0, 0, 0))
        self.computer = Computer(self.player2, self.ball)
        self.scoring = Scoring(self.board, self.ball, self.player2, self.ball)

    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            self.ball.move(self.board, self.player1, self.player2)
            self.board.draw(self.ball, self.player1, self.player2, self.scoring)
            self.computer.move()
            self.fps_clock.tick(30)

    def handle_events(self):
        """
        Obsługa myszki
        :return True - wyjście z gry
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.locals.MOUSEMOTION:
                # myszka steruje ruchem pierwszego gracza
                x, y = event.pos
                self.player1.move(x)

#To musi być zawsze na końcu
if __name__ == "__main__":
    game = PongGame(800, 400)
    game.run()