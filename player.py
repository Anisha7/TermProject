# player set up
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.x = 0
        self.y = 0
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        dist = 5

        if pressed_keys[K_UP]:
            #move_ip = move in place
            #self.rect.move_ip(0, -5)
            self.y -= dist
        if pressed_keys[K_DOWN]:
            self.y += dist
            #self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.x -= dist
            #self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.x += dist
            #self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))