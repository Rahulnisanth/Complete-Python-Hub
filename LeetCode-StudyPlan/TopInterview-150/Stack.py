
# VALID PARENTHESIS :
def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    return False if stack else True


# SIMPLIFIED PATH [DIRECTORY] :
def simplifyPath(path: str) -> str:
    directories = path.split('/')
    stack = []
    for files in directories:
        if files == '' or files == '.':
            continue
        elif files == '..':
            if stack:
                stack.pop()
        else:
            stack.append(files)
    return '/' + '/'.join(stack)


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


# BASIC CALCULATOR USING STACK :
def calculate(s: str) -> int:
    operand, result, sign, stack = 0, 0, 1, []
    
    for char in s:
        if char.isdigit():
            operand = operand * 10 + int(char)
        elif char == '+':
            result += sign * operand
            sign = 1
            operand = 0
        elif char == '-':
            result += sign * operand
            sign = -1
            operand = 0
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = 0
        elif char == ')':
            result += sign * operand
            result *= stack.pop()  
            result += stack.pop() 
            operand = 0

    return result + sign * operand


# REMOVAL OF UNBALANCED PARENTHESIS IN A STRING :
def remove_unbalanced_parentheses(s:str) -> str:
    stack = []
    balanced_indexes = set()

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                balanced_indexes.add(stack.pop())
                balanced_indexes.add(i)
    
    balanced_string = ''.join([char for i, char in enumerate(s) if i in balanced_indexes or char not in '()'])
    return balanced_string


# REVERSE POLISH STRING :
def evalRPN(tokens) -> int:
    stack = []
    operators = ["*","-","+","/"]

    for token in tokens:
        if token in operators:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+": 
                result = num1 + num2
            elif token == "-": 
                result = num1 - num2
            elif token == "*": 
                result = num1 * num2
            elif token == "/": 
                result = int(num1 / num2)
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]
                