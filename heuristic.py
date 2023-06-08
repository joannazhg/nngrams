import sys
import random

# Copy arr and insert val at position pos
def insert(arr, pos, val):
    out = arr.copy()
    out.insert(pos, val)
    return out

# Compute heuristic for the real constraints (solnConst) and artificial matching
# constraints (curConst)
def constraintDiff(solnConst, curConst):
    # recursive algorithm for checking alternative padding strategies
    def f(curBest, longConst, shortConst):
        out = 0
        # add differences to out
        for i in range(len(shortConst)):
            out += abs(longConst[i] - shortConst[i])
        # add remaining unpaired constraints to out
        for i in range(len(shortConst), len(longConst)):
            out += abs(longConst[i])
        out = min(out, curBest)
        # If they are the same length, that implies we've performed maximum padding
        return out
        #if len(shortConst) == len(longConst):
        #    return out
        #else:
        #    # Recurse with padding in every possible location, take minimal result
        #    return min([f(out, longConst, insert(shortConst, i, 0)) for i in range(len(shortConst))])
    # check whether the actual or artificial constraints are longer, and call f accordingly
    if len(solnConst) > len(curConst):
        return f(sys.maxsize, solnConst, curConst)
    else:
        return f(sys.maxsize, curConst, solnConst)

# Calculate heuristic on given parameters (either rows or columns)
# nonogramSpecDim = one of the dimensions of the nonogram specification
# attempt = the rows or columns of the nonogram (whichever corresponds to the dim above)
def genericHeuristic(nonogramSpecDim, attempt):
    hVal = 0
    for i in range(len(nonogramSpecDim)):
        constraints = nonogramSpecDim[i]
        matchingConstraints = []
        curConstraint = 0
        # construct artificial matching constraints
        for square in attempt[i]:
            if square:
                length = len(matchingConstraints)
                if curConstraint == length:
                    matchingConstraints.insert(len(matchingConstraints), 1)
                else:
                    matchingConstraints[curConstraint] += 1
            else:
                curConstraint += len(matchingConstraints) - curConstraint
        hVal += constraintDiff(constraints, matchingConstraints)
    return hVal

# Calculate heuristic on rows
def rowHeuristic(nonogramSpec, nonogramSoln):
    return genericHeuristic(nonogramSpec['rows'], nonogramSoln)

# Create and return a new table, which is the transpose of the input
def transpose(table):
    rows = len(table)
    cols = len(table[0])
    out = [[False for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            out[j][i] = table[i][j]
    return out

# Calculate heuristic on columns
def colHeuristic(nonogramSpec, nonogramSoln):
    return genericHeuristic(nonogramSpec['cols'], transpose(nonogramSoln))

def additiveHeuristic(nonogramSpec, nonogramSoln):
    hVal = 0
    # check heuristic on rows
    hVal += rowHeuristic(nonogramSpec, nonogramSoln)
    # check heuristic on columns
    hVal += colHeuristic(nonogramSpec, nonogramSoln)
    return hVal

def randomHeuristic(nonogramSpec, nonogramSoln):
    if random.choice([False, True]):
        return rowHeuristic(nonogramSpec, nonogramSoln)
    else:
        return colHeuristic(nonogramSpec, nonogramSoln)
