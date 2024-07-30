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