# DECODE PIN ARRAY :
def cumulativeSum(n):
    cum = 0
    while n != 0:
        cum += n % 10
        n //= 10
    return cum if cum < 10 else cumulativeSum(cum) 

def decode_pin(pinArray):
    cumSum = []
    for num in pinArray:
        cumSum.append(cumulativeSum(num))
        
    result = ""
    for digit in cumSum:
        if digit % 2 != 0:
            result += chr(ord("a") + digit)
        else:
            result += str(digit)
    return result
