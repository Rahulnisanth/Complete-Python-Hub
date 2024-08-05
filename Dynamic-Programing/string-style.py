# LONGEST PALINDROMIC SUBSTRING :
def longestPalindrome(s: str) -> str:
    N = len(s)
    result, maxLen = "", 0
    dp = [[0] * (N) for _ in range(N)]
    for diff in range(N):
        for i in range(N):
            j = i + diff
            if i < N and j < N:
                # First diagonal :
                if i == j:
                    dp[i][j] = 1
                # Second diagonal :
                elif diff == 1:
                    dp[i][j] = 2 if s[i] == s[j] else 0
                # Other diagonal :
                elif s[i] == s[j] and dp[i + 1][j - 1] > 0:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # Handling the substring len and result :
                if dp[i][j] > 0:
                    if j - i + 1 > maxLen:
                        maxLen = j + 1
                        result = s[i : maxLen]
    return result


# WORD BREAK :
def wordBreak(s: str, wordDict) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]


# LONGEST PALINDROMIC SUBSEQUENCE :
def longestPalindromicSubSequence(S) -> int:
    R = S[::-1]
    dp = [[0] * (len(R) + 1) for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(R) + 1):
            if S[i - 1] == R[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]


# EDIT DISTANCE >> MIN OPERATIONS TO CONVERT WORD 1 TO WORD 2 :
def minDistance(self, word1: str, word2: str) -> int:
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    # First row :
    for i in range(len(word2) + 1):
        dp[0][i] = i
    # First column :
    for j in range(len(word1) + 1):
        dp[j][0] = j
    # Edge cases:
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
    return dp[-1][-1]


# MINIMUM DELETE TO ASCII SUM :
def minimumDeleteSum(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp =[[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, n2 + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                del_1 = ord(s1[i - 1]) + dp[i - 1][j]
                del_2 = ord(s2[j - 1]) + dp[i][j - 1]
                dp[i][j] = min(del_1, del_2)
    return dp[-1][-1]