# background set up
import pygame
from pygamegame import *
import math
from GameObject import *

class Environment1(GameObject):  

    def __init__(self, x, y):
        
        # width, height
        self.x = x
        self.y = y
        
        # self.bgsurf = pygame.Surface((self.x*4, self.y*4))
        # self.bgsurf.fill((70, 165, 224))
        # rect = self.bgsurf.get_rect()
        Environment.setup(self)
    
        print(pygame.display.get_surface())
        self.screen = pygame.display.get_surface()
        self.viewport = self.screen.get_rect(bottom=self.rect.bottom)

        
        #self.viewport.clamp_ip(self.level_rect)
        
    
    def setup(self):
        Environment.bgsurf = pygame.Surface((self.x*4, self.y*4))
        Environment.bgsurf.fill((70, 165, 224))
        self.rect = Environment.bgsurf.get_rect()

        # creating ground
        Environment.ground = pygame.image.load('modules/level1/Ground1.png').convert_alpha()
        Environment.ground = pygame.transform.scale(Environment.ground, (self.x*4, self.y//4))
        self.rect = Environment.ground.get_rect()

        super(Environment, self).__init__(self.x, self.y, Environment.ground, 30)

    def update(self, keyCode, modifier):
        print("here")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print("right")
                self.viewport[i] += 10
                self.viewport.clamp_ip(self.rect)
                # scroll(dx, dy)
                Environment.bgsurf.scroll(10, 0)


            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print("left")
                # scroll(dx, dy)
                Environment.bgsurf.scroll(-10, 0)







