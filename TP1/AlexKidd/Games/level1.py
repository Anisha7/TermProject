# game for level1

import pygame
#from game import *
from pygamegame import *

class RockPaperScissor(PygameGame):

    def __init__(self):
        
        super().__init__()

        self.surf = pygame.image.load('modules/Stage.png')
        self.rect = self.surf.get_rect
        #self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        # Game setup
        

    def update(self, pressed_keys):
        pass


    def draw(self, surface):
        surface.blit(self.surf, (self.width, self.height))
        circle1 = pygame.draw.circle(surface, (70, 165, 224), (300, 300), 20)
        #pygame.display.flip()
