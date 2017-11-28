# enemies set up

#############################################################################

import pygame
import random

#############################################################################

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        super(Enemy, self).__init__()
        # x,y pos for enemy
        # initialize in game.py when creating enemy
        #print(pos)
        self.x = x
        self.y = y
        self.count = 0
        self.dist = 2
        self.dist2 = 0.2

        self.surf = pygame.image.load('modules/enemyCar.png')
        self.image = self.surf
        
        self.rect = self.surf.get_rect()
        self.rect.move_ip(x, y)


    def update(self):
        
        #dist = 2
        if self.count == 50:
            self.dist *= -1
            self.count = 0
       
        self.count += 1

        # move enemy sprite
        self.rect.move_ip(self.dist, 0)
        pygame.display.flip()

        # change images (won't work, use sprite command)
        if self.dist < 0:
            self.surf = pygame.image.load('modules/enemyCarLeft.png')
        else:
            self.surf = pygame.image.load('modules/enemyCar.png')

    def remove(self):
        self.kill()
        # self.kill if collide with player's boomerang


    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))
# enemies