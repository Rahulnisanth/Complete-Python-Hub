def rob(amounts, n):
    if n == 1:
        return amounts[0]
    # Linear condition :
    def rob_linear(amounts):
        n = len(amounts)
        if n == 0:
            return 0
        if n == 1:
            return amounts[0]
        prev1, prev2 = 0, 0
        for num in amounts:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        return prev1
    return max(rob_linear(amounts[:-1]), rob_linear(amounts[1:]))


# Input stream :
amounts = list(map(int, input().split(",")))
print(rob(amounts, len(amounts))) 
