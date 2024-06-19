def rob(nums, N) -> int:
    if N == 0: 
        return 0
    if N == 1: 
        return nums[0]
    else:
        dp = [0] * N
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, N):
            take = nums[i] + dp[i - 2]
            not_take = dp[i - 1]
            dp[i] = max(take, not_take)
        return dp[-1]

# Input drive :
N = int(input())
houses = list(map(int, input().split()))
print(rob(houses, N))