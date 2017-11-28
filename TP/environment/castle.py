# castle and mini game setup

#############################################################################

import pygame
from main.player import Player
from games.level1 import *
from games.level1checkers import *

#############################################################################

class Castle(pygame.sprite.Sprite):

    def __init__(self, x, y, score, game, level):
        # x, y pos for Castle
        self.score = score
        self.x = x
        self.y = y
        self.game = game # tracks which mini game
        self.level = level

        self.surf = pygame.image.load('modules/castle1.png')
        self.rect = self.surf.get_rect
        self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        self.rockPaperScissor = RockPaperScissor(self.score)
        self.checkers = Checkers()


    def update(self, pressed_keys):
        self.rockPaperScissor.update(pressed_keys)

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def castleCollide(self, playerx):

        if (abs(self.x - playerx) <= self.x):
            return True
        else:
            return False

    def inGame(self, surface):
        #print("YO")
        if self.level == 1:
            if self.game == 1:
                self.rockPaperScissor.draw(surface)
                self.score = self.rockPaperScissor.score

            if self.game == 2:
                self.checkers.draw(surface)
                pass

    def exitCastle(self):
        if self.game == 1:
            self.rockPaperScissor = RockPaperScissor(self.score)
        if self.game == 2:
            pass
        pass