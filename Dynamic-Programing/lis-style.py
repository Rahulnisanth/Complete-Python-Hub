# LONGEST INCREASING SUB-SEQUENCE :
def lengthOfLIS(nums) -> int:
    if not nums:
        return 0
    N = len(nums)
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# NUMBER OF LIS IN GIVEN ARRAY :
def numberOfLIS(nums) -> int:
    if not nums:
        return 0
    N = len(nums)
    M, dp, count = 0, [1] * N, [1] * N
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[i] == dp[j] + 1:
                    count[i] += count[j]
        M = max(M, dp[i])
    return sum(c for l, c in zip(dp, count) if l == M)