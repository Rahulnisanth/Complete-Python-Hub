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


# IS VALID STRING :
def checkValidString(s: str) -> bool:
    startP, endP = 0, 0
    for ch in s:
        if ch == '(':
            startP += 1 
            endP += 1
        if ch == ')':
            startP -= 1
            endP -= 1
        if ch == '*':
            startP += 1
            endP -= 1
        if startP < 0:
            return False
        if endP < 0:
            endP = 0
    return endP == 0


# NUMBER OF STUDENTS UNABLE TO EAT LUNCH ;
def countStudents(students, sandwiches) -> int:
    counts = [0, 0]
    for student in students:
        counts[student] += 1
    remain = len(sandwiches)
    for sandwich in sandwiches:
        if counts[sandwich] == 0:
            break
        if remain == 0:
            break
        counts[sandwich] -= 1
        remain -= 1
    return remain


# REMOVE K DIGITS TO MAKE THE NUMBER SMALLEST :
def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1
    
    result = ''.join(stack).lstrip('0')

    return result if result else '0'


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
