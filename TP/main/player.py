# player.py

#############################################################################

import pygame
from pygame.locals import *
from main.pygamegame import *
from environment import *

#############################################################################

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, lives, score, PID):
        pygame.sprite.Sprite.__init__(self)
        super(Player, self).__init__()
        self.PID = PID
        self.surf = pygame.image.load('modules/AKplayer.png')
        self.image = self.surf
        rect = self.surf.get_rect()
        self.rect = rect
        
        self.x = x//3
        
        self.y = y - 50 - rect.h//2
        self.ground = y - 50 - rect.h//2
        self.lives = lives
        self.score = score
        self.level = 1

        # track player's direction
        self.d = 1

        # jumping
        self.jump = False
        self.jumpCount = 0
        self.jumpd = 14
        self.jumpPress = 0

    def timerFired(self):
        if self.jump == True:
            if self.jumpd == 14:
                self.y -= self.jumpd
            else:
                while self.y < self.ground:
                    self.y -= self.jumpd
            
            self.jumpCount += 1
            if self.jumpCount == 4:
                self.jumpd *= -1

            if self.jumpCount == 8:
                self.jump = False
                self.jumpd *= -1
                self.jumpCount = 0

    def update(self, pressed_keys):
        dist = 16
        
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

        if pressed_keys[K_UP]:
            self.jump = True
            self.jumpPress += 1
            if self.jumpPress < 2:
                self.jumpCount = 0
            if self.jumpPress == 2:
                self.jumpPress = 0
            
    def getPos(self):
        return (self.x, self.y)

    def move(self,x,y):
        self.x = x
        self.y = y

        # self.lives -= 1 if collide with enemy
        

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def enemyCollided(self, enemyX, enemyWidth):
        #if self.x >= enemyX - enemyWidth//2 and self.x <= enemyX + enemyWidth//2:
        #print("enemyX: ", enemyX)
        #print("self.x: ", self.x)
        if self.x >= enemyX and self.x <= enemyX + 100:
            return True
        else:
            return False

    def coinCollided(self, x):
        if self.x >= x and self.x <= x + 50:
            return True
        else:
            return False

    def changePID(self, PID):
        self.PID = PID

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # x, y player died here
        self.x = x
        self.y = y
        # player's ghost initialization
        self.surf = pygame.image.load('modules/ghost.png')
        self.image = self.surf
        rect = self.surf.get_rect()
        self.rect = rect
        self.rect.move_ip(self.x, self.y)

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def updateGhost(self):
        self.y -= 5


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
            self.image = self.surf
        else:
            self.vx = -8
            self.surf = pygame.image.load('modules/boomerangLeft.png')
            self.image = self.surf

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