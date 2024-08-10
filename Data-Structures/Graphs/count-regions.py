def regionsBySlashes(grid) -> int:
    def is_valid(x, y, N):
        return 0 <= x < N and 0 <= y < N
    def dfs(x, y, visited, board, N):
        visited[x][y] = 1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_valid(nx, ny, N) and visited[nx][ny] == 0 and board[nx][ny] == 0:
                dfs(nx, ny, visited, board, N)
    # Core drive :
    N = len(grid)
    board = [[0] * (N * 3) for _ in range(N * 3)]
    visited = [[0] * (N * 3) for _ in range(N * 3)]
    space = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    forward = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    backward = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "\\":
                mat = backward
            elif grid[i][j] == "/":
                mat = forward
            else:
                mat = space
            # Filling the matrix :
            for x in range(3):
                for y in range(3):
                    board[i * 3 + x][j * 3 + y] = mat[x][y]
    # Counting the spaces :
    count = 0
    for i in range(N * 3):
        for j in range(N * 3):
            if visited[i][j] == 0 and board[i][j] == 0:
                dfs(i, j, visited, board, N * 3)
                count += 1
    return count