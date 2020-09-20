from board import buildGrid
from board import toBoard
from boardConfigurations import EASY_BOARD
from boardConfigurations import MEDIUM_BOARD
from boardConfigurations import HARD_BOARD
from cleanUpPuzzle import CleanUpPuzzle
from display import displayProblemSolution
from search import astar_search
from heuristics import nonAdmissibleHeuristic
from timer import Timer

BOARD_SIZE = 11

def run(puzzle = None, difficulty = None):
    watch = Timer()
    solution = astar_search(
        puzzle,
        nonAdmissibleHeuristic
    )
    watch.stop()
    displayProblemSolution(solution, 'astar_search (Difficulty ' + difficulty + ')', watch.getTotalTime())


# Non Admissible Heuristic
GOAL_STATE = buildGrid(BOARD_SIZE)

run(CleanUpPuzzle(toBoard(EASY_BOARD), GOAL_STATE), 'EASY')
run(CleanUpPuzzle(toBoard(MEDIUM_BOARD), GOAL_STATE), 'MEDIUM')
run(CleanUpPuzzle(toBoard(HARD_BOARD), GOAL_STATE), 'HARD')

