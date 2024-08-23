# FRACTION ADDITION & SUBTRACTION :
from fractions import Fraction
def fractionAddition(expression: str) -> str:
    result = Fraction(0)
    i, n = 0, len(expression)
    while i < n:
        sign = 1
        if expression[i] == "-":
            sign = -1
            i += 1
        elif expression[i] == "+":
            i += 1
        numerator = 0
        while i < n and expression[i].isdigit():
            numerator = numerator * 10 + int(expression[i])
            i += 1
        i += 1
        denominator = 0
        while i < n and expression[i].isdigit():
            denominator = denominator * 10 + int(expression[i])
            i += 1
        result += sign * Fraction(numerator, denominator)
    return f"{result.numerator}/{result.denominator}"