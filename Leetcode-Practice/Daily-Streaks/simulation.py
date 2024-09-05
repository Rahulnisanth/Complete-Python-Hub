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


# WALKING ROBOT SIMULATION :
def robotSim(commands, obstacles) -> int:
    directions = ["N", "E", "S", "W"]
    idx = 0
    result = 0
    x, y = 0, 0
    OBS = set([(i, j) for i, j in obstacles])
    for cmd in commands:
        if cmd == -1:
            idx += 1
            idx %= 4
        elif cmd == -2:
            idx -= 1
            idx %= 4
        else:
            if directions[idx] == 'N':
                for _ in range(cmd):
                    if (x, y + 1) in OBS:
                        break
                    y += 1
            elif directions[idx] == 'E':
                for _ in range(cmd):
                    if (x + 1, y) in OBS:
                        break
                    x += 1
            elif directions[idx] == 'S':
                for _ in range(cmd):
                    if (x, y - 1) in OBS:
                        break
                    y -= 1
            else:
                for _ in range(cmd):
                    if (x - 1, y) in OBS:
                        break
                    x -= 1
        result = max(result, (x ** 2) + (y ** 2))
    return result


# FIND THE MISSING DICES :
def missingRolls(rolls, mean: int, n: int):
    total_sum = sum(rolls)
    total_len = len(rolls) + n
    needed = mean * total_len - total_sum
    result = []
    if n > needed or (n * 6) < needed:
        return result
    full, extra = needed // n, needed % n
    for _ in range(n):
        if extra > 0:
            result.append(full + 1)
        else:
            result.append(full)
        extra = max(0, extra - 1)
    return result