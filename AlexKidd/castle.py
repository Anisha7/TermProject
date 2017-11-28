# castle
import pygame
from player import Player
from Games.level1 import *
from Games.level1checkers import *
# helpers for game setup

class Castle(pygame.sprite.Sprite):

    def __init__(self, x, y, score, game):
        # x, y pos for Castle
        self.score = score
        self.x = x
        self.y = y
        self.game = game # tracks which mini game

        self.surf = pygame.image.load('modules/castle1.png')
        self.rect = self.surf.get_rect
        self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        self.rockPaperScissor = RockPaperScissor(self.score)
        self.checkers = Checkers()

        # Game setup
        

    def update(self, pressed_keys):
        self.rockPaperScissor.update(pressed_keys)



    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def inGame(self, surface):
        #print("YO")
        if self.game == 1:
            self.rockPaperScissor.draw(surface)
            self.score = self.rockPaperScissor.score

        if self.game == 1.2:
            self.checkers.draw(surface)


    def inGame2(self, surface):
        pass

    def exitCastle(self):
        if self.game == 1:
            self.rockPaperScissor = RockPaperScissor(self.score)
        if self.game == 2:
            pass
        pass