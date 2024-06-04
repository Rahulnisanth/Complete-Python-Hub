def count_shortest_subsequence(s, t, x, y, dp) -> int:
    if x == 0 or y == 0: 
        dp[x][y] = x + y
    if dp[x][y] == 0:
        if s[x - 1] == t[y - 1]:
            dp[x][y] = count_shortest_subsequence(s, t, x - 1, y - 1, dp) + 1
        else:
            dp[x][y] = min(count_shortest_subsequence(s, t, x - 1, y, dp) + 1, count_shortest_subsequence(s, t, x, y - 1, dp) + 1)
    return dp[x][y]

# Input stream :
s = input()
t = input()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
print(count_shortest_subsequence(s, t, len(s), len(t), dp))