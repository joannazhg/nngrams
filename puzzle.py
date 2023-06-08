def get_block_lengths(lst):
    return [len(list(g)) for k, g in groupby(lst) if k]

def check_line(line, blocks):
    filled_blocks = get_block_lengths(line)
    if len(filled_blocks) != len(blocks):
        return False
    return all(fb == b for fb, b in zip(filled_blocks, blocks))

def initial_board(constraints):
    rows = constraints['rows']
    cols = constraints['cols']
    n = len(rows)
    m = len(cols)
    return [[False]*m for _ in range(n)]

def check_solution(board, constraints):
    rows = constraints['rows']
    cols = constraints['cols']
    for i, row in enumerate(board):
        if not check_line(row, rows[i]):
            return False
    for j, col in enumerate(zip(*board)):
        if not check_line(col, cols[j]):
            return False
    return True

def solve_puzzle(constraints):
    board = initial_board(constraints)
    stack = [(board, 0, 0)]
    while stack:
        board, i, j = stack.pop()
        if i == len(board):
            if check_solution(board, constraints):
                return board
        else:
            for val in [True, False]:
                new_board = [row.copy() for row in board]
                new_board[i][j] = val
                new_i, new_j = (i, j+1) if j+1 < len(board[0]) else (i+1, 0)
                stack.append((new_board, new_i, new_j))
    return None
