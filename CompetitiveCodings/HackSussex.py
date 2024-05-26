# NUMBER OF SQUARES FORMED FROM THE RECTANGLES :
def numberRectangles(rectangles : list[list[int]]) -> int :
    sideOfSquares = []
    for i in range(len(rectangles)):
        sideOfSquares.append(min(rectangles[i]))

    maxNumberOfRectangles = 0
    for i in range(len(rectangles)):
        maxNumberOfRectangles += rectangles[i].count(max(sideOfSquares)) if min(rectangles[i]) == max(sideOfSquares) else 0
    return maxNumberOfRectangles


# MAKE ARRAY ZERO BY SUBTRACTING EQUAL AMOUNTS:
def alterArray(array):
    def helper(nums, steps):
        nums = [num for num in nums if num > 0]
        if not nums:
            return steps
        k = min(nums)
        nums = [num - k for num in nums]
        return helper(nums, steps + 1)
    steps = helper(array, 0)
    return steps
# or
def alterArray(array):
    array = set(array)
    array.discard(0)
    return len(array)


# CHECK THE TWO STRINGS ARE EQUAL OR NOT IN REPLACEMENT :
def checkString(s1, s2) -> bool :
    return True if sorted(s1) == sorted(s2) else False


# MAXIMUM NUMBER OF WORDS CAN TYPE USING DEFECTED KEYBOARD :
def numberOfWord(words, defectKey):
    words = words.split()
    defectKey = set(defectKey)
    points = 0
    for word in words:
        if not any(letter in defectKey for letter in word):
            points += 1
    return points


# SORT ODD & EVENT INDICES INDEPENDENTLY :
def sortArray(nums):
    even = [nums[i] for i in range(len(nums)) if i % 2 == 0]
    odd = [nums[i] for i in range(len(nums)) if i % 2 != 0]
    even.sort()
    odd.sort(reverse=True)
    return list(zip(even, odd))


