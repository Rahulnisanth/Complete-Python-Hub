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


# GAS STATION :
def canCompleteCircuit(gas: [int], cost: [int]) -> int:
        start = remainingGas = totalGas = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if remainingGas >= 0:
                remainingGas += diff
            else:
                start = i
                remainingGas = diff
            totalGas += diff
        if totalGas >= 0:
            return start
        return -1


# ZIGZAG CONVERSION OF STRING :
def convert(s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            rows = [[] for i in range(numRows)]
            index, step = 0, 1
            for char in s:
                rows[index].append(char)
                if index == 0:
                    step = 1
                elif index == numRows - 1:
                    step = -1
                index += step
            
            for i in range(numRows):
                rows[i] = ''.join(rows[i])
            return ''.join(rows)


# MINIMUM SIZE SUB-ARRAY SUM :
def minSubArrayLen( target, nums):
    i, j, summation = 0, 0, 0
    ans = 10000000
    while j < len(nums):
        summation += nums[j]
        while summation >= target:
            ans = min(ans, j - i + 1)
            summation -= nums[i]
            i += 1
        j += 1
    return 0 if ans == 10000000 else ans


# TRAPPING RAIN WATER :
def trap(height) -> int:
        water, n = 0, len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[n - 1] = height[n - 1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]
            
        return water


# GROUP ANAGRAMS :
from collections import defaultdict
def groupAnagrams(strs) :
        myDict = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            myDict[sortedWord].append(word)
        return list(myDict.values())


# ARRAY PLUS ONE :
def plusOne(digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits = [1] + [0] * len(digits)
        return digits


# TRAILING-ZEROES [FACTORIAL] :
def trailingZeroes(n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count