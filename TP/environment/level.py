# level setup

#############################################################################

import pygame
import random

from game import Game
from main.pygamegame import *
from main.player import *
from environment.enemy import *
from environment.castle import *

############################################################################

pygame.font.init()
red = (255, 0, 0)
blue = (70, 165, 224)
purple = (255, 0, 255)
white = (255, 255, 255)

############################################################################

class Level(Game):
    def __init__(self):
        super().init()

    def one(self, screen):
        # draw castle
        self.castle.draw(self.mainMap)
        self.castle2.draw(self.mainMap)

        # draw trees

        # draw ground
        #rect1 = pygame.draw.rect(self.mainMap, white, (0, self.windowH - 25, 1700, self.windowH))
        surf = pygame.image.load(self.groundImage)
        surf = pygame.transform.smoothscale(surf, (1700, self.windowH//4))
        #pygame.Surface.blit(self.mainMap, surf, rect1)
        screen.blit(surf, (0, self.windowH))

        # draw finish line flag
        flag = pygame.image.load('modules/finishFlag.png')
        self.mainMap.blit(flag, (self.mapWidth - 350, self.windowH//4))

        # check if player finished level1
        # if self.player.x >= self.mapWidth - 350:
        #     self.levelOver = True
        #     self.player.level += 1
        
        # enemies

        self.enemies.draw(self.mainMap)

        # coins

        # treasure chests 

    def levelDraw(self, screen):
        if self.level == 1:
            Level.one(screen)


