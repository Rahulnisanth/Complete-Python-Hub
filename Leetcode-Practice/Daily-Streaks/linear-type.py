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