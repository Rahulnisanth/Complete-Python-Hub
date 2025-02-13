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
def missingRolls(rolls, mean, n):
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
# OR 
def missingRolls(rolls, mean, n):
    total_sum = mean * (n + len(rolls))
    roll_sum = sum(rolls)
    needed = total_sum - roll_sum
    if needed < n or needed > (n * 6):
        return []
    quot, rem = needed // n, needed % n
    return [quot + (1 if i < rem else 0) for i in range(n)]


# SPIRAL MATRIX - IV :
def spiralMatrix(m, n, head):
    matrix = [[-1] * n for _ in range(m)]
    top, left = 0, 0
    down, right = m - 1, n - 1
    while left <= right and top <= down and head:
        # Top
        for i in range(left, right + 1):
            if not head:
                break
            matrix[top][i] = head.val
            head = head.next
        top += 1
        # Right
        for i in range(top, down + 1):
            if not head:
                break
            matrix[i][right] = head.val
            head = head.next
        right -= 1
        if top <= down and left <= right and head:
            # Down 
            for i in range(right, left - 1, -1):
                if not head:
                    break
                matrix[down][i] = head.val
                head = head.next
            down -= 1
            # Left
            for i in range(down, top - 1, -1):
                if not head:
                    break
                matrix[i][left] = head.val
                head = head.next
            left += 1
    return matrix


# CHECK WHETHER THE ARRAY OF PAIRS DIVISIBLE BY K :
def canArrange(arr, k) -> bool:
    N = len(arr)
    freq = [0] * k
    for num in arr:
        rem = num % k
        if freq[(k - rem) % k] != 0:
            freq[(k - rem) % k] -= 1
        else:
            freq[rem] += 1
    for rem in freq:
        if rem != 0:
            return False
    return True


# FIND THE SCORE OF AN ARRAY AFTER MARKING ALL ELEMENTS :
def findScore(nums):
    N, score = len(nums), 0
    visited = [False] * N
    idxs = list(range(N))
    idxs.sort(key=lambda x:(nums[x], x))
    for idx in idxs:
        if visited[idx]:
            continue
        score += nums[idx]
        visited[idx] = True
        if idx > 0: visited[idx - 1] = True
        if idx + 1 < N: visited[idx + 1] = True
    return score