# MERGE TWO ARRAYS IN SORTED ORDER :
def merge( nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    start = m
    for i in range(n):
        nums1[start] = nums2[i]
        start += 1
    nums1.sort()


# REMOVE THE GIVEN ELEMENTS IN THE ARRAY WITHOUT MODIFYING :
def removeElement(nums, val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


# REMOVE THE DUPLICATE ELEMENTS IN THE SORTED ARRAY :
def removeDuplicates(nums) -> int:
    newList = []
    for i in nums:
        if i not in newList:
            newList.append(i)
    return len(newList)


# REMOVE THE DUPLICATE ELEMENTS IN THE SORTED ARRAY II :
def removeDuplicates(nums) -> int:
    index = 0
    for i in range(len(nums)):
        if nums.count(nums[i]) <= 2 and nums[index] != nums[i]:
            nums[index] = nums[i]
            index += 1
    return index + 1


# MAJORITY ELEMENT IN THE ARRAY :
def majorityElement(nums) -> int:
    for i in nums:
        if nums.count(i) > len(nums) // 2:
            return i


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


# BEST TIME TO SELL AND BUY STOCKS :
def maxProfit(prices) -> int:
    if len(prices) == 1:
        return 0
    else:
        buy, maxProfit = 0, 0
        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
        return maxProfit


# BEST TIME TO SELL AND BUY STOCKS II :
def maxProfit(prices) -> int:
    if len(prices) < 1:
        return 0
    else:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit


# JUMP GAME :
def canJump(nums) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False


# H-INDEX :
def hIndex(citations) -> int:
    citations.sort()
    hIndex = 0
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] > hIndex:
            hIndex += 1
    return hIndex


# PRODUCT ARRAY EXCEPT SELF :
def productExceptSelf(nums):
    product = [0] * len(nums)
    for i in range(len(nums)):
        proCurr = 1
        for j in range(len(nums)):
            if i == j:
                continue
            proCurr *= nums[j]
        product[i] = proCurr
    return product


# GAS STATION :
def canCompleteCircuit( gas, cost) -> int:
    start = rem = total = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        if rem >= 0:
            rem += diff
        else:
            start = i
            rem = diff
        total += diff
    if total >= 0:
        return start
    return -1


# CANDIES :
def candy(ratings) -> int:
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


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


# ROMAN TO INTEGER :
def romanToInt( s: str) -> int:
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    number = 0
    for i in s:
        number += map[i]
    return number


# INTEGER TO ROMAN :
def intToRoman(num):
    if num > 0:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = []
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman.append(roman_letters[i])
        return ''.join(roman)
    else:
        return ""


# LENGTH OF THE LAST WORD :
def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(' ')[-1])


# REVERSE EVERY WORD IN THE SENTENCE :
def reverseWords(s: str) -> str:
    return " ".join(s.strip().split()[::-1])


# LONGEST COMMON PREFIX :
def longestCommonPrefix(strs) -> str:
    strs.sort()
    end = min(len(strs[0]), len(strs[len(strs)-1]))
    index = 0
    while(index < end and strs[0][index] == strs[len(strs)-1][index]):
        index += 1
    return strs[0][0:index]



# ZIG ZAG CONVERSION :
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


# FIND THE OCCURRENCE OF THE STRING :
def strStr(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


# TOTAL MAXIMUM FREQUENCY OF THE ARRAY :
def maxFrequencyElements(nums) -> int:
    counts = [nums.count(num) for num in set(nums)]
    maxCount = 0
    for count in counts:
        if count == max(counts):
            maxCount += count
    return maxCount


# GET THE COMMON ELEMENT WITH MORE FREQUENCY :
def getCommon(nums1, nums2) -> int:
    commons = set(nums1).intersection(set(nums2))
    return min(commons) if commons else -1


# PIVOT ELEMENT FOR THE GIVEN RANGE 'N' :
from math import sqrt
def pivotInteger(self, n):
    x = sqrt(n * (n + 1) / 2)
    converted = int(x)
    return converted if converted == x else -1


# FINDING THE DUPLICATES :
def findDuplicates(nums):
    duplex = {}
    for num in nums:
        if num in duplex:
            duplex[num] += 1
        else:
            duplex[num] = 1
    return [k for k, v in duplex.items() if v >= 2]

        