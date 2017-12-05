# platforms
import pygame
from pygame.locals import *
from main.pygamegame import *
import random

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, level):
        pygame.sprite.Sprite.__init__(self)
        super(Platform, self).__init__()
        # x,y = loc
        # x between 50 and self.width
        # width, height of map

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        w = 0
        if level == 1:
            w = random.randint(20, 100)
            surf = pygame.image.load('modules/level1/Ground1.png')
            self.surf = pygame.transform.smoothscale(surf, (w, 50))
            self.image = self.surf
            self.rect = self.surf.get_rect()

        if level == 2:
            self.w = 0

            #w,h for platform
            if self.x >= self.width//2:
                w = self.width - x
            else:
                w = self.x
                self.x = 0

            self.w = w

            surf = pygame.image.load('modules/level1/Ground1.png')
            self.surf = pygame.transform.smoothscale(surf, (self.w, 50))
            self.image = self.surf
            self.rect = self.surf.get_rect()
            
        self.rect.move_ip(self.x, self.y)
        
    def draw(self, surface):
        surface.blit(surf, (self.x, self.y))