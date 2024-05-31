def denominations(amount):
    notes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in notes:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return -1

    result = []
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin == -1:
            return -1  
        result.append(coin)
        current_amount -= coin

    return result


t = int(input())
for _ in range(t):
    amount = int(input())
    print(*denominations(amount))