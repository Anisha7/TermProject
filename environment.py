# background set up
import pygame
from pygamegame import *
import math
from GameObject import *

class Environment(GameObject):

    def init(self, x, y):
        # width, height

        Environment.ground = pygame.image.load('modules/level1/Ground1.png').convert_alpha()
        Environment.ground = pygame.transform.scale(Environment.ground, (3*x, y//2))
        rect = Environment.ground.get_rect()
        rect.inflate(x, y//4)
        # Environment.ground = pygame.transform.scale(
        #     pygame.image.load('modules/level1/Ground1.png').convert_alpha(),
        #     (60, 100))

        

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(Environment, self).__init__(self.x, self.y, Environment.ground, 30)
        
    def keyPressed(self):
        pass