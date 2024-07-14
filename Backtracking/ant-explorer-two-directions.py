def longest_path_count(n, grid) -> int:
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n
    def helper(x, y):
        if dp[x][y] != -1: 
            return dp[x][y]
        temp_max = 1
        directions = [(-1, 0), (0, -1)]
        for i, j in directions:
            nx = x - i
            ny = y - j
            if is_valid(nx, ny) and abs(grid[x][y] - grid[nx][ny]) == 1:
                temp_max = max(temp_max, 1 + helper(nx, ny))
        dp[x][y] = temp_max
        return dp[x][y]
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    max_length = 0
    for i in range(n):
        for j in range(n):
            max_length = max(max_length, helper(i, j))
    return max_length

# Input stream :
n, m = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append([int(num) for num in input().split(", ")])
print(longest_path_count(n, grid))