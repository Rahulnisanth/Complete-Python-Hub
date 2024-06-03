# Rod cutting using unbounded knapsack approach :
def find_maximum_profit(prices, length, maxLength, n) -> int:
    def rod_cutting(prices, length, maxLength, n) -> int:
        # Base case :
        if n == 0 or maxLength == 0: return 0
        # Cache :
        if dp[n][maxLength] != -1: return dp[n][maxLength]
        # Exclusion [Current length > maximum length] :
        if length[n - 1] > maxLength:
            dp[n][maxLength] =  rod_cutting(prices, length, maxLength, n - 1)
        # Inclusion (and) Exclusion :
        else:
            dp[n][maxLength] = max((prices[n - 1] + rod_cutting(prices, length, maxLength - length[n - 1], n)),\
                                rod_cutting(prices, length, maxLength, n - 1))
        return dp[n][maxLength]
    dp = [[-1 for _ in range(maxLength + 1)] for _ in range(n + 1)]
    return rod_cutting(prices, length, maxLength, n)
prices = list(map(int, input().split(", ")))
print(find_maximum_profit(prices, list(range(1, len(prices) + 1)), len(prices), len(prices)))