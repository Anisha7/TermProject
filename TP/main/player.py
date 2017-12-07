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
        self.jumpd = 20
        self.jumpPress = 0
        self.jumpAdded = 0

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        self.newPlatform = False


    def timerFired(self):
        #print("I'm here in player timer fired")
        if self.moveLeft == True:
            #print("moving left")
            self.x -= 16
            self.surf = pygame.image.load('modules/AKplayerLeft.png')
            self.d = -1
        if self.moveRight == True:
            #print("moving right")
            self.x += 16
            self.surf = pygame.image.load('modules/AKplayer.png')
            self.d = 1

        if self.moveUp == True:
            self.y -= 14

        if self.moveDown == True:
            self.y += 14

        if self.level == 2:
            if self.x > 700:
                self.x = 100
            if self.x < 100:
                self.x = 700

        if self.level == 1:
            if self.jump == True:
                if self.jumpCount < 4:
                    self.y -= self.jumpd
                    #self.jumpAdded += self.jumpd
                else:
                    if self.newPlatform == False:
                        #self.jumpAdded += self.y
                        if self.y < self.ground:
                            self.y += self.jumpd

                        if self.y >= self.ground:
                            self.jumpCount = 0
                            self.jump = False
                            self.y = self.ground

                # while self.y < self.ground:
                #     self.y -= self.jumpd
            
                self.jumpCount += 1


    def update(self, pressed_keys):
        if self.level == 1:
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

    def platformCollide(self, x, y, w):

        if self.x >= x + w*2 and self.x <= x - w*2:
            # if self.jump == True:
            #     self.y = y
            if self.y >= y-20 and self.y <= y+50:
                return True
        return False

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))

    def enemyCollided(self, enemyX, enemyWidth, enemyy):

        if self.y <= enemyy-5 and self.y>= enemyy+5:
            return False

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
    speed = 35
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
            self.vx = 15
            self.surf = pygame.image.load('modules/boomerang.png')
            self.image = self.surf
        else:
            self.vx = -15
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