# player set up
import pygame
from pygame.locals import *
from pygamegame import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((200, 155, 255))
        self.x = 0
        self.y = y - y//4
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        dist = 5

        if pressed_keys[K_UP]:
            self.y -= dist
        if pressed_keys[K_DOWN]:
            self.y += dist
        if pressed_keys[K_LEFT]:
            self.x -= dist
        if pressed_keys[K_RIGHT]:
            self.x += dist

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))