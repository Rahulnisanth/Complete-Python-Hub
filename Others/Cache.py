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