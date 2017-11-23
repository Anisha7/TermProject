# enemies set up
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()


        self.surf = pygame.Surface((75, 25))
        self.surf.fill((200, 165, 205))
        self.x = x//6 - x//2
        self.y = y//2
        self.rect = self.surf.get_rect()
        self.count = 0

        self.enemies = pygame.sprite.Group()


    def update(self):
        
        dist = 2
        if self.count == 5:
            dist *= -1
            count = 0
       
        self.x += dist
        self.count += 1


    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))