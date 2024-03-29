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


# SUBSTRING WITH ALL THE CONCATENATION OF THE WORD ARRAY :
def findSubstring(s: str, words):
    result = []
    length = len(words[0])
    # Map to store the frequency :
    word_map = {}
    for word in words:
        word_map[word] = word_map.get(word, 0) + 1

    for i in range(len(s) - length * len(words) + 1):
        copy_map = word_map.copy() # Copy map to track the frequencies ...
        for j in range(len(words)):
            word = s[(i + j * length) : (i + j * length + length)]
            if word in copy_map:
                count = copy_map[word]
                if count == 1:
                    del copy_map[word]
                else:
                    copy_map[word] = count - 1
                if not copy_map:
                    result.append(i)
                    break
            else:
                break

    return result


# MINIMUM WINDOW SUBSTRING :
def minWindow(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    map = [0] * 128
    count = len(t)
    start = 0
    end = 0
    min_len = float('inf')
    start_index = 0
    # UPVOTE !
    for char in t:
        map[ord(char)] += 1

    while end < len(s):
        if map[ord(s[end])] > 0:
            count -= 1
        map[ord(s[end])] -= 1
        end += 1

        while count == 0:
            if end - start < min_len:
                start_index = start
                min_len = end - start

            if map[ord(s[start])] == 0:
                count += 1
            map[ord(s[start])] += 1
            start += 1

    return "" if min_len == float('inf') else s[start_index:start_index + min_len]


# NUMBER OF MINIMUM SUB-PRODUCTS IN A ARRAY <= K :
def numSubarrayProductLessThanK(nums, k) -> int:
    if k <= 1:
        return 0

    count = 0
    product = 1
    left = 0        
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1
        count += right - left + 1
    
    return count


# LENGTH OF THE LONGEST SUB-ARRAY WITH MOST K FREQUENCY :
def maxSubarrayLength(nums, k: int) -> int:
    ans = 0
    mapper = {}
    l = 0
    n = len(nums)
    for r in range(n):
        mapper[nums[r]] = mapper.get(nums[r], 0) + 1
        if mapper[nums[r]] > k:
            while nums[l] != nums[r]:
                mapper[nums[l]] -= 1
                l += 1
            mapper[nums[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
    return ans


# COUNTING THE NO. OF SUB-ARRAYS WITH KTH OCCURRENCE OF MAX ELEMENT :
def countSubarrays(nums, k: int) -> int:
    maxNum = max(nums)
    count = 0
    left = 0
    right = 0
    ans = 0
    
    while right < len(nums) or left > right:
        if nums[right] == maxNum:
            count += 1
        
        while count >= k:
            if nums[left] == maxNum:
                count -= 1
            left += 1
            ans += len(nums) - right
        
        right += 1
    
    return ans

