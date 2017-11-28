# player.py

#############################################################################

import pygame
from pygame.locals import *
from main.pygamegame import *
from environment import *

#############################################################################

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, lives):
        pygame.sprite.Sprite.__init__(self)
        super(Player, self).__init__()
        
        self.surf = pygame.image.load('modules/AKplayer.png')
        self.image = self.surf
        rect = self.surf.get_rect()
        self.rect = rect
        
        self.x = x//3
        self.y = y - 50 - rect.h//2
        self.lives = lives
        self.score = 0
        self.level = 1

        # track player's direction
        self.d = 1

    def update(self, pressed_keys):
        dist = 15

        if self.x > 150:
            if pressed_keys[K_LEFT]:
                self.surf = pygame.image.load('modules/AKplayerLeft.png')
                self.x -= dist
                self.d = -1
        if self.x < 1600:
            if pressed_keys[K_RIGHT]:
                self.surf = pygame.image.load('modules/AKplayer.png')
                self.x += dist
                self.d = 1

        # self.lives -= 1 if collide with enemy
        

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def enemyCollided(self, enemyX, enemyWidth):
        if self.x >= enemyX - enemyWidth//2 and self.x <= enemyX + enemyWidth//2:
            return True
        else:
            return False

    def killed(self, surface):
        self.surf = pygame.image.load('modules/AKplayer.png')
        self.image = self.surf
        rect = self.surf.get_rect()
        self.rect = rect
        

class Punches(pygame.sprite.Sprite):
    speed = 25
    time = 50 * 4 
    size = 10

    def __init__(self, x, y, d):
        # x, y : player's x,y pos
        pygame.sprite.Sprite.__init__(self)
        super().__init__()

        size = Punches.size

        self.surf = pygame.image.load('modules/boomerang.png')
        self.image = self.surf

        rect = self.surf.get_rect()
        self.rect = rect
        self.rect.move_ip(x, y)

        #self.image = pygame.image.load('modules/boomerang.png')

        self.x = x
        self.y = y

        #image = pygame.Surface((Punches.size, Punches.size), pygame.SRCALPHA)
        #pygame.draw.circle(image, (255, 255, 255), (size // 2, size // 2), size // 2)
        # create a group of boomeranges that are shot when punch activated
        self.velocity = Punches.speed
        self.timeOnScreen = 0

        # direction
        self.d = d
        if self.d > 0:
            self.vx = 8
            self.surf = pygame.image.load('modules/boomerang.png')
        else:
            self.vx = -8
            self.surf = pygame.image.load('modules/boomerangLeft.png')

        # distance travelled
        self.dist = 0

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def update(self):
        self.dist += abs(self.vx)
        self.rect.move_ip(self.vx, 0)

        if self.dist > 600:
            self.kill()
        # if self.x > windowW or self.x < 0:
        #     self.kill()

    def checkCollision(self, enemyx):

        if self.rect.x == enemyx:
            
            return True
        return False

    def remove(self):
        self.kill()
        
# player