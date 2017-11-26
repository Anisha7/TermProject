#coins.py

# coin image from clipartlord.com

import pygame
from pygame.locals import *
from pygamegame import *

class Coins(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.surf = pygame.image.load('modules/coin.png')
        rect = self.surf.get_rect()

    def update(self):
        # if collide with player
        # self.kill()
        # add 1 to player scor/

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

