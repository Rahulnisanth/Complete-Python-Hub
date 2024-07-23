# LENGTH OF THE LONGEST PALINDROME THAT CAM BE BUILT USING THE GIVEN STRING :
from collections import Counter
def lengthLongestPalindrome(s:str) -> int:
    freq = Counter(s)
    result, odd_flag = 0, False
    for count in freq.values():
        if count % 2 == 0:
            result += count
        else:
            result += (count - 1)
    return result + 1 if odd_flag else result