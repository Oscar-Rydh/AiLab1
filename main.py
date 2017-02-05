from game import GameState
from move import Move
from minimax import AI
import copy


game = GameState()
game.initialize()
while (True):
    coordinates = [1]
    while(len(coordinates) != 2):
        print ("")
        if (game.getPlayerOneTurn()):
            game.printGameState()
            coordinates = input('Give me your coordinates: \n').split(' ')
            print ('Player W')
            x = int(coordinates[0]) - 1
            y = int(coordinates[1]) - 1
            game.placeDisk(Move(x, y))
        else:
            #print ('Player B')
            ai = AI()
            aiGame = copy.deepcopy(game)
            aiGame.suppresPrint()
            action = ai.minimax(aiGame, 5)
            game.placeDisk(action['move'])

            print ('Comupter placed in: ' + str(action['move'].getX() + 1) + ' ' + str(action['move'].getY() + 1))





    if (len(game.validMoves()) == 0):
        if (game.stateValue() > 0):
            print ('Human Won!!')
        elif(game.stateValue() < 0):
            print ('Computer Won!!')
        else:
            print ('Its a draw!')
