def denominations(amount):
    notes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for note in notes:
        for i in range(note, amount + 1):
            dp[i] = min(dp[i], dp[i - note] + 1)
            coin_used[i] = note

    if dp[amount] == float('inf'):
        return -1
    print(coin_used)
    result = []
    current_amount = amount
    while current_amount > 0:
        if note == -1:
            return -1 
        note = coin_used[current_amount]
        result.append(note)
        current_amount -= note

    return result


t = int(input())
for _ in range(t):
    amount = int(input())
    print(*denominations(amount))
