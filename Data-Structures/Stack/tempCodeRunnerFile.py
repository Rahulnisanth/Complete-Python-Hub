def convert_to_text(word) -> bool:
    stack = []
    for letter in word:
        if letter == '#': stack.pop()
        stack.append(letter)
    return ''.join(stack)  


s = input().strip()
t = input().strip()
print(convert_to_text(s) == convert_to_text(t))