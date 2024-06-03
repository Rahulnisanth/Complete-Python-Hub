def how_sum(target, nums):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]
    for i in range(target + 1):
        for j in range(len(nums)):
            if i == 0: 
                dp[nums[j]].append(nums[j])
            elif len(dp[i]) > 0 and i + nums[j] <= target:
                dp[i + nums[j]].extend(dp[i])
                dp[i + nums[j]].append(nums[j])
    return set(dp[target])

target = int(input())
string = input().strip()
nums = list(map(int, string.replace("[","").replace("]","").replace(","," ").split()))
print(how_sum(target, nums))

