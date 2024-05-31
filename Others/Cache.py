def calculateOddSum(nums) -> int:
    left, right, total = 0, len(nums) - 1, 0
    while left <= right:
        if nums[left] % 2 != 0 :
            total += nums[left] 
        if nums[right] % 2 != 0:
            total += nums[right]
        left += 1
        right -= 1
    return total


# BITWISE MANIPULATION :
def tackle(n1, n2):
    if bin(n1)[-1] == '1' and bin(n2)[-1] == '1':
        n1 = n1 ^ n2
        n2 = n1 ^ n2
        n1 = n1 ^ n2
    if bin(n1)[-1] == '0' and bin(n2)[-1] == '0':
        n1 = n1 << 3
        n2 = n2 << 3
    return [n1, n2]
    
n1, n2 = list(map(int, input().split()))
print(tackle(n1, n2))

# IS SUM PRESENT IN ARRAY :
def is_found(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1):
            if i != j and nums[i] + nums[j] == k: return f"index1: {j}\nindex2: {i}"
    return "No two sum solution"

nums = list(map(int, input().split()))
k = int(input())
print(is_found(nums, k))


def solvePuzzle(n):
    def helper(dp, left, right):
        if left >= right:
            return 0
        if dp[left][right] != 0:
            return dp[left][right]
        else:
            result = float('inf') # max value:
            for guess in range(left, right + 1):
                temp = guess + max(helper(dp, guess + 1, right), helper(dp, left, guess - 1))
                result = min(result, temp)
        return result

    dp = [[0] * (n+1)] * (n+1)
    print(dp)
    helper(dp, 0, len(dp))

print(solvePuzzle(10))