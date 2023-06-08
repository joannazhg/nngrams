import heuristic

def displayNonogram(solution):
    for row in solution:
        print("")
        for square in row:
            print("#" if square else ".", end=" ")
    print("\n")

def prepareInitialSolution(nonogramSpecification):
    nonogramSize = len(nonogramSpecification['rows'])
    result = [[False for _ in range(nonogramSize)] for _ in range(nonogramSize)]
    i = 0
    for row in nonogramSpecification['rows']:
        j = 0
        for constraint in row:
            for _ in range(constraint):
                result[i][j] = True
                j += 1
            j += 1
        i += 1

    return result

def createInitialNode(nonogramSpecification):
    node = {}
    node['depth'] = 0
    node['soln'] = prepareInitialSolution(nonogramSpecification)
    return node

def pushToStack(stack, node):
    stack.insert(len(stack), node)

def popFromStack(stack):
    result = stack[len(stack) - 1]
    del stack[len(stack) - 1]
    return result

# Shifts the contents of a nonogram row by one square to the right from the provided starting position shiftStart
def shiftRowContents(row, shiftStart):
    if row[len(row) - 1] or shiftStart >= len(row):
        return False

    for offset in range(0, len(row) - shiftStart - 1):
        pos = len(row) - offset - 1
        row[pos] = row[pos - 1]

    row[shiftStart] = False

    return True


def depthLimitedDFS(nonogramSpecification, maximumDepth):
    def isSolutionCorrect(solution):
        return heuristic.rowHeuristic(nonogramSpecification, solution) == 0 and\
               heuristic.colHeuristic(nonogramSpecification, solution) == 0

    # Generate all the children of node and push them to stack
    def pushAllChildren(stack, node):
        for i in range(len(node['soln'])):
            j = 0
            while j < len(node['soln'][i]):
                while j < len(node['soln'][i]) and not node['soln'][i][j]:
                    j += 1
                child = {}
                child['soln'] = [row.copy() for row in node['soln']]
                child['depth'] = node['depth'] + 1

                if shiftRowContents(child['soln'][i], j):
                    pushToStack(stack, child)

                if isSolutionCorrect(child['soln']):
                    return child['soln']

                while j < len(node['soln'][i]) and node['soln'][i][j]:
                    j += 1
        return False

    stack = []
    startNode = createInitialNode(nonogramSpecification)
    pushToStack(stack, startNode)

    if isSolutionCorrect(startNode['soln']):
        return startNode

    while len(stack) > 0:
        current = popFromStack(stack, )
        #displayNonogram(current['soln'])
        if current['depth'] < maximumDepth:
            foundSolution = pushAllChildren(stack, current)
            if foundSolution:
                return foundSolution
    return False

# Solve a nonogram, with constraints as described in nonogramSpecification
def nonogramSolver(nonogramSpecification, maxMaxDepth):
    maxDepth = 0
    while maxDepth <= maxMaxDepth:
        print(maxDepth)
        solution = depthLimitedDFS(nonogramSpecification, maxDepth)
        if solution:
            return solution
        max
        
#
