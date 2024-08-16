# COUNT THE NO.OF 1S IN GIVEN RANGE :
def countBits(n: int):
    counts = [0] * (n + 1)
    for i in range(1, n + 1) :
        counts[i] = counts[i >> 2] + (i & i)
        # {OR} >>> counts[i] = counts[i // 2] + (i % 2) 
    return counts


# SINGLE NUMBER MANIPULATION :
def singleNumber(nums) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


# MINIMUM FLIPS TO MAKE A OR B EQUAL TO C :
def minFlips(a, b, c):
    flips = 0
    while a > 0 or b > 0 or c > 0:
        bit_a = a & 1
        bit_b = b & 1
        bit_c = c & 1
        if bit_c == 1:
            if bit_a == 0 and bit_b == 0:
                flips += 1
        else:
            flips += (bit_a + bit_b)
        a >>= 1
        b >>= 1
        c >>= 1
    return flips
