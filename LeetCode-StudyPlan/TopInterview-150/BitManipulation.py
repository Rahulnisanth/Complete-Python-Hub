# ADDITION OF BINARY NUMBERS :
def addBinary(a: str, b: str) -> str:
        result = ''
        ax = len(a) - 1
        bx = len(b) - 1
        carry = 0
        while ax >= 0 or bx >= 0:
            sum = carry
            if ax >= 0 : sum += int(a[ax])
            if bx >= 0 : sum += int(b[bx])
            result += str(sum % 2)
            carry = sum // 2
            ax -= 1
            bx -= 1
        if carry != 0 : result += str(carry)
        return result[::-1]



# REVERSING THE BINARY NUMBER TO INTEGER :
def reverseBits(n: int) -> int:
    n = format(n, 'b').zfill(32)[::-1]
    return int(n, 2)


# COUNTING THE NO.OF 1S IN A BINARY NUMBER:
def hammingWeight(n):
    count = 0
    while n != 0:
        n &= (n - 1)
        count += 1
    return count
#       [or]
def hammingWeight(n):
    string = bin(n)[2:]
    return string.count('1')


# SINGLE NUMBER MANIPULATION :
def singleNumber(nums) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


# SINGLE NUMBER MANIPULATION II :
def singleNumber(nums) -> int:
    ones = 0
    twos = 0
    for num in nums:
        twos |= ones & num
        ones ^= num
        mask = ~(ones & twos)
        ones &= mask
        twos &= mask
    return ones


# BITWISE RANGE [&] :
def rangeBitwiseAnd(left: int, right: int) -> int:
    while right > left:
        right &= right - 1
    return right