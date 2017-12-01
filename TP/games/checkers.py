# checkers helpers

# Wrote my own algorithms for making checkers work
# Such that it shows the player all moves it can make
# and helps pick the best move for the enemy (computer)

# check if checkers board move is legal

# plan
    # create function that generates all possible moves 
        # for given point and board

    # moves can only be diagonal
    # can only move if position is not full
    # can jump over opponent 
        # if next diagonal pos is empty
    # can make two jumps over oponent
        # if diagonal map is:
            # player, opponent, empty, opponent, empty


    # check for long jumps over enemy (recursive function?)
    # when using pos, if legal, make sure to
        # check distance between pos to del enemy
        # if long jump

#############################################################################
def getBoard(player1, player2, board):

    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = 'E'

    for tuple in player1:
        row = tuple[0]
        col = tuple[1]

        board[row][col] = 1

    for tuple in player2:
        row = tuple[0]
        col = tuple[1]

        board[row][col] = 2

    return board

def onBoard(row, col, board):
    # check if on board
    if row < 0:
        return False
    if row > 7:
        return False

    if col < 0:
        return False
    if col > 7:
        return False

    return True

def isLegalMove(pos, board):
    row = pos[0]
    col = pos[1]

    if not onBoard(row, col, board):
        return False
    # check if empty
    if board[row][col] == "E":
        return True

    return False

def queenList(player1):

    playerQueens = []
    for i in range(16):
        pos = player1[i]

        if pos[0] == 0:
            playerQueens += [i]

    return playerQueens


def queenList2(player2):
    enemyQueens = []
    for i in range(16):
        pos = player2[i]

        if pos[0] == 7:
            enemyQueens += [i]

    return enemyQueens

# check if a piece was killed
def onePieceKill(pos1, pos2):
    if abs(pos2[0] - pos1[0]) == 2:
        return True
    return False



def twoPieceKill(pos1, pos2):
    if abs(pos2[0] - pos1[0]) == 4:
        return True
    return False


# for one long jump
def piecesKilled(pos1, pos2):

    row1 = pos1[0] #player
    row2 = pos2[0] #enemy
    col1 = pos1[1]
    col2 = pos2[1]

    if row1 > row2:
        row = row1 - 1
    else:
        row = row1 + 1

    if col1 > col2:
        col = col1 - 1
    else:
        col = col1 + 1

    return (row,col)

#############################################################################
# for player

def getAllMoves(pos, board, player1, player2):
    # board[row-1][col+1]
    # board[row-1][col-1]
    # ifQueen: board[row+1][col+1], board[row+1][col-1]
    board = getBoard(player1, player2, board)
    row = pos[0]
    col = pos[1]
    legalMoves = []

    if isLegalMove((row-1,col+1), board):
        legalMoves += [(row-1, col+1)]
    if isLegalMove((row-1,col-1), board):
        legalMoves += [(row-1, col-1)]

    if onBoard(row-1, col+1, board):
        if board[row-1][col+1] == 2: 
            if isLegalMove((row-2, col+2), board):
                legalMoves += [(row-2, col+2)]
    if onBoard(row-1, col-1, board):
        if board[row-1][col-1] == 2: 
            if isLegalMove((row-2, col-2), board):
                legalMoves += [(row-2, col-2)]

    legalMoves += getBonusMoves(row, col, board)

    # if queens
    # playerQueens = queenList(player1)
    # for i in playerQueens:
    #     if (row,col) == player1[i]:
    #         legalMoves += getAllMoves2(pos, board, player2, player1)

    return legalMoves

# for enemy
def getBonusMoves(row, col, board, count = 0, bonusMoves = None):
    
    if bonusMoves == None:
        bonusMoves = []

    if count == 2:
        return bonusMoves

    else:
        if onBoard(row-1, col+1, board):
            if board[row-1][col+1] == 2: 
                if isLegalMove((row-2, col+2), board):
                    bonusMoves += [(row-2, col+2)]
                    bonusMoves += getBonusMoves2(row-2, col+2, board, count + 1, bonusMoves)

        if onBoard(row-1, col-1, board):
            if board[row-1][col-1] == 2: 
                if isLegalMove((row-2, col-2), board):
                    bonusMoves += [(row-2, col-2)]
                    bonusMoves += getBonusMoves2(row-2, col-2, board, count + 1, bonusMoves)

        return bonusMoves



#############################################################################           
# for enemy
def getAllMoves2(pos, board, player1, player2):
    # board[row+1][col+1]
    # board[row+1][col-1]
    # ifQueen: board[row-1][col+1], board[row-1][col-1]
    board = getBoard(player1, player2, board)
    row = pos[0]
    col = pos[1]
    legalMoves = []

    if isLegalMove((row+1,col+1), board):
        legalMoves += [(row+1, col+1)]
    if isLegalMove((row+1,col-1), board):
        legalMoves += [(row+1, col-1)]

    # check for long jumps over enemy
    # when using this pos, if legal, make sure to
        # check distance between pos to del enemy
        # if long jump
    if onBoard(row+1, col+1, board):
        if board[row+1][col+1] == 1: 
            if isLegalMove((row+2, col+2), board):
                legalMoves += [(row+2, col+2)]
            # check for double long jump
            
    if onBoard(row+1, col-1, board):
        if board[row+1][col-1] == 1: 
            if isLegalMove((row+2, col-2), board):
                legalMoves += [(row+2, col-2)]

    legalMoves += getBonusMoves2(row, col, board)

    # enemyQueens = queenList2(player2)
    # for i in enemyQueens:
    #     if (row,col) == player2[i]:
    #         legalMoves += getAllMoves(pos, board, player2, player1)
    print(legalMoves)
    return legalMoves


# for enemy
def getBonusMoves2(row, col, board, count = 0, bonusMoves = None):
    
    if bonusMoves == None:
        bonusMoves = []

    if count == 2:
        return bonusMoves

    else:
        if onBoard(row+1, col+1, board):
            if board[row+1][col+1] == 1: 
                if isLegalMove((row+2, col+2), board):
                    bonusMoves += [(row+2, col+2)]
                    bonusMoves += getBonusMoves2(row+2, col+2, board, count + 1, bonusMoves)
        if onBoard(row+1, col-1, board):
            if board[row+1][col-1] == 1: 
                if isLegalMove((row+2, col-2), board):
                    bonusMoves += [(row+2, col-2)]
                    bonusMoves += getBonusMoves2(row+2, col-2, board, count + 1, bonusMoves)

        return bonusMoves



