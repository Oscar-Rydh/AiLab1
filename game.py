import copy

class GameState:

    def __init__(self, gameState = None, playerOneTurn = None, width = 8):
        if width%2 is not 0:
            width = width+1
        self.width = width
        self.gameState = [[0 for i in range(width)] for j in range(width)]
        self.playerOneTurn = True
        if(gameState is not None):
            self.gameState = gameState
        if(playerOneTurn is not None):
            self.playerOneTurn = playerOneTurn

    def __deepcopy__(self, memo):
        newState = [[] for j in range(self.width)]
        for i in range(self.width):
            newState[i] = copy.deepcopy(self.gameState[i]);


        newPlayerTurn = copy.deepcopy(self.playerOneTurn)
        return GameState(newState, newPlayerTurn);


    def initialize(self):
        middleSmall = int((self.width/2)-1)
        middleLarge = int(self.width/2)
        self.gameState[middleSmall][middleLarge] = -1
        self.gameState[middleLarge][middleSmall] = -1
        self.gameState[middleSmall][middleSmall] = 1
        self.gameState[middleLarge][middleLarge] = 1

    def getPlayerOneTurn(self):
        return self.playerOneTurn

    def placeDisk(self, x,y):
        # global playerOneTurn
        if(self.validPlay(x, y)):
            if(self.playerOneTurn):
                self.gameState[x][y] = 1
            else:
                self.gameState[x][y] = -1
            self.switchCheckers(x, y)
            self.playerOneTurn =  not self.playerOneTurn
        else:
            print ('Could not place disk')

    def placementLegal(self, x, y):
        if (self.shouldISwitch('N', x, y-1, False, True)):
            return True
        elif (self.shouldISwitch('NE', x+1, y-1, False, True)):
            return True
        elif (self.shouldISwitch('E', x+1, y, False, True)):
            return True
        elif (self.shouldISwitch('SE', x+1, y+1, False, True)):
            return True
        elif (self.shouldISwitch('S', x, y+1, False, True)):
            return True
        elif (self.shouldISwitch('SW', x-1, y+1, False, True)):
            return True
        elif (self.shouldISwitch('W', x-1, y, False, True)):
            return True
        elif (self.shouldISwitch('NW', x-1, y-1, False, True)):
            return True
        else:
            return False


    def switchCheckers(self, x, y):
        self.shouldISwitch('N', x, y-1, True, True)
        self.shouldISwitch('NE', x+1, y-1, True, True)
        self.shouldISwitch('E', x+1, y, True, True)
        self.shouldISwitch('SE', x+1, y+1, True, True)
        self.shouldISwitch('S', x, y+1, True, True)
        self.shouldISwitch('SW', x-1, y+1, True, True)
        self.shouldISwitch('W', x-1, y, True, True)
        self.shouldISwitch('NW', x-1, y-1, True, True)

    def shouldISwitch(self, direction, x, y, switch, firstIteration = True):
        if (x > 7 or x < 0 or y > 7 or y < 0):
            return False
        # global gameState
        #Check if other player has disc here
        otherPlayer = 20
        currentPlayer = 20
        if (self.playerOneTurn):
            otherPlayer = -1
            currentPlayer = 1
        else:
            otherPlayer = 1
            currentPlayer = -1
        if (self.gameState[x][y] == otherPlayer):
            #Fetch direction
            dx = 0
            dy = 0
            if(direction == 'N'):
                dx = 0
                dy = -1
            elif (direction == 'NE'):
                dx = 1
                dy = -1
            elif (direction == 'E'):
                dx = 1
                dy = 0
            elif (direction == 'SE'):
                dx = 1
                dy = 1
            elif (direction == 'S'):
                dx = 0
                dy = 1
            elif (direction == 'SW'):
                dx = -1
                dy = 1
            elif (direction == 'W'):
                dx = -1
                dy = 0
            elif (direction == 'NW'):
                dx = -1
                dy = -1
            #ask the next cell
            ans = self.shouldISwitch(direction, x+dx, y+dy, switch, False)
            if(ans):
                # Change the disc
                if(switch):
                    print ('Switching')
                    self.gameState[x][y] = currentPlayer
                    print (direction)
                    print (str(x) + ' ' + str(y))
                    print (self.gameState[x][y])
            return ans

        elif (self.gameState[x][y] == currentPlayer and not firstIteration):
            return True
        else:
            return False


    def validPlay(self, x, y):
        return (self.gameState[x][y] is not -1 and self.gameState[x][y] is not 1) and self.placementLegal(x, y)

    #Found on stackoverflow
    def printGameState(self):
        printMatrix = [['·' for i in range(9)] for j in range(9)]

        printMatrix[0][0] = 0
        for col in range(self.width):
            printMatrix[col+1][0] = col+1
            printMatrix[0][col+1] = col+1
            for row in range(self.width):
                if(self.validPlay(col, row)):
                    printMatrix[col+1][row+1] = '+'
                elif(self.gameState[col][row] is 1 ):
                    printMatrix[col+1][row+1] = 'W'
                elif(self.gameState[col][row] is  -1):
                    printMatrix[col+1][row+1] = 'B'


                    #    if (placementLegal(col,row)):
            #        stateCopy[col][row] = '+'
            #    if (stateCopy[col][row] is not 0):
            #        printMatrix[col+1][row+1] = stateCopy[col][row]


        s = [[str(e) for e in row] for row in printMatrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '  '.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print ('\n'.join(table))


    def checkWin(self):
        winner = set()
        for col in range(self.width):
            for row in range(self.width):
                if(self.gameState[col][row] is not 0):
                    winner.add(self.gameState[col][row])

                if(len(winner) > 1):
                    return False

        return True
