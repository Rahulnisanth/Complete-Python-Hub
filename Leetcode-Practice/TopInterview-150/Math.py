# VALID PALINDROME NUMBER :
def isPalindrome(self, x: int) -> bool:
    string = str(x)
    return True if string == string[::-1] else False


# ARRAY PLUS ONE :
def plusOne(digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits = [1] + [0] * len(digits)
        return digits


# TRAILING-ZEROES [FACTORIAL] :
def trailingZeroes(n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


# SQRT(X) WITHOUT IN-BUILT FUNCTION :
def mySqrt(x: int) -> int:
        if x < 2:
            return x
        # BINARY SEARCH MODULE -->
        start, end = 1, x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1
        return end


# POWER (X, N) :
def powerFunc(x: float, n: int) -> float:
    return x**n


# MAX POINTS IN A STRAIGHT LINE :
from collections import defaultdict
def maxPoints(points) -> int:
        if len(points) <= 1:
            return len(points)
        
        max_points = 1

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicate_points = 0
            current_max = 1

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    duplicate_points += 1
                else:
                    # calculate the slopes foe every point-paris ...
                    slope = float('inf') if x1 == x2 else (y2 - y1) / (x2 - x1)
                    slopes[slope] += 1
                    current_max = max(current_max, slopes[slope])
            max_points = max(max_points, current_max + duplicate_points + 1)
        return max_points