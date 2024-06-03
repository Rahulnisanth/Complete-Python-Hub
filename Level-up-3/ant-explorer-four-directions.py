def longest_path_count(n, grid) -> int:
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n
    
    def longest_path_from(x, y):
        if dp[x][y] != -1: return dp[x][y]
        temp_max =  1
        for dx, dy in [(-1, 0), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and abs(grid[nx][ny] - grid[x][y]) == 1:
                temp_max = max(temp_max, 1 + longest_path_from(nx, ny))
        dp[x][y] = temp_max
        return dp[x][y]
    
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    max_path_length = 0
    for i in range(n):
        for j in range(n):
            max_path_length = max(max_path_length, longest_path_from(i, j))
    return max_path_length

# Input stream :
n, m = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append([int(num) for num in input().split(", ")])
print(longest_path_count(n, grid))