# VALID PALINDROME :
def isPalindrome(s: str) -> bool:
    stripped = "".join([char for char in s if char.isalpha() or char.isdigit()])
    return True if stripped.lower()[::-1] == stripped.lower() else False


# IS SUBSEQUENCE :
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# TWO SUM SORTED ARRAY :
def twoSum(numbers, target: int):
    start, end = 0, len(numbers) - 1
    while(True):
        if numbers[start] + numbers[end] == target:
            return [start + 1, end + 1]
        elif numbers[start] + numbers[end] > target:
            end -= 1
        else:
            start += 1


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


# THREE SUM :
def threeSum(nums):
    finalArr = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums)- 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0 :
                finalArr.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
    return finalArr
