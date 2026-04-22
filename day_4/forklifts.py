from itertools import product

import numpy


def is_blocked(c, r, matrix):
    # count surrounding rolls
    # [c - 1, c, c + 1], [r - 1, r, r + 1]
    total_rolls = 0

    for x, y in product(
            [c - 1, c, c + 1],
            [r - 1, r, r + 1],
    ):
        if (x == c and y == r) or x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix):
            # keep in matrix bounds and don't count self
            continue

        if matrix[x][y] == 1:
            total_rolls += 1

        if total_rolls >= 4:
            return True

    return False

def solve_first_challenge(matrix):
    total_accessible_rolls = 0

    for x, y in product(range(len(matrix)), range(len(matrix))):
        if matrix[x][y] and not is_blocked(x, y, matrix):
            total_accessible_rolls += 1

    return total_accessible_rolls

def solve_second_challenge(matrix):

    total_accessible_rolls = 0
    stop_iteration = False

    while not stop_iteration:
        total_single_run = 0
        for x, y in product(range(len(matrix)), range(len(matrix))):
            if matrix[x][y] and not is_blocked(x, y, matrix):
                total_single_run += 1
                matrix[x][y] = not matrix[x][y]

        if total_single_run == 0:
            stop_iteration = True
        else:
            total_accessible_rolls += total_single_run

    return total_accessible_rolls

def read_input(file_path):
    # read
    with open(file_path, 'r') as file:
        text = file.read()

    # save to matrix
    lines = text.strip().split('\n')

    num_of_rows = len(lines)
    num_of_cols = len(lines[0])

    matrix = numpy.zeros((num_of_rows, num_of_cols), dtype=bool)

    for i, line in enumerate(lines):
        matrix[i] = [c == '@' for c in line]

    return matrix

if __name__ == "__main__":
    file_path = 'input.txt'
    matrix = read_input(file_path)
    result = solve_second_challenge(matrix)
    print(result)