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
