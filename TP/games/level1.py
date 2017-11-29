# game for level1
#############################################################################

import pygame

from main.pygamegame import *
from main.player import *
import random

#############################################################################

class RockPaperScissor(PygameGame):

    def __init__(self, score):
        
        super().__init__()

        self.score = score

        self.surf = pygame.image.load('modules/Stage.png')
        self.rect = self.surf.get_rect
        self.surf = pygame.transform.smoothscale(self.surf, (950,600))

        # Game setup

        self.paper = pygame.image.load('modules/Game1/paper.png')
        self.paper = pygame.transform.smoothscale(self.paper, (100,100))
        self.rock = pygame.image.load('modules/Game1/rock.png')
        self.rock = pygame.transform.smoothscale(self.rock, (90,90))
        self.scissors = pygame.image.load('modules/Game1/scissors.png')
        self.scissors = pygame.transform.smoothscale(self.scissors, (80,100))
        self.moves = [self.paper, self.rock, self.scissors]
        self.i = 0
        self.playerMove = self.moves[0]
        n = random.randint(0,2)
        self.enemyMove = self.moves[0]
        
        # count wins
        self.enemyWins = 0
        self.playerWins = 0

        # who won
        self.endText = None

        self.playing = True

        self.prizes = [50,100,200,300,500]
        self.n = random.randint(0, 4)
        self.prize = 0
        self.count = 0

        self.enemyTurn = False


    def update(self, pressed_keys):

        # check if 3 games have played and get winner
        if self.enemyWins != self.playerWins:
            if self.enemyWins + self.playerWins >= 3:
                self.playing = False

        # if game is being played, get win counts
        if self.playing == True:
            if pressed_keys[K_RIGHT]:
                self.enemyTurn = False
                self.i += 1
                if self.i > 2:
                    self.i = 0

                self.endText = None
                
            if pressed_keys[K_LEFT]:
                self.enemyTurn = False
                self.i -= 1
                if self.i < 0:
                    self.i = 2

                self.endText = None
            #print(self.i)
            self.playerMove = self.moves[self.i]

            if pressed_keys[K_RETURN]:
                n = random.randint(0,2)
                self.enemyMove = self.moves[n]
                self.enemyTurn = True
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
            surface.blit(self.surf, (0 - 50, 0))
            surface.blit(self.playerMove, (950//4, self.height//2 - 100))
            if self.enemyTurn == True:
                #print("yes")
                surface.blit(self.enemyMove, (950 - 950//3, self.height//2 - 100))

            # scores
            
            playerScore = "Your Score: %d"%(self.playerWins)
            textsurf = myfont.render(playerScore, False, (0, 0, 0))
            surface.blit(textsurf,(self.width//4, 40))

            enemyScore = "Enemy Score: %d"%(self.enemyWins)
            textsurf = myfont.render(enemyScore, False, (0, 0, 0))
            surface.blit(textsurf,(950 - 950//3, 40))

            # who won each mini match
            if self.endText != None:
                textsurf = myfont.render(self.endText, False, (0, 0, 0))
                surface.blit(textsurf,(950//2, self.height//4))

        # end game screen, who won, what reward player gets
        if self.playing == False:
            # change font colors after testing code
            self.endsurf = pygame.draw.rect(surface, (255, 255, 255), (0, 0, 950, 600))
            #surface.blit(self.endsurf, (0, 0))
            # who won
            if self.playerWins > self.enemyWins:
                self.endText = "You Win!"
                textsurf = myfont.render(self.endText, False, (0, 0, 0))
                surface.blit(textsurf, (950//2, self.height//4))

                # what did player win
                
                # prize initialization
                self.prize = self.prizes[self.n]
                

                text = "You won %d coins!"%(self.prize)
                textsurf = myfont.render(text, False, (0, 0, 0))
                surface.blit(textsurf,(950//2, self.height//2))

                score = 0
                score += self.prize
                #Game.updateScore(prize)
                score = "Score: %d"%(score)
                textsurf = myfont.render(score, False, (0, 0, 0))
                surface.blit(textsurf,(950 - 10, 20))
                # put prize image here

                if self.count < 1:
                    self.score += self.prize
                    self.count += 1
                # screen when player wins

                
            if self.enemyWins > self.playerWins:
                self.endText = "You Lost!"
                textsurf = myfont.render(self.endText, False, (0, 0, 0))
                print("I'm here")
                surface.blit(textsurf,(950//2, self.height//2))
            
            exitInst = "Press ESC to exit Castle"
            textsurf = myfont.render(exitInst, False, (0, 0, 0))
            surface.blit(textsurf,(950//2, self.height - self.height//4))
            #self.endsurf.blit(textsurf,(self.width//2, self.height - self.height//4), 40)


        #pygame.display.flip()
