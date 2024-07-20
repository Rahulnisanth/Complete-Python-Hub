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
def restoreMatrix(rowSum, colSum):
    row, col = len(rowSum), len(colSum)
    matrix = [[0] * (col) for _ in range(row)]
    i = j = 0
    while i < row and j < col:
        x = min(rowSum[i], colSum[j])
        matrix[i][j] = x
        rowSum[i] -= x
        colSum[j] -= x
        i += (rowSum[i] == 0)
        j += (colSum[j] == 0)
    return matrix
