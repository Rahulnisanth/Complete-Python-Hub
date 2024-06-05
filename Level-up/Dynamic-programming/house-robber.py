
def knapsack(idx, nums, dp) -> int:
    if idx == 0: dp[idx] =  nums[idx]
    if idx < 0: return 0
    if dp[idx] != -1: return dp[idx]
    # take :
    take = nums[idx] + knapsack(idx - 2, nums, dp)
    # Not take :
    not_take = 0 + knapsack(idx - 1, nums, dp)
    dp[idx] = max(take, not_take)
    return dp[idx]


amounts = list(map(int, input().split(",")))
amounts.pop()
n = len(amounts)
dp = [-1 for _ in range(n)]
print(knapsack(n-1, amounts, dp))