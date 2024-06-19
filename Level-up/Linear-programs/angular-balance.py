def is_balanced(string, chance) -> int:
    stack = []
    needed_chance = 0
    for char in string:
        if char == '<': 
            stack.append(char)
        elif char == '>':
            if stack and stack[-1] == '<':
                stack.pop()
            else:
                needed_chance += 1
    return 1 if needed_chance <= chance else 0

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


