# level1-2 game
# checkers

#############################################################################

from main.pygamegame import *
from main.player import *
from games.checkers import *

import random

#############################################################################

class Checkers(PygameGame):
    def __init__(self):
        
        super().__init__()

        
        # Game setup

        # instructions screen
        self.start = False

        # Making board
        rows = 8
        cols = 8
        board = []
        
        for i in range(rows):
            board.append(["E"]*cols) 
         
        self.margin = 100
        self.squareSize = (500 - self.margin) // 8

        self.score = 0

        # self.player (red circle?)
        # player pieces: positions on board
        self.enemy =   [  (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
                            (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7)
                        ]
        self.killedEnemies = []
        # self.enemy (blue circle?)
        # enemy pieces: positions on board
        self.player =   [  (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7),
                            (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7)
                        ]
        self.killedPlayers = []

        self.board = getBoard(self.player, self.enemy, board)
        # initial row and col for player selected
        self.row = 0
        self.col = 0
        #self.selected = False
        self.selected = None
        self.playermoves = None

        # track turns
        self.playerTurn = True

        # check if game is over
        self.gameOver = True

    def startScreen(self, surface):
        pass

    def endScreen(self, surface):
        endsurf = pygame.draw.rect(surface, (0, 0, 0), (0, 0, 800, 500))

        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        if len(self.player) > len(self.enemy):
            endText = "You Win!"
            textsurf = myfont.render(endText, False, (255, 255, 255))
            surface.blit(textsurf, (400, 100))

            endText = "For each piece alive, you get +5 points."
            textsurf = myfont.render(endText, False, (255, 255, 255))
            surface.blit(textsurf, (400, 300))

            for i in self.player:
                self.score += 5

            endText = "Score: %d"%(self.score)
            textsurf = myfont.render(endText, False, (255, 255, 255))
            surface.blit(textsurf, (400, 250))

        else:
            endText = "You Lose!"
            textsurf = myfont.render(endText, False, (255, 255, 255))
            surface.blit(textsurf, (400, 100))

        exitInst = "Press ESC to exit Castle"
        textsurf = myfont.render(exitInst, False, (255, 255, 255))
        surface.blit(textsurf,(400, 450))  


    def gameScreen(self, surface):

        
        

        self.surf = pygame.draw.rect(surface, (183, 106, 47), [0, 0, 800, 500]) # background surface
        colorList = [(229, 212, 188), (71, 39, 19)]
        i = 0
        count = 0


        # Draw score
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        score = "Score: %d"%(self.score)
        textsurf = myfont.render(score, False, (0, 0, 0))
        surface.blit(textsurf,(400, 20))


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

                #if self.playerTurn == True:

                

                # highlighting selected player checker piece

                if self.selected != None:
                    #print("selected: ", self.selected)
                    #if row == self.selected[0] and col == self.selected[1]:
                    playermoves = getAllMoves(self.selected, self.board, self.player, self.enemy)
                    self.playermoves = playermoves
                    #print(playermoves)
                    for pos in playermoves:
                        posr = pos[0]
                        posc = pos[1]
                        if row == posr and col == posc:
                            color = (60, 247, 69)

                    if row == self.selected[0] and col == self.selected[1]:
                        color = (255,248,8)

                # highlighting selected rect
                if row == self.row and col == self.col:
                    color = (255, 0, 255)

                pygame.draw.rect(surface, color, [left, top, self.squareSize, self.squareSize])
             

        # draw player peices
        for pos in self.player:
            row = pos[0]
            col = pos[1]
            r = self.squareSize//2

            left = (self.squareSize * col) + self.margin//2 + 150 + r
            top = (self.squareSize * row) + self.margin//2 + r

            color = (255, 0, 0) # red
            
            pygame.draw.circle(surface, color, (left, top),r , 0)

        # draw enemy pieces
        for pos in self.enemy:
            #print("enemy: ", pos)
            row = pos[0]
            col = pos[1]

            r = self.squareSize//2

            left = (self.squareSize * col) + self.margin//2 + 150 + r
            top = (self.squareSize * row) + self.margin//2 + r

            color = (70, 165, 224) # blue

            pygame.draw.circle(surface, color, (left, top),r , 0)

        # # draw killed enemies

        for i in range(len(self.killedEnemies)):
            r = self.squareSize//2
            x = self.squareSize
            y = self.squareSize*i + self.margin

            if i > 7:
                x += self.squareSize*2
                y += self.squareSize*i + self.margin

            color = (70, 165, 224) # blue
            pygame.draw.circle(surface, color, (x, y),r , 0)

        # # draw killed players

        for i in range(len(self.killedPlayers)):
            r = self.squareSize//2
            x = self.squareSize + 550 + self.margin//2
            y = self.squareSize*i + self.margin

            if i > 7:
                x += self.squareSize
                y += self.squareSize*i + self.margin

            color = (255, 0, 0) # blue
            pygame.draw.circle(surface, color, (x, y),r , 0)


    def draw(self, surface):
        if self.start == True:
            Checkers.startScreen(self, surface)
        elif len(self.player) == 0 or len(self.enemy) == 0:
            Checkers.endScreen(self, surface)
        else:
            Checkers.gameScreen(self, surface)

    def timerFired(self):
        pass

    def update(self, pressed_keys):

        # if self.start == False:
        #     if pressed_keys[K_RETURN]:
        #         self.start = True

        # update board
        self.board = getBoard(self.player, self.enemy, self.board)

        if self.playerTurn == True:
            # tracking player navigation on board
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

            # if player piece is selected
            if self.selected == None:
                if pressed_keys[K_RETURN]:

                    row = self.row
                    col = self.col
                    if self.board[row][col] == 1:
                        self.selected = (row, col)

                    #print("I'm selected!", self.selected)

            else:
                # moving selected player piece to legal pos
                if pressed_keys[K_RETURN]:
                    point = (self.row, self.col)

                    if point == self.selected:
                        if pressed_keys[K_RETURN]:
                            self.selected = None

                    if (point in self.playermoves):
                        #print("HELLO THERE")
                        if self.selected in self.player:
                            #print("I'm Legal")
                            i = self.player.index(self.selected)
                            self.player[i] = point

                            # check if long jump
                            if abs(self.row - self.selected[0]) == 2:
                                enemyKilled = piecesKilled(self.selected, (self.row, self.col))
                                j = self.enemy.index(enemyKilled)
                                self.killedEnemies += [self.enemy.pop(j)]
                                print(self.killedEnemies)
                                self.score += 5
                                # check if enemy is killed

                            self.selected = None
                            self.playerTurn = False


            # deselecting player piece
            if pressed_keys[K_RSHIFT] or pressed_keys[K_LSHIFT]:
                self.selected = None

        # update board
        self.board = getBoard(self.player, self.enemy, self.board)
        
        # enemyTurn: pick best move for enemy, or random pick
        # created my own algorithm to pick the best move for the enemy
        if self.playerTurn == False:


            # pick random enemy
            i = random.randint(0,len(self.enemy) - 1)
            pos = self.enemy[i]

            # check if there is a bonus move for enemy
            for loc in self.enemy:
                bonusList = getBonusMoves2(loc[0], loc[1], self.board)
                if len(bonusList) > 0:
                    print("new loc: ", loc)
                    pos = loc
                    i = self.enemy.index(loc)

            # to make long jumps work for one and two kills

            # make a normal random move for enemy if no bonuses
            def makeMove(i, pos, moves):
                if len(moves) > 0:
                    if len(moves) == 1:
                        num = 0
                    else:
                        num = random.randint(0, len(moves) - 1)
                    
                    print("Moves: ", moves)
                    self.enemy[i] = moves[num]
                    moveMade = moves[num]
                    self.playerTurn = True
                    return

                else:
                    i = random.randint(0,len(self.enemy) - 1)
                    pos = self.enemy[i]
                    moves = getAllMoves2(pos, self.board, self.player, self.enemy)
                    makeMove(i, pos, moves)

            # find bonus moves
            moves = getAllMoves2(pos, self.board, self.player, self.enemy)
            bonusMoves = []
            for move in moves:
                if move[0] == pos[0] + 2:
                    bonusMoves += [move]

            # helper to make one jump or two jump enemy move
            def enemyBonusMove(i, bonusMoves, moveMade = None, count = 0):
                if count == 2:
                    self.playerTurn = True
                    return
                if len(bonusMoves) == 0:
                    return

                else:
                    # make one jump bonus move
                    
                    if len(bonusMoves) == 1:
                        num = 0
                    else:
                        num = random.randint(0, len(bonusMoves) - 1)
                    
                    self.enemy[i] = bonusMoves[num]
                    moveMade = bonusMoves[num]
                    # remove killed player
                    if moveMade != None:
                        if abs(moveMade[0] - pos[0]) == 2:
                            playerKilled = piecesKilled(moveMade, pos)
                            l = self.player.index(playerKilled)
                            self.killedPlayers += [self.player.pop(l)]
                            print(self.killedPlayers)
                            moveMade = None

                    # get new moves
                    moves = getAllMoves2(self.enemy[i], self.board, self.player, self.enemy)
                    bonusMoves = []
                    for move in moves:
                        if move[0] == pos[0] + 2:
                            bonusMoves += [move]

                    print("******2", bonusMoves)
                    if len(bonusMoves) > 0:
                        enemyBonusMove(i, bonusMoves, None, 1)
                    
                    return

            if len(bonusMoves) > 0:
                enemyBonusMove(i, bonusMoves)
                self.playerTurn = True

            else:
                makeMove(i, pos, moves)
                self.playerTurn = True

            # update board
            self.board = getBoard(self.player, self.enemy, self.board)

