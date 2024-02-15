# VALID SUDOKU MATRIX :
def isValidSudoku(board) -> bool:
        # MAIN-DRIVE :
        def isValidRow(row):
            seen = set()
            for num in row:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        # Row checking :
        for row in board:
            if not isValidRow(row):
                return False
        # Column checking :
        for col in range(9):
            column  = [board[row][col] for row in range(9)]
            if not isValidRow(column):
                return False
        # Sub-Box checking :
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subBox = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not isValidRow(subBox):
                    return False
        return True


# SPIRAL MATRIX :
def spiralOrder(matrix):
    spiralMatrix = []
    top = 0
    left = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1
    
    while top <= bottom and left <= right:
        
        for i in range(left, right + 1):
            spiralMatrix.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            spiralMatrix.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiralMatrix.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiralMatrix.append(matrix[i][left])
            left += 1

    return spiralMatrix


# ROTATE IMAGE :
def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i] = matrix[i][::-1]


# SET MATRIX ZEROES :
def setZeroes(matrix):
    row = len(matrix)
    col = len(matrix[0])
    firstRowZero = False
    firstColZero = False

    for i in range(row):
        if matrix[i][0] == 0:
            firstColZero = True
            break
    
    for j in range(col):
        if matrix[0][j] == 0:
            firstRowZero = True
            break
    
    
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if firstRowZero:
        for j in range(col):
            matrix[0][j] = 0
    
    if firstColZero:
        for i in range(row):
            matrix[i][0] = 0
    
    return matrix