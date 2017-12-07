# chinese checkers


# emptyBoard = [
#                 [ 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0,-1, 0,-1, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0,-1,-1, 0,-1,-1, 0, 0, 0, 0],
#                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
#                 [ 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
#                 [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0],
#                 [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0],
#                 [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0],
#                 [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0],
#                 [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0],
#                 [ 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
#                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
#                 [ 0, 0, 0, 0,-1,-1, 0,-1,-1, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0,-1, 0,-1, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0, 0],

#                 ]

# # players: 1,2,3,4,5,6
# fullBoard = [
#                 [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
#                 [ 6, 6, 6, 6,-1,-1,-1,-1,-1, 2, 2, 2, 2],
#                 [ 0, 6, 6, 6,-1,-1,-1,-1,-1,-1, 2, 2, 2],
#                 [ 0, 0, 6, 6,-1,-1,-1,-1,-1,-1, 2, 2, 0],
#                 [ 0, 0, 6,-1,-1,-1,-1,-1,-1,-1, 2, 0, 0],
#                 [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0],
#                 [ 0, 0,-1, 5,-1,-1,-1,-1,-1,-1, 3, 0, 0],
#                 [ 0, 0, 5, 5,-1,-1,-1,-1,-1,-1, 3, 3, 0],
#                 [ 0, 5, 5, 5,-1,-1,-1,-1,-1,-1, 3, 3, 3],
#                 [ 5, 5, 5, 5,-1,-1,-1,-1,-1, 3, 3, 3, 3],
#                 [ 0, 0, 0, 0, 4, 4, 0, 4, 4, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],

#             ]

# fullBoard = [
#                 [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#                   [ 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#                   [ 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#                 [ 6, 6, 6, 6,-1,-1,-1,-1,-1, 2, 2, 2, 2],
#                   [ 6, 6, 6,-1,-1,-1,-1,-1,-1, 2, 2, 2],
#                 [ 0, 6, 6,-1,-1,-1,-1,-1,-1,-1, 2, 2, 0],
#                   [0, 6,-1,-1,-1,-1,-1,-1,-1,-1, 2, 0],
#                 [ 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1, 0, 0],
#                   [ 0, 5,-1,-1,-1,-1,-1,-1,-1,-1, 3, 0],
#                 [ 0, 5, 5,-1,-1,-1,-1,-1,-1,-1, 3, 3, 0],
#                   [ 5, 5, 5,-1,-1,-1,-1,-1,-1, 3, 3, 3],
#                 [ 5, 5, 5, 5,-1,-1,-1,-1,-1, 3, 3, 3, 3],
#                   [ 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0],
#                   [ 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0],
#                 [ 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],

#             ]

# board = [
#                                 [ 1],
#                                [ 1, 1],
#                               [ 1, 1, 1],
#                              [ 1, 1, 1, 1],
#                 [ 6, 6, 6, 6,-1,-1,-1,-1,-1, 2, 2, 2, 2],
#                   [ 6, 6, 6,-1,-1,-1,-1,-1,-1, 2, 2, 2],
#                    [ 6, 6,-1,-1,-1,-1,-1,-1, -1, 2, 2],
#                      [ 6,-1,-1,-1,-1,-1,-1,-1, -1, 2],
#                        [ -1,-1,-1,-1,-1,-1,-1,-1,-1],
#                        [ 5,-1,-1,-1,-1,-1,-1,-1,-1, 3],
#                       [ 5, 5,-1,-1,-1,-1,-1,-1,-1, 3, 3],
#                     [ 5, 5, 5,-1,-1,-1,-1,-1,-1, 3, 3, 3],
#                    [ 5, 5, 5, 5,-1,-1,-1,-1,-1, 3, 3, 3, 3],
#                                  [ 4, 4, 4, 4],
#                                    [ 4, 4, 4],
#                                      [ 4, 4],
#                                        [ 4]

#             ]

import copy
# puts board in form that works for AI
def getBoard(board):
    for row in board:
        if len(row)%2 != 0:
            while len(row) < 13:
                row.insert(0,0)
                row.insert(len(row), 0)
        else:
            while len(row) < 12:
                row.insert(0,0)
                row.insert(len(row), 0)
    return board

