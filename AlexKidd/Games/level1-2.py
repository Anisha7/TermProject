# level1-2 game
# checkers
from pygamegame import *
from player import *
import random
#from game import Game

class Checkers(PygameGame):
    def __init__(self, surface):
        
        super().__init__()

        self.surf = pygame.draw.rect(surface, (0,0,0), [0, 0, self.width, self.height]) # background surface
        self.rect = self.surf.get_rect
        #self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        # Game setup
        # Making board
        rows = 9
        cols = 9
        board = []
        
        for i in range(rows):
            board.append(["E"]*cols) 
        self.boardH = board # tracks initial board values
        self.userBoard = copy.deepcopy(board) # tracks user input
        self.margin = 20
        self.squareSize = (data.width - data.margin) / 9
        # grid

    def drawBoard(self):
        pass

