# REMOVE STARS IN THE GIVEN STRING :
def removeStars(s: str) -> str:
    if not s:
        return ""
    stack = []
    for ch in s:
        if ch == '*':
            if stack: 
                stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


# ASTEROID COLLISION :
def asteroidCollision(asteroids):
    if not asteroids:
        return []
    stack = []
    for ast in asteroids:
        while ast < 0 and stack and stack[-1] > 0:
            if stack[-1] < abs(ast):
                stack.pop()
                continue
            elif stack[-1] == abs(ast):
                stack.pop()
            break
        else:
            stack.append(ast)
    return stack


# DECODE THE GIVEN STRING :
def decodeString(s: str) -> str:
    stack = []
    for ch in s:
        if ch != ']':
            stack.append(ch)
        else:
            result = ''
            while stack[-1] != '[' :
                result += stack.pop()
            stack.pop()
            n = ''
            while len(stack) != 0 and stack[-1].isdigit():
                n += stack.pop()
            stack.append(result * int(n[::-1]))
    return ''.join([word[::-1] for word in stack ])