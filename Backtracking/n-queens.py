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



