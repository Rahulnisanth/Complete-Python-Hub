# BEST TIME TO BUT & SELL THE STOCK [IV] :
def maxProfit(K: int, prices) -> int:
    if K <= 0:
        return 0
    else:
        dp = [[[0 for _ in range(K + 1)] for _ in range(2)] for _ in range(len(prices) + 1)]
        for i in range(len(prices) - 1, -1, -1):
            for j in range(2):
                for k in range(1, 3):
                    if j:
                        dp[i][j][k] = max(dp[i + 1][0][k] - prices[i], dp[i + 1][j][k])
                    else:
                        dp[i][j][k] = max(prices[i] + dp[i + 1][1][k - 1], dp[i + 1][j][k])
        return dp[0][1][K]


# MAXIMIZE THE XOR TOTAL OF THE SUBSET OF LENGTH N // 2 :
def maximumXor(values, N):
    dp = [[0] * (N // 2 + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N // 2 + 1):
            take = dp[i - 1][j - 1] ^ values[i - 1]
            not_take = dp[i - 1][j]
            dp[i][j] = max(take, not_take)
    return max(dp[-1])


# BEST TIME TO BUY AND SELL THE STOCKS [III] :
def maxProfit(prices) -> int:
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(prices) + 1)]
    for i in range(len(prices) - 1, -1, -1):
        for j in range(2):
            for k in range(1, 3):
                if j:
                    dp[i][j][k] = max(dp[i + 1][0][k] - prices[i], dp[i + 1][j][k])
                else:
                    dp[i][j][k] = max(prices[i] + dp[i + 1][1][k - 1], dp[i + 1][j][k])
    return dp[0][1][2]
