# NUMBER GUESSING GAME :
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guessNumber(n: int) -> int:
    left, right = 0, n
    while left < right:
        flag = (left & right) + ((left ^ right) >> 1)
        if guess(flag) == 0: # type: ignore
            return flag
        elif guess(flag) == 1: # type: ignore
            left = flag + 1
        else:
            right = flag - 1
    return left


# FIND THE PEAK ELEMENT IN THE ARRAY :
def findPeakElement(nums) -> int:
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


# SUCCESSFUL PAIRS OF SPELLS AND POTIONS :
def successfulPairs(
    self, spells: List[int], potions: List[int], success: int
) -> List[int]:
    result = []
    potions.sort()
    N = len(potions)
    for spell in spells:
        minPotionNeeded = math.ceil(success / spell)
        potionIDX = bisect.bisect_left(potions, minPotionNeeded)
        successPairCount = N - (potionIDX)
        result.append(successPairCount)
    return result
