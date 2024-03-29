# game for level2
#############################################################################

import pygame

from main.pygamegame import *
from main.player import *
from games.chineseCheckers import *
import random
import copy
import math

#############################################################################

class ChineseCheckers(object):
    """docstring for ChineseCheckers"""
    def __init__(self):
        super(ChineseCheckers, self).__init__()
        # Game setup

        # instructions screen
        self.start = False

        # make board
        #pygame.draw.polygon()
        #draw a shape with any number of sides
        #polygon(Surface, color, pointlist, width=0) -> Rect
        self.c = (400, 250) # center of board
        xc = self.c[0]
        yc = self.c[1]
        d = 120
        self.pointlist = [   (xc-d//2,yc-d), (xc+d//2, yc-d), 
                        (xc+d, yc),
                        (xc+d//2, yc+d), (xc-d//2, yc+d),
                        (xc-d, yc)
                    ]

        # triangle points
        self.t1 = [(xc-d//2,yc-d), (xc, yc-(d*2)) ,(xc+d//2, yc-d)]
        #((xc+d//2) + r*11
        self.t2 = [(xc+d//2, yc-d), (xc+180,yc-d)  ,(xc+d, yc)]
        self.t3 = [(xc+d, yc), (xc+180, yc+(d)), (xc+d//2, yc+d)]
        self.t4 = [(xc+d//2, yc+d),(xc, yc+(d*2)),(xc-d//2, yc+d)]
        self.t5 = [(xc-d//2, yc+d), (xc-180, yc+d) ,(xc-d, yc)]
        self.t6 = [(xc-d, yc), (xc-180,yc-d), (xc-d//2,yc-d)]

        r = 100//11
        self.r = r
        # pygame.draw.circle()
        # circle(Surface, color, pos, radius, width=0) -> Rect
        self.circlePoints =[    [((xc), (yc-(d*2)) + r*3)], # triangle 1 begins
                                [((xc - r*2 + 5), (yc-(d*2)) + r*6), ((xc + r*2 - 5), (yc-(d*2)) + r*6)],
                                [((xc - r*3 + 3), (yc-(d*2)) + r*9), ((xc), (yc-(d*2)) + r*9), 
                                    ((xc + r*3 - 3), (yc-(d*2)) + r*9)],
                                [((xc - r*4), (yc-(d*2)) + r*12),((xc - r*2 + 5), (yc-(d*2)) + r*12),
                                    ((xc + r*2 - 5), (yc-(d*2)) + r*12),((xc + r*4), (yc-(d*2)) + r*12)], # triangle 1 ends
                                [((xc-d//2) - r*11, (yc-d) + r+2), ((xc-d//2) - r*8, (yc-d) + r+2),
                                    ((xc-d//2) - r*5, (yc-d) + r+2), ((xc-d//2) - r*2, (yc-d) + r+2), #triangle6
                                    ((xc-d//2) + r, (yc-d) + r+2), ((xc-d//2) + r*4, (yc-d) + r+2), 
                                    ((xc-d//2) + r*7, (yc-d) + r+2), ((xc-d//2) + r*10, (yc-d) + r+2), 
                                    ((xc-d//2) + r*13, (yc-d) + r+2), # hexagon 1st line
                                    ((xc+d//2) + r*2, (yc-d) + r+2), ((xc+d//2) + r*5, (yc-d) + r+2), 
                                    ((xc+d//2) + r*8, (yc-d) + r+2), ((xc+d//2) + r*11, (yc-d) + r+2), #triangle2
                                ], # triangle 2, 6, and hexagon begins
                                [((xc-d//2) - r*6, (yc-d) + r*4), ((xc-d//2) - r*3, (yc-d) + r*4), 
                                    ((xc-d//2) - r*9, (yc-d) + r*4), #triangle6
                                    ((xc-d//2)-2, (yc-d) + r*4), ((xc-d//2) + r*3-2, (yc-d) + r*4), 
                                    ((xc-d//2) + r*6-2, (yc-d) + r*4), ((xc-d//2) + r*9-2, (yc-d) + r*4), 
                                    ((xc-d//2) + r*12-2, (yc-d) + r*4),((xc-d//2) + r*15-2, (yc-d) + r*4), # hexagon 2nd line
                                    ((xc+d//2) + r*4, (yc-d) + r*4), ((xc+d//2) + r*7, (yc-d) + r*4), 
                                    ((xc+d//2) + r*10, (yc-d) + r*4), #triangle2
                                ],
                                [((xc-d//2) - r*8 +3, (yc-d) + r*7), ((xc-d//2) - r*5, (yc-d) + r*7),  #triangle6
                                    ((xc-d//2) - r*2 + 2, (yc-d) + r*7), ((xc-d//2) + r-2, (yc-d) + r*7), 
                                    ((xc-d//2) + r*4-2, (yc-d) + r*7), ((xc-d//2) + r*7-2, (yc-d) + r*7), 
                                    ((xc-d//2) + r*10-2, (yc-d) + r*7), ((xc-d//2) + r*13-2, (yc-d) + r*7),
                                    ((xc-d//2) + r*16-2, (yc-d) + r*7), # hexagon 3rd line
                                    ((xc+d//2) + r*5, (yc-d) + r*7), ((xc+d//2) + r*8, (yc-d) + r*7) #triangle2
                                ],
                                [((xc-d//2) - r*6, (yc-d) + r*10), #triangle6
                                    ((xc-d//2) - r*2 -3, (yc-d) + r*10), ((xc-d//2), (yc-d) + r*10), 
                                    ((xc-d//2) + r*3 -4, (yc-d) + r*10), ((xc-d//2) + r*6 -4, (yc-d) + r*10), 
                                    ((xc-d//2) + r*9 -4, (yc-d) + r*10), ((xc-d//2) + r*12 -4, (yc-d) + r*10), 
                                    ((xc-d//2) + r*15 -4, (yc-d) + r*10),((xc-d//2) + r*17, (yc-d) + r*10), # hexagon 4th line
                                    ((xc+d//2) + r*6, (yc-d) + r*10) #triangle2
                                ], # triangle 2, 6 ends
                                [((xc-d//2) - r*6, (yc-d) + r*13), 
                                    ((xc-d//2)-r*3, (yc-d) + r*13), ((xc-d//2), (yc-d) + r*13), 
                                    ((xc-d//2) + r*3, (yc-d) + r*13), ((xc-d//2) + r*6, (yc-d) + r*13), 
                                    ((xc-d//2) + r*9, (yc-d) + r*13), ((xc-d//2) + r*12, (yc-d) + r*13), 
                                    ((xc-d//2) + r*15, (yc-d) + r*13),((xc-d//2) + r*18, (yc-d) + r*13)], # hexagon halfpoint
                                [((xc-d), yc + r*3), # triangle 5
                                    ((xc-d) + r*3, yc + r*3), ((xc-d) + r*6, yc + r*3), ((xc-d) + r*9, yc + r*3),
                                    ((xc-d) + r*12, yc + r*3), ((xc-d) +r*15, yc + r*3), ((xc-d) +r*18, yc + r*3),
                                    ((xc-d) +r*21, yc + r*3), ((xc-d) + r*24, yc + r*3), # hexagon 6th line
                                    (xc+d, yc + r*3) #triangle 3
                                ], # triangle 3,5 begin
                                [((xc-d) - r*2, yc + r*6), ((xc-d) + r, yc + r*6),# triangle 5
                                    ((xc-d) + r*4, yc + r*6), ((xc-d) + r*7, yc + r*6), ((xc-d) + r*10, yc + r*6),
                                    ((xc-d) + r*13, yc + r*6), ((xc-d) +r*16, yc + r*6), ((xc-d) +r*19, yc + r*6),
                                    ((xc-d) +r*22, yc + r*6), # hexagon 7th line
                                    (xc+d - r, yc + r*6), (xc+d + r*2, yc + r*6) #triangle 3
                                ],
                                [((xc-d) - r*4, yc + r*9), ((xc-d) - r, yc + r*9), ((xc-d) + r*2, yc + r*9),# triangle 5
                                    ((xc-d) + r*5, yc + r*9), ((xc-d) + r*8, yc + r*9), ((xc-d) + r*11, yc + r*9),
                                    ((xc-d) + r*14, yc + r*9), ((xc-d) +r*17, yc + r*9), ((xc-d) +r*20, yc + r*9), # hexagon 8th line
                                    (xc+d - r*3, yc + r*9), (xc+d, yc + r*9), (xc+d + r*3, yc + r*9) #triangle 3
                                ],
                                [((xc-d) - r*5, yc + r*12), ((xc-d) - r*2, yc + r*12), 
                                    ((xc-d) + r, yc + r*12), ((xc-d) + r*4, yc + r*12),# triangle 5
                                    ((xc-d) + r*7, yc + r*12), ((xc-d) + r*10, yc + r*12), ((xc-d) + r*13, yc + r*12),
                                    ((xc-d) + r*16, yc + r*12), ((xc-d) +r*19, yc + r*12), # hexagon 8th line
                                    (xc+d - r*4, yc + r*12), (xc+d - r, yc + r*12), 
                                    (xc+d + r*2, yc + r*12), (xc+d + r*5, yc + r*12) #triangle 3
                                ], # triangle 3,5 end
                                [(xc - r*4, yc+(d*2) - r*12), (xc - r, yc+(d*2) - r*12), (xc + r*2, yc+(d*2) - r*12), (xc + r*5, yc+(d*2) - r*12)], # triangle 4 begins
                                [(xc - r*3 + 3, yc+(d*2) - r*9), (xc, yc+(d*2) - r*9), (xc + r*3 - 3, yc+(d*2) -r*9)],
                                [(xc - r*2 + 5, yc+(d*2) - r*6), (xc + r*2 -5, yc+(d*2) - r*6)],
                                [(xc, (yc+(d*2) - r*3))] #triangle 4 ends
                            ]

        self.board = [
                [ 1],
                [ 1, 1],
                [ 1, 1, 1],
                [ 1, 1, 1, 1],
                [ 6, 6, 6, 6,-1,-1,-1,-1,-1, 2, 2, 2, 2],
                [ 6, 6, 6,-1,-1,-1,-1,-1,-1, 2, 2, 2],
                [ 6, 6,-1,-1,-1,-1,-1,-1, -1, 2, 2],
                [ 6,-1,-1,-1,-1,-1,-1,-1, -1, 2],
                [ -1,-1,-1,-1,-1,-1,-1,-1,-1],
                [ 5,-1,-1,-1,-1,-1,-1,-1,-1, 3],
                [ 5, 5,-1,-1,-1,-1,-1,-1,-1, 3, 3],
                [ 5, 5, 5,-1,-1,-1,-1,-1,-1, 3, 3, 3],
                [ 5, 5, 5, 5,-1,-1,-1,-1,-1, 3, 3, 3, 3],
                [ 4, 4, 4, 4],
                [ 4, 4, 4],
                [ 4, 4,],
                [ 4]

            ]

        self.board2 = [
                [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [ 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                  [ 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [ 6, 6, 6, 6,-1,-1,-1,-1,-1, 2, 2, 2, 2],
                  [ 6, 6, 6,-1,-1,-1,-1,-1,-1, 2, 2, 2],
                [ 0, 6, 6,-1,-1,-1,-1,-1,-1,-1, 2, 2, 0],
                  [0, 6,-1,-1,-1,-1,-1,-1,-1,-1, 2, 0],
                [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0],
                  [ 0, 5,-1,-1,-1,-1,-1,-1,-1,-1, 3, 0],
                [ 0, 5, 5,-1,-1,-1,-1,-1,-1,-1, 3, 3, 0],
                  [ 5, 5, 5,-1,-1,-1,-1,-1,-1, 3, 3, 3],
                [ 5, 5, 5, 5,-1,-1,-1,-1,-1, 3, 3, 3, 3],
                  [ 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0],
                  [ 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],

            ]
        board = copy.deepcopy(self.board)

        #print(getBoard(board))
        self.board2 = getBoard(board)
        #print(revertBoard(self.board2))

        #print(self.board2)

        circlePoints = copy.deepcopy(self.circlePoints)
        self.circlePoints2 = getBoard(circlePoints)
        #print(self.circlePoints2)


        self.selected = (0,6)
        self.chosen = None # when selected is entered
        self.moves = None # all moves for the chosen
        self.bonusmoves = None
        self.playerTurn = True
        self.turn = 1

        self.enemyMoved = dict()
        self.score = 0

        self.playerWon = False

    def win(self):
        win = 0

        winPoints = [(-1, 6), (-2, 5), (-2, 6), (-3, 5), (-3, 6), (-3, 7), 
                        (-4, 4), (-4, 5), (-4, 6), (-4, 7)]

        for point in winPoints:
            i = point[0]
            j = point[1]

            if self.board2[i][j] == 1:
                win += 1

        self.score = win*5

        if win == len(winPoints):
            self.playerWon = True
        
    def update(self, pressed_keys):
        print("UPDATING")

        self.win()

        if self.playerTurn == True:
            # tracking player navigation on board
            i = self.selected[0]
            j = self.selected[1]
            if pressed_keys[K_LEFT]:
                j -= 1
            if pressed_keys[K_RIGHT]:
                j += 1
            if pressed_keys[K_DOWN]:
                i += 1
            if pressed_keys[K_UP]:
                i -= 1

            if self.board2[i][j] != 0:
                self.selected = (i,j)

            # Selecting a piece for moves
            if self.chosen == None:
                if pressed_keys[K_RETURN]:
                    if self.board2[self.selected[0]][self.selected[1]] == 1:
                        self.chosen = self.selected
                        self.moves = moves(self.board2, self.chosen)
                        #self.bonusmoves = bonusMove(self.board2, self.chosen)
                        self.bonusmoves = legalBonusMoves(self.board2, self.chosen)
                    #self.bonusmoves = bonusMoves(self.board2, self.chosen)
                    #allMoves(self.board2, self.chosen)
                    print("moves", self.moves)
                    print("bonusmoves", self.bonusmoves)
                    print("legal bonus moves: ",legalBonusMoves(self.board2, self.chosen))
            else:
                if pressed_keys[K_RETURN]:
                    if self.selected == self.chosen:
                        self.chosen = None
                        self.moves = None
                        self.bonusmoves = None
                    elif (self.selected in self.moves):
                        self.board2[self.selected[0]][self.selected[1]] = 1
                        self.board2[self.chosen[0]][self.chosen[1]] = -1
                        self.chosen = None
                        self.moves = None
                        self.bonusmoves = None
                        self.turn += 1
                        self.playerTurn = False
                    elif (self.selected in self.bonusmoves):
                        self.board2[self.selected[0]][self.selected[1]] = 1
                        self.board2[self.chosen[0]][self.chosen[1]] = -1
                        self.chosen = None
                        self.moves = None
                        self.bonusmoves = None
                        self.turn += 1
                        self.playerTurn = False
                        # make move at self.selected

            if self.playerTurn == False:

                while self.turn <=6:
                    piecePos = []
                    for i in range(len(self.board2) - 1):
                        for j in range(len(self.board2[i]) - 1):
                            if self.board2[i][j]==self.turn:
                                piecePos += [(i,j)]

                    # make bonus move
                    piece = None
                    movepiece = None
                    l = 0 # length of move
                    for piece in piecePos:
                        bonusmoves = bonusMove(self.board2, piece)
                        print("bonuses: ", bonusmoves)
                        
                        if len(bonusmoves) <= 0:
                            continue

                        for bonusmovep in bonusmoves:
                            row = bonusmovep[0]
                            col = bonusmovep[1]
                            dist = int(math.sqrt(((piece[0]-row)**2) + ((piece[1]-col)**2)))
                            if dist > l:
                                if piece in self.enemyMoved.keys() and self.enemyMoved[piece] != movepiece:
                                    l = dist
                                    movepiece = bonusmovep
                                    piece = piece

                    print("piece: ", piece)
                    print("move: ", movepiece)

                    if piece != None and movepiece != None:
                        self.board2[piece[0]][piece[1]] = -1
                        self.board2[movepiece[0]][movepiece[1]] = self.turn
                        self.turn += 1
                        self.enemyMoved[piece] = movepiece

                    # if no bonus moves
                    else:

                        # pick random piece
                        i = random.randint(0, len(piecePos)-1)
                        piece = piecePos[i]
                        movepiece = None

                        normalmoves = moves(self.board2, piece)
                        # if no moves for the random piece
                        while normalmoves == None or len(normalmoves) < 1:
                            i = random.randint(0, len(piecePos)-1)
                            piece = piecePos[i]

                            normalmoves = moves(self.board2, piece)

                        if len(normalmoves) <= 1:
                            movepiece = normalmoves[0]
                            if piece in self.enemyMoved.keys() and self.enemyMoved[piece] != movepiece:
                                i = random.randint(0, len(piecePos)-1)
                                piece = piecePos[i]
                                normalmoves = moves(self.board2, piece)
                                movepiece = normalmoves[0]

                        else:
                            
                            j = random.randint(0, len(normalmoves)-1)
                            movepiece = normalmoves[j]
                            while piece in self.enemyMoved.keys() and self.enemyMoved[piece] == movepiece:
                                j = random.randint(0, len(normalmoves)-1)
                                movepiece = normalmoves[j]

                        if movepiece != None:
                            self.board2[piece[0]][piece[1]] = -1
                            self.board2[movepiece[0]][movepiece[1]] = self.turn
                            self.enemyMoved[piece] = movepiece
                        else:
                            print("NO MOVE??")


                self.turn = 1
                self.playerTurn = True

        print("updated",self.selected)
        

    def startScreen(self, surface):
        pass

    def gameScreen(self, surface):
        self.surf = pygame.draw.rect(surface, (244,187,144), [0, 0, 800, 500])
        pygame.draw.polygon(surface, (249,140,58), self.pointlist)
        pygame.draw.polygon(surface, (219,19,31), self.t1)
        pygame.draw.polygon(surface, (225,225,225), self.t2)
        pygame.draw.polygon(surface, (0,78,47), self.t3)
        pygame.draw.polygon(surface, (247,225,17), self.t4)
        pygame.draw.polygon(surface, (0,0,0), self.t5)
        pygame.draw.polygon(surface, (15,69,147), self.t6)

        for i in range(len(self.circlePoints2)):
            for j in range(len(self.circlePoints2[i])):
                point = self.circlePoints2[i][j]
                #print(self.selected)
                if point != 0:
                    color = (124,70,34)
                    if self.board2[i][j] == -1:
                        color = (124,70,34)
                    if self.board2[i][j] == 1:
                        color = (231,166,0)
                    if self.board2[i][j] == 2:
                        color = (71,68,61)
                    if self.board2[i][j] == 3:
                        color = (49,185,244)
                    if self.board2[i][j] == 4:
                        color = (139,2,16)
                    if self.board2[i][j] == 5:
                        color = (226,201,205)
                    if self.board2[i][j] == 6:
                        color = (67,130,114)

                    
                    if self.moves != None:
                        for move in self.moves:
                            if (i,j) == move:
                                color = (164, 205, 57)
                                
                    if self.bonusmoves != None:
                        for move in self.bonusmoves:
                            if (i,j) == move:
                                color = (164, 205, 57)

                    if (i,j) == self.selected:
                        color = (255, 0, 255)
                    if (i,j) == self.chosen:
                        color = (104, 13, 163)
                        # choose chosen color

                    pygame.draw.circle(surface, color, point, self.r)


        

    def endScreen(self, surface):
        self.surf = pygame.draw.rect(surface, (244,187,144), [0, 0, 800, 500])

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = "YOU WON"
        textsurf = myfont.render(text, False, (0, 0, 0))
        surface.blit(textsurf,(350, 200))

        text = "score: %d"%(self.player.score)
        textsurf = myfont.render(text, False, (0, 0, 0))
        surface.blit(textsurf,(350, 300))

    def draw(self, surface):
        if self.start == True:
            ChineseCheckers.startScreen(self, surface)
        elif self.playerWon == True:
            self.endScreen(surface)
        else:
            ChineseCheckers.gameScreen(self, surface)
            

