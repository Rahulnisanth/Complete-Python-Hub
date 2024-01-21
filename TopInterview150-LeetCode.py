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


# ARRAY ROTATION :
def rightRotater(arr, k) -> list[int]:
    def rotater(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    k %= len(arr)
    rotater(arr, 0, len(arr) - 1)
    rotater(arr, k, len(arr) - 1)
    rotater(arr, 0, k - 1)
    return arr


# MEDIAN OF THE GIVEN ARRAY :
def findMedianSortedArrays(nums1, nums2) -> float:
    nums1 += nums2
    nums1.sort()
    n = len(nums1)
    if n % 2 == 0:
        return (nums1[n // 2] + nums1[(n // 2) - 1]) / 2
    else:
        return nums1[n // 2]


# POWER (X, N) :
def powerFunc(x: float, n: int) -> float:
    return x**n


# CLOCKWISE - SPIRAL MATRIX :
def spiralOrder(matrix):
    spiralMatrix = []
    top = 0
    left = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            spiralMatrix.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            spiralMatrix.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiralMatrix.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiralMatrix.append(matrix[i][left])
            left += 1

    return spiralMatrix


# VALID PARENTHESIS :
def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    return False if stack else True
