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
