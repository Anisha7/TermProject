# enemies set up
import pygame
import random

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
        # test for group
        n = random.randint(300, 1400)
        #self.rect = self.surf.get_rect(topleft = n)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(x, y)

        #print("in enemy", self.alive())
        #self.image = pygame.image.load('modules/enemyCar.png')
        #self.rect = self.image.get_rect

    def update2(self):

        self.rect.move_ip(self.x + self.dist, 0)

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

        self.rect.move_ip(self.dist, 0)
        pygame.display.flip()
        # self.kill if collide with player's boomerang


    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))
