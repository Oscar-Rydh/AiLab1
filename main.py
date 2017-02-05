from game import GameState
import minimax


game = GameState()
game.initialize()
game.printGameState()
while (True):
    print ('')
    coordinates = [1]
    while(len(coordinates) != 2):
        if (game.getPlayerOneTurn()):
            print ('Player W')
        else:
            print ('Player B')
        coordinates = input('Give me your coordinates: \n').split(' ')

    x = int(coordinates[0]) - 1
    y = int(coordinates[1]) - 1
    game.placeDisk(x, y)
    game.printGameState()
    if(game.checkWin()):
        if(game.getPlayerOneTurn()):
            print ('Winner is: Player B')

        else:
            print ('Winner is: Player W')
        break