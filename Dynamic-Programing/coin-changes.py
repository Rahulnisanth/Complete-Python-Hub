# MINIMUM WAYS TO CHANGE n CENTS WITH "inf" SUPPLY OF COINS :
def solve(N, coins):
    dp = [0] * (N + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, N + 1):
            dp[i] += dp[i - coin]
    return dp[-1]