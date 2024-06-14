# Island-counting problem using recursive dynamic approach :
def is_valid(i, j):
    return 0 <= i < n and 0 <= j < m

def count_island(i, j, grid, dp):
    if not is_valid(i, j) or grid[i][j] == 0: 
        return 0
    if dp[i][j] != -1: 
        return dp[i][j]
    else:
        dump_count = 0
        grid[i][j] = 0
        dump_count += count_island(i, j + 1, grid, dp) # Right
        dump_count += count_island(i + 1, j, grid, dp) # Down
        dump_count += count_island(i - 1, j, grid, dp) # Up
        dump_count += count_island(i, j - 1, grid, dp) # Left
        dp[i][j] = dump_count + 1
        return dp[i][j]

def fill_table(grid, n, m):
    total_count = 0
    dp = [[-1] * (m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if count_island(i, j, grid, dp) > 0: 
                    total_count += 1
    return total_count 

# input stream :
n = int(input())
m = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(fill_table(grid, n, m))