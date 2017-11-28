# level1-2 game
# checkers
from main.pygamegame import *
from main.player import *
import random
#from game import Game

class Checkers(PygameGame):
    def __init__(self):
        
        super().__init__()

        #self.surf = pygame.draw.rect(surface, (125,125,125), [0, 0, 950, 600]) # background surface init
        #self.rect = None
        #self.surf = pygame.transform.smoothscale(self.surf, (400,400))

        # Game setup
        # Making board
        rows = 8
        cols = 8
        board = []
        
        for i in range(rows):
            board.append(["E"]*cols) 
        self.board = board 
        self.margin = 100
        self.squareSize = (500 - self.margin) // 8

        # self.player (red circle?)
        # player pieces: positions on board
        self.player =   [  (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
                            (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7)
                        ]
        # self.enemy (blue circle?)
        # enemy pieces: positions on board
        self.enemy =   [  (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7),
                            (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7)
                        ]

        # initial row and col for player selected
        self.row = 0
        self.col = 0
        self.selected = False

    def draw(self, surface):
        self.surf = pygame.draw.rect(surface, (183, 106, 47), [0, 0, 800, 500]) # background surface
        colorList = [(229, 212, 188), (71, 39, 19)]
        i = 0
        count = 0
        # create grid
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                
                # draw board
                left = (self.squareSize * col) + self.margin/2 + 150
                #print("left: ", left)
                top = (self.squareSize * row) + self.margin/2
                right = (self.squareSize * (col + 1)) + self.margin/2
                bottom = (self.squareSize * (row + 1)) + self.margin/2

                # getting interchanging color
                color = colorList[i]

                count += 1
                i += 1
                if i > 1:
                    i = 0

                if count > 7:
                    count = 0
                    if i == 1:
                        i = 0
                    else:
                        i = 1

                # highlighting selected rect
                if row == self.row and col == self.col:
                    color = (255, 0, 255)

                pygame.draw.rect(surface, color, [left, top, self.squareSize, self.squareSize])
             
        for pos in self.player:
            row = pos[0]
            col = pos[1]
            r = self.squareSize//2

            left = (self.squareSize * col) + self.margin//2 + 150 + r
            top = (self.squareSize * row) + self.margin//2 + r

            color = (255, 0, 0) # red
            #print("circle testing")
            #print(left)
            #print(top)
            #print(self.squareSize)
            pygame.draw.circle(surface, color, (left, top),r , 0)

        for pos in self.enemy:
            row = pos[0]
            col = pos[1]
            r = self.squareSize//2

            left = (self.squareSize * col) + self.margin//2 + 150 + r
            top = (self.squareSize * row) + self.margin//2 + r

            color = (70, 165, 224) # blue

            #print("circle testing")
            #print(left)
            #print(top)
            #print(self.squareSize)
            pygame.draw.circle(surface, color, (left, top),r , 0)

    def update(self, pressed_keys):
        
        if self.selected == False:
            if pressed_keys[K_LEFT]:
                if self.col > 0:
                    self.col -= 1
            if pressed_keys[K_RIGHT]:
                if self.col < 7:
                    self.col += 1
            if pressed_keys[K_DOWN]:
                if self.row < 7:
                    self.row += 1
            if pressed_keys[K_UP]:
                if self.row > 0:
                    self.row -= 1

        if pressed_keys[K_RETURN]:
            self.selected = True

        if self.selected == True:
            row = self.row
            col = self.col
            # pos for self.player tuple

            # write is legal function for checkers
            # if islegal


