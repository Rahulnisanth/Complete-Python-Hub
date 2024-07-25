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