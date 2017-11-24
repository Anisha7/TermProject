# castle
import pygame
from player import Player
from Games.level1 import *
# helpers for game setup

class Castle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # x, y pos for Castle

        self.x = x
        self.y = y

        self.surf = pygame.image.load('modules/castle1.png')
        self.rect = self.surf.get_rect
        self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        self.rockPaperScissor = RockPaperScissor()

        # Game setup
        

    def update(self, pressed_keys):
        pass


    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def inGame(self, surface):
        print("YO")
        self.rockPaperScissor.draw(surface)

        pass

    def exitCastle(self):
        print("HO")
        pass