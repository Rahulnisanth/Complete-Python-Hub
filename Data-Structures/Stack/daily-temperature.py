def dailyTemperatures(temperatures) :
    n = len(temperatures)
    waitingDays = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            waitingDays[prev_idx] = i - prev_idx
        stack.append(i)
    return waitingDays

n = int(input())
temperatures = [int(input()) for _ in range(n)]
result = dailyTemperatures(temperatures)
for i in range(len(result)):
    if i < len(result) - 1: print(result[i], end=',')
    else: print(result[i], end='')