# puts board back in start form for pygame
def revertBoard(board):
    newBoard = []

    for i in range(len(board)-1):
        row = []
        for j in range(len(board[i])-1):
            if board[i][j] != 0:
                row+= [board[i][j]]
        newBoard += [row]
        row = []

    return newBoard

def onBoard(board, row, col=0):

    if row < 0 or row >len(board)-1:
        return False

    if col < 0 or col > len(board[row])-1:
        return False

    return True

def moves(board, pos, all = False):
    movesl = []
    row = pos[0]
    col = pos[1]

    drow = row + 1
    urow = row - 1
    lcol = col - 1
    rcol = col + 1
    print("getting moves")
    possibleMoves = []
    if len(board[row])%2 != 0:
        possibleMoves = [(drow, lcol),(drow, col),
                            (row, lcol), (row, rcol),
                                (urow, col), (urow, lcol)]
    if len(board[row])%2 == 0:
        possibleMoves = [(drow, col), (drow, rcol),
                            (row, lcol), (row, rcol),
                                (urow, col), (drow, rcol)]
    print("possible moves: ", possibleMoves)
    for move in possibleMoves:
        if onBoard(board, move[0], move[1]):
            if all == False:
                if board[move[0]][move[1]] == -1:
                    movesl += [move]
            else:
                movesl += [move]
    print("moves: ", movesl)
    
    return movesl

def isFull(board, pos):
    if board[pos[0]][pos[1]] > 0:
        return True
    return False

def posMoves(board, pos):
    movesl = []
    row = pos[0]
    col = pos[1]

    drow = row + 1
    urow = row - 1
    lcol = col - 1
    rcol = col + 1
    print("getting moves")
    possibleMoves = []
    if len(board[row])%2 != 0:
        possibleMoves = [(drow, lcol),(drow, col),
                            (row, lcol), (row, rcol),
                                (urow, col), (urow, lcol)]
    if len(board[row])%2 == 0:
        possibleMoves = [(drow, col), (drow, rcol),
                            (row, lcol), (row, rcol),
                                (urow, col), (drow, rcol)]
    print("possible moves: ", possibleMoves)
    for move in possibleMoves:
        if onBoard(board, move[0], move[1]):
            if board[move[0]][move[1]] != 0:
                movesl += [move]
    print("moves: ", movesl)

    return movesl


def bonusMove(board, pos):
    # pos is selected pos
    movesL = moves(board, pos, True)
    print(movesL)
    bonuses = []
    for i in range(len(movesL)):
        if isFull(board, movesL[i]):
            print("I'm full: ", movesL[i])

            posMoves = moves(board, movesL[i])
            # possible moves

            for move in posMoves:
                if move in movesL:
                    continue
                if isFull(board, move):
                    continue
                else:
                    bonuses += [move]
    print("new bonuses: ", bonuses)
    return bonuses


# before calling the function: moves = moves(board, pos)
def legalBonusMoves(board, pos, legalMoves = None, c = 0):
    if legalMoves == None:
        legalMoves = []

    if len(legalMoves) == 0 and c > 0:
        return legalMoves

    else:
        posmoves = bonusMove(board, pos)

        for point in posmoves:
            legalMoves += [point] + legalBonusMoves(board, point, None, 1)

        return legalMoves



def bonusMoves(board, pos):
    

    board = getBoard(board)
    moveslistcopy = None
    moveslistcopy = moves(board, pos)
    bonusList = legalBonusMoves(board, pos, moveslistcopy)
    print("***legalBonusMoves(): ",legalBonusMoves(board, pos, moveslistcopy))
    print("bonuses: ",bonusList)
    # print("board: ", board)
    # print("moves(board, pos): ",moves(board, pos))
    # moveslist = moves(board, pos)
    # print("legalBonusMoves(board, pos): ",legalBonusMoves(board, pos, moveslist))
    # moveslistcopy = copy.deepcopy(moveslist)
    # bonusmoves = legalBonusMoves(board, pos, moveslistcopy)
    # moveslist += legalBonusMoves(board, pos, moveslistcopy)

    # allmovesList += bonusmoves
    return bonusList


