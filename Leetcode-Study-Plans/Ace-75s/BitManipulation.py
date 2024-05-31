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


# WONDERFUL-SUBSTRING :
def wonderfulSubstrings(word: str) -> int:
    count = [0] * 1024
    result, xor, count[xor] = 0, 0, 1
    for char in word:
        idx = ord(char) - ord('a')
        xor ^= 1 << idx
        result += count[xor]
        for i in range(10):
            result += count[xor ^ (1 << i)]
        count[xor] += 1
    return result


# SINGLE NUMBER III :
def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    xor & -xor
    result = [0, 0]
    for num in nums:
        if num & xor == 0:
            result[0] ^= num
        else:
            result[1] ^= num
    return result