# EUCLID ALGORITHM TO FIND THE GCD OF TWO NUMBERS :
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
