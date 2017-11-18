import pygame
from pygamegame import PygameGame


def test_set_at(self):

        #24bit surfaces 
        s = pygame.Surface( (100, 100), 0, 24)
        s.fill((0,0,0))

        # set it with a tuple.
        s.set_at((0,0), (10,10,10, 255))
        r = s.get_at((0,0))
        self.failUnless(isinstance(r, pygame.Color))
        self.assertEqual(r, (10,10,10, 255))

        # try setting a color with a single integer.
        s.fill((0,0,0,255))
        s.set_at ((10, 1), 0x0000FF)
        r = s.get_at((10,1))
        self.assertEqual(r, (0,0,255, 255))
test_set_at()

class myProject(PygameGame):
    def init(self):
        self.message = "World Helo"
    def mousepressed(self, x, y):
        print(self.message)

#creating and running the game
game = myProject()
game.run()