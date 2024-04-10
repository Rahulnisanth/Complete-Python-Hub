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