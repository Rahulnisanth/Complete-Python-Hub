# MINIMUM NUMBER OF DELETION TO MAKE STRING BALANCED :
def minimumDeletions(s: str) -> int:
    N = len(s)
    dp = [0] * (N + 1)
    countB = 0
    for i in range(1, N + 1):
        if s[i - 1] == 'b':
            dp[i] = dp[i - 1]
            countB += 1
        else:
            dp[i] = min(dp[i - 1] + 1, countB)
    return dp[-1]


# MAXIMUM NUMBER OF POINTS WITH COST :
def maxPoints(points) -> int:
    N, M = len(points), len(points[0])
    dp = [0] * M
    for i in range(N):
        left_max = [0] * M
        right_max = [0] * M
        # Left
        left_max[0] = dp[0]
        for j in range(1, M):
            left_max[j] = max(left_max[j - 1] - 1, dp[j])
        # Right
        right_max[M - 1] = dp[M - 1]
        for j in range(M - 2, -1, -1):
            right_max[j] = max(right_max[j + 1] - 1, dp[j])
        # Overall 
        for j in range(M):
            dp[j] = points[i][j] + max(left_max[j], right_max[j])
    return max(dp)
# {OR}
def maxPoints(points) -> int:
    N, M = len(points), len(points[0])
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N):
        for j in range(1, M + 1):
            dp[i][j] =  points[i - 1][j - 1] +\
                        max([dp[i - 1][col] - abs(j - col) for col in range(1, M + 1)])
    return max(dp[-1])


# STRANGE PRINTER :
def strangePrinter(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            dp[i][j] = dp[i][j - 1] + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0))
    return dp[0][-1]