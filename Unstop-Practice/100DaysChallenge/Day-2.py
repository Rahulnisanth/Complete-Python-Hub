'''
Problem Statement
In a lively car showroom, an array of cars awaits, each with its distinctive features. Picture yourself mixing and matching these cars in unique combinations to create dream blends which has a fscore equal to the XOR value of the combination. 

Your mission: compute the blend score, which is the XOR of the f-score values for all these dreamy combinations. Now, it's time to reveal the grand total!
'''
def calculateFScore(cars, n) -> int:
    def combinations(arr):
        dump = 0
        for i in range(len(arr)):
            subset = 0
            for j in range(i + 1):
                subset ^= arr[j]
            dump ^= subset
        return dump
    result = 0
    for i in range(n):
        result ^= combinations(cars[i:])
    return result if 1 <= n < 10000 else 0


'''
Problem statement :
In a magical land, there is a young explorer named Raju who embarks on a thrilling adventure with his enchanted vehicle. This magical vehicle can only move in four directions: right (R), left (L), up (U), and down (D). Raju starts his journey at the heart of the mystical forest, located at coordinates (0, 0).

As Raju follows a sequence of mysterious symbols etched on ancient stones, he maneuvers his magical vehicle accordingly. 'R' guides him to the right, 'L' to the left, 'U' upwards, and 'D' downwards. The direction he faces does not matter; the symbols' magic ensures his vehicle moves in the intended direction. Can you assist Raju in deciphering his fate? If he ends up back at the starting point, please say YES; otherwise, say NO.
'''
n = int(input())
moves= input()
position = [0, 0]
for move in moves:
    if move == 'U': position[0] += 1
    if move == 'D': position[0] -= 1
    if move == 'R': position[1] += 1
    if move == 'L': position[1] -= 1
print('YES' if position[0] == 0 and position[1] == 0 else 'NO')


'''
Problem Statement :
One day, Chris arrived at the entrance of Adventureland. There is an n × n magic grid on the entrance, which is filled with only 1s.
Any person gets the entry when they count the sum of the diagonal integers right. Chris is working on counting the sum.
Can you help him to solve it fast?
'''
n = int(input())
if 2 <= n <= 100000: print(n * 2 if n % 2 == 0 else (n * 2) - 1)
elif n == 1: print(1)
else: print(0)


'''
Problem Statement
In a game, there are 2 queens which are to be placed on 2 mats. The mats are arranged with orders specified with numbers on them. The placement of the queen is to be done in such a manner that when one of the orders of the mat, when divided with the other order, gives the maximum possible value. The order of the mats is between the two integers denoted by l and r.
Find the order of mats on which the two queens can be placed.
'''
import math
n = int(input())
for _ in range(n):
    left, right = list(map(int, input().split()))
    if left == right:
        print(0)
    else:
        mods = (right % left) if (right / 2 < left) else right % ((right / 2) + 1)
        print(math.ceil(mods))
