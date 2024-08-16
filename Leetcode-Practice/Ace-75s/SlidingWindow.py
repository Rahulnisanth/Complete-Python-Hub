# MAXIMUM AVERAGE SUB-ARRAY I :
def findMaxAverage(nums, k: int) -> float:
    currSum = maxSum = sum(nums[:k])
    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, currSum)
    return maxSum / k


# MAXIMUM NUMBER OF VOWELS IN SUB-ARRAY :
def maxVowels(s: str, k: int) -> int:
    vowel_count = 0
    vowels = "aeiou"
    m_vowels = 0
    for i in range(k):
        if s[i] in vowels:
            vowel_count += 1
            m_vowels = max(m_vowels, vowel_count)
    i = 0
    for j in range(k, len(s)):
        if s[j] in vowels:
            vowel_count += 1
        if s[i] in vowels and k > 1:
            vowel_count -= 1
        i += 1
        m_vowels = max(m_vowels, vowel_count)
    return min(m_vowels, k)


# MAXIMUM CONSECUTIVE ONES III :
def longestOnes(nums, k) -> int:
    left, zeroes, maxLen = 0, 0, 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        maxLen = max(maxLen, right - left + 1)
    return maxLen


# LONGEST LENGTH OF SUB-ARRAY AFTER DELETING ONE ELEMENT :
def longestSubArray(nums) -> int:
    if not nums:
        return 0
    left, zeroes, k = 0, 0, 1
    result = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        result = max(result, right - left + 1)
    return result - k