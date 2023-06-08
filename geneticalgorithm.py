import heuristic
import random


def printNonogram(soln):
    for row in soln:
        print("")
        for square in row:
            print("#" if square else ".", end=" ")
    print("\n")


def crossoverCols(parent1, parent2):
    crossoverPoint = random.randrange(len(parent1)) or 1
    child1 = []
    child2 = []
    for i in range(crossoverPoint):
        child1.insert(i, [parent1[j][i] for j in range(len(parent1))])
        child2.insert(i, [parent2[j][i] for j in range(len(parent1))])
    for i in range(crossoverPoint, len(parent1)):
        child1.insert(i, [parent2[j][i] for j in range(len(parent1))])
        child2.insert(i, [parent1[j][i] for j in range(len(parent1))])
    return heuristic.transpose(child1), heuristic.transpose(child2)


def crossoverRows(parent1, parent2):
    crossoverPoint = random.randrange(len(parent1)) or 1
    child1 = []
    child2 = []
    for i in range(crossoverPoint):
        child1.insert(i, parent1[i].copy())
        child2.insert(i, parent2[i].copy())
    for i in range(crossoverPoint, len(parent1)):
        child1.insert(i, parent2[i].copy())
        child2.insert(i, parent1[i].copy())
    return child1, child2


def crossover(parent1, parent2):
    if random.choice([False, True]):
        return crossoverRows(parent1, parent2)
    else:
        return crossoverCols(parent1, parent2)


def initPop(popSize, nonogramSize):
    return [[[random.choice([False, True]) for _ in range(nonogramSize)] for _ in range(nonogramSize)] for _ in range(popSize)]


def solver(nonogramSpec, popFactor, mutationRate, maxIterations, h, restart=False):
    def fitness(individual):
        return h(nonogramSpec, individual)

    def solnCorrect(individual):
        return heuristic.rowHeuristic(nonogramSpec, individual) == 0 and\
            heuristic.colHeuristic(nonogramSpec, individual) == 0

    def mutate(individual):
        for _ in range(len(nonogramSpec['rows'])):
            i = random.randrange(len(individual))
            j = random.randrange(len(individual))
            individual[i][j] = not individual[i][j]

    popSize = popFactor * 4  # must be multiple of 4
    pop = initPop(popSize, len(nonogramSpec['rows']))
    generation = 1

    while True:
        minFit = 1000000
        possibleSoln = []
        # Natural selection tournament; compare each 2 individuals
        for i in range(0, popSize//2):
            fit1 = fitness(pop[i])
            # fitness must = 0 for solution to be correct, so we check that first
            if fit1 == 0 and solnCorrect(pop[i]):
                printNonogram(pop[i])
                return pop[i]

            fit2 = fitness(pop[i + 1])
            if fit2 == 0 and solnCorrect(pop[i + 1]):
                printNonogram(pop[i+1])
                return pop[i + 1]

            if fit1 < minFit:
                minFit = fit1
                possibleSoln = pop[i]
            elif fit2 < minFit:
                minFit = fit2
                possibleSoln = pop[i + 1]

            # Get rid of whichever option is less fit
            if fit1 < fit2:
                del pop[i + 1]
            else:
                del pop[i]

        generation += 1
        if generation % 50 == 0:
            print(generation, minFit)
            printNonogram(possibleSoln)
        if generation > maxIterations:
            if restart:
                return solver(nonogramSpec, popFactor, mutationRate, maxIterations, h, restart=restart)
            else:
                return

        # Reproduction
        for i in range(0, popSize//2, 2):
            child1, child2 = crossover(pop[i], pop[i + 1])
            if random.randrange(mutationRate) == 0:
                mutate(child1)
            if random.randrange(mutationRate) == 0:
                mutate(child2)
            pop.insert(len(pop), child1)
            pop.insert(len(pop), child2)
