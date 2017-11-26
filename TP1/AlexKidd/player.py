# player set up
import pygame
from pygame.locals import *
from pygamegame import *
from environment import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((200, 155, 255))
        self.surf = pygame.image.load('modules/AKplayer.png')
        rect = self.surf.get_rect()
        #print("recth: ",rect.h)
        #print(Environment.groundh)
        self.x = x//3
        self.y = y - 50 - rect.h//2
        self.rect = self.surf.get_rect()
        self.lives = 3
        self.score = 0
        self.level = 1

    def update(self, pressed_keys):
        dist = 15

        if pressed_keys[K_UP]:
            self.y -= dist
        if pressed_keys[K_DOWN]:
            self.y += dist

        if self.x > 150:
            if pressed_keys[K_LEFT]:
                self.surf = pygame.image.load('modules/AKplayerLeft.png')
                self.x -= dist
        if self.x < 550:
            if pressed_keys[K_RIGHT]:
                self.surf = pygame.image.load('modules/AKplayer.png')
                self.x += dist

        # self.lives -= 1 if collide with enemy
        

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

class Punches(pygame.sprite.Sprite):
    speed = 25
    time = 50 * 4 
    size = 10

    def __init__(self, x, y):
        # x, y : player's x,y pos
        super().__init__()
        size = Punches.size

        self.surf = pygame.image.load('modules/boomerang.png')
        rect = self.surf.get_rect
        #self.image = pygame.image.load('modules/boomerang.png')

        self.x = x
        self.y = y

        #image = pygame.Surface((Punches.size, Punches.size), pygame.SRCALPHA)
        #pygame.draw.circle(image, (255, 255, 255), (size // 2, size // 2), size // 2)
        # create a group of boomeranges that are shot when punch activated
        self.velocity = Punches.speed
        self.timeOnScreen = 0

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def update(self, windowW, vx):
        #self.x += self.velocity
        if vx < 0:
            self.surf = pygame.image.load('modules/boomerangLeft.png')
        else:
            self.surf = pygame.image.load('modules/boomerang.png')

        self.x += vx
        self.timeOnScreen += 1
        if self.timeOnScreen > Punches.time:
            #self.kill()
            pass

        if self.x > windowW or self.x < 0:
            self.kill()

    def checkCollision(self, enemyx, enemyy):
        if self.x == enemyx and self.y == enemyy:
            pass

        pass
