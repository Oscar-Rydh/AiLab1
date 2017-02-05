import numpy
import copy
gameState = [[0 for i in range(8)] for j in range(8)]
playerOneTurn = True

def placeDisk(x,y):
    global playerOneTurn
    if(validPlay(x, y)):
        if(playerOneTurn):
            gameState[x][y] = 1
        else:
            gameState[x][y] = 2
        switchCheckers(x, y)
        playerOneTurn =  not playerOneTurn
    else:
        print ('Could not place disk')

def placementLegal(x, y):
    if (shouldISwitch('N', x, y-1, False, True)):
        return True
    elif (shouldISwitch('NE', x+1, y-1, False, True)):
        return True
    elif (shouldISwitch('E', x+1, y, False, True)):
        return True
    elif (shouldISwitch('SE', x+1, y+1, False, True)):
        return True
    elif (shouldISwitch('S', x, y+1, False, True)):
        return True
    elif (shouldISwitch('SW', x-1, y+1, False, True)):
        return True
    elif (shouldISwitch('W', x-1, y, False, True)):
        return True
    elif (shouldISwitch('NW', x-1, y-1, False, True)):
        return True
    else:
        return False


def switchCheckers(x, y):
    shouldISwitch('N', x, y-1, True, True)
    shouldISwitch('NE', x+1, y-1, True, True)
    shouldISwitch('E', x+1, y, True, True)
    shouldISwitch('SE', x+1, y+1, True, True)
    shouldISwitch('S', x, y+1, True, True)
    shouldISwitch('SW', x-1, y+1, True, True)
    shouldISwitch('W', x-1, y, True, True)
    shouldISwitch('NW', x-1, y-1, True, True)

def shouldISwitch(direction, x, y, switch, firstIteration = True):
    if (x > 7 or x < 0 or y > 7 or y < 0):
        return False
    global gameState
    #Check if other player has disc here
    otherPlayer = 20
    currentPlayer = 20
    if (playerOneTurn):
        otherPlayer = 2
        currentPlayer = 1
    else:
        otherPlayer = 1
        currentPlayer = 2
    if (gameState[x][y] == otherPlayer):
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
        ans = shouldISwitch(direction, x+dx, y+dy, switch, False)
        if(ans):
            # Change the disc
            if(switch):
                print ('Switching')
                gameState[x][y] = currentPlayer
                print (direction)
                print (str(x) + ' ' + str(y))
                print (gameState[x][y])
        return ans

    elif (gameState[x][y] == currentPlayer and not firstIteration):
        return True
    else:
        return False


def validPlay(x, y):
    return (gameState[x][y] is not 2 and gameState[x][y] is not 1) and placementLegal(x, y)

#Found on stackoverflow
def printGameState():
    #stateCopy = copy.deepcopy(gameState)
    printMatrix = [['·' for i in range(9)] for j in range(9)]

    printMatrix[0][0] = 0
    for col in range(8):
        printMatrix[col+1][0] = col+1
        printMatrix[0][col+1] = col+1
        for row in range(8):
            if(validPlay(col, row)):
                printMatrix[col+1][row+1] = '+'
            elif(gameState[col][row] is 1 or gameState[col][row] is  2):
                printMatrix[col+1][row+1] = gameState[col][row]


        #    if (placementLegal(col,row)):
        #        stateCopy[col][row] = '+'
        #    if (stateCopy[col][row] is not 0):
        #        printMatrix[col+1][row+1] = stateCopy[col][row]


    s = [[str(e) for e in row] for row in printMatrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '  '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))


def main():
    while (True):
        print ('')
        coordinates = [1]
        while(len(coordinates) != 2):
            if (playerOneTurn):
                print ('Player 1')
            else:
                print ('Player 2')
            coordinates = input('Give me your coordinates: \n').split(' ')

        x = int(coordinates[0]) - 1
        y = int(coordinates[1]) - 1
        placeDisk(x, y)
        printGameState()

gameState[3][3] = 1
gameState[4][4] = 1
gameState[3][4] = 2
gameState[4][3] = 2
printGameState()
main()