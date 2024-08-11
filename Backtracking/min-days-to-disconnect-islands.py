# MINIMUM NUMBER OF DAYS TO DISCONNECT THE LANDS IN THE GRID :
def minDays(grid) -> int:
        N = len(grid)
        M = len(grid[0])

        def is_valid(x, y):
            return 0 <= x < N and 0 <= y < M
        # DFS to traverse one island for each pointed land...
        def dfs(x, y, grid, visited):
            if not is_valid(x, y) or grid[x][y] == 0 or visited[x][y]:
                return
            visited[x][y] = True
            dfs(x + 1, y, grid, visited)
            dfs(x - 1, y, grid, visited)
            dfs(x, y + 1, grid, visited)
            dfs(x, y - 1, grid, visited)
        # Main drive
        visited = [[False] * M for _ in range(N)]
        initial_islands = 0
        # Counting the initial no. of. islands
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, grid, visited)
                    initial_islands += 1
        if initial_islands != 1:
            return 0
        # Marking the land to water [1 -> 0] one-by-one to find exact result 
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    visited = [[False] * M for _ in range(N)]
                    new_island_count = 0
                    for x in range(N):
                        for y in range(M):
                            if grid[x][y] == 1 and not visited[x][y]:
                                dfs(x, y, grid, visited)
                                new_island_count += 1
                    grid[i][j] = 1
                    if new_island_count > 1 or new_island_count == 0:
                        return 1
        return 2
