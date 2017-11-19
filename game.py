# Game.py
# Actually implements the game
import pygame
from pygamegame import *
from environment import *
from player import *

class Game(PygameGame):
    def init(self):
        super().__init__()
        self.bgColor = (70, 165, 224)

        Environment.init(self, self.width, self.height)
        self.groundGroup = pygame.sprite.Group(Environment(0, self.height))


    def keyPressed(self, keyCode, modifier):
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        Environment.update(self, keyCode, modifier)

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        x = 0
        y = 0
        #surface.blit(source, dest, area=None)
        screen.blit(Environment.bgsurf, (0, 0, self.width, self.height))
        Environment.bgsurf.blit(Environment.ground, pygame.Rect(0,self.height - (self.height//4),self.width*6,self.height//2))
        # draw ground
        #screen.blit(Environment.bgsurf, (0, 0))
        #screen.blit(Environment.ground, pygame.Rect(0,self.height - (self.height//4),self.width*6,self.height//2))
        
        player = Player(self.width, self.height)
        player.draw(screen)
        #self.groundGroup.draw(screen)

Game(800, 500).run()