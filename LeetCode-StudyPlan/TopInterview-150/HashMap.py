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


# GROUP ANAGRAMS :
from collections import defaultdict
def groupAnagrams(strs) :
        myDict = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            myDict[sortedWord].append(word)
        return list(myDict.values())


# VALID WORD PATTERN :
from itertools import zip_longest
def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    return (len(set(pattern)) ==
            len(set(s)) ==
            len(set(zip_longest(pattern, s)))
            )


# TWO SUM TARGET :
def twoSum(nums, target: int):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# HAPPY NUMBER :
def isHappy(n: int) -> bool:
    while n != 1 and n != 4 :
        summation = 0
        while n != 0 :
            rem = n % 10
            summation += rem ** 2
            n //= 10
        n = summation
        
    return True if n == 1 else False


# CONTAINS DUPLICATES :
def containsNearbyDuplicate(nums, k: int) -> bool:
    hashSet = {}
    for i, num in enumerate(nums):
        if num in hashSet and i - hashSet[num] <= k: return True
        hashSet[num] = i
    return False


# LONGEST CONSECUTIVE SEQUENCE :
def longestConsecutive(nums) -> int:
    num_set = set(nums)
    maxLength = 0
    while maxLength < len(num_set):
        num = num_set.pop()
        longest = num + 1
        while longest in num_set:
            num_set.remove(longest)
            longest += 1
        num = num-1
        while num in num_set:
            num_set.remove(num)
            num -= 1
        maxLength = max(maxLength, longest - num - 1)
    return maxLength