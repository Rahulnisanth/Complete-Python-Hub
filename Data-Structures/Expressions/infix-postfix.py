# Function to check the character is a digit / alphabet :
def is_operator(letter) -> bool:
    return (not letter.isdigit()) and (not letter.isalpha())

# Priority for the characters :
def get_priority(letter) -> int:
    if letter == '+' or letter == '-': return 1
    if letter == '*' or letter == '/': return 2
    if letter == '^': return 3
    else: return 0

# Traversing the characters :
def infixToPostfix(input) -> str:
    input = '(' + input + ')'
    stack = []
    result = ''

    for i in range(len(input)):
        # Digit / Alphabet :
        if input[i].isalpha() or input[i].isdigit():
            result += input[i]
        # If open parenthesis '(' += stack :
        elif input[i] == '(': stack.append(input[i])
        # IF close parenthesis ')' pop the stack until it reaches the open '(' :
        elif input[i] == ')':
            while stack[-1] != '(': 
                result += stack.pop()
            stack.pop()
        # If an operator found :
        else:
            if is_operator(input[i]):
                if input[i] == '^':
                    while get_priority(input[i]) <= get_priority(stack[-1]):
                        result += stack.pop()
                else:
                    while get_priority(input[i]) < get_priority(stack[-1]):
                        result += stack.pop()
                # Adding the current operator to stack :
                stack.append(input[i])
    
    # At-last Appending the operators to the end of the result :
    while len(stack) < 0:
        result += stack.pop()
    return result

# Input stream :
print(infixToPostfix("x+y*z/w+u"))


