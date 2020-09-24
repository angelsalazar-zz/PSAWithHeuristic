from board import buildGrid
from board import toBoard
from boardConfigurations import EASY_BOARD
from boardConfigurations import MEDIUM_BOARD
from boardConfigurations import HARD_BOARD
from cleanUpPuzzle import CleanUpPuzzle
from display import displayProblemSolution
from search import astar_search
from heuristics import nonAdmissibleHeuristic
from heuristics import admissibleHeuristic
from timer import Timer

BOARD_SIZE = 11
PRINT_SOLUTION = False

def run(puzzle = None, heuristicType = None, difficulty = None, h = None):
    watch = Timer()
    solution = astar_search(puzzle, h)
    watch.stop()
    if (PRINT_SOLUTION):
        displayProblemSolution(solution, 'astar_search (Heuristic type: ' + heuristicType + ', Difficulty ' + difficulty + ')', watch.getTotalTime())
    else: 
        print('astar_search (Heuristic type: ' + heuristicType + ', Difficulty ' + difficulty + ') = ' + str(watch.getTotalTime()))
    return watch.getTotalTime()

def comparePerformance(nonAdmissible, admissible):
    indexes = ['EASY', 'MEDIUM', 'HARD']
    cols = ['Difficulty', 'Non Admissible Time (NA)', 'Admissible Time (A)', 'Time Diff (A - NA)', 'NA Time Saving %']
    headers = []
    rows = []
    STR_TEMPLATE = ' {:<25}'
    NUM_TEMPLATE = ' {:<25.10f}'
    PER_TEMPLATE = ' {:<25}'
    
    for col in cols:
        headers.append(STR_TEMPLATE.format(col))
    rows.append('|'.join(headers))
    
    for index in indexes:
        nonAdmissibleTime = nonAdmissible[index]
        admissibleTime = admissible[index]
        difference = admissible[index] - nonAdmissible[index]
        performance = (difference / nonAdmissibleTime) * 100
        label = ' slower'
        if performance > 0:
            label = ' faster'
        rows.append(
            '|'.join([
                STR_TEMPLATE.format(index),
                NUM_TEMPLATE.format(nonAdmissibleTime),
                NUM_TEMPLATE.format(admissibleTime),
                NUM_TEMPLATE.format(difference),
                PER_TEMPLATE.format('{:.5f}'.format(performance) + label)
            ])
        )
    print('\n'.join(rows))

GOAL_STATE = buildGrid(BOARD_SIZE)
nonAdmissibleResultsByDifficulty = dict()
# Non Admissible Heuristic
nonAdmissibleResultsByDifficulty['EASY'] = run(CleanUpPuzzle(toBoard(EASY_BOARD), GOAL_STATE), 'Non admissible heuristic', 'EASY', nonAdmissibleHeuristic)
nonAdmissibleResultsByDifficulty['MEDIUM'] = run(CleanUpPuzzle(toBoard(MEDIUM_BOARD), GOAL_STATE), 'Non admissible heuristic', 'MEDIUM', nonAdmissibleHeuristic)
nonAdmissibleResultsByDifficulty['HARD'] = run(CleanUpPuzzle(toBoard(HARD_BOARD), GOAL_STATE), 'Non admissible heuristic','HARD', nonAdmissibleHeuristic)

admissibleResultsByDifficulty = dict()
# Admissible Heuristic
admissibleResultsByDifficulty['EASY'] = run(CleanUpPuzzle(toBoard(EASY_BOARD), GOAL_STATE), 'Admissible', 'EASY', admissibleHeuristic)
admissibleResultsByDifficulty['MEDIUM'] = run(CleanUpPuzzle(toBoard(MEDIUM_BOARD), GOAL_STATE), 'Admissible', 'MEDIUM', admissibleHeuristic)
admissibleResultsByDifficulty['HARD'] = run(CleanUpPuzzle(toBoard(HARD_BOARD), GOAL_STATE), 'Admissible','HARD', admissibleHeuristic)

comparePerformance(nonAdmissibleResultsByDifficulty, admissibleResultsByDifficulty)