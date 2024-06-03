def denomination_steps(coins, amount, n):
    def count(dp, coins, amount, n) -> int:
        # Base case if amount if formed :   
        if amount == 0:
            dp[n][amount] = 1
            return dp[n][amount]
        # Edge case :
        if n == 0 or amount <= 0: return 0
        # If sub-problem already found:
        if dp[n][amount] != -1: return dp[n][amount]
        # Calculating the combinations using recursive approach:
        # Exclude the last coin [LEFT] (or) Include and reduce the amount with last coin [RIGHT] 
        dp[n][amount] = count(dp, coins, amount - coins[n - 1], n) + count(dp, coins, amount, n - 1)

        return dp[n][amount]
    dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]
    return count(dp, coins, amount, n)

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())
    print(denomination_steps(coins, amount, n))