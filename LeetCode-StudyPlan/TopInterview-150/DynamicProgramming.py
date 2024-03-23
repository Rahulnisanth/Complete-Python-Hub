
# MIN SUB ARRAY USING DYNAMIC PROGRAMMING :
def maxSumAfterPartitioning(arr , k) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_val = float('-inf')
            for j in range(1, min(i, k) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)
        return dp[n]


# CLIMBING STAIRS :
def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    _oneBefore, _twoBefore = 1, 1
    total = 0
    for i in range(2, n + 1):
        total = _oneBefore + _twoBefore
        _twoBefore = _oneBefore
        _oneBefore = total
    return total