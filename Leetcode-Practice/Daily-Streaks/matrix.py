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