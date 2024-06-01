def result(ops):
    stack = []
    for op in ops:
        if op == 'C': 
            if stack: stack.pop()
        elif op == 'D': 
            if stack: stack.append(stack[-1] * 2)
        elif op == '+': 
            if len(stack) >= 2: stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)

n = int(input())
ops = input().split()
print(result(ops))