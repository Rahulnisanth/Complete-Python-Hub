# RANDOM-NUMBER GUESSING GAME >>

# importing the random function:
from random import randint
# storing the random number in a variable:
answer = randint(1, 10)
# Looping through the statements and matching the correct guess!
while True:
    try:
        guess = int(input("Guess a number from 1 to 10:  "))
        if 0 < guess < 11:
            if guess == answer:
                print("!! You are a genius !!")
                break
        else:
            print("!! Hey Mate, Please select a number between 1 to 10 !!")

    except ValueError:
        print("!! Hey Mate, Please enter a number !!")
