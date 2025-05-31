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
            if ch == "D" and stack[-1] == "C":
                stack.pop()
            elif ch == "B" and stack[-1] == "A":
                stack.pop()
        stack.append(ch)
    return len(stack)


# MAXIMUM WIDTH OF THE RAMP :
def maxWidthRamp(nums) -> int:
    stack, N = [], len(nums)
    for i in range(N):
        if not stack or nums[i] < nums[stack[-1]]:
            stack.append(i)
    result = 0
    for j in range(N - 1, -1, -1):
        while stack and nums[j] >= nums[stack[-1]]:
            result = max(result, j - stack.pop())
            if result == j:
                return result
    return result


# PARSING A BOOLEAN EXPRESSION :
def parseBoolExpr(self, expression: str) -> bool:
    # Helper function
    def to_bool(char: str) -> bool:
        return char == 't'
    
    stack = []
    for char in expression:
        if char == ')':
            sub_expr = []
            while stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()  
            operator = stack.pop()  
            
            if operator == '!':
                result = not to_bool(sub_expr[0])
            elif operator == '&':
                result = all(to_bool(val) for val in sub_expr)
            elif operator == '|':
                result = any(to_bool(val) for val in sub_expr)
            
            stack.append('t' if result else 'f')
        elif char not in (',', ' '): 
            stack.append(char)
    
    return to_bool(stack.pop())


# REVERSE ONLY THE LETTERS :
def reverseOnlyLetters(self, s: str) -> str:
    stack = [ch for ch in s if ch.isalpha()]
    answer = ''
    for ch in s:
        if ch.isalpha():
            answer += stack.pop()
        else:
            answer += ch
    return answer
