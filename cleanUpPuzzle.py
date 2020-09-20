from search import Problem
from board import toggleCell
from board import getAffectedCellsByPosition
from board import parseBoard


#### allow actions
TAB = 'TAB'

class CleanUpPuzzle(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
       
    # actions
    # computes all possible movements
    # that can be perfomed on the state
    def actions(self, state):
        return getPossibleMovements(state)

    # result
    # changes the state based on a given action
    def result(self, state, action):
        return toggleCell(state, action[1])

# getPossibleMovements scans the full board
# which is not optimal (a more efficient algorithm is needed)
def getPossibleMovements(state):
    board = parseBoard(state)
    size = len(board)
    actions = []
    for row in range(size):
        for col in range(size):
            affectedCells = getAffectedCellsByPosition((row, col), size)
            for cell in affectedCells:
                if board[cell[0]][cell[1]] == '1':
                    actions.append((TAB, (row, col)))
                    break
    return actions