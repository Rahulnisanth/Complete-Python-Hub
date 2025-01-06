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


# COMBINATION SUM - III
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    result = []
    self.makeKCombinations(1, n, k, result, [])
    return result
def makeKCombinations(self, start, target, K, result, path) -> List[int]:
    if K == 0 and target == 0:
        result.append(path[:])
        return
    if K == 0 or target <= 0:
        return
    for i in range(start, 10):
        path.append(i)
        self.makeKCombinations(i + 1, target - i, K - 1, result, path)
        path.pop()
