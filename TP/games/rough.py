#### old code
def enemyMove(i, pos):
                moves = getAllMoves2(pos, self.board, self.player, self.enemy)
                bonusMoves = []
                # track what move was made
                moveMade = None
                print("moves: ", moves)
                for move in moves:
                    if move[0] == pos[0] + 4:
                        print("***",move)
                        bonusMoves += move

                if len(bonusMoves) > 0:
                    if len(bonusMoves) == 1:
                        num = 0
                    else:
                        num = random.randint(0, len(bonusMoves) - 1)
                    print("bonusMoves: ", bonusMoves)
                    self.enemy[i] = bonusMoves[num]
                    moveMade = bonusMoves[num]
                    self.playerTurn = True

                else:

                    for move in moves:
                        if move[0] == pos[0] + 2:
                            bonusMoves += [move]

                    if len(bonusMoves) > 0:
                        if len(bonusMoves) == 1:
                            num = 0
                        else:
                            num = random.randint(0, len(bonusMoves) - 1)
                        print("bonusMoves2: ", bonusMoves)
                        self.enemy[i] = bonusMoves[num]
                        moveMade = bonusMoves[num]
                        self.playerTurn = True

                    else:
                        #num = 0
                        # use try and except for value error
                        if len(moves) <= 0:
                            i = random.randint(0,len(self.enemy) - 1)
                            pos = self.enemy[i]
                            enemyMove(i, pos)
                        else:
                            if len(moves) == 1:
                                num = 0
                            else:
                                num = random.randint(0, len(moves) - 1)
                            

                            print("Moves: ", moves)
                            self.enemy[i] = moves[num]
                            moveMade = moves[num]
                            self.playerTurn = True

                if moveMade != None:
                    if abs(moveMade[0] - pos[0]) == 2:
                        playerKilled = piecesKilled(moveMade, pos)
                        l = self.player.index(playerKilled)
                        self.killedPlayers += [self.player.pop(l)]
                        print(self.killedPlayers)
                        moveMade = None


#### improved code

# find bonus moves
moves = getAllMoves2(pos, self.board, self.player, self.enemy)
bonusMoves = []


for move in moves:
    if move[0] == pos[0] + 2:
        bonusMoves += [move]


 if len(bonusMoves) > 0:
                enemyBonusMove(i, bonusMoves)

            else:
                moveMade = None
                if len(moves) <= 0:
                    i = random.randint(0,len(self.enemy) - 1)
                    pos = self.enemy[i]
                    enemyMove(i, pos)
                else:
                    if len(moves) == 1:
                        num = 0
                    else:
                        num = random.randint(0, len(moves) - 1)
                    
                    print("Moves: ", moves)
                    self.enemy[i] = moves[num]
                    moveMade = moves[num]
                    self.playerTurn = True

                if moveMade != None:
                    if abs(moveMade[0] - pos[0]) == 2:
                        playerKilled = piecesKilled(moveMade, pos)
                        l = self.player.index(playerKilled)
                        self.killedPlayers += [self.player.pop(l)]
                        print(self.killedPlayers)
                        moveMade = None

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


# helper to make one jump or two jump enemy move
def enemyBonusMove(i, bonusMoves, moveMade = None, count = 0):
    if count == 2:
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

        enemyBonusMove(i, bonusMoves, None, 1)
        self.playerTurn = True

        return

if len(bonusMoves) > 0:
    enemyBonusMove(i, bonusMoves)

else:
    moveMade = None
    if len(moves) <= 0:
        i = random.randint(0,len(self.enemy) - 1)
        pos = self.enemy[i]
        enemyMove(i, pos)
    else:
        if len(moves) == 1:
            num = 0
        else:
            num = random.randint(0, len(moves) - 1)
        
        print("Moves: ", moves)
        self.enemy[i] = moves[num]
        moveMade = moves[num]
        self.playerTurn = True

    if moveMade != None:
    if abs(moveMade[0] - pos[0]) == 2:
        playerKilled = piecesKilled(moveMade, pos)
        l = self.player.index(playerKilled)
        self.killedPlayers += [self.player.pop(l)]
        print(self.killedPlayers)
        moveMade = None


