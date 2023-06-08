import sys
import random

# Duplicates array and appends value at specified position
def add_element(arr, pos, val):
    output_arr = arr.copy()
    output_arr.insert(pos, val)
    return output_arr

# Computes heuristic difference between actual constraints and artificial matching constraints
def diff_constraints(actualConstraints, artificialConstraints):
    
    # Recursive method for exploring different padding options
    def alternative_padding(current_best, longer_constraints, shorter_constraints):
        total = 0
        # Calculate difference and add to total
        for i in range(len(shorter_constraints)):
            total += abs(longer_constraints[i] - shorter_constraints[i])
        # Add remaining unmatched constraints to total
        for i in range(len(shorter_constraints), len(longer_constraints)):
            total += abs(longer_constraints[i])
        total = min(total, current_best)
        # If they are of same length, maximum padding has been achieved
        return total

    # Determines which set of constraints is longer and calls the function 'alternative_padding' accordingly
    if len(actualConstraints) > len(artificialConstraints):
        return alternative_padding(sys.maxsize, actualConstraints, artificialConstraints)
    else:
        return alternative_padding(sys.maxsize, artificialConstraints, actualConstraints)

# Computes heuristic based on provided parameters 
def calculate_heuristic(nonogram_dimension, attempt):
    h_value = 0
    for i in range(len(nonogram_dimension)):
        constraints = nonogram_dimension[i]
        matching_constraints = []
        current_constraint = 0
        # Constructs matching constraints
        for square in attempt[i]:
            if square:
                length = len(matching_constraints)
                if current_constraint == length:
                    matching_constraints.insert(len(matching_constraints), 1)
                else:
                    matching_constraints[current_constraint] += 1
            else:
                current_constraint += len(matching_constraints) - current_constraint
        h_value += diff_constraints(constraints, matching_constraints)
    return h_value

# Computes heuristic on rows
def heuristic_rows(nonogram_spec, nonogram_sol):
    return calculate_heuristic(nonogram_spec['rows'], nonogram_sol)

# Transposes the input table and returns a new one
def transposition(table):
    rows_count = len(table)
    cols_count = len(table[0])
    output_table = [[False for _ in range(rows_count)] for _ in range(cols_count)]
    for i in range(rows_count):
        for j in range(cols_count):
            output_table[j][i] = table[i][j]
    return output_table

# Computes heuristic on columns
def heuristic_columns(nonogram_spec, nonogram_sol):
    return calculate_heuristic(nonogram_spec['cols'], transposition(nonogram_sol))

# Calculates additive heuristic
def combined_heuristic(nonogram_spec, nonogram_sol):
    h_value = 0
    # Checks heuristic on rows
    h_value += heuristic_rows(nonogram_spec, nonogram_sol)
    # Checks heuristic on columns
    h_value += heuristic_columns(nonogram_spec, nonogram_sol)
    return h_value

# Returns heuristic value either from rows or columns, chosen randomly
def random_choice_heuristic(nonogram_spec, nonogram_sol):
    if random.choice([False, True]):
        return heuristic_rows(nonogram_spec, nonogram_sol)
    else:
        return heuristic_columns(nonogram_spec, nonogram_sol)
