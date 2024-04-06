# MAKE A GOOD STRING :
def makeGood(s: str) -> str:
    if len(s) > 1:
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
    return s


# MINIMUM REMOVE TO MAKE VALID PARENTHESIS :
def minRemoveToMakeValid(s: str) -> str:
    result = []
    stack, invalidIdx = [], set()
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                invalidIdx.add(i)

    invalidIdx.update(stack)

    for i, ch in enumerate(s):
        if i not in invalidIdx:
            result.append(ch)
    
    return ''.join(result)