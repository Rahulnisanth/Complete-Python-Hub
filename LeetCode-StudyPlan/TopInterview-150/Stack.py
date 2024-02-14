
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