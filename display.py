
def displayProblemSolution(goal_node, methodName, processingTime):
    print('METHOD: ' + methodName)
    print('--- search terminated after %s seconds ---' % (processingTime))
    if not goal_node:
        print('has not found a solution')
        return
    actions = goal_node.solution()
    nodes = goal_node.path()
    print('SOLUTION')
    print('State:' )
    print(nodes[0].state)
    for na in range(len(actions)):
        print('ACTION: ' + str(actions[na]))
        print('State:')
        print(nodes[na+1].state)
        print('END \n')