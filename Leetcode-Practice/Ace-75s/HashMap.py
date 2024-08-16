# FIND THE DIFFERENCE OF TWO ARRAYS :
def findDifference(nums1, nums2):
    first = list(set(nums1) - set(nums2))
    second = list(set(nums2) - set(nums1))
    return [first, second]


# DETERMINE IF TWO STRINGS ARE CLOSE :
from collections import Counter
def isClose(word1, word2) -> bool:
    if set(word1) != set(word2):
        return False
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())