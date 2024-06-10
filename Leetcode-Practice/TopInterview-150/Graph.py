# SURROUNDED REGIONS :
from collections import deque
def solve(board) -> None:
    n = len(board)
    m = len(board[0])
    Q = deque()
    for i in range(n):
        if board[i][0] == "O":
            Q.append((i, 0))
        if board[i][m - 1] == "O":
            Q.append((i, m - 1))

    for j in range(m):
        if board[0][j] == "O":
            Q.append((0, j))
        if board[n - 1][j] == "O":
            Q.append((n - 1, j))

    def inBounds(i, j):
        return (0 <= i < n) and (0 <= j < m)

    while Q:
        i, j = Q.popleft()
        board[i][j] = "#"

        for di, dj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not inBounds(di, dj):
                continue
            if board[di][dj] != "O":
                continue
            Q.append((di, dj))
            board[di][dj] = "#"

    for i in range(n):
        for j in range(m):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "#":
                board[i][j] = "O"
