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