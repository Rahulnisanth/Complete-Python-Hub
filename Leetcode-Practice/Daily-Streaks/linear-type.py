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
