# UNIQUE PATHS :
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0] * (n + 1)] * (m + 1)
    dp[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[m][n]


# MIN PATH SUM :
def minPathSum(self, grid) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    # First-row:
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    # First-col:
    for j in range(1, m):
        dp[j][0] = dp[j - 1][0] + grid[j][0]
    # Edge cases :
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


# UNIQUE PATHS - WITH OBSTACLES :
def uniquePathsWithObstacles(self, obstacleGrid) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * (n + 1)]  * (m + 1)
    dp[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if obstacleGrid[i - 1][j - 1] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m][n]


# MIN PATH SUM IN TRIANGLE [BOTTOM-UP APPROACH] :
def minimumTotal(triangle) -> int:
    n = len(triangle)
    dp = [[0] * (i + 1) for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            if i == n - 1:
                dp[i][j] = triangle[i][j]
            else:
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]


# MINIMUM FALLING PATH SUM IN 2D GRID :
def minFallingPathSum(matrix) -> int:
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i > 0:
                # Leftmost:
                if j == 0:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1])
                # Middle:
                if j - 1 >= 0 and j + 1 < m:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])
                # Rightmost:
                if j == m - 1:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j - 1])
    return min(matrix[n - 1])


# MAXIMAL SQUARE :
def maximalSquare(matrix) -> int:
    if not matrix or len(matrix) < 1:
        return 0
    else:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_area = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    max_area = max(max_area, dp[i][j])
        return (max_area * max_area)


# MAXIMUM CONSECUTIVE DAYS FOR VACATION WITH OBLIGATIONS :
def maximumVacationDays(n: int, m: int, k: int, arr: List[int]) -> int: # type: ignore
    result = 0
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(k + 1):
            if i in arr:
                if j > 0:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + 1
            result = max(result, dp[i][j])
    return result
