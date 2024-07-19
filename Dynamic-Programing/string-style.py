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
