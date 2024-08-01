'''
Problem Statement :

You have been given a string S of length N. The given string is a binary string which consists of only 0’s and ‘1’s. Ugliness of a string is defined as the decimal   number that this binary string represents.
Example:
“101” represents 5.
“0000” represents 0.
“01010” represents 10.
There are two types of operations that can be performed on the given string.
    1. Swap any two characters by paying a cost of A coins.
    2. Flip any character by paying a cost of B coins
Initially, you have been given coins equal to the value defined in CASH. Your task is to minimize the ugliness of the string by performing the above mentioned operations on it. Since the answer can be very large, return the answer modulo 10^9+7.

Sample Input
N = 4
String = 1111
Cost = 7
Swap = 1
Flip = 2

Sample Output
1
Explanation: 3 flips can be used to create “0001” which represents 1.
'''
def minimize_ugliness(S, cost, swap_cost, flip_cost):
    def swap(S, cost):
        i = S.index("1")
        j = ''.join(S).rfind("0")  
        if i < j:
            S[i], S[j] = S[j], S[i]
            cost -= swap_cost
        else:
            S, cost = flip(S, cost)
        return S, cost
    def flip(S, cost):
        i = S.index("1")
        S[i] = "0"
        cost -= flip_cost
        print(f"Flipping=> {S}\tCost=> {cost}")
        return S, cost

    while cost > swap_cost or cost > flip_cost:
        S, cost = swap(S, cost)
    return int(''.join(S), 2)

# Input drive :
N = int(input())
string = list(input())
cost = int(input())
swap_cost = int(input())
flip_cost = int(input())
print(minimize_ugliness(string, cost, swap_cost, flip_cost))



'''
Problem Statement :

One of the first lessons IT students learn is the representation of natural numbers in the binary number system (base 2) This system uses only two digits, 0 and 1. In everyday life we use for convenience the decimal system (base 10) which uses ten digits, from 0 to 9. In general, we could use any numbering system.
Computer scientists often use systems based on 8 or 16. The numbering system based on K uses K digits with a value from 0 to K-1. Suppose a natural number M is given, written in the decimal system To convert it to the corresponding writing in the system based on K, we successively divide M by K until we reach a quotient that is less than K
The representation of M in the system based on K is formed by the final quotient (as first digit) and is followed by the remainder of the previous divisionsFor example :
If M=122 and K=8, 122 in base 10= 172 in base 8 This means that the number
In decimal system = 172 in octal system.
172 in base 8 = 1*8^2 + 7*8 + 2 = 122 
You made the following observation in applying the above rule of converting natural numbers to another numbering system
In some cases in the new representation all the digits of the number are the same. For example 63 in base 10= 333 in base 4
Given a number M in its decimal representation, your task is find the minimum base B such that in the representation of M at base B all digits are the same.

Sample Input
41
Sample Output
40
Explanation : Here 41 in base 40. will be 11 so it has all digits the same, and there is no smaller base satisfying the requirements 
'''
def solveBase(M, base):
    rem = M % base
    M //= base
    while M >= base and (M % base == rem):
        M //= base
    if rem == M:
        return True
    return False

# Input drive :
M = int(input())
base = 2
while not solveBase(M, base):
    base += 1
print(base)
