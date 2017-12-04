# game.py

#############################################################################

import pygame
import random

from main.pygamegame import *
from main.player import *
from environment.enemy import *
from environment.castle import *
from environment.coins import *
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

# Game Play Instructions
    # Left, right arrow keys to move
    # space bar to attack (cars are enemies)
    # enter to enter castle (need to be in front of castle)
    
class Game(PygameGame):

    def init(self):
        super().__init__()

        # SET UP GAME
        # self.width, self.height from pygamegame
        # screen width and height

        self.startScreen = True
        self.splash = False
        self.splashCount = 0

        self.blue = (70, 165, 224)

        self.mapWidth = 2000
        self.mapHeight = 700
        mainMap = pygame.Surface((self.mapWidth, self.mapHeight))
        self.mainMap = mainMap.convert()
        self.mainMap.fill(self.blue)

        self.level = 1
        self.levelOver = False
        self.playerLives = 3
        self.score = 0
        # PLAYER
        self.player = Player(self.width, self.height, self.playerLives, self.score)

        self.punches = pygame.sprite.Group()

        # castles
        self.castle = Castle(200, self.player.y - 235, self.player.score, 1, self.level)
        self.inMiniGame1 = False
        self.castle2 = Castle(900, self.player.y - 235, self.player.score, 2, self.level)
        self.inMiniGame2 = False

        # level 2


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

        # coins
        self.coinTime = 0
        self.coins = pygame.sprite.Group()

        for i in range(4):
            x = random.randint(100, 1400)
            self.coins.add(Coin(x, self.player.y))




    def update(self, pressed_keys, keyCode, modifier):
        # scrolling when player reaches end of screen
        mapXc = -10
        if self.inMiniGame1 == False and self.inMiniGame2 == False:
            
            if self.playerKilled == False:
                # level one scrolling
                if self.level == 1:
                    if pressed_keys[K_LEFT]:
                        self.mapX -= mapXc
                    #if self.player.x > 250:
                    if pressed_keys[K_RIGHT]:
                        self.mapX += mapXc

                if self.level == 2:
                    if pressed_keys[K_UP]:
                        self.mapX -= mapXc
                    #if self.player.x > 250:
                    if pressed_keys[K_DOWN]:
                        self.mapX += mapXc

                # add punches, for player attack
                if pressed_keys[K_SPACE]:
                    self.punches.add(Punches(self.player.x, self.player.y + 50, self.player.d))


            enemynum = len(self.enemies)
            # remove enemy if attacked
            pygame.sprite.groupcollide(self.enemies, self.punches, True, True)

            if len(self.enemies) < enemynum:
                self.player.score += 5
                self.score = self.player.score

            for enemy in self.enemies:
                print(enemy)
                if self.player.enemyCollided(enemy.x, enemy.rect.width):
                    #self.player.killed()
                    self.playerGhost = Ghost(self.player.x, self.player.y)
                    self.playerLives -= 1
                    print("I died. lives left: ", self.playerLives)
                    self.player = Player(self.width, self.height, self.playerLives, self.score)
                    
                    self.playerKilled = True
                    
            

            # check coin collide
            for coin in self.coins:
                if self.player.coinCollided(coin.x):
                    self.player.score += 1
                    self.score = self.player.score
                    coin.remove()


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

        if self.startScreen == True:

            if pressed_keys[K_RETURN]:
                print("In HERE")
                self.startScreen = False
                self.splash = True

        else:
            
            Game.update(self,pressed_keys, keyCode, modifier)
            print(self.playerKilled)
            if self.playerKilled == False:
                print("I'm still ALIVE")
                if self.inMiniGame1 == False and self.inMiniGame2 == False:
                    self.player.update(pressed_keys)
                if self.inMiniGame1 == True:
                    print("in game update func")
                    self.castle.update(pressed_keys)
                if self.inMiniGame2 == True:
                    self.castle2.update(pressed_keys)


        ## to return to start screen
        if pressed_keys[K_e]:
            print("exit game")
            self.startScreen = True
        # if self.inMiniGame1 == False and self.inMiniGame2 == False:
        #     print("I'm not in a mini game")
        #     if pressed_keys[K_ESCAPE]:
        #         self.startScreen = True

    def timerFired(self, dt):

        if self.splash == True:
            self.splashCount += 1
            print("in level spash screen")

            if self.splashCount == 20:
                self.splashCount = 0
                self.splash = False

        if self.playerKilled == False:
            self.enemies.update()
            self.punches.update()

        if self.playerKilled == True:
            self.timeCount += 10
            self.playerGhost.updateGhost()
            if self.timeCount == 500:
                self.playerKilled = False
                self.timeCount = 0
                self.mapX = 0

        # add coin every 20 secs. It stays on screen for 20 sec.
        self.coinTime += 1

        if self.coinTime == 20:

            x = random.randint(100, 1400)
            self.coins.add(Coin(x, self.player.y))
        
        if self.coinTime == 40:
            for coin in self.coins:
                coin.remove()
                break
            #self.coins.remove(self.coins[0])
            self.coinTime = 0

        if self.inMiniGame2 == True:
            self.castle.timerFired()

        self.player.timerFired()

    def startScreen(self, surface):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        surf =  pygame.image.load('modules/AlexKiddStartScreen.png')
        surface.blit(surf, (0, 0))

    def mainDraw(self, screen):

        # draw circles to test scrolling
        # circle1 = pygame.draw.circle(self.mainMap, white, (1000, 300), 20)
        # circle1 = pygame.draw.circle(self.mainMap, purple, (1000, 200), 20)
        # circle1 = pygame.draw.circle(self.mainMap, blue, (1000, 100), 20)

        
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

    def levelSplashScreen(self, screen):
        self.surf = pygame.draw.rect(screen, (0, 0, 0), [0, 0, 800, 500])

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = "Level: %d"%(self.level)
        textsurf = myfont.render(text, False, (225, 225, 225))
        screen.blit(textsurf,(350, 100))

        # lives = "Lives: "
        # textsurf = myfont.render(lives, False, (0, 0, 0))
        # screen.blit(textsurf,(400, 20))

        n = 0
        life = pygame.image.load('modules/life.png')
        life = pygame.transform.smoothscale(life, (20,20))
        if self.player.lives > 0:
            for i in range(self.player.lives):
                n += 30
                screen.blit(life, (320 + n, 200))


    def levelOneDraw(self, screen):
        #print("in here")
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

        else:
            self.player.score += self.castle.score
            self.castle.score = 0
            self.score = self.player.score

        if self.inMiniGame2 == True and self.inMiniGame1 == False:
            #self.castle2.inGame(self.mainMap)
            self.castle2.inGame(screen)

        # draw trees


        # draw finish line flag
        flag = pygame.image.load('modules/finishFlag.png')
        self.mainMap.blit(flag, (1500, self.width//4))

        # check if player finished level1
        if self.player.x >= 1500 and self.player.x <= 1600:
            self.player.level += 1
            self.level = self.player.level
            self.splash = True
        
        # enemies

        self.enemies.draw(self.mainMap)

        
        if self.inMiniGame1 == False or self.inMiniGame2 == False:
            # coins
            self.coins.draw(self.mainMap)
            # player 
            if self.playerKilled == False:
                self.player.draw(self.mainMap)
                self.punches.draw(self.mainMap)
            if self.playerKilled == True:
                self.playerGhost.draw(screen)

    def levelTwoDraw(self, screen):
        self.mapWidth = 800
        self.mapHeight = 2000
        mainMap = pygame.Surface((self.mapWidth, self.mapHeight))
        self.mainMap = mainMap.convert()
        self.mainMap.fill(self.blue)
        screen.blit(self.mainMap, (0, self.mapX, self.width, self.mapX + self.height))

        ## not drawing
        surf = pygame.image.load('modules/level1/Ground1.png')
        surf = pygame.transform.smoothscale(surf, (self.width, self.width//4))
        self.mainMap.blit(surf, (0, self.mapHeight - self.width//16))
        ##

        Game.mainDraw(self, screen)


        ## not showing up...why?
        # draw circles to test scrolling
        circle1 = pygame.draw.circle(self.mainMap, white, (self.mapWidth//2, 1000), 20)
        circle1 = pygame.draw.circle(self.mainMap, purple, (self.mapWidth//2, 300), 20)
        circle1 = pygame.draw.circle(self.mainMap, blue, (200, 50), 20)
        
        pygame.draw.rect(self.mainMap, red, (0, self.mapHeight - 25, self.mapWidth, self.mapHeight))
        pygame.draw.rect(self.mainMap, red, (0, 0, 400, self.mapHeight))
        pygame.draw.rect(self.mainMap, red, (self.mapWidth - 400, 0, self.mapWidth, self.mapHeight))
        ##
        #pygame.display.update()
        pygame.display.flip()

    def redrawAll(self, screen):
        # game setup

        # start screen
        if self.startScreen == True:
            Game.init(self)
            Game.startScreen(self, screen)

        else:
            if self.splash == True:
                Game.levelSplashScreen(self, screen)

            else:
                # draw level one game screen
                if self.player.level == 1:
                    Game.levelOneDraw(self, screen)

                if self.player.level == 2:
                    Game.levelTwoDraw(self, screen)
        # self.inMiniGame1 = True
        # self.castle = Castle(200, self.player.y - 235, self.player.score, 1, 2)
        # self.castle.inGame(screen)

                
                

        pygame.display.flip()



Game(800, 500).run()


