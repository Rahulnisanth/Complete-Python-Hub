def isValidSudoku(board) -> bool:
    # Row:
    for i in range(9):
        num_set = set()
        for j in range(9):
            num = board[i][j]
            if num in num_set:
                return False
            elif num != '.':
                num_set.add(num)
    # Col :
    for i in range(9):
        num_set = set()
        for j in range(9):
            num = board[j][i]
            if num in num_set:
                return False
            elif num != '.':
                num_set.add(num)
    # Each 3x3 Grid:
    starts=[(0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)]
    for i, j in starts:
        num_set = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                num = board[row][col]
                if num in num_set:
                    return False
                elif num != '.':
                    num_set.add(num)
    return True