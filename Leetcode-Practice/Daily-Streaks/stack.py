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


# MIN STRING LENGTH AFTER THE REMOVAL OF SUB-STRINGS :
def minLength(s: str) -> int:
    stack = []
    for ch in s:
        if stack:
            if ch == 'D' and stack[-1] == 'C':
                stack.pop()
            elif ch == 'B' and stack[-1] == 'A':
                stack.pop()
        stack.append(ch)
    return len(stack)