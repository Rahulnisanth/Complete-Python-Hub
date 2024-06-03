# DYNAMIC PROGRAMMING :
# CALCULATING THE NO. OF. POSSIBLE WAYS TO REACH THE END OF THE 2D GRID :
def solve_puzzle(row, col):
    dp = [[0] * (col + 1)] * (row + 1)
    dp[1][1] = 1
    for i in range(1, row + 1):
        for j in range(2, col + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[row][col]

row = int(input())
col = int(input())
print(solve_puzzle(row, col))




