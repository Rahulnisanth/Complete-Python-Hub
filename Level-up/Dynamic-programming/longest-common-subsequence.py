def find_lcs(word_1, word_2, x, y, dp) -> int:
    if x == 0 or y == 0: return 0
    if dp[x][y] != -1: return dp[x][y]  
    # If character matches :
    if word_1[x - 1] == word_2[y - 1]: 
        dp[x][y] = 1 + find_lcs(word_1, word_2, x - 1, y - 1, dp)
        return dp[x][y]
    # If character not matches :
    dp[x][y] = max(find_lcs(word_1, word_2, x, y - 1, dp), find_lcs(word_1, word_2, x - 1, y, dp))
    return dp[x][y]

# Input stream :
word_1 = input().strip()
word_2 = input().strip()
n1, n2 = len(word_1), len(word_2)
dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
print(find_lcs(word_1, word_2, len(word_1), len(word_2), dp))