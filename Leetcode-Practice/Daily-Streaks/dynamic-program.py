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
    M, N = len(points), len(points[0])
    maxPoints = [0] * N
    rightView = [0] * N
    for row in points:
        # Right -> Left
        currMax = 0
        for i in range(N - 1, -1, -1):
            currMax = max(currMax, maxPoints[i])
            rightView[i] = currMax
            currMax -= 1
        # Left -> Right
        currMax = 0
        for i in range(N):
            currMax = max(currMax, maxPoints[i])
            maxPoints[i] = max(currMax, rightView[i]) + row[i]
            currMax -= 1
    
    return max(maxPoints)
