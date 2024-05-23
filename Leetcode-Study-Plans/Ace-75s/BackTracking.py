# LETTER COMBINATIONS OF PHONE NUMBER :
def letterCombinations(digits: str):
    if not digits:
        return []
    result = []
    digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def backtrack(current, idx):
        if len(current) == len(digits):
            result.append(current)
            return
        else:
            for letter in digits_to_letters[digits[idx]]:
                backtrack(current + letter, idx + 1)
    
    backtrack('', 0)
    return result


# THE NUMBER OF BEAUTIFUL SUBSETS :
from collections import defaultdict
def beautifulSubsets(nums, k):
    count = 0
    def explore(index):
        nonlocal count
        if len(nums) == index:
            count += 1
            return
        num = nums[index]
        if not num - k in map and not num + k in map :
            map[num] += k
            explore(index + 1)
            map[num] -= k
            if map[num] == 0:
                del map[num]
        explore(index + 1)
    map = defaultdict(int)
    explore(0)
    return count - 1
