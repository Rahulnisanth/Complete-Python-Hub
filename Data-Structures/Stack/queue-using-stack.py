# IMPLEMENT QUEUE USING 2 STACKS :
class MyQueue:

    def __init__(self):
        self.S1 = []
        self.S2 = []
        

    def push(self, x: int) -> None:
        while len(self.S1) != 0:
            self.S2.append(self.S1.pop())
        self.S1.append(x)
        while len(self.S2) != 0:
            self.S1.append(self.S2.pop())
        

    def pop(self) -> int:
        if self.S1:
            return self.S1.pop()
        

    def peek(self) -> int:
        if self.S1:
            return self.S1[-1]
        

    def empty(self) -> bool:
        return len(self.S1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
