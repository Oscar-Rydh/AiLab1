import copy

class AI:

    def minimax(self, gameState, depth, maximizingplayer = True):

        if (depth == 0 or len(gameState.validMoves()) == 0):
            return {'move': None, 'value': gameState.stateValue()}


        if maximizingplayer:
            moves = []
            for move in gameState.validMoves():
                newGameState = copy.deepcopy(gameState)
                newGameState.placeDisk(move)
                value = self.minimax(newGameState, depth-1, False)['value']
                moveAndValue = {'move': move,'value': value}
                moves.append(moveAndValue)
            bestMove = {'value': -1000000}
            for moveAndValue in moves:
                if moveAndValue['value'] > bestMove['value']:
                    bestMove = moveAndValue
            return bestMove

        else:
            moves = []
            for move in gameState.validMoves():
                newGameState = copy.deepcopy(gameState)
                newGameState.placeDisk(move)
                value = self.minimax(newGameState, depth-1, True)['value']
                moveAndValue = {'move': move,'value': value}
                moves.append(moveAndValue)
            bestMove = {'value': 1000000}
            for moveAndValue in moves:
                if moveAndValue['value'] < bestMove['value']:
                    bestMove = moveAndValue
            return bestMove