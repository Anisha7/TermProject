# game.py for single player

#############################################################################
#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
#############################

import socket
import threading
from queue import Queue

HOST = "" # put your IP address here if playing on multiple computers
PORT = 50003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")

def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")

############################################################################      
import pygame
import random

from main.pygamegame import *
from main.player import *
from environment.enemy import *
from environment.castle import *
from environment.coins import *
from environment.platforms import *
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

        mainMap2 = pygame.Surface((self.mapHeight + 100, self.mapWidth))
        self.mainMap2 = mainMap2.convert()
        self.mainMap2.fill(self.blue)

        self.level = 1
        self.levelOver = False
        self.playerLives = 3
        self.score = 0
        # PLAYER
        self.player = Player(self.width, self.height, self.playerLives, self.score, "Lonely")
        self.me = self.player
        # self.otherStrangers = dict()
        self.others = []
        self.ground = self.player.y

        # multiplayer
        
        self.server = server
        self.serverMsg = serverMsg

        #self.player = player

        self.punches = pygame.sprite.Group()

        # castles
        self.inMiniGame = False

        # level 1
        self.castle = Castle(200, self.player.y - 235, self.player.score, 1, self.level)
        self.inMiniGame1 = False
        self.castle2 = Castle(900, self.player.y - 235, self.player.score, 2, self.level)
        self.inMiniGame2 = False

        # level 2
        self.castle3 = Castle(400, self.mapHeight + 900, self.player.score, 1, 2)
        self.inMiniGame3 = False

        self.castle4 = Castle(400, self.mapHeight + 300, self.player.score, 1, 2)
        self.castle5 = Castle(400, 500, self.player.score, 1, 2)
        


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
            y = random.randint(self.player.y, self.player.y + 20)
            self.coins.add(Coin(x, y))

        # platforms
        # level1
        self.platforms1 = pygame.sprite.Group()
        x = 500
        y = self.player.y - 30

        for i in range(6):
            platform = Platform(x,y,self.mapWidth, self.mapHeight, 1)
            x = random.randint(500, 1700)
            y = random.randint(self.player.y - 50, self.player.y - 30)

            if x <= 900 or x >= 1400:
                self.platforms1.add(platform)
        
        # level2
        self.platforms2 = pygame.sprite.Group()

        y = 30
        x = 0
        while y < self.mapHeight + 1200:
            platform = Platform(x,y,self.mapHeight + 100, self.mapWidth, 2)
            y += 50
            x = random.randint(0,self.width)

            self.platforms2.add(platform)


        

    def levelOneUpdate(self, pressed_keys, keyCode, modifier):
        # scrolling when player reaches end of screen

        
        if self.inMiniGame1 == False and self.inMiniGame2 == False:
            
            

            enemynum = len(self.enemies)
            # remove enemy if attacked
            pygame.sprite.groupcollide(self.enemies, self.punches, True, True)

            if len(self.enemies) < enemynum:
                self.player.score += 5
                self.score = self.player.score

            for enemy in self.enemies:
                #print(enemy)
                if self.player.enemyCollided(enemy.x, enemy.rect.width, enemy.y):
                    #self.player.killed()
                    self.playerGhost = Ghost(self.player.x, self.player.y)
                    self.playerLives -= 1
                    print("I died. lives left: ", self.playerLives)
                    self.player = Player(self.width, self.height, self.playerLives, self.score, self.player.PID)
                    
                    self.playerKilled = True
                    diff = random.randint(400, 800)
                    num = 350 + diff

                    self.enemies.add(Enemy(num + diff, self.player.y))
          
            platformHitList1 = pygame.sprite.spritecollide(self.player, self.platforms1, False)

            for platform in platformHitList1:
                self.player.y = platform.rect.y

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
                #print("exit castle")
                #self.castle.exitCastle()
                self.inMiniGame1 = False
                self.castle.exitCastle()

        if self.inMiniGame2 == True:
            if pressed_keys[K_ESCAPE]:
                #self.castle.exitCastle()
                self.inMiniGame2 = False
                self.castle2.exitCastle()

        
    def levelTwoUpdate(self, pressed_keys, keyCode, modifier):
        if self.inMiniGame3 == False:
            if self.castle3.castleCollide(self.player.x):
                if pressed_keys[K_RETURN]:
                    self.inMiniGame3 = True

            if self.castle4.castleCollide(self.player.x):
                if pressed_keys[K_RETURN]:
                    self.inMiniGame3 = True

            if self.castle5.castleCollide(self.player.x):
                if pressed_keys[K_RETURN]:
                    self.inMiniGame3 = True


            mapXc = -14
            # if pressed_keys[K_UP]:
            #     self.mapX -= mapXc
            #if self.player.x > 250:
            if pressed_keys[K_DOWN]:
                self.mapX += mapXc

            enemynum = len(self.enemies)
            # remove enemy if attacked
            pygame.sprite.groupcollide(self.enemies, self.punches, True, True)

            if len(self.enemies) < enemynum:
                self.player.score += 5
                self.score = self.player.score

            for enemy in self.enemies:
                #print(enemy)
                if self.player.enemyCollided(enemy.x, enemy.rect.width, enemy.y):
                    #self.player.killed()
                    self.playerGhost = Ghost(self.player.x, self.player.y)
                    self.playerLives -= 1
                    print("I died. lives left: ", self.playerLives)
                    self.player.x = 400
                    self.player.y = self.mapHeight + 1100
                    
                    self.playerKilled = True
                    diff = random.randint(400, 800)
                    num = 350 + diff

                    self.enemies.add(Enemy(num + diff, self.player.y))

            # platformHitList2 = pygame.sprite.spritecollide(self.player, self.platforms2, False)

            # for platform in platformHitList2:
            #     self.player.y = platform.y

        if self.inMiniGame3 == True:
            if pressed_keys[K_ESCAPE]:
                #self.castle.exitCastle()
                self.inMiniGame3 = False
                self.castle3.exitCastle()
                self.castle4.exitCastle()
                self.castle5.exitCastle()




    def update(self, pressed_keys, keyCode, modifier):

        if self.player.level == 1:
            Game.levelOneUpdate(self, pressed_keys, keyCode, modifier)

        if self.player.level == 2:
            Game.levelTwoUpdate(self, pressed_keys, keyCode, modifier)
        # if collide(self.player, self.castle):
        #     print("collided")

        if self.playerKilled == False:
            
            # add punches, for player attack
            if pressed_keys[K_SPACE]:
                self.punches.add(Punches(self.player.x, self.player.y + 50, self.player.d))

            # check coin collide
            for coin in self.coins:
                if self.player.coinCollided(coin.x):
                    self.player.score += 1
                    self.score = self.player.score
                    coin.remove()
                    try: #Background music is loaded here.
                        sound = pygame.mixer.Sound("sounds/coins-to-table-1.ogg")
                        sound.play(loops = 0)
                    except pygame.error as message:
                        print("Cannot load coin sound")
            # collision with platforms
              
        

    def keyPressed(self, keyCode, modifier):
        pressed_keys = pygame.key.get_pressed()

        if self.startScreen == True:

            if pressed_keys[K_RETURN]:
                #print("In HERE")
                self.startScreen = False
                self.splash = True

        else:
            
            Game.update(self,pressed_keys, keyCode, modifier)
            #print(self.playerKilled)
            if self.playerKilled == False:
                #print("I'm still ALIVE")
                if self.inMiniGame == False:
                    # update player's position
                    self.player.update(pressed_keys)
                    # send message to server
                    (x, y) = self.player.getPos()
                    msg = "playerMoved %d %d\n" % (x, y)
                    self.server.send(msg.encode())

                if self.inMiniGame1 == True:
                    #print("in game update func")
                    self.castle.update(pressed_keys)
                if self.inMiniGame2 == True:
                    self.castle2.update(pressed_keys)
                if self.inMiniGame3 == True:
                    print("in game class, castle3 update")
                    self.castle3.update(pressed_keys)
                    self.castle4.update(pressed_keys)
                    self.castle5.update(pressed_keys)

        #print(self.isKeyPressed(K_RIGHT))
        ## to return to start screen
        if pressed_keys[K_e]:
            print("exit game")
            self.startScreen = True
            #self.init()
        # if self.inMiniGame1 == False and self.inMiniGame2 == False:
        #     print("I'm not in a mini game")
        #     if pressed_keys[K_ESCAPE]:
        #         self.startScreen = True
        

    def myTimerFired(self, dt):
        # my player
        self.player.timerFired()

        if self.splash == True:
            self.splashCount += 1
            #print("in level spash screen")

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
            if self.player.level == 1:
                x = random.randint(100, 1400)
                y = random.randint(self.player.y, self.player.y + 30)
                
            if self.player.level == 2:
                # for i in range(5):
                x = random.randint(100,700)
                y = random.randint(100,1400)
            self.coins.add(Coin(x, y))
        
        if self.coinTime == 40:
            for coin in self.coins:
                coin.remove()
                # if self.player.level == 2:
                #     for i in range(4):
                        # coin.remove()
                break
            #self.coins.remove(self.coins[0])
            self.coinTime = 0

        if self.inMiniGame2 == True:
            self.castle2.timerFired()

        

        # print("HELD", self.isKeyPressed(K_RIGHT))

        if self.playerKilled == False:
            if self.isKeyPressed(K_RIGHT) == True:
                self.player.moveRight = True
                if self.player.level == 1:
                    self.mapX += -10
            else:
                self.player.moveRight = False

            if self.isKeyPressed(K_LEFT) == True:
                self.player.moveLeft = True
                if self.player.level == 1:
                    self.mapX -= -10
            else:
                self.player.moveLeft = False

            if self.player.level == 2:
                if self.isKeyPressed(K_UP) == True:
                    self.player.moveUp = True
                    self.mapX -= -14

                else:
                    self.player.moveUp = False

                if self.isKeyPressed(K_DOWN) == True:
                    self.player.moveDown = True
                    self.mapX += -14

                else:
                    self.player.moveDown = False
        

        if self.inMiniGame1 == True:
            self.inMiniGame = True
        elif self.inMiniGame2 == True:
            self.inMiniGame = True
        elif self.inMiniGame3 == True:
            self.inMiniGame = True
        else:
            self.inMiniGame = False

        # sounds
        try: #Background music is loaded here.
            sound = pygame.mixer.music.load("sounds/midnight-ride-01a.ogg")
            pygame.mixer.music.play(-1, 0.0)
        except pygame.error as message:
            print("Cannot load coin sound")

    def timerFired(self, dt):
        Game.myTimerFired(self, dt)
        
        # multiplayer: get and update positions of other players
        # timerFired receives instructions and executes them
        while (serverMsg.qsize() > 0):
            msg = serverMsg.get(False)
            try:
                print("received: ", msg, "\n")
                msg = msg.split()
                command = msg[0]

                if (command == "myIDis"):
                    myPID = msg[1]
                    self.me.changePID(myPID)
                    print("other strangers in 1:", self.otherStrangers)

                if (command == "newPlayer"):
                    print("adding new player to other strangers")
                    newPID = msg[1]
                    self.otherStrangers[newPID] = Player(self.width, self.height, 3, 0, newPID)
                    print("other strangers in 2:", self.otherStrangers)
                    self.others += [Player(self.width, self.height, 3, 0, newPID)]

                if (command == "playerMoved"):
                    PID = msg[1]
                    x = int(msg[2])
                    y = int(msg[3])
                    self.otherStrangers[PID].move(x, y)
                    print("other strangers in 3:", self.otherStrangers)

                    for player in self.others:
                        if player.PID == PID:
                            player.move(x,y)

            except Exception as error:
                print(self.otherStrangers)
                print("error:")
                print(error)
                print(command)
                print(msg)
                print("failed")
            serverMsg.task_done()


    def startScreen(self, surface):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        surf =  pygame.image.load('modules/AlexKiddStartScreen.png')
        surface.blit(surf, (0, 0))

    def gameOverScreen(self, surface):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        surf =  pygame.image.load('modules/gameOver.png')
        surface.blit(surf, (0, 0))

        text = "score: %d"%(self.player.score)
        textsurf = myfont.render(text, False, (0, 0, 0))
        surface.blit(textsurf,(100, self.height//2))

        text = "level reached: %d"%(self.player.level)
        textsurf = myfont.render(text, False, (0, 0, 0))
        surface.blit(textsurf,(100, self.height//2 + 40))


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
            surf = pygame.transform.smoothscale(surf, (1800, self.width//4))
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
        #self.platforms1.draw(self.mainMap)

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

        # draw platforms
        self.platforms1.draw(self.mainMap)

        # draw finish line flag
        flag = pygame.image.load('modules/finishFlag.png')
        self.mainMap.blit(flag, (1500, self.width//4))

        # check if player finished level1
        if self.player.x >= 1500 and self.player.x <= 1600:
            # level 2 set up
            self.player.level += 1
            self.level = self.player.level
            self.splash = True
            self.mapX = 0
            self.castle = Castle(200, self.player.y - 235, self.player.score, 1, 2)
            self.player.x = 400
            self.player.y = self.mapHeight + 1100

            # create random number of enemies for level 2

            x = random.randint(3, 6)
            for i in range(x):
                w = random.randint(100, 500)
                self.enemies.add(Enemy(w, 400 + 400*i))
            
        # enemies

        self.enemies.draw(self.mainMap)

        
        if self.inMiniGame3 == False:
            # coins
            self.coins.draw(self.mainMap)
            # player 
            if self.playerKilled == False:
                self.player.draw(self.mainMap)
                self.punches.draw(self.mainMap)
            if self.playerKilled == True:
                self.playerGhost.draw(screen)

            # draw other players
            # draw other players
            # for playerName in self.otherStrangers:
            #     print("I CAN BE UPDATED")
            #     print(self.otherStrangers[playerName])
            #     self.otherStrangers[playerName].draw(self.mainMap)

    def levelTwoDraw(self, screen):
        # self.mapWidth = 800
        # self.mapHeight = 2000
        # mainMap = pygame.Surface((self.mapWidth, self.mapHeight))
        # self.mainMap = mainMap.convert()
        # self.mainMap.fill(self.blue)
        screen.blit(self.mainMap2, (0, self.mapX - 1498, 800, self.mapX + self.height - 1498))
        self.mainMap2.fill(self.blue)
        #print((0, self.mapX, 800, self.mapX + self.height))
        #screen.blit(self.mainMap2, (0, self.mapX , 800, self.mapHeight - self.mapX))

        surf = pygame.image.load('modules/level1/Ground1.png')
        surf = pygame.transform.smoothscale(surf, (800, self.width//4))
        self.mainMap2.blit(surf, (0, self.mapHeight + 1200))

        self.platforms2.draw(self.mainMap2)
        
        #pygame.draw.rect(self.mainMap2, red, (0, 0, 100, self.mapWidth))
        # left wall
        surf = pygame.image.load('modules/level1/Ground1.png')
        surf = pygame.transform.smoothscale(surf, (100, self.mapWidth))
        self.mainMap2.blit(surf, (0, 0))
        self.mainMap2.blit(surf, (700, 0))

        self.castle3.draw(self.mainMap2)
        self.castle4.draw(self.mainMap2)
        self.castle5.draw(self.mainMap2)

         # draw finish line flag
        flag = pygame.image.load('modules/finishFlag.png')
        self.mainMap2.blit(flag, (600, 300))

        # check if player finished level 2
        if self.player.x >= 500 and self.player.x <= 700:
            if self.player.y >= 250 and self.player.y <= 350:
                self.player.lives = 0



        self.enemies.draw(self.mainMap2)

        
        #self.player.draw(self.mainMap2)

        #pygame.draw.rect(self.mainMap2, red, (self.mapHeight, 0, self.mapHeight, self.mapWidth))
        #pygame.draw.rect(self.mainMap2, red, (self.mapHeight - 25, 0, self.mapHeight, self.mapWidth))
        ##
        #pygame.display.update()
        if self.inMiniGame == False:
            # coins
            self.coins.draw(self.mainMap2)
            # player 
            if self.playerKilled == False:
                self.player.draw(self.mainMap2)
                self.punches.draw(self.mainMap2)
            if self.playerKilled == True:
                self.playerGhost.draw(screen)

            Game.mainDraw(self, screen)

        if self.inMiniGame3 == True:
            self.castle3.inGame(screen)
            #self.castle4.inGame(screen)
            #self.castle5.inGame(screen)
        
        #pygame.display.flip()

    def redrawAll(self, screen):
        # game setup
        
        # start screen
        if self.startScreen == True:
            #Game.init(self)
            Game.startScreen(self, screen)

        elif self.player.lives <= 0:
            Game.gameOverScreen(self, screen)

        else:
            if self.splash == True:
                Game.levelSplashScreen(self, screen)

            else:
                # draw level one game screen
                if self.player.level == 1:
                    Game.levelOneDraw(self, screen)

                if self.player.level == 2:
                    Game.levelTwoDraw(self, screen)
        
            # draw other players
            #print("in redrawall", self.otherStrangers)
            for playerName in self.otherStrangers:
                print("I CAN BE UPDATED")
                print(self.otherStrangers[playerName])
                if self.otherStrangers[playerName].level == 1:
                    self.otherStrangers[playerName].draw(self.mainMap)
                if self.otherStrangers[playerName].level == 2:
                    self.otherStrangers[playerName].draw(self.mainMap2)

            #print(self.others)
            for player in self.others:
                player.draw(self.mainMap)
        # self.inMiniGame3 = True
        # # self.castle = Castle(200, self.player.y - 235, self.player.score, 1, 2)
        # self.castle3.inGame(screen)
                

        pygame.display.flip()

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

Game(800, 500).run()


