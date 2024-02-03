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


# SQRT(X) WITHOUT IN-BUILT FUNCTION :
def mySqrt(x: int) -> int:
        if x < 2:
            return x
        # BINARY SEARCH MODULE -->
        start, end = 1, x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1
        return end


# SUMMARY RANGES :
def summaryRanges(nums):
        if len(nums) < 1:
            return []
        else:
            lister = []
            start = nums[0]
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1] + 1:
                    if start == nums[i - 1]:
                        lister.append(str(start))
                    else:
                        lister.append(str(start) + "->" + str(nums[i - 1]))
                    start = nums[i]
            if start == nums[-1]:
                lister.append(str(start))
            else:
                lister.append(str(start) + "->" + str(nums[-1]))
    
            return lister


# DAILY TEMPERATURES :
def dailyTemperatures(temperatures) :
        n = len(temperatures)
        waitingDays = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                waitingDays[prev_idx] = i - prev_idx
            stack.append(i)
        return waitingDays


# MAX POINTS IN A STRAIGHT LINE :
from collections import defaultdict
def maxPoints(points) -> int:
        if len(points) <= 1:
            return len(points)
        max_points = 1
        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicate_points = 0
            current_max = 1

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    duplicate_points += 1
                else:
                    # calculate the slopes foe every point-paris ...
                    slope = float('inf') if x1 == x2 else (y2 - y1) / (x2 - x1)
                    slopes[slope] += 1
                    current_max = max(current_max, slopes[slope])
            max_points = max(max_points, current_max + duplicate_points + 1)
        return max_points


# SIMPLIFIED PATH [FOLDER PATHS] :
def simplifyPath(path: str) -> str:
        directories = path.split('/')
        stack = []
        for files in directories:
            if files == '' or files == '.':
                continue
            elif files == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(files)
        return '/' + '/'.join(stack)


# MIN SUB ARRAY USING DYNAMIC PROGRAMMING :
def maxSumAfterPartitioning(arr , k) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_val = float('-inf')
            for j in range(1, min(i, k) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)
        return dp[n]