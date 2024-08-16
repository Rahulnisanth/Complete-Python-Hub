# MAXIMUM AVERAGE SUB-ARRAY I :
def findMaxAverage(nums, k: int) -> float:
    currSum = maxSum = sum(nums[:k])
    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, currSum)
    return maxSum / k


# MAXIMUM CONSECUTIVE ONES III :
def longestOnes(nums, k) -> int:
    left, zeroes, maxLen = 0, 0, 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        maxLen = max(maxLen, right - left + 1)
    return maxLen