# game for level2
#############################################################################

import pygame

from main.pygamegame import *
from main.player import *
from games.chineseCheckers import *
import random
import copy

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
                                [((xc-d//2) - r*2, (yc-d) + r+2), ((xc-d//2) - r*5, (yc-d) + r+2), 
                                    ((xc-d//2) - r*8, (yc-d) + r+2), ((xc-d//2) - r*11, (yc-d) + r+2), #triangle6
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
        self.playerTurn = True

    def update(self, pressed_keys):
        print("UPDATING")
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
            if pressed_keys[K_RETURN]:
                self.chosen = self.selected
                self.moves = allMoves(self.board2, self.chosen)
                print(self.moves)



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

        # for i in range(len(self.circlePoints)):
        #     for j in range(len(self.circlePoints[i])):
        #         point = self.circlePoints[i][j]
        #         color = (124,70,34)
        #         if self.board[i][j] == -1:
        #             color = (124,70,34)
        #         if self.board[i][j] == 1:
        #             color = (231,166,0)
        #         if self.board[i][j] == 2:
        #             color = (71,68,61)
        #         if self.board[i][j] == 3:
        #             color = (49,185,244)
        #         if self.board[i][j] == 4:
        #             color = (139,2,16)
        #         if self.board[i][j] == 5:
        #             color = (226,201,205)
        #         if self.board[i][j] == 6:
        #             color = (67,130,114)

        #         pygame.draw.circle(surface, color, point, self.r)


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

                    if (i,j) == self.selected:
                        color = (255, 0, 255)

                    pygame.draw.circle(surface, color, point, self.r)
        # for row in range(len(self.board2)):
        #     for col in range(len(self.board2[row])):
        #         for i in range(len(self.circlePoints)):
        #             for j in range(len(self.circlePoints[i])):
        #                 #col2 = 0
                
        #                 if self.board2[row][col] != 0:

        #                     point = self.circlePoints[i][j]
        #                     color = (124,70,34)

        #                     if self.board2[row][col] == -1:
        #                         color = (124,70,34)
        #                     if self.board2[row][col] == 1:
        #                         color = (231,166,0)
        #                     if self.board2[row][col] == 2:
        #                         color = (71,68,61)
        #                     if self.board2[row][col] == 3:
        #                         color = (49,185,244)
        #                     if self.board2[row][col] == 4:
        #                         color = (139,2,16)
        #                     if self.board2[row][col] == 5:
        #                         color = (226,201,205)
        #                     if self.board2[row][col] == 6:
        #                         color = (67,130,114)

        #                     pygame.draw.circle(surface, color, point, self.r)
        #                     # col2 +=1


        # for pointList in self.circlePoints:
        #     for point in pointList:
        #         color = (124,70,34)

                # pygame.draw.circle(surface, color, point, self.r)



    def endScreen(self, surface):
        pass

    def draw(self, surface):
        if self.start == True:
            ChineseCheckers.startScreen(self, surface)
        else:
            ChineseCheckers.gameScreen(self, surface)
            

