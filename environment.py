# background set up
import pygame
from pygamegame import *
import math
from GameObject import *

class Environment(GameObject):

    def init(self, x, y):
        # width, height

        # setting up background surface
        Environment.bgsurf = pygame.Surface((x*4, y*4))
        Environment.bgsurf.fill((70, 165, 224))
        rect = Environment.bgsurf.get_rect()

        # creating ground
        Environment.ground = pygame.image.load('modules/level1/Ground1.png').convert_alpha()
        Environment.ground = pygame.transform.scale(Environment.ground, (x*4, y//2))
        rect = Environment.ground.get_rect()
        rect.inflate(x, y//4)
        # Environment.ground = pygame.transform.scale(
        #     pygame.image.load('modules/level1/Ground1.png').convert_alpha(),
        #     (60, 100))

        

    def __init__(self, width, height):
        self.w = width
        self.h = height

        super(Environment, self).__init__(self.w, self.h, Environment.ground, 30)
        
    def update(self, keyCode, modifier):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print("right")
                # scroll(dx, dy)
                Environment.bgsurf.scroll(3, 0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print("left")
                # scroll(dx, dy)
                Environment.bgsurf.scroll(-3, 0)





