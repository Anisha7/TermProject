# coins

#############################################################################

import pygame
from pygame.locals import *
from main.pygamegame import *

#############################################################################

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        super(Coin, self).__init__()
        # x,y loc for coin

        self.x = x
        self.y = y + 30

        self.surf = pygame.image.load('modules/coin.png')
        self.surf = pygame.transform.smoothscale(self.surf, (50,50))
        self.image = self.surf
        rect = self.surf.get_rect()
        self.rect = rect
        self.rect.move_ip(self.x, self.y)


    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def remove(self):
        self.kill()