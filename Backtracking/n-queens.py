# Python program to solve N Queen 
global N

# Printing solution :
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print (board[i][j], end=' ')
		print()

# Checking is-safe function :
def isSafe(board, row, col):
	# Check this row on left side
	for i in range(col):
		if board[row][i] == 'Q':
			return False
	# Check upper diagonal on left side
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 'Q':
			return False
	# Check lower diagonal on left side
	for i, j in zip(range(row, N), range(col, -1, -1)):
		if board[i][j] == 'Q':
			return False
	return True


# Base case control section :
def solveNQUtil(board, col):
	if col >= N:
		return True
	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 'Q'
			if solveNQUtil(board, col + 1) == True:
				return True
			board[i][col] = '.'
	return False

# Main drive program :
N = int(input())
board = [['.'] * (N) for _ in range(N)]
if solveNQUtil(board, 0) == False:
    print ("Solution does not exist")
else:
    printSolution(board)


# FINDING ALL POSSIBLE SOLUTIONS TO SOLVE N-QUEENS :
def solveNQueens(self, n: int) -> List[List[str]]:
	RESULT = []
	# Board
	board = [["."] * n for _ in range(n)]
	
	def is_safe(board, row, col):
	    # left row
	    for i in range(col):
		if board[row][i] == "Q":
		    return False
	    # upper diagonal
	    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == "Q":
		    return False
	    # lower diagonal
	    for i, j in zip(range(row, n), range(col, -1, -1)):
		if board[i][j] == "Q":
		    return False
	    return True
	
	def solve(board, col):
	    if col >= n:
		RESULT.append(["".join(board[i]) for i in range(n)])
		return
	    for i in range(n):
		if is_safe(board, i, col):
		    board[i][col] = "Q"
		    if solve(board, col + 1):
			return True
		    board[i][col] = "."
	
	solve(board, 0)
	return RESULT
	
	
