# UNIQUE PATHS :
def uniquePaths( m: int, n: int) -> int:
    dp = [[0] * (n + 1)] * (m + 1)
    dp[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[m][n]


# LONGEST COMMON SUB-SEQUENCE :
def longestCommonSubsequence(text1, text2) -> int:
    dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
    for i in range(1, len(text2) + 1):
        for j in range(1, len(text1) + 1):
            if text2[i - 1] == text1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


# BEST TIME TO BUY AND SELL STOCK WITH TRANSACTION FEES :
def maxProfit(prices, fee) -> int:
    if not prices:
        return 0
    cash, hold = 0, -prices[0]
    for price in prices:
        prev = cash
        cash = max(cash, hold + price - fee)
        hold = max(hold, prev - price)
    return cash


# EDIT DISTANCE :
def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # FIRST ROW
    for i in range(1, m + 1):
        dp[i][0] = i
    # FIRST COLUMN
    for j in range(1, n + 1):
        dp[0][j] = j
    # TABLE FILLING
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    # RESULT
    return dp[m][n]