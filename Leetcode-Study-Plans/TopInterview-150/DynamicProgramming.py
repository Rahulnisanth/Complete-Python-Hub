
# MIN SUB ARRAY USING DYNAMIC PROGRAMMING :
def maxSumAfterPartitioning(arr , k) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_val = float('-inf')
            for j in range(1, min(i, k) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)
        return dp[n]


# CLIMBING STAIRS :
def climbStairs( n: int) -> int:
    if n == 1:
        return 1
    _oneBefore, _twoBefore = 1, 1
    total = 0
    for i in range(2, n + 1):
        total = _oneBefore + _twoBefore
        _twoBefore = _oneBefore
        _oneBefore = total
    return total


# HOUSE ROBBER :
def rob(nums) -> int:
    rob, noRob = 0, 0
    for i in range(len(nums)):
        newRob = noRob + nums[i]
        newNoRob = max(noRob, rob)
        rob, noRob = newRob, newNoRob
    return max(rob, noRob)  


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