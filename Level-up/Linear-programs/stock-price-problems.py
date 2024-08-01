def maxProfit_stocks(prices, N):
    days = []
    result, i = 0, 0
    while i < N - 1:
        while i < N - 1 and prices[i + 1] <= prices[i]:
            i += 1
        buy = i
        i += 1
        while i < N and prices[i] >= prices[i - 1]:
            i += 1
        sell = i - 1
        if buy < sell:
            days.append((buy, sell))
            result += prices[sell] - prices[buy]
    return days, result

# Input drive :
N = int(input())
prices = [int(input()) for _ in range(N)]
days, profit = maxProfit_stocks(prices, N)
for buy, sell in days:
    print(f"Buy on day:{buy},Sell on day:{sell}", end='\n')
print(f"The maximum profit is:{profit}")