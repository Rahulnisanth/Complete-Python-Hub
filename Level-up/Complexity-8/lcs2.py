# Longest common sub-sequence using knapsack [Tabulation method] :
def knapsack(str1, str2) -> int:
    n1, n2 = len(str1), len(str2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

# Input drive :
str1 = input()
str2 = input()
print(knapsack(str1, str2))