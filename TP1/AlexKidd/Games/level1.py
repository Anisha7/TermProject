# game for level1

import pygame
#from game import *
from pygamegame import *
from player import *
import random

class RockPaperScissor(PygameGame):

    def __init__(self):
        
        super().__init__()

        self.surf = pygame.image.load('modules/Stage.png')
        self.rect = self.surf.get_rect
        #self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        # Game setup

        self.paper = pygame.image.load('modules/Game1/paper.png')
        self.rock = pygame.image.load('modules/Game1/rock.png')
        self.scissors = pygame.image.load('modules/Game1/scissors.png')
        self.moves = [self.paper, self.rock, self.scissors]
        self.i = 0
        self.playerMove = self.moves[0]
        n = random.randint(0,2)
        self.enemyMove = self.moves[n]
        
        # count wins
        self.enemyWins = 0
        self.playerWins = 0

        # who won
        self.endText = None

        self.playing = True

        self.prizes = [50,100,200,300,500]


    def update(self, pressed_keys):

        # check if 3 games have played and get winner
        if self.enemyWins != self.playerWins:
            if self.enemyWins + self.playerWins >= 3:
                self.playing = False

        # if game is being played, get win counts
        if self.playing == True:
            if pressed_keys[K_RIGHT]:
                self.i += 1
                if self.i > 2:
                    self.i = 0

                self.endText = None
                
            if pressed_keys[K_LEFT]:
                self.i -= 1
                if self.i < 0:
                    self.i = 2

                self.endText = None

            self.playerMove = self.moves[self.i]

            if pressed_keys[K_RETURN]:
                # show enemy move
                # show who won
                if self.enemyMove == self.paper:
                    if self.playerMove == self.rock:
                        self.enemyWins += 1
                        self.endText = "You Lose!"
                    if self.playerMove == self.paper:
                        self.endText = "Tie!"
                    if self.playerMove == self.scissors:
                        self.playerWins += 1
                        self.endText = "You Win!"

                if self.enemyMove == self.rock:
                    if self.playerMove == self.rock:
                        self.endText = "Tie!"
                    if self.playerMove == self.paper:
                        self.playerWins += 1
                        self.endText = "You Win!"
                    if self.playerMove == self.scissors:
                        self.enemyWins += 1
                        self.endText = "You Lose!"

                if self.enemyMove == self.scissors:
                    if self.playerMove == self.rock:
                        self.playerWins += 1
                        self.endText = "You Win!"
                    if self.playerMove == self.paper:
                        self.enemyWins += 1
                        self.endText = "You Lose!"
                    if self.playerMove == self.scissors:
                        self.endText = "Tie!"


    def draw(self, surface):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        if self.playing == True:
            surface.blit(self.surf, (0, 0))
            surface.blit(self.playerMove, (self.width//4, self.height//2))
            surface.blit(self.enemyMove, (self.width - self.width//4, self.height//2))

            # scores
            
            playerScore = "Your Score: %d"%(self.playerWins)
            textsurf = myfont.render(playerScore, False, (0, 0, 0))
            surface.blit(textsurf,(self.width//4, 40))

            enemyScore = "Your Score: %d"%(self.enemyWins)
            textsurf = myfont.render(enemyScore, False, (0, 0, 0))
            surface.blit(textsurf,(self.width - self.width//4, 40))

            # who won each mini match
            if self.endText != None:
                textsurf = myfont.render(self.endText, False, (0, 0, 0))
                surface.blit(textsurf,(self.width//2, self.height//4))

        # end game screen, who won, what reward player gets
        if self.playing == False:
            self.endsurf = pygame.draw.rect(self.mainMap, white, (0, 0, self.width, self.height))
            surface.blit(self.endsurf, (0, 0))
            # who won
            if self.playerWins > self.enemyWins:
                self.endText = "You Win!"
                textsurf = myfont.render(self.endText, False, (0, 0, 0))
                surface.blit(textsurf,(self.width//2, self.height//4), 40)

                # what did player win
                n = random.randint(0, 4)
                prize = self.prizes[n]

                text = "You won %d coins!"%(prize)
                textsurf = myfont.render(text, False, (0, 0, 0))
                surface.blit(textsurf,(self.width//2, self.height//2), 40)

                Player.score += prize
                score = "Score: %d"%(self.player.score)
                textsurf = myfont.render(score, False, (0, 0, 0))
                screen.blit(textsurf,(self.windowW - 10, 20))
                # put prize image here

                exitInst = "Press ESC to exit Castle"
                textsurf = myfont.render(exitInst, False, (0, 0, 0))
                surface.blit(textsurf,(self.width//2, self.height - self.height//4), 40)
                # screen when player wins

                
            if self.enemyWins > self.playerWins:
                self.endText = "You Lost!"
            


        #pygame.display.flip()
