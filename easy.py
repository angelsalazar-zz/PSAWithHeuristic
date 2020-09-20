from board import buildGrid
from board import toggleCell
from board import buildGrid
from board import parseBoard
from cleanUpPuzzle import CleanUpPuzzle
from search import depth_limited_search
from search import breadth_first_search
from search import uniform_cost_search
from display import displayProblemSolution
import time

BOARD_SIZE = 6

def solutionFiller(row, col): 
    return '0'

def easyBoard(row, col): 
    if row == 0 and col == 1: return '1'
    if row == 0 and col == 4: return '1'
    if row == 1 and col == 0: return '1'
    if row == 1 and col == 2: return '1'
    if row == 1 and col == 5: return '1'
    if row == 2 and col == 1: return '1'
    if row == 3 and col == 3: return '1'
    if row == 4 and col == 2: return '1'
    if row == 4 and col == 4: return '1'
    if row == 5 and col == 3: return '1'

    return '0'

start_time = time.time()
goal1 = depth_limited_search(
    CleanUpPuzzle(
        buildGrid(size = BOARD_SIZE, filler = easyBoard), 
        buildGrid(size = BOARD_SIZE)
    ), 
    limit=5
)
displayProblemSolution(goal1, 'depth_limited_search', time.time() - start_time)

start_time = time.time()
goal1 = breadth_first_search(
    CleanUpPuzzle(
        buildGrid(size = BOARD_SIZE, filler = easyBoard), 
        buildGrid(size = BOARD_SIZE)
    )
)
displayProblemSolution(goal1, 'breadth_first_search', time.time() - start_time)

start_time = time.time()
goal1 = uniform_cost_search(
    CleanUpPuzzle(
        buildGrid(size = BOARD_SIZE, filler = easyBoard), 
        buildGrid(size = BOARD_SIZE)
    )
)
displayProblemSolution(goal1, 'uniform_cost_search', time.time() - start_time)