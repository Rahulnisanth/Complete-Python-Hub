# SORT PEOPLE BASED ON HEIGHTS :
def sortPeople(names, heights):
    mapper = {}
    for name, height in list(zip(names, heights)):
        mapper[height] = name
    mapper = sorted(mapper.items(), key=lambda x: x[0], reverse=True)
    return [mapper[i][1] for i in range(len(mapper))]


# SORT THE ARRAY BASED ON FREQUENCIES :
from collections import Counter
def frequencySort(nums):
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (freq[x], -x))


# SORT THE JUMBLED NUMBERS :
def sortJumbled(mapping, nums):
    def translate_integer(num):
        digits = []
        num = str(num)
        for i in range(len(digits)):
            digits[i] = str(mapping[int(digits[i])])
        return int("".join(digits))
    number_mapping = {}
    for num in nums:
        number_mapping[num] = translate_integer(num)
    nums.sort(key=lambda x: number_mapping[x])
    return nums


# SORT USING ANY SORTING ALGORITHM IN O(N LOG N) :
def sortNumber(nums):
    def merge(nums, low, mid, high):
        temp = []
        left, right = low, mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        for i in range(low, high + 1):
            nums[i] = temp[i - low]
    def divide(nums, low, high):
        if low == high: 
            return 
        mid = (low + high) // 2
        divide(nums, low, mid)
        divide(nums, mid + 1, high)
        merge(nums, low, mid, high)
    divide(nums, 0, len(nums) - 1)
    return nums


# COUNT OF THE NUMBER OF TEAM ACCORDING TO THE RATINGS :
def numTeams(rating) -> int:
    if not rating:
        return 0
    count, N = 0, len(rating)
    for i in range(N - 2):
        for j in range(i, N - 1):
            for k in range(j, N):
                if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                    count += 1
    return count


# RANGE SUM OF SORTED SUB-ARRAY :
def rangeSum(nums, n, left, right)->int:
    if not nums:
        return 0
    result = []
    for i in range(n):
        dump = 0
        for j in range(i, n):
            dump += nums[j]
            result.append(dump)
    return sum(sorted(result)[left - 1:right])


# MINIMUM PUSHES TO MAKE THE WORD :
def minimumPushes(word: str) -> int:
    if not word:
        return 0
    mapper = Counter(word)
    # Sorting the dictionary based on value...
    sorted_mapper = {k:v for k, v in sorted(mapper.items(), key=lambda x:x[1], reverse=True)}
    # Core drive...
    keyCount = 0
    result = 0
    push = 1
    for count in sorted_mapper.values():
        if count == 0: 
            break
        result += (count * push)
        keyCount += 1
        if keyCount % 8 == 0: 
            push += 1
    return result


# A CLASS IMPLEMENTATION TO FIND THE KTH LARGEST ELEMENT OF STREAM :
import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, value):
        heapq.heappush(value)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# KTH SMALLEST PAIR :
def smallestDistancePair(nums, k):
    nums.sort()
    def helper(mid):
        count, left = 0, 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
        return count
    
    low, high = 0, nums[-1] - nums[0]
    while low < high:
        mid = (low + high) // 2
        if helper(mid) >= k:
            high = mid
        else:
            low = mid + 1
    
    return low


# MAXIMUM DISTANCE IN ARRAYS :
def maxDistance(arrays)->int:
    if not arrays:
        return 0
    N = len(arrays)
    min_value = arrays[0][0]
    max_value = arrays[0][-1]
    result = 0
    for i in range(1, N):
        result = max(result, abs(arrays[i][-1] - min_value))
        result = max(result, abs(arrays[i][0] - max_value))
        min_value = min(min_value, arrays[i][0])
        max_value = max(max_value, arrays[i][-1])
    return result


# NTH UGLY NUMBER :
from heapq import heappop, heappush
def nthUglyNumber(n: int) -> int:
    primes = [2, 3, 5]
    heap = [1]
    visited = set()
    visited.add(1)
    for _ in range(n):
        current = heappop(heap)
        for prime in primes:
            new_num = current * prime
            if new_num not in visited:
                visited.add(new_num)
                heappush(heap, new_num)
    return current


