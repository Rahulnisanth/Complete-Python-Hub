def convert_to_text(word) -> bool:
    if not word:
        return ''
    stack = []
    for letter in word:
        if letter == '#': 
            if stack: 
                stack.pop()
        else: 
            stack.append(letter)
    return ''.join(stack)  

# Input stream :
s = input().strip()
t = input().strip()
print(convert_to_text(s) == convert_to_text(t))