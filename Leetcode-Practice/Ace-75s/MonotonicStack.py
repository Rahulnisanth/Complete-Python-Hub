# DAILY TEMPERATURES :
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


# ONLINE STOCK SPAN :
class StockSpanner:
    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        count = 1
        while self.stock and self.stock[-1][0] <= price:
                count += self.stock.pop()[1]
        self.stock.append((price, count))
        return count
