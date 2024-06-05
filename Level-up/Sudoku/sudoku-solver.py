import time

def find_next_empty(puzzle):
    # Finding the non-zeroed number in puzzle
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None

def is_valid_guess(puzzle, guess, row, col):
    # Checking the row values for reputation
    row_values = puzzle[row]
    if guess in row_values:
        return False
    # Checking the column values for the reputation
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False
    # Checking the 3-by-3 grid for the reputation
    row_start = (row // 3) * 3
    col_start = (col // 3 )* 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if guess == puzzle[r][c]:
                return False
    return True

def solve_sudoku(puzzle):
    if time.time() - start_time > time_limit:
        return False
    row, col = find_next_empty(puzzle)
    if row is None or col is None:
        return True
    for guess in range(1, 10):
        if is_valid_guess(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # Solving the puzzle recursively after filling the correct guess :
            if solve_sudoku(puzzle): 
                return True
        # Backtracking for the wrong guess :
        puzzle[row][col] = 0
    return False

puzzle = [list(map(int, input().split())) for _ in range(9)]
time_limit = 1.5
start_time = time.time()
print(solve_sudoku(puzzle))
if solve_sudoku(puzzle):
# final solved_sudoku :
    for r in range(9):
        for c in range(9):
            print(puzzle[r][c], end=' ')
        print()
else: print("No solution")