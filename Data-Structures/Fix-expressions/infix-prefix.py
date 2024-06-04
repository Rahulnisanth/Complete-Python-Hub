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
def infixToPostfix(input_string):
    input_string = '(' + input_string + ')'
    stack = []
    result = ''

    for i in range(len(input_string)):
        # Digit / Alphabet :
        if input_string[i].isalpha() or input_string[i].isdigit():
            result += input_string[i]
        # If open parenthesis '(' += stack :
        elif input_string[i] == '(': stack.append(input_string[i])
        # IF close parenthesis ')' pop the stack until it reaches the open '(' :
        elif input_string[i] == ')':
            while stack[-1] != '(': 
                result += stack.pop()
            stack.pop()
        # If an operator found :
        else:
            if is_operator(input_string[i]):
                if input_string[i] == '^':
                    while get_priority(input_string[i]) <= get_priority(stack[-1]):
                        result += stack.pop()
                else:
                    while get_priority(input_string[i]) < get_priority(stack[-1]):
                        result += stack.pop()
                stack.append(input_string[i])
    
    # Appending the operators to the end of the result :
    while len(stack) < 0:
        result += stack.pop()
    return result

# Infix to prefix using postfix :
def infixToPrefix(input_string):
    input_string = input_string[::-1]
    for i in range(len(input_string)):
        if input_string[i] == '(':
            input_string.replace(input_string[i],")")
        elif input_string[i] == ')': 
            input_string.replace(input_string[i],'(')
    print(input_string)
    prefix = infixToPostfix(input_string)
    return prefix[::-1]

# Input stream :
print(infixToPrefix("(a*b+c)*d"))


