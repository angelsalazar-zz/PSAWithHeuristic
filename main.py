from board import buildGrid
from board import toggleCell
from board import buildGrid
from board import parseBoard
from cleanUpPuzzle import CleanUpPuzzle
from search import breadth_first_search
from search import uniform_cost_search
from display import displayProblemSolution
import time

BOARD_SIZE = 6

HARD_BOARD = [
    '0|1|0|0|0|1',
    '0|0|1|0|0|0',
    '0|0|0|1|0|1',
    '0|1|0|0|1|0',
    '0|0|1|0|0|0',
    '0|0|0|0|0|0'
]

start_time = time.time()
easy_goal = breadth_first_search(
    CleanUpPuzzle(
        '\n'.join(HARD_BOARD), 
        buildGrid(size = BOARD_SIZE)
    )
)

displayProblemSolution(easy_goal, 'breadth_first_search', time.time() - start_time)