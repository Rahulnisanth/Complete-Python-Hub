# FIND THE DIFFERENCE OF TWO ARRAYS :
def findDifference(nums1, nums2):
    first = list(set(nums1) - set(nums2))
    second = list(set(nums2) - set(nums1))
    return [first, second]


# UNIQUE NUMBER OF OCCURRENCE :
def uniqueOccurrences(arr) -> bool:
    occurrence = []
    arrSet = set(arr)
    for num in arrSet:
        occurrence.append(arr.count(num))
    for count in occurrence:
        if occurrence.count(count) > 1:
            return False
    return True


# DETERMINE IF TWO STRINGS ARE CLOSE :
from collections import Counter
def isClose(word1, word2) -> bool:
    if set(word1) != set(word2):
        return False
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())


# COUNT THE EQUAL ROW AND COLUMN PAIRS :
def equalPairs(grid) -> int:
    if not grid:
        return 0
    def helper(grid, row, col):
        row_list = grid[row]
        col_list = [grid[i][col] for i in range(len(grid))]
        return row_list, col_list
    # Main drive...
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            row_list, col_list = helper(grid, i, j)
            if row_list == col_list:
                count += 1
    return count