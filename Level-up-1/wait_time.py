# WAITING GAME USING TIME MODULES :
import time
import random

def waiting_game():
    print(" ---- Welcome to Waiting Game ---- ")
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