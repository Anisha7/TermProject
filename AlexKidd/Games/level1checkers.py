# level1-2 game
# checkers
from pygamegame import *
from player import *
import random
#from game import Game

class Checkers(PygameGame):
    def __init__(self):
        
        super().__init__()

        self.surf = None # background surface init
        self.rect = None
        #self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        # Game setup
        # Making board
        rows = 8
        cols = 8
        board = []
        
        for i in range(rows):
            board.append(["E"]*cols) 
        self.board = board # tracks initial board values
        #self.userBoard = copy.deepcopy(board) # tracks user input
        self.margin = 20
        self.squareSize = (self.width - self.margin) / 8
        # grid

    def draw(self, surface):
        self.surf = pygame.draw.rect(surface, (0,0,0), [0, 0, 950, 600]) # background surface
        self.rect = self.surf.get_rect
        
        # create grid
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                color = "pink"
                
                # highlighting a cell
                #[rowH, colH] = data.highlightCell
                #print(rowH, colH)
                if rowH == row and colH == col:
                    color = "purple"
                
                # draw board
                left = (self.squareSize * col) + margin/2
                #print("left: ", left)
                top = (self.squareSize * row) + margin/2
                right = (self.squareSize * (col + 1)) + margin/2
                bottom = (self.squareSize * (row + 1)) + margin/2

                #anvas.create_rectangle(left, top, right, bottom,
                       # width = 1, fill = color, outline = "purple")

                pygame.draw.rect(surface, (125,125,125), [left, top, right, bottom])
             

