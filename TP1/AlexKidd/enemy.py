# enemies set up
import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        # x,y pos for enemy
        # initialize in game.py when creating enemy
        #print(pos)
        self.x = x
        self.y = y
        self.count = 0
        self.dist = 2

        self.surf = pygame.image.load('modules/enemyCar.png')
        self.rect = self.surf.get_rect
        #self.image = pygame.image.load('modules/enemyCar.png')
        #self.rect = self.image.get_rect


    def update(self):
        
        #dist = 2
        if self.count == 50:
            self.dist *= -1
            self.count = 0
       
        self.x += self.dist
        self.count += 1

        if self.dist < 0:
            self.surf = pygame.image.load('modules/enemyCarLeft.png')
        else:
            self.surf = pygame.image.load('modules/enemyCar.png')


    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))