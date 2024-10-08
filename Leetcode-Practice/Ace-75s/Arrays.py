# MERGE STRINGS ALTERNATIVELY :
def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min((len(word1), len(word2)))
        result = ""
        for i in range(n):
            result += word1[i]
            result += word2[i]
        result += word1[n:] + word2[n:]
        return "".join(result)


# GCD OF TWO STRINGS :
from math import gcd
def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1 :
        return ""
    return str1[ : gcd(len(str1), len(str2))]


#  KIDS WITH MOST CANDIES :
def kidsWithCandies(candies, extraCandies):
    maxCandy = max(candies)
    result = []
    for candy in candies:
        if candy + extraCandies >= maxCandy:
            result.append(True)
        else:
            result.append(False)
    return result


#  CAN PLACE FLOWERS :
def canPlaceFlowers(flowerbed, n: int) -> bool:
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        i += 1

    return count >= n



# VOWELS REVERSAL :
def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s = list(s)
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] in vowels and s[end] in vowels:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
        elif s[start] in vowels:
            end -= 1
        elif s[end] in vowels:
            start += 1
        else:
            start += 1
            end -= 1

    return "".join(s)


# REVERSE EVERY WORD IN THE SENTENCE :
def reverseWords(s: str) -> str:
    return " ".join(s.strip().split()[::-1])


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


# INCREASING TRIPLET :
def increasingTriplet(nums) -> bool:
    small = float('inf')
    mid = float('inf')
    for big in nums:
        if big <= small:
            small = big
        elif big <= mid:
            mid = big
        else:
            return True
    return False


# STRING COMPRESSION :
def compress(chars) -> int:
    i, k = 0, 0
    while i < len(chars) :
        j = i
        while j < len(chars) and chars[j] == chars[i] :
            j += 1
        chars[k] = chars[i]
        k += 1
        if (j - i) > 1 :
            s = str((j - i))
            for ch in s :
                chars[k] = ch
                k += 1
        i = j
    return k




