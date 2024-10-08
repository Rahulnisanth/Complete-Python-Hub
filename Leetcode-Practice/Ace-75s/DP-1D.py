# NTH TRIBONACCI NUMBER :
def tribonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    else:
        dp = [0] * (n + 1)
        dp[1] =  1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        return dp[n]
    

# MIN COST OF CLIMBING STAIRS :
def minCostClimbingStairs(cost) -> int:
    n = len(cost)
    for i in range(2, n):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[n - 1], cost[n - 2])


# HOUSE ROBBER :
def rob(nums) -> int:
    N = len(nums)
    if N == 0: 
        return 0
    if N == 1: 
        return nums[0]
    dp = [0] * N
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, N):
        take = nums[i] + dp[i - 2]
        not_take = dp[i - 1]
        dp[i] = max(take, not_take)
    return dp[-1]