def longest_increasing_path(grid, row, col):
    dp = [[-1] * col for _ in range(row)]
    # Depth-first approach :
    def dfs(x, y):
        if dp[x][y] != -1: return dp[x][y]
        # Tracking the steps basis maximum :
        max_length = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == grid[x][y] + 1:
                max_length = max(max_length, 1 + dfs(nx, ny))
        dp[x][y] = max_length
        return max_length
    # Overall grid maximum path :
    longest_path = 0
    for i in range(row):
        for j in range(col):
            longest_path = max(longest_path, dfs(i, j))
    return longest_path

# Input stream :
row, col = list(map(int, input().split()))
grid = []
for _ in range(row):
    grid.append([int(i) for i in input().split()])
print(longest_increasing_path(grid, row, col)) 