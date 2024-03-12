#  MERGE THE TWO STRINGS ALTERNATIVELY :
def mergeAlternately(word1: str, word2: str) -> str:
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