# MAXIMUM AVERAGE SUB-ARRAY I :
def findMaxAverage(nums, k: int) -> float:
    currSum = maxSum = sum(nums[:k])
    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, currSum)
    return maxSum / k