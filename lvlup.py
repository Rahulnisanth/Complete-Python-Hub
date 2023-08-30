# PRIME FACTORIZATION :
def prime_factorization(n):
    factors = []
    divisor = 2 # Starting the iterator with 2
    while divisor <= n: # Looping for all numbers form 2 -> n
        if n % divisor == 0: # Condition for proper divisor
            factors.append(divisor)
            n //= divisor # Modifying the given number by the divisors 
        else:
            divisor += 1 # Case for increasing the common factors
    return factors


# PALINDROME IDENTIFIER :
import re # Importing regular expression for skipping the characters other than alphabets
def is_palindrome(phrase):
    forward = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backward = forward[::-1] # Reversing original phrase
    return (forward == backward)


# SORTING THE WORDS & IGNORING THE SPACES :
def wordSort(words):
    return ' '. join(sorted(words.split(), key=str.casefold)) # Converting all the strings to lower and sorting them


# FINDING INDICES OF GIVEN ELEMENT :
def find_index(examples, search):
    indices = []
    for index, value in enumerate(examples):
        if value == search:
            indices.append([index])
        elif isinstance(examples[index], list): # Case for checking the list instance inside a list
            for i in find_index(examples[index], search): # Recursing the same function over the inside loop
                indices.append([index] + i) # Appending the outer index + inner index
    return indices


# WAITING GAME USING TIME MODULES :
import time
import random

def waiting_game():
    print("Welcome to Waiting Game")
    target = random.randint(1, 5) # Choosing the target timing randomly
    print(f'Your target time is {target} seconds\n')

    input(' ---- Please Enter to Begin ---- ')
    start = time.perf_counter() # Start Bound

    input(f' ---- Please Enter again after {target} seconds ---- ')
    end = time.perf_counter() - start # End Bound
    # Condition checking :
    if target ==  end:
        print(' ---- Unbelievable!! You won the Waiting game ---- ')
    elif end < target:
        print(f' ---- You are {end} fast ---- ')
    else:
        print(f' ---- You are {end} slow ---- ')



# SERIALIZING & DE-SERIALIZING A DICT FILE :
import pickle

def save_file(content, file_name): # Saving the contents in a file using pickle.dump()
    with open(file_name, mode="wb") as file:
        pickle.dump(content, file)
    
def load_file(file_name): # Encrypting the contents in the file using pickle.load()
    with open(file_name, mode="rb") as file:
        return pickle.load(file)





