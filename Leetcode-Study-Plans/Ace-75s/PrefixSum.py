# FIND THE HIGHEST ALTITUDE :
def largestAltitude(gain) -> int:
    currentAltitude, highestPoint = 0, 0
    for altitude in gain:
        currentAltitude += altitude
        highestPoint = max(highestPoint, currentAltitude)
    return highestPoint


# PIVOT INDEX :
def pivotIndex(nums) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1