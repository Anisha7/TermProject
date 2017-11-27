# Attempt at scrolling
import pygame
from pygame.locals import *
from pygamegame import *
import math
#from GameObject import *
from game import *

#pygame.init()

class Environment(Game): 

    def __init__(self):
        super().__init__()
        # width, height
        # self.windowW = width
        # self.windowH = height
        # self.blue = (0, 0, 255)
        # self.groundImage = 'modules/level1/Ground1.png'

        # self.mapWidth = 2000
        # self.mapHeight = 700
        # mainMap = pygame.Surface((self.mapWidth, self.mapHeight))
        # self.mainMap = mainMap.convert()
        #Environment.draw()

    def draw(self):
        #self.mainMap.fill(self.blue)

        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (070, 165, 224)
        orange = (255, 100, 0)
        purple = (255, 0, 255)
        black = (0, 0, 0)
        white = (255, 255, 255)

        colors = [blue, orange, purple, white]
        rect1 = pygame.draw.rect(self.mainMap, red, (0, self.windowH - 25, 1700, self.windowH))
        circle1 = pygame.draw.circle(self.mainMap, white, (1000, 300), 20)
        circle1 = pygame.draw.circle(self.mainMap, purple, (1000, 200), 20)
        circle1 = pygame.draw.circle(self.mainMap, blue, (1000, 100), 20)

    def update(self, pressed_keys, keyCode, modifier):
        print(self.mapX, self.mapY)
        mapXc = -10
        if pressed_keys[K_LEFT]:
            self.mapX += mapXc
        if pressed_keys[K_RIGHT]:
            self.mapX -= mapXc

        if self.mapX > 0:
            self.mapX = 0
        if self.mapX < -(self.mapWidth-self.windowW):
            self.mapX = -(self.mapWidth-self.windowW)
        print(self.mapX, self.mapY)

        # while True:
        #     if pressed_keys[K_LEFT]:
        #         self.mapX += mapXc
        #     if pressed_keys[K_RIGHT]:
        #         self.mapX -= mapXc

        #     if self.mapX > 0:
        #         self.mapX = 0
        #     if self.mapX < -(self.mapWidth-self.windowW):
        #         self.mapX = -(self.mapWidth-self.windowW)
                

