def knapsack(profits, weights, W):
    n = len(profits)
    dp = [[-1] * (W + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            # base case:
            if i == 0 or j == 0:
                dp[i][j] = 0
            # Edge case
            elif j >= weights[i - 1]:
                not_take = dp[i - 1][j]
                take = profits[i - 1] + dp[i - 1][j - weights[i - 1]]
                dp[i][j] = max(take, not_take)
            # Last case
            else:
                dp[i][j] = dp[i - 1][j]
    # result
    return dp[n][W]


profits = list(map(int, input().replace('{',"").replace('}','').split(',')))
weights = list(map(int, input().replace('{',"").replace('}','').split(',')))
W = int(input())
print(knapsack(profits, weights, W))
