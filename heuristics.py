# nonAdmissibleHeuristic
# this counts the number of tiles in a given node
def nonAdmissibleHeuristic(node):
    return node.state.count('1')
