# level1-2 game
# checkers

class Checkers(PygameGame):
    def __init__(self):
        
        super().__init__()

        self.surf = pygame.image.load('modules/')
        self.rect = self.surf.get_rect
        #self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        # Game setup