# 2 KEYS KEYBOARD :
def minSteps(n: int) -> int:
    def helper(current):
        if current == 1: 
            return 0
        ans = current
        idx = 2
        while idx * idx <= current:
            if current % idx == 0:
                ans = min(ans, helper(current // idx) + idx)
            idx += 1
        return ans
    return helper(n)


# ONES COMPLEMENT :
def findComplement(num: int) -> int:
    bin_val = list(bin(num))[2:]
    result = ''
    for val in bin_val:
        result += '1' if val == '0' else '0'
    return int(result, 2)


# FIND THE STUDENT THAT WILL REPLACE THE CHALK:
def chalkReplacer(chalk, k) -> int:
    k %= sum(chalk)
    if k <= 0:
        return 0
    for idx, c in enumerate(chalk):
        if k < c:
            return idx
        k -= c


# COUNT THE CONSISTENT STRINGS :
def countConsistentStrings(allowed, words) -> int:
    count = 0
    def is_correct(word):
        for ch in word:
            if ch not in allowed:
                return False
        return True
    for word in words:
        if is_correct(word):
            count += 1
    return count


# MINIMUM TIME DIFFERENCE :
def findMinDifference(timePoints) -> int:
    sorted_time = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
    sorted_time.sort()
    minDiff = float("inf")
    for i in range(1, len(sorted_time)):
        minDiff = min(minDiff, abs(sorted_time[i - 1] - sorted_time[i]))
    minDiff = min(minDiff, 1440 + sorted_time[0] - sorted_time[-1])
    return minDiff


# UNCOMMON WORD FROM TWO SENTENCE :
def uncommonFromSentences(s1: str, s2: str):
    mapper = Counter(s1.split()) + Counter(s2.split())
    result = []
    for word, count in mapper.items():
        if count == 1:
            result.append(word)
    return result


# LARGEST NUMBER :
from functools import cmp_to_key
def largestNumber(nums) -> str:
    # Comparator...
    def compare(x, y):
        return -1 if x + y > y + x else 1
    if not nums:
        return ''
    sorted_arr = sorted(list(map(str, nums)), key=cmp_to_key(compare))
    return str(int(''.join(sorted_arr)))


# SHORTEST PALINDROME :
def shortestPalindrome(s: str) -> str:
    reversed_str = s[::-1]
    for i in range(len(s)):
        if s.startswith(reversed_str[i:]):
            return reversed_str[:i] + s


# MY CALENDAR I :
class MyCalendar:
    def __init__(self):
        self.data = []

    def book(self, start: int, end: int) -> bool:
        for x, y in self.data:
            if max(start, x) < min(end, y):
                return False
        self.data.append([start, end])
        return True


# MY CALENDAR II :
class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for x, y in self.overlaps:
            if max(start, x) < min(end, y):
                return False
        for x, y in self.events:
            if max(start, x) < min(end, y):
                self.overlaps.append((max(start, x), min(end, y)))
        self.events.append((start, end))
        return True


# RANK TRANSFORM OF THE ARRAY :
def arrayRankTransform(arr):
    if not arr:
        return []
    sorted_set = sorted(set(arr))
    ranks = {num: rank + 1 for rank, num in enumerate(sorted_set)}
    return [ranks[num] for num in arr]


# MAKE SUM DIVISIBLE BY P :
def minSubArray(nums, p) -> int:
    n = len(nums)
    total = sum(nums) % p
    if total == 0:
        return 0
    prefix_sum, result = 0, n + 1
    mapper = {0 : -1}
    for i, v in enumerate(nums):
        prefix_sum += v
        cur = prefix_sum % p - total
        if cur < 0:
            cur += p
        if cur in mapper:
            result = min(result, i - mapper[cur])
        mapper[prefix_sum % p] = i
    return result if result < n else -1


# DIVIDE THE TEAMS OF THE PLAYERS BY EQUAL SKILLS :
def dividePlayers(skill) -> int:
    skill.sort()
    total_skill = skill[0] + skill[-1]
    N, result = len(skill), 0
    for i in range(N // 2):
        if (skill[i] + skill[N - i - 1]) != total_skill:
            return -1
        result += (skill[i] * skill[N - i - 1])
    return result


# MIN SWAPS TO MAKE THE STRING BALANCED :
def minSwaps(s: str) -> int:
    count = 0
    for ch in s:
        if ch == '[': 
            count += 1
        elif count > 0: 
            count -= 1
    return (count + 1) // 2


# MIN ADDS TO MAKE THE PARENTHESIS BALANCED :
def minAddToMakeValid(s: str) -> int:
    opens = closes = 0
    for ch in s:
        if ch == '(':
            opens += 1
        elif ch == ')':
            if opens > 0:
                opens -= 1
            else:
                closes += 1
    return opens + closes


# FINAL PRICES WITH SPECIAL DISCOUNT :
def finalPrices(prices):
    result = []
    N = len(prices)
    for i in range(N):
        curr = prices[i]
        discount = 0
        for j in range(i + 1, N):
            if j > i and prices[j] <= prices[i]:
                discount = prices[j]
                break
        result.append(curr - discount)
    return result


# MAX CHUNKS TO MAKE IT SORTED :
def maxChunksToSorted(arr) -> int:
    max_num, chunks = 0, 0
    for i, num in enumerate(arr):
        max_num = max(max_num, num)
        if max_num == i:
            chunks += 1
    return chunks


# COUNT THE VOWELS IN RANGE OF QUERIES :
def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    vowels = "aeiou"
    N = len(words)

    def willSatisfy(word):
        return True if word[0] in vowels and word[-1] in vowels else False

    prefix_sum = [0] * (N + 1)
    result = []
    for i in range(1, N + 1):
        if willSatisfy(words[i - 1]):
            prefix_sum[i] = prefix_sum[i - 1] + 1
        else:
            prefix_sum[i] = prefix_sum[i - 1]

    for left, right in queries:
        count = prefix_sum[right + 1] - prefix_sum[left]
        result.append(count)
    return result


# STRING MATCHING :
def stringMatching(words: List[str]) -> List[str]:
    result = []
    words.sort(key=lambda x: len(x))
    for i in range(len(words)):
        searchWord = words[i]
        for j in range(i + 1, len(words)):
            if searchWord in words[j]:
                result.append(searchWord)
                break
    return result


# COUNT THE WORDS WITH GIVEN PREFIX :
def prefixCount(words: List[str], pref: str) -> int:
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count


# CAN CONSTRUCT K PALINDROME STRINGS :
def canConstruct(self, s: str, k: int) -> bool:
    if len(s) < k:
        return False
    counter = Counter(s)
    odd_count = sum(1 for k, v in counter.items() if v % 2 != 0)
    return odd_count <= k
