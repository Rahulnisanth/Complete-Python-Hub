# PHONE NUMBER + LETTER COMBINATIONS :
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


# ARRAY PERMUTATIONS :
def permute(nums) :
    def backtrack(resultList, tempList, nums):
        if len(tempList) == len(nums):
            resultList.append(tempList[:])
            return
        else:
            for number in nums: 
                if number not in tempList:
                    tempList.append(number)
                    backtrack(resultList, tempList, nums)
                    tempList.pop()
    resultList = []
    backtrack(resultList, [], nums)
    return resultList


# COMBINATIONS :
def combine(n: int, k: int):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    result = []
    backtrack(1, [])
    return result