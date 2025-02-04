# IMPLEMENT STACK USING 2 QUEUES :
class MyStack:

    def __init__(self):
        self.Q1 = deque()
        self.Q2 = deque()

    def push(self, x: int) -> None:
        self.Q2.append(x)
        while self.Q1:
            self.Q2.append(self.Q1.popleft())
        self.Q1, self.Q2 = self.Q2, self.Q1
        
    def pop(self) -> int:
        return self.Q1.popleft()
        

    def top(self) -> int:
        if self.Q1:
            return self.Q1[0]
        

    def empty(self) -> bool:
        return len(self.Q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
