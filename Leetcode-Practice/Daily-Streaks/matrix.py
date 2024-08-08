# LUCKY NUMBER IN THE MATRIX :
def luckyNumbers (matrix):
    if not matrix:
        return []
    min_elements = set(min(row) for row in matrix)
    max_elements = set()
    for j in range(len(matrix[0])):
        dump = matrix[0][j]
        for i in range(len(matrix)):
            if matrix[i][j] > dump: 
                dump = matrix[i][j]
        max_elements.add(dump)
    return (max_elements & min_elements)


# BUILD MATRIX USING ROW-SUM AND COLUMN-SUM :
def spiralMatrixIII(self, rows, cols, rStart, cStart):
    i, j = rStart, cStart
    dir_x, dir_y = 0, 1 
    twice = 2
    res = []
    moves = 1
    next_moves = 2
    while len(res) < (rows * cols):
        if (-1 < i < rows) and ( -1 < j < cols):
            res.append([i,j])
        i += dir_x
        j += dir_y
        moves -= 1
        if moves == 0:
            dir_x, dir_y = dir_y, -dir_x 
            twice -= 1
            if twice == 0:
                twice = 2
                moves = next_moves
                next_moves += 1
            else:
                moves = next_moves - 1
    return res