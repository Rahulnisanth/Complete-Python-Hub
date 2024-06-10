# MOVE ZEROES TO END OF THE ARRAY :
def moveZeroes(nums) -> None:
    start = 0
    for num in nums:
        if num != 0:
            nums[start] = num
            start += 1
    for i in range(start, len(nums)):
        nums[i] = 0


# IS SUBSEQUENCE :
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


#  CONTAINER WITH MOST WATER :
def mostWater(height) -> int:
    maxArea = 0
    start, bound = 0, len(height) - 1
    while start < bound:
        maxArea = max(maxArea, min(height[start], height[bound]) * (bound - start))
        if height[start] < height[bound]:
            start += 1
        else:
            bound -= 1
    return maxArea


# MAXIMUM NUMBER OF K-PAIR SUM:
def maxOperations(nums, k: int) -> int:
    nums.sort()
    count, left, right = 0, 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == k :
            count += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] < k:
            left += 1
        else :
            right -= 1
    return count