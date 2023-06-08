import random
import heuristic

# Display the nonogram solution
def display_nonogram(solution):
    for row in solution:
        print("")
        for square in row:
            print("#" if square else ".", end=" ")
    print("\n")

# Crossover method on the columns of the parent nonograms
def cross_cols(parent1, parent2):
    cross_point = random.randrange(len(parent1)) or 1
    offspring1, offspring2 = [], []
    for i in range(cross_point):
        offspring1.append([parent1[j][i] for j in range(len(parent1))])
        offspring2.append([parent2[j][i] for j in range(len(parent1))])
    for i in range(cross_point, len(parent1)):
        offspring1.append([parent2[j][i] for j in range(len(parent1))])
        offspring2.append([parent1[j][i] for j in range(len(parent1))])
    return heuristic.transpose(offspring1), heuristic.transpose(offspring2)

# Crossover method on the rows of the parent nonograms
def cross_rows(parent1, parent2):
    cross_point = random.randrange(len(parent1)) or 1
    offspring1, offspring2 = [], []
    for i in range(cross_point):
        offspring1.append(parent1[i].copy())
        offspring2.append(parent2[i].copy())
    for i in range(cross_point, len(parent1)):
        offspring1.append(parent2[i].copy())
        offspring2.append(parent1[i].copy())
    return offspring1, offspring2

# Crossover function that chooses between row and column crossover
def cross(parent1, parent2):
    if random.choice([False, True]):
        return cross_rows(parent1, parent2)
    else:
        return cross_cols(parent1, parent2)

# Initialize population with random values
def initialize_population(pop_size, nonogram_size):
    return [[[random.choice([False, True]) for _ in range(nonogram_size)] for _ in range(nonogram_size)] for _ in range(pop_size)]

# Nonogram solver function
def solve_nonogram(nonogram_spec, pop_factor, mutation_rate, max_iterations, heuristic_func, restart=False):
    # Fitness function for individuals
    def calculate_fitness(individual):
        return heuristic_func(nonogram_spec, individual)

    # Check if solution is correct
    def is_solution_correct(individual):
        return heuristic.rowHeuristic(nonogram_spec, individual) == 0 and\
            heuristic.colHeuristic(nonogram_spec, individual) == 0

    # Mutate an individual
    def mutate(individual):
        for _ in range(len(nonogram_spec['rows'])):
            i = random.randrange(len(individual))
            j = random.randrange(len(individual))
            individual[i][j] = not individual[i][j]

    pop_size = pop_factor * 4  # must be multiple of 4
    population = initialize_population(pop_size, len(nonogram_spec['rows']))
    generation_count = 1

    while True:
        min_fitness = 1000000
        possible_solution = []
        # Tournament selection: compare pairs of individuals
        for i in range(0, pop_size//2):
            fitness1 = calculate_fitness(population[i])
            if fitness1 == 0 and is_solution_correct(population[i]):
                display_nonogram(population[i])
                return population[i]

            fitness2 = calculate_fitness(population[i + 1])
            if fitness2 == 0 and is_solution_correct
