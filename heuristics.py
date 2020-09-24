# nonAdmissibleHeuristic
# this counts the number of tiles in a given node
def nonAdmissibleHeuristic(node):
    size = len(node.state.split('\n'))
    remaningTilesCount = node.state.count('1')
    return (remaningTilesCount * 100) / (size*size)

# admissibleHeuristic
# this computes the percentage of cells occupied in the board
def admissibleHeuristic(node):
    rows = node.state.split('\n')
    count = 0
    for index in range(len(rows) - 1):
        count = count + rows[index].count('1')
    return count