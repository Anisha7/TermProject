# game.py

#############################################################################

import pygame
import random

from main.pygamegame import *
from main.player import *
from environment.enemy import *
from environment.castle import *
#from environment.level import *

############################################################################

pygame.font.init()
red = (255, 0, 0)
blue = (70, 165, 224)
purple = (255, 0, 255)
white = (255, 255, 255)

def collide(sprite1, sprite2):
    pygame.sprite.collide_rect(sprite1, sprite2)
############################################################################

class Game(PygameGame):

    def init(self):
        super().__init__()

        # SET UP GAME
        # self.width, self.height from pygamegame
        # screen width and height

        self.blue = (70, 165, 224)

        self.mapWidth = 2000
        self.mapHeight = 700
        mainMap = pygame.Surface((self.mapWidth, self.mapHeight))
        self.mainMap = mainMap.convert()
        self.mainMap.fill(self.blue)

        self.level = 1
        self.levelOver = False
        self.playerLives = 3
        # PLAYER
        self.player = Player(self.width, self.height, self.playerLives)

        self.punches = pygame.sprite.Group()

        # level one castles
        self.castle = Castle(200, self.player.y - 235, self.player.score, 1, self.level)
        self.inMiniGame1 = False
        self.castle2 = Castle(900, self.player.y - 235, self.player.score, 2, self.level)
        self.inMiniGame2 = False

        # scrolling tracker
        self.mapX = 0


        # ENEMY
        self.enemies = pygame.sprite.Group()

        # create random number of enemies
        x = random.randint(2, 5)
        #num = random.randint(self.width, self.mapWidth - 600)
        num = 350
        diff = 0
        for i in range(x):
            self.enemies.add(Enemy(num + diff, self.player.y))
            num += diff
            diff = random.randint(400, 800)

        self.pause = False
        # pause screen for animations
        self.playerKilled = False
        self.timeCount = 0
        # track which animation: when player is killed

        self.playerGhost = None




    def update(self, pressed_keys, keyCode, modifier):
        # scrolling when player reaches end of screen
        mapXc = -10
        if self.inMiniGame1 == False and self.inMiniGame2 == False:
            if self.playerKilled == False:
                if pressed_keys[K_LEFT]:
                    self.mapX -= mapXc
                #if self.player.x > 250:
                if pressed_keys[K_RIGHT]:
                    self.mapX += mapXc

                # add punches, for player attack
                if pressed_keys[K_SPACE]:
                    self.punches.add(Punches(self.player.x, self.player.y + 50, self.player.d))



            # remove enemy if attacked
            pygame.sprite.groupcollide(self.enemies, self.punches, True, True)

            for enemy in self.enemies:
                if self.player.enemyCollided(enemy.x, enemy.rect.width):
                    #self.player.killed()
                    self.playerLives -= 1
                    print("I died. lives left: ", self.playerLives)
                    self.player = Player(self.width, self.height, self.playerLives)
                    self.mapX = 0
                    self.playerKilled = True
                    self.playerGhost = Ghost(self.player.x, self.player.y)
            

            # entering castle
            if self.castle.castleCollide(self.player.x):
                #print("collided")
                if pressed_keys[K_RETURN]:
                    #self.castle.inGame(self.mainMap)
                    self.inMiniGame1 = True
                

            if self.castle2.castleCollide(self.player.x):
                #print("collided2")
                if pressed_keys[K_RETURN]:
                    #print("in castle 2")
                    #self.castle2.inGame(self.mainMap)
                    self.inMiniGame2 = True
               

        # exiting castle
        if self.inMiniGame1 == True:
            if pressed_keys[K_ESCAPE]:
                print("exit castle")
                #self.castle.exitCastle()
                self.inMiniGame1 = False
                self.castle.exitCastle()

        if self.inMiniGame2 == True:
            if pressed_keys[K_ESCAPE]:
                #self.castle.exitCastle()
                self.inMiniGame2 = False
                self.castle2.exitCastle()

        # if collide(self.player, self.castle):
        #     print("collided")

    def keyPressed(self, keyCode, modifier):
        pressed_keys = pygame.key.get_pressed()
        Game.update(self,pressed_keys, keyCode, modifier)

        if self.playerKilled == False:
            if self.inMiniGame1 == False and self.inMiniGame2 == False:
                self.player.update(pressed_keys)
            if self.inMiniGame1 == True or self.inMiniGame2 == True:
                self.castle.update(pressed_keys)

    def timerFired(self, dt):

        if self.playerKilled == False:
            self.enemies.update()
            self.punches.update()

        if self.playerKilled == True:
            self.timeCount += 10
            self.playerGhost.updateGhost()
            if self.timeCount == 500:
                self.playerKilled = False
                self.timeCount = 0


    def mainDraw(self, screen):

        # draw circles to test scrolling
        circle1 = pygame.draw.circle(self.mainMap, white, (1000, 300), 20)
        circle1 = pygame.draw.circle(self.mainMap, purple, (1000, 200), 20)
        circle1 = pygame.draw.circle(self.mainMap, blue, (1000, 100), 20)

        
        # score on screen
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        score = "Score: %d"%(self.player.score)
        textsurf = myfont.render(score, False, (0, 0, 0))
        screen.blit(textsurf,(self.width - 10, 20))

        # lives on screen
        lives = "Lives: "
        textsurf = myfont.render(lives, False, (0, 0, 0))
        screen.blit(textsurf,(100, 20))

        n = 0
        life = pygame.image.load('modules/life.png')
        life = pygame.transform.smoothscale(life, (20,20))
        if self.player.lives > 0:
            for i in range(self.player.lives):
                n += 30
                screen.blit(life, (140 + n, 20))

    def levelOneDraw(self, screen):
        #print("in here")
        # draw castle
        self.castle.draw(self.mainMap)
        self.castle2.draw(self.mainMap)

        if self.inMiniGame1 == True:
            self.castle.inGame(screen)
            # saving outside castle position
            x = self.player.x
            y = self.player.y
            #print(x,y) # 170, 302 ideal pos inside castle
            self.player.x = 170
            self.player.y = 302
            self.player.draw(screen)
            self.player.x = x
            self.player.y = y

            self.player.score = self.castle.score

        if self.inMiniGame2 == True and self.inMiniGame1 == False:
            self.castle2.inGame(self.mainMap)

        # draw trees


        # draw finish line flag
        flag = pygame.image.load('modules/finishFlag.png')
        self.mainMap.blit(flag, (1500, self.width//4))

        # check if player finished level1
        if self.player.x >= self.mapWidth - 350:
            self.levelOver = True
            self.player.level += 1
        
        # enemies

        self.enemies.draw(self.mainMap)

        # coins

        # treasure chests 

    def redrawAll(self, screen):
        # game setup

        # update scrolling on screen
        screen.blit(self.mainMap, (self.mapX, 0, self.mapX + self.width, self.height))
        if self.inMiniGame1 == False and self.inMiniGame2 == False:
            self.mainMap.fill(self.blue)

            # draw ground
            surf = pygame.image.load('modules/level1/Ground1.png')
            surf = pygame.transform.smoothscale(surf, (1700, self.width//4))
            self.mainMap.blit(surf, (0, self.height - self.width//16))

            Game.mainDraw(self, screen)

            # draw ground
            #rect1 = pygame.draw.rect(self.mainMap, white, (0, self.windowH - 25, 1700, self.windowH))
            surf = pygame.image.load('modules/level1/Ground1.png')
            surf = pygame.transform.smoothscale(surf, (1700, self.width//4))
            #pygame.Surface.blit(self.mainMap, surf, rect1)
            self.mainMap.blit(surf, (0, self.width))
        # draw level one game screen
        if self.player.level == 1:
            Game.levelOneDraw(self, self.mainMap)

        if self.inMiniGame1 == False or self.inMiniGame2 == False:
            # player 
            if self.playerKilled == False:
                self.player.draw(self.mainMap)
                self.punches.draw(self.mainMap)
            if self.playerKilled == True:
                self.playerGhost.draw(screen)



        pygame.display.flip()



Game(800, 500).run()



