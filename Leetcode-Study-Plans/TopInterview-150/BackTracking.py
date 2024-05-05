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


# WORD SEARCHING BOARD GAME :
def exist(board, word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if dfs(board, i, j, word, 0):
                return True
    return False
def dfs(board, i, j, word, word_idx): # Recursive[DFS] to analyze the adjacent letters...
    if board[i][j] != word[word_idx]:
        return False
    if word_idx + 1 == len(word):
        return True
    board[i][j] = '#'
    result = (
            (i > 0 and dfs(board, i - 1, j, word, word_idx + 1)) or
            (i < len(board) - 1 and dfs(board, i + 1, j, word, word_idx + 1)) or
            (j > 0 and dfs(board, i, j - 1, word, word_idx + 1)) or
            (j < len(board[i]) - 1 and dfs(board, i, j + 1, word, word_idx + 1))
            )
    board[i][j] = word[word_idx]
    return result


# GENERATE PARENTHESIS :
def generateParenthesis(n : int):
    # Helper func [backtracking] :
    def backtrack(combination, open, close):
        if len(combination) == 2 * n:
            result.append(combination)
            return 
        if open < n:
            backtrack(combination + '(', open + 1, close)
        if close < open:
            backtrack(combination + ')', open, close + 1)
    # Main drive :
    result = []
    backtrack('', 0, 0)
    return result
