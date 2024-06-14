def is_balanced(string, chances) -> int:
    stack = []
    for i in range(len(string)):
        if string[i] == '>':
            if stack and stack[-1] == '<':
                continue
            else:
                chances -= 1
                if chances <= 0: return False
        else: stack.append(string[i])
    return True if len(stack) == 0 else False

print(is_balanced("<>>>>", 2))
print(is_balanced("<><>", 2))