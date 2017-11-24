# Game.py
# Actually implements the game
import pygame
from pygamegame import *
#from environment import *
#from env import *
from player import *
from enemy import *
from castle import *

import random

pygame.font.init()

class Game(PygameGame):
    def init(self):
        super().__init__()


        #set up
        self.windowW = self.width
        self.windowH = self.height
        self.blue = (70, 165, 224)
        self.groundImage = 'modules/level1/Ground1.png'

        self.mapWidth = 2000
        self.mapHeight = 700
        mainMap = pygame.Surface((self.mapWidth, self.mapHeight))
        self.mainMap = mainMap.convert()

        self.mainMap.fill(self.blue)
        #screen.blit(self.mainMap, (0, 0, self.windowW, self.windowH))

        # scrolling tracker
        self.mapX = 0

        self.player = Player(self.width, self.height)
        
        # track if player is punching
        self.punches = Punches(self.player.x, self.player.y + 50)
        self.punch = False
        self.d = 1
        self.vx = 4

        #self.punches = pygame.sprite.Group()

        # enemies
        x = random.randint(2, 5)
        enemyList = []
        for i in range(x):

            num = random.randint(self.windowW, self.mapWidth - 200)
            print(num)
            enemyList += [Enemy(num, self.player.y)]

        self.enemyList = enemyList

        # castle
        self.castle = Castle(200, self.player.y - 215)
        self.inMiniGame = False


    def update(self, pressed_keys, keyCode, modifier):

        # scrolling when player reaches end of screen
        mapXc = -10

        if self.player.x < 200:
            if pressed_keys[K_LEFT]:
                self.mapX -= mapXc
        if self.player.x > 450:
            if pressed_keys[K_RIGHT]:
                self.mapX += mapXc

        # direction of boomerang 
        if pressed_keys[K_LEFT]:
            self.d = -1
        if pressed_keys[K_RIGHT]:
            self.d = 1

        if pressed_keys[K_SPACE]:
            self.punch = True
            if self.d > 0:
                self.vx = 4
            else:
                self.vx = -4
            
            self.punches = Punches(self.player.x, self.player.y + 50)

        # get inside castle
        if abs(self.castle.x - self.player.x) <= 200:
            if pressed_keys[K_RETURN]:
                #self.castle.inGame(self.mainMap)
                self.inMiniGame = True
            if pressed_keys[K_ESCAPE]:
                #self.castle.exitCastle()
                self.inMiniGame = False


    def keyPressed(self, keyCode, modifier):
        pressed_keys = pygame.key.get_pressed()
        
        Game.update(self,pressed_keys, keyCode, modifier)

        self.player.update(pressed_keys)

    def timerFired(self, dt):
        #self.enemy.update()
        self.punches.update(self.windowW + 200, self.vx)
        if self.punches.x > self.windowW + 200:
            self.punch = False
            self.punches = Punches(self.player.x, self.player.y + 50)

        for enemy in self.enemyList:
            enemy.update()
            #print(enemy.x, self.punches.x)
            #if enemy.x == self.punches.x:
                #enemyList.remove(enemy)

            # if pygame.sprite.collide_rect(enemy, self.punches):
            #     enemyList.remove(enemy)
            #pass
        

    def redrawAll(self, screen):

        x = 0
        y = 0
        red = (255, 0, 0)
        blue = (70, 165, 224)
        purple = (255, 0, 255)
        white = (255, 255, 255)
        
        if self.inMiniGame == False:
            # update scrolling on screen
            screen.blit(self.mainMap, (self.mapX, 0, self.mapX + self.windowW, self.windowH))
            self.mainMap.fill(self.blue)

            # draw castle
            self.castle.draw(self.mainMap)

            # draw ground
            #rect1 = pygame.draw.rect(self.mainMap, white, (0, self.windowH - 25, 1700, self.windowH))
            surf = pygame.image.load(self.groundImage)
            surf = pygame.transform.smoothscale(surf, (1700, self.windowH//4))
            #pygame.Surface.blit(self.mainMap, surf, rect1)
            screen.blit(surf, (0, self.windowH))

            # draw circles to test scrolling
            circle1 = pygame.draw.circle(self.mainMap, white, (1000, 300), 20)
            circle1 = pygame.draw.circle(self.mainMap, purple, (1000, 200), 20)
            circle1 = pygame.draw.circle(self.mainMap, blue, (1000, 100), 20)


            # score on screen
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            score = "Score: %d"%(self.player.score)
            textsurf = myfont.render(score, False, (0, 0, 0))
            screen.blit(textsurf,(self.windowW - 10, 20))

            # lives on screen
            lives = "Lives: %d"%(self.player.lives)
            textsurf = myfont.render(lives, False, (0, 0, 0))
            screen.blit(textsurf,(100, 20))

            

            # player
            self.player.draw(screen)
            if self.punch == True:
                self.punches.draw(screen)
                #self.punch = False
            #self.punches.draw(screen)

            # level 1 enemies

            #self.enemies.draw(screen)
            for enemy in self.enemyList:
                enemy.draw(self.mainMap)

        if self.inMiniGame == True:
            self.castle.inGame(self.mainMap)

        pygame.display.flip()

        
      

Game(800, 500).run()