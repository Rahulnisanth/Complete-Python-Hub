def is_balanced(string, chance) -> int:
    string = string[::-1]
    stack = []
    for char in string:
        if char == '>': 
            stack.append(char)
        elif char == '<':
            if stack and stack[-1] == '>':
                stack.pop()
    return 1 if len(stack) <= chance else 0

# Storage fields
strings = []
chances = []

# Input stream
n = int(input())
for _ in range(n):
    strings.append(input().strip())
m = int(input())
for _ in range(m):
    chances.append(int(input()))

# Core drive
for i in range(n):
    print(is_balanced(strings[i], chances[i]))
