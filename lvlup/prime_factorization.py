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