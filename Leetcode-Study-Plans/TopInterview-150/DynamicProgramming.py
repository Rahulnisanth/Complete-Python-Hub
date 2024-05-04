
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
def climbStairs( n: int) -> int:
    if n == 1:
        return 1
    _oneBefore, _twoBefore = 1, 1
    total = 0
    for i in range(2, n + 1):
        total = _oneBefore + _twoBefore
        _twoBefore = _oneBefore
        _oneBefore = total
    return total


# HOUSE ROBBER :
def rob(nums) -> int:
    rob, noRob = 0, 0
    for i in range(len(nums)):
        newRob = noRob + nums[i]
        newNoRob = max(noRob, rob)
        rob, noRob = newRob, newNoRob
    return max(rob, noRob)  


# BEST TIME TO BUY AND SELL [HARD] :
def maxProfit(prices) -> int:
    first_buy = second_buy = -prices[0]
    first_profit = total_profit = 0
    for price in prices:
        first_buy = max(first_buy, -price)
        first_profit = max(first_profit, price + first_buy)
        second_buy = max(second_buy, first_profit - price)
        total_profit = max(total_profit, price + second_buy)
    return total_profit


# COIN CHANGE CALCULATION :
def coinChange(coins, amount) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# LENGTH OF THE LONGEST INCREASING SEQUENCE :
def lengthOfLIS(nums) -> int:
    if not nums:
        return 0
    else:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)