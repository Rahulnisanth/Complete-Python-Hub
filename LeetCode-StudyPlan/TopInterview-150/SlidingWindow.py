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


# LENGTH OF THE LONGEST NON-REPEATING SUBSTRING :
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    else:
        char_index = {}
        max_length = 0
        start = 0
        # Looping through chars >>
        for end in range(n):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            else:
                max_length = max(max_length, end - start + 1)
            char_index[s[end]] = end
        return max_length