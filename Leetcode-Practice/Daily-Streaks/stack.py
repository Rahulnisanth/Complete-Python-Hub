# CREATE A CUSTOM STACK TO IMPLEMENT INCREMENT OPERATION :
class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
        
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop(-1)
        return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(len(self.stack)):
                if i < k:
                    self.stack[i] += val