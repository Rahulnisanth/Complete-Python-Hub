def knapsack(idx, W, dp) -> int:
    # Base case for single element :
    if idx == 0: 
        if weights[idx] <= W: dp[idx][W] = profits[idx]
        else: dp[idx][W] = 0
    # Memos :
    if dp[idx][W] != -1: return dp[idx][W]
    # Not - take :
    un_take = 0 + knapsack(idx - 1, W, dp)
    # Take :
    take = float("-inf")
    if(weights[idx] <= W):
        take = profits[idx] + knapsack(idx - 1, W - weights[idx], dp)
    dp[idx][W] =  max(take, un_take)
    return dp[idx][W]

profits = list(map(int, input().replace('{',"").replace('}','').split(',')))
weights = list(map(int, input().replace('{',"").replace('}','').split(',')))
W = int(input())
n = len(profits)
dp = [[-1] * (W + 1) for _ in range(n)]
print(knapsack(n - 1, W, dp))