# LONGEST COMMON SUBSEQUENCE :
def longestCommonSubsequence(text1, text2) -> int:
    dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
    for i in range(1, len(text2) + 1):
        for j in range(1, len(text1) + 1):
            if text2[i - 1] == text1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


# UNCROSSED LINES :
def maxUncrossedLines(nums1, nums2) -> int:
    dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]
    for i in range(1, len(nums2) + 1):
        for j in range(1, len(nums1) + 1):
            if nums2[i - 1] == nums1